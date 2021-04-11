# Use Case UC-301: 자동 채점

| | UC-301: 자동 채점 |
| - | - |
| __Related REQ__          | FR4 |
| __Initiating Actor__     | TBI |
| __Actor's Goal__         | 제출된 코드에 대한 테스트를 실행하고 결과를 반환 |
| __Participating Actors__ | 데이터베이스 |
| __Preconditions__        | 없음 (다른 모듈에 의해서 invoke 되는 케이스임) |
| __Postconditions__       | 데이터베이스에 채점 결과가 저장됨 |

|    | Flow of Events for Main Success Scenario |
| - | - |
| -> | 1. [TBI]가 채점 큐에 자동 채점이 필요한 코드와 테스트 케이스에 대한 정보를 넣는다. |
| <- | 2. 시스템은 큐에서 정보를 하나씩 꺼내 (a) 제공된 코드와 테스트 케이스를 이용해 자동화 테스트를 실행하고, (b) 그 결과를 데이터베이스에 저장한다. |

-------

### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>

- - -

### Comment
1. 아무래도 어떤 actor들이 있는지에 대해 충분히 검토하지 못한 듯.
2. 역시 순서대로 했어야 전체적인 그림이 그려지면서 use case에 대한 설명이 정확하게 나올 수 있을 듯.
3. 어째 모듈간 의존성이 생기는 듯? 갑자기 제대로 가고 있나 의문이 생겨버림...