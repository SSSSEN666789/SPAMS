# Use Case UC-203: 과제 제출 결과 확인

|                          | UC-203: 과제 제출 결과 확인               |
| ------------------------ | ---------------------------------------------- |
| __Related REQ__          | FR9                                     |
| __Initiating Actor__     | 학생                                   |
| __Actor's Goal__         | 제출물의 런타임, 테스트 케이스 등 결과를 확인 하기 위해      |
| __Participating Actors__ | 과제 관리자, 과제DB               |
| __Preconditions__        | 학생이 해당 과제를 제출한 적이 있어야 함.        |
| __Postconditions__       | 제출한 코드 등 제출물을 바탕으로 런타임, 테스트 케이스 등 결과를 도출해냄. |

|      | Flow of Events for Main Success Scenario                     |
| ---- | ------------------------------------------------------------ |
|    | 1. Extends UC-202 과제 제출. |
| <-   | 2. 테스트 케이스, 런타임 등을 계산한다.         |
|  <-   | 3. 교육자와 학생에게 도출된 결과를 표시한다.                                 |


### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>

