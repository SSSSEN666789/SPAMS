# Use Case UC-301: 자동 채점

| | UC-301: 자동 채점 |
| - | - |
| __Related REQ__          | FR4 |
| __Initiating Actor__     | Module 2 |
| __Actor's Goal__         | 제출된 코드에 대한 테스트를 실행하고 결과를 반환 |
| __Participating Actors__ | 과제 데이터베이스 |
| __Preconditions__        | 없음 (다른 모듈에 의해서 invoke 되는 케이스임) |
| __Postconditions__       | 과제 데이터베이스에 채점 결과가 저장됨 |

|    | Flow of Events for Main Success Scenario |
| - | - |
| -> | 1. Module 2이 채점 대기열에 자동 채점이 필요한 코드와 테스트 케이스에 대한 정보를 넣는다. |
| <- | 2. 시스템은 대기열에서 정보를 하나씩 꺼내 (a) 제공된 코드와 테스트 케이스를 이용해 자동화 테스트를 실행하고, (b) 그 결과를 데이터베이스에 저장한다. |

-------

### Use Case 링크

[UserStory](UserStory)