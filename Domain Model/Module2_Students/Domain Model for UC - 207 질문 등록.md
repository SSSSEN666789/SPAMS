# Domain Model for UC - 207 질문 등록

| Responsibility Description                          | Type | Concept Name     |
| --------------------------------------------------- | ---- | ---------------- |
| 각 컨셉들의 동작을 제어하고 다른 컨셉과 연결해준다. | D    | 컨트롤러         |
| 학생이 입력한 질문 내용                         | K    | 질문 입력 요청 |
| 질문을 질문 게시판에 추가한다.                         | D    | 질문 입력자    |
| 질문DB와 각 컨셉들을 연결해준다.                 | D    | 질문 DB 커넥션   |

##### Associations

| Concept pair                    | Association Description                          | Association name |
| ------------------------------- | ------------------------------------------------ | ---------------- |
| 질문 입력 요청 -> 컨트롤러    | 질문을 입력할 강의실 ID와 입력할 질문 전달 | receives         |
| 컨트롤러 -> 질문 입력자       | 코멘트 입력을 요청                               | conveys request  |
| 질문 입력자 -> 질문 DB 커넥션 | 코멘트가 입력된 제출물로 등록 요청             | requests update  |

##### Attributes

| Concept          | Attributes | Attribute Description       |
| ---------------- | ---------- | --------------------------- |
| 질문 입력 요청 | 내용       | 학생이 입력한 코멘트 내용 |
| 질문 입력자 | 강의실 ID | 질문을 입력할 강의실의 ID |
|  | 내용 | 게시판에 입력할 질문 |



##### Diagram
-------
![DM207](https://github.com/SSSSEN666789/SPAMS/blob/main/Domain%20Model/Module2_Students/img/DM207.jpg)