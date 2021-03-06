# Use Case UC-110: 질문 답변

|                          | UC-110: 질문 답변                                  |
| ------------------------ | -------------------------------------------------- |
| __Related REQ__          | FR6 FR10                                           |
| __Initiating Actor__     | 교육자                                             |
| __Actor's Goal__         | 학생이 등록한 질문에 대답하여 직접적인 피드백 제공 |
| __Participating Actors__ | 학생, 질문DB                                       |
| __Preconditions__        | 강의실에 등록된 학생이 질문을 게시해야함.          |
| __Postconditions__       | 교육자가 답변을 남겼음을 학생에게 전달됨.          |

|      | Flow of Events for Main Success Scenario                     |
| ---- | ------------------------------------------------------------ |
|      | 1. Extends UC-109 질문 열람                                  |
| ->   | 2. 답변 버튼을 누르고 답변 내용을 입력한다.                  |
| <-   | 3. (a) 질문에 답변이 기록된다. (b) 질문을 게시한 학생에게 답변이 남겨졌음을 알린다. |

