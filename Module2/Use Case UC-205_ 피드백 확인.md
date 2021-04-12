# Use Case UC-205: 피드백 확인

|                          | UC-205: 피드백 확인                                          |
| ------------------------ | ------------------------------------------------------------ |
| __Related REQ__          | FR10                                                    |
| __Initiating Actor__     | 학생                                                       |
| __Actor's Goal__         | 시스템에서 자동적으로 해결할 수 없는 과제의 채점(점수 기입)  |
| __Participating Actors__ | 교육자, 과제 관리 시스템, 과제 알리미                                      |
| __Preconditions__        | 교육자가 해당 과제에 피드백을 보냈어야 함.|
| __Postconditions__       | 학생에게 피드백의 내용을 보여주고 아래에 답글을 달수 있게 함.                                      |

|      | Flow of Events for Main Success Scenario      |
| ---- | --------------------------------------------- |
|      | 1. Extends UC-107 과제 코멘트                   |
| <-   | 2. 과제 알리미가 학생에게 피드백 알림을 전달한다.  |
| ->  | 3. 학생은 기록된 과제 코멘트를 확인 할 수 있게 된다. |

-------

### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>