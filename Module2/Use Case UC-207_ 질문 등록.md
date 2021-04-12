# Use Case UC-207: 질문 등록

|                          | UC-207: 질문 등록                                          |
| ------------------------ | ------------------------------------------------------------ |
| __Related REQ__          | FR10                                                    |
| __Initiating Actor__     | 학생                                                       |
| __Actor's Goal__         | 과제중에 생기는 학생의 의문점들을 해소 하기 위해.                    |
| __Participating Actors__ | 교육자, 과제 관리 시스템, 과제 알리미, 에디터                 |
| __Preconditions__        | 해당 과제가 생성되고 열려 있어야함. |
| __Postconditions__       | 학생이 남긴 질문이 교육자에게 전달됨.                    |

|      | Flow of Events for Main Success Scenario                     |
| ---- | ------------------------------------------------------------ |
| ->   | 1. 에디터에 질문 내용을 입력하고 질문 등록을 누른다.     |
| <-   | 3. (a)과제 관리 시스템이 과제에 질문을 기록한다. <br />(b) 과제 알리미는 과제에 질문이 기록되었음을 교육자에게 알린다. |

-------

### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>
