# 샘플 1 PR 템플릿 (minimal)

## 브랜치 전략
GitHub Flow를 사용해 main 브랜치를 안정적으로 유지하고, feature/add-greeting 브랜치에서 작은 단위로 변경 후 PR로 검토합니다.

## 변경 사항
- app/greeting.py 파일을 수정했습니다.
- 이름이 비어 있으면 Guest 인사말을 반환하고, 이름이 있으면 해당 이름을 포함한 인사말을 반환하도록 구현했습니다.
- PR 설명에 로컬 검증 결과와 체크리스트를 포함했습니다.

## 테스트
- python3 대화형 실행으로 get_greeting("")과 get_greeting("Yujeong") 반환값을 확인했습니다.
- sample-solutions-minimal/sample-3-testing에서 python3 -m pytest -q 실행 결과 2 passed를 확인했습니다.
- python3 -m ruff check . 명령으로 정적 검사를 확인했습니다.
- GitHub Actions Sample CI 통과: https://github.com/yuujjjj/AIOSS/actions/runs/26266439753/job/77310623519

## 롤백 계획
- 문제가 발생하면 이 PR을 revert 하거나 app/greeting.py의 변경 전 구현으로 되돌립니다.

## 체크리스트
- [x] 코드 동작 확인
- [x] 자체 리뷰 완료
- [x] 문서 또는 설명 보강
