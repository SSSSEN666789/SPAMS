# Use Case UC-107: 과제 코멘트

|                          | UC-107: 과제 코멘트                                          |
| ------------------------ | ------------------------------------------------------------ |
| __Related REQ__          | FR6, FR10                                                    |
| __Initiating Actor__     | 교육자                                                       |
| __Actor's Goal__         | 제출한 과제에 대해 직접적인 피드백 제공                      |
| __Participating Actors__ | 학생, 에디터, 과제 관리 시스템, 과제 알리미                  |
| __Preconditions__        | 강의실에 소속된 학생이 제출한 과제가 과제 관리 시스템에 등록되어 있어야 함. |
| __Postconditions__       | 교육자가 남긴 코멘트가 학생에게 전달됨.                      |

|      | Flow of Events for Main Success Scenario                     |
| ---- | ------------------------------------------------------------ |
|      | 1. Extends 과제열람 (UC-104)                                 |
| ->   | 2. 피드백 버튼을 누르고 에디터에 피드백 내용을 입력한다.     |
| <-   | 3. (a)과제 관리 시스템이 과제에 피드백을 기록한다. <br />(b) 과제 알리미는 과제에 피드백이 기록되었음을 학생에게 알린다. |

-------

### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>

