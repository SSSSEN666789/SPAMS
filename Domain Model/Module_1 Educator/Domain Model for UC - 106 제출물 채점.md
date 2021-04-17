# Domain Model for UC - 106 제출물 채점

| Responsibility Description                          | Type | Concept Name     |
| --------------------------------------------------- | ---- | ---------------- |
| 각 컨셉들의 동작을 제어하고 다른 컨셉과 연결해준다. | D    | 컨트롤러         |
| 교육자가 점수를 입력하려고 하는 제출물의 ID와 점수  | K    | 점수 기록 요청   |
| 점수를 제출물에 추가                                | D    | 채점자           |
| 제출물 DB와 각 컨셉들을 연결해준다.                 | D    | 제출물 DB 커넥션 |

##### Associations

| Concept pair                 | Association Description                           | Association name |
| ---------------------------- | ------------------------------------------------- | ---------------- |
| 점수 기록 요청 -> 컨트롤러   | 점수를 기록할 제출물의 ID와 점수 전달             | receives         |
| 컨트롤러 -> 제출물 DB 커넥션 | 점수를 기록할 제출물을 DB 커넥션에게 반환 요청    | conveys request  |
| 컨트롤러 -> 채점자           | 점수 입력을 요청                                  | conveys request  |
| 체점자 -> 제출물 DB 커넥션   | 입력된 점수를 바탕으로 제출물의 점수를 갱신 요청. | request update   |

##### Attributes

| Concept        | Attributes | Attribute Description         |
| -------------- | ---------- | ----------------------------- |
| 점수 기록 요청 | 제출물 ID  | 제출물 ID                     |
|                | 점수       | 교육자가 입력한 제출물의 점수 |

