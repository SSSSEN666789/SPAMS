# Use Case UC-107: 제출물 진행도 확인

|                          | UC-107: 제출물 진행도 확인                                   |
| ------------------------ | ------------------------------------------------------------ |
| __Related REQ__          | FR3, FR4, FR5, FR8                                           |
| __Initiating Actor__     | 교육자                                                       |
| __Actor's Goal__         | 전체 과제의 진행 상황(제출율, 정답율 등)과 각 학생에 대한 과제 진행도를 파악 |
| __Participating Actors__ | 과제DB, 제출물DB                                             |
| __Preconditions__        | 교육자가 강의실에 과제를 등록한 적이 있어야 함.              |
| __Postconditions__       | 각 분류 별 과제 진행도를 교육자에게 보여줌.                  |

|      | Flow of Events for Main Success Scenario                     |
| ---- | ------------------------------------------------------------ |
| ->   | 1. 강의실 페이지에 접속하여 과제 진행도 확인 버튼을 누른다.  |
|      | 2. 필터를 설정한다. (ex)전체 과제에 대한 전체 학생 진행도, 특정 과제에 대한 특정 학생 진행도) |
| <-   | 3. 필터의 조건에 따라 정보(제출율, 정답비율 등)를 교육자에게 표시한다. |

