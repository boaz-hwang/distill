# Skilloom

유용한 스킬을 제대로 만들어보세요.

[English](README.md) · [MIT](LICENSE)

| 스킬 | 역할 |
| --- | --- |
| [distill](skills/distill/README.ko.md) | 완료한 업무에서 스킬 생성 |
| [refine](skills/refine/README.ko.md) | 스킬 하나의 전체 구조·지침 정비 |
| [evolve](skills/evolve/README.ko.md) | 실제 사용에서 관찰된 문제를 관련 부분만 수정해 개선 |
| [consolidate](skills/consolidate/README.ko.md) | 여러 스킬의 중복을 검토하고 적합한 것끼리 통합 |

## 배경

Skilloom은 스킬에 불필요한 지침이 쌓여 길어지는 문제에서 출발했습니다. 유능한 모델의 판단력을 믿고, 원하는 결과에 필요한 최소 조건만 남깁니다. 완료한 업무, 기존 지침, 실행 피드백을 근거로 스킬을 만들고 다듬습니다. 삭제부터 검토하되 필수 품질은 보존하고, 코드가 검증할 부분과 사람이 판단할 부분을 구분합니다.

## 설치

코딩 에이전트에 아래 한 줄을 붙여넣으세요.

```text
https://github.com/boaz-hwang/skilloom 을 git clone해서 skills/ 안의 네 스킬을 각각 네 스킬 폴더에 설치해줘.
```

기존 저장소 루트에서 설치한 distill은 skills/distill에서 다시 설치하세요.

## 사용

목적에 맞는 스킬을 호출하세요. 위 링크마다 복사할 수 있는 요청문이 있습니다. 네 스킬은 각각 독립적으로 사용합니다.

추천 모델:

- Fable 5.1
- Astra 6
