# Use Case UC-105: 과제 채점

|                          | UC-105: 과제 채점                                            |
| ------------------------ | ------------------------------------------------------------ |
| __Related REQ__          | FR6, FR10                                                    |
| __Initiating Actor__     | 교육자                                                       |
| __Actor's Goal__         | 시스템에서 자동적으로 해결할 수 없는 과제의 채점(점수 기입)  |
| __Participating Actors__ | 학생, 과제 관리 시스템                                       |
| __Preconditions__        | 강의실에 소속된 학생이 제출한 과제가 과제 관리 시스템에 등록되어 있어야 함. |
| __Postconditions__       | 과제에 점수가 부여됨.                                        |

|      | Flow of Events for Main Success Scenario      |
| ---- | --------------------------------------------- |
|      | 1. Extends UC-104 과제 열람                   |
| ->   | 2. 과제 채점 버튼을 누르고 점수를 입력한다.   |
| <-   | 3. 과제 관리 시스템은 과제의 점수를 기록한다. |

-------

### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>
