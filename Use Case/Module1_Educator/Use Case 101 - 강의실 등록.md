# Use Case UC-101: 강의실 등록

|                          | UC-101: 강의실 등록                        |
| ------------------------ | ------------------------------------------ |
| __Related REQ__          | FR1                                        |
| __Initiating Actor__     | 교육자                             |
| __Actor's Goal__         | 학생들에게 과제를 배부하고, 소통           |
| __Participating Actors__ | 학생, 강의실 DB      |
| __Preconditions__        | 교육자 계정으로 로그인이 되어 있어야 함. |
| __Postconditions__       | 강의실이 개설되고 학생들이 등록됨.       |

|      | Flow of Events for Main Success Scenario                     |
| ---- | ------------------------------------------------------------ |
| ->   | 1. 강의실 등록 버튼을 누른다.                                |
|      | 2. 강의실 정보를 입력한다. (강의명, 강의정보, 과제일정 등)   |
| <-   | 3. (a) 생성된 강의실을 교육자 보여준다. (b) 강의실 DB에 강의실 정보를 등록한다. |

### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>

