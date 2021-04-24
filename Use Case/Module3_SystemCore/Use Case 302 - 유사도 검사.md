# Use Case UC-302: 유사도 검사

| | UC-302: 유사도 검사|
| - | - |
| __Related REQ__          | FR5 |
| __Initiating Actor__     | 교육자 |
| __Actor's Goal__         | 제출된 과제들 사이의 유사도를 검사|
| __Participating Actors__ | 데이터베이스 |
| __Preconditions__        | 제출된 과제가 두 개 이상이어야 함 |
| __Postconditions__       | 데이터베이스에 유사도 검사 결과 값이 저장됨 |

|      | Flow of Events for Main Success Scenario |
| - | - |
| ->   | 1. 교육자가 제출물 유사도 검사 버튼을 누르거나, 과제가 마감되는 시점에 유사도 검사가 시작됨. |
| <-   | 2. 시스템은 데이터베이스에서 제출 완료된 자료들에 한해 유사도 검사를 실시하고, 그 결과를 데이터베이스에 반환한다. | 


------- 




### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>



