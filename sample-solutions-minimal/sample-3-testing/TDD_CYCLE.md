# TDD 사이클 메모 (minimal)

## RED
- tests/test_calculator.py에 add(2, 3) == 5, subtract(10, 3) == 7을 검증하는 테스트 2개를 먼저 작성했습니다.
- app/calculator.py 구현 전에는 NotImplementedError로 테스트가 실패하는 흐름을 확인할 수 있습니다.

## GREEN
- app/calculator.py에서 add는 a + b, subtract는 a - b를 반환하도록 최소 구현했습니다.
- python3 -m pytest -q 실행 결과: 2 passed in 0.01s

## REFACTOR
- 불필요한 미구현 예외를 제거하고, 테스트가 유지되는 범위에서 단순한 함수 구현만 남겼습니다.
- python3 -m ruff check . 실행 결과: All checks passed!
