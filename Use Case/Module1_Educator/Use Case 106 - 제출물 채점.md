# Use Case UC-106: 제출물 채점

|                          | UC-106: 제출물 채점                                          |
| ------------------------ | ------------------------------------------------------------ |
| __Related REQ__          | FR6, FR10                                                    |
| __Initiating Actor__     | 교육자                                                       |
| __Actor's Goal__         | 시스템에서 자동적으로 해결할 수 없는 과제의 채점(점수 기입)  |
| __Participating Actors__ | 학생, 제출물 DB                                              |
| __Preconditions__        | 강의실에 소속된 학생이 해당 과제의 제출물을 제출한 적이 있어야 함. |
| __Postconditions__       | 제출물에 점수가 부여됨.                                      |

|      | Flow of Events for Main Success Scenario      |
| ---- | --------------------------------------------- |
|      | 1. Extends UC-105 제출물 열람                 |
| ->   | 2. 제출물 채점 버튼을 누르고 점수를 입력한다. |
| <-   | 3. 제출물의 점수가 기록된다.                  |

-------

### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>
