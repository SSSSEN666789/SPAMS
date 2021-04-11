# Use Case UC-302: 유사도 검사

| | UC-302: 유사도 검사|
| - | - |
| __Related REQ__          | FR5 |
| __Initiating Actor__     | 교육자? |
| __Actor's Goal__         | 제출된 과제들 사이의 유사도를 검사하고 해당 결과를 반환한다. |
| __Participating Actors__ | 데이터베이스 |
| __Preconditions__        | 제출된 과제가 두 개 이상이어야 함 |
| __Postconditions__       | 데이터베이스에 유사도 검사 결과 값이 저장됨 |

|      | Flow of Events for Main Success Scenario |
| - | - |
| ->   | 1. 학생이 모두 과제를 제출하여 교육자의 요청에 의해 유사도 검사가 시작됨 |
| <-   | 2. 시스템은 데이터베이스에서 제출 완료된 자료들에 한해 유사도 검사를 실시하고, 그 결과를 데이터베이스에 반환한다. | 


-------




### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>

- - -
### 질문
1. Initiating Actor 에서 교육자가 검사를 요청하는지, 혹은 학생이 과제를 제출했을 때 시스템이 자동적으로 모든 과제에 대해서 검사를 실시하는지 / 해당 UC에서는 과제 제출이 마감되었을 때 교육자가 평가를 위해 일괄적으로 유사도 검사를 시행한다 가정 하에 작성함.

