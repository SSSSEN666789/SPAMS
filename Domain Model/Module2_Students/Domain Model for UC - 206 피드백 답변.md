# Domain Model for UC - 206 피드백 답변

| Responsibility Description                          | Type | Concept Name   |
| --------------------------------------------------- | ---- | -------------- |
| 각 컨셉들의 동작을 제어하고 다른 컨셉과 연결해준다. | D    | 컨트롤러       |
| 답변할 피드백의 ID와 답변의 내용               | K    | 답변 기록 요청 |
| 답변을 피드백 아래에 추가한다.                      | D    | 답변 입력자    |
| 제출물 DB와 각 컨셉들을 연결함.                       | D    | 제출물 DB 커넥션 |
| 답변 입력자에게 답변 정보를 받아와 교육자에게 알린다. | D    | 알리미         |

##### Associations

| Concept pair                  | Association Description                              | Association name |
| ----------------------------- | ---------------------------------------------------- | ---------------- |
| 답변 기록 요청 -> 컨트롤러    | 답변을 기록할 피드백ID 와 답변의 내용을 전달  | receives         |
| 컨트롤러 -> 제출물 DB 커넥션    | 답변할 피드을 DB 커넥션에게 검색 요청                | conveys request  |
| 컨트롤러 -> 답변 입력자       | 답변 입력을 요청                                     | conveys request  |
| 답변 입력자 -> 제출물 DB 커넥션 | 피드백이 기록된 제출물로 등록을 요청                   | requests update  |
| 답변 입력자 -> 알리미         | 답변 입력자에게 입력된 답변의 내용을 알리미에게 제공 | provides data    |

##### Attributes

| Concept        | Attributes           | Attribute Description                          |
| -------------- | -------------------- | ---------------------------------------------- |
| 답변 기록 요청 | 피드백 ID       | 답변을 기록할 피드백의 ID                 |
|                | 답변                 | 피드백에 기록할 답변                             |
| 답변 입력자    | 피드백 ID, 답변 | 전달받은 답변 기록요청                         |
| 알리미         | 답변                 | 교육자에게 전달할 답변 내용                      |
|                | 알림 내용            | 답변이 기록됨을 교육자에게 알리기 위한 알림 내용 |



##### Diagram
-------
![DM206](https://github.com/SSSSEN666789/SPAMS/blob/main/Domain%20Model/Module2_Students/img/DM206.jpg)
