# Use Case UC-103: 과제 수정

|                          | UC-103: 과제 수정 (sub-use case)                             |
| ------------------------ | ------------------------------------------------------------ |
| __Related REQ__          | FR1, FR2                                                     |
| __Initiating Actor__     | 교육자                                                       |
| __Actor's Goal__         | 이미 제출한 과제의 내용을 수정하기 위하여                    |
| __Participating Actors__ | 과제 DB                                                      |
| __Preconditions__        | 교육자가 과제를 등록한 적이 있어야 함.<br />교육자가 제출한 과제의 페이지를 열람해야 함. |
| __Postconditions__       | 교육자가 입력한 내용을 바탕으로 과제가 수정됨.               |

|      | Flow of Events for Main Success Scenario                     |
| ---- | ------------------------------------------------------------ |
| ->   | 1. 등록한 과제의 페이지로 이동하여 과제 수정 버튼을 클릭한다. |
| <-   | 2. 기존에 입력했던 과제의 내용을 에디터에 표시한다.          |
| ->   | 3. 과제의 내용을 수정한다.                                   |
| <-   | 4. 입력한 정보를 바탕으로 과제 관리 시스템이 과제를 수정한다. |

### Use Case 링크

[UserStory](UserStory)<br/>[UC-another: another](UC-another: another)<br/>

