#!/usr/bin/env python3
"""Audita a qualidade estática dos testes Python (sem rodar nada, sem dependência nova).

Objetivo: pegar "verde mentiroso" - teste que passa mas não prova nada.

Dois tipos de achado:
  1. Função `def test_*(...)` sem nenhuma prova de verificação no corpo (nem direta,
     nem via helper chamado que já prova por dentro). Prova = `assert`, `pytest.fail(...)`
     ou `raise ...`. Este repo não usa `assert` cru: os helpers e os testes verificam
     via `pytest.fail()` ou `raise Exception(...)`, então essas duas formas contam
     como prova tanto quanto `assert` - sem isso o script acusaria falso positivo em
     quase todo teste real do repo.
  2. Asserção tautológica: `assert True`, `assert False` literal, ou `assert X == X`
     com os dois lados identicos (mesma dump da AST).

Uso: python scripts/audit_test_quality.py
Saída: lista "arquivo:linha: mensagem" por achado. Exit code 1 se achou algo, 0 se limpo.
"""
import ast
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEST_GLOB = "playwright_tests/**/test_*.py"
HELPERS_FILE = "playwright_tests/helpers.py"


def is_proof_node(node: ast.AST) -> bool:
    """True se o nó é uma prova de verificação: assert, pytest.fail(...) ou raise."""
    if isinstance(node, ast.Assert):
        return True
    if isinstance(node, ast.Raise):
        return True
    if isinstance(node, ast.Call):
        func = node.func
        # pytest.fail(...) ou fail(...) (import direto)
        if isinstance(func, ast.Attribute) and func.attr == "fail":
            return True
        if isinstance(func, ast.Name) and func.id == "fail":
            return True
    return False


def function_has_proof(func_node: ast.FunctionDef) -> bool:
    """Varre todo o corpo (inclusive dentro de try/except/if) atrás de uma prova direta."""
    for node in ast.walk(func_node):
        if node is func_node:
            continue
        if is_proof_node(node):
            return True
    return False


def called_function_names(func_node: ast.FunctionDef) -> set:
    names = set()
    for node in ast.walk(func_node):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                names.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                names.add(node.func.attr)
    return names


def find_tautologies(func_node: ast.FunctionDef, filepath: Path, findings: list):
    for node in ast.walk(func_node):
        if not isinstance(node, ast.Assert):
            continue
        test = node.test
        # assert True / assert False literal
        if isinstance(test, ast.Constant) and isinstance(test.value, bool):
            findings.append(
                f"{filepath}:{node.lineno}: assert literal tautológico (assert {test.value})"
            )
            continue
        # assert X == X (mesmo dump dos dois lados)
        if isinstance(test, ast.Compare) and len(test.ops) == 1 and isinstance(test.ops[0], ast.Eq):
            left_dump = ast.dump(test.left)
            right_dump = ast.dump(test.comparators[0])
            if left_dump == right_dump:
                findings.append(
                    f"{filepath}:{node.lineno}: assert tautológico (comparação idêntica dos dois lados)"
                )


def parse_file(filepath: Path):
    source = filepath.read_text(encoding="utf-8")
    return ast.parse(source, filename=str(filepath))


def main() -> int:
    findings = []

    # 1) mapeia quais funções dos helpers já provam algo por dentro (propaga pros testes que as chamam)
    helper_proves = {}
    helpers_path = REPO_ROOT / HELPERS_FILE
    if helpers_path.exists():
        tree = parse_file(helpers_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                helper_proves[node.name] = function_has_proof(node)

    # 2) varre os arquivos de teste
    test_files = sorted(REPO_ROOT.glob(TEST_GLOB))
    for filepath in test_files:
        rel = filepath.relative_to(REPO_ROOT)
        tree = parse_file(filepath)
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef) or not node.name.startswith("test_"):
                continue

            find_tautologies(node, rel, findings)

            if function_has_proof(node):
                continue

            called = called_function_names(node)
            if any(helper_proves.get(name) for name in called):
                continue

            findings.append(
                f"{rel}:{node.lineno}: '{node.name}' não tem nenhuma verificação "
                f"(sem assert, sem pytest.fail, sem raise - direto ou via helper chamado)"
            )

    if findings:
        print("Auditoria de qualidade dos testes encontrou problema(s):\n")
        for f in findings:
            print(f" - {f}")
        print(f"\nTotal: {len(findings)} achado(s).")
        return 1

    print("Auditoria de qualidade dos testes: nenhum teste vazio ou tautológico encontrado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
