# Domain Model for UC - 109 질문 열람

| Responsibility Description                          | Type | Concept Name      |
| --------------------------------------------------- | ---- | ----------------- |
| 각 컨셉들의 동작을 제어하고 다른 컨셉과 연결해준다. | D    | 컨트롤러          |
| 질문 게시판이 소속된 강의실의 ID.                   | K    | 질문 목록 요청    |
| 열람을 요청한 질문 게시물의 ID.                     | K    | 질문 열람 요청    |
| 질문 DB와 각 컨셉들을 연결함.                       | D    | 질문 DB 커넥션    |
| 교육자의 화면에 표시하는 HTML 문서를 렌더링 한다.   | D    | 페이지 생성자     |
| 사용자가 보는 페이지.                               | K    | 인터페이스 페이지 |

##### Associations

| Concept pair                       | Association Description                                      | Association name |
| ---------------------------------- | ------------------------------------------------------------ | ---------------- |
| 질문 목록 요청 -> 컨트롤러         | 강의실 ID 전달                                               | receives         |
| 질문 열람 요청 -> 컨트롤러         | 질문 게시물 ID 전달                                          | receives         |
| 컨트롤러 -> 질문 DB 커넥션         | 컨트롤러가 질문 DB 커넥션에게 검색 요청                      | conveys request  |
| 컨트롤러 -> 페이지 생성자          | 컨트롤러가 받은 요청의 내용과 종류 전달.                     | conveys request  |
| 컨트롤러 -> 인터페이스 페이지      | 인터페이스 페이지에게 게시 요청.                             | posts            |
| 질문 DB 커넥션 -> 페이지 생성자    | DB 커넥션이 요청받은 질문 목록 혹은 질문 게시물의 내용을 페이지 생성자에 게 제공 | provides data    |
| 페이지 생성자 -> 인터페이스 페이지 | 페이지 생성자가 인터페이스 페이지 생성을 준비함.             | prepares.        |

##### Attributes

| Concept        | Attributes       | Attribute Description                     |
| -------------- | ---------------- | ----------------------------------------- |
| 질문 목록 요청 | 강의실 ID        | 질문 목록을 출력할 강의실의 ID            |
| 질문 열람 요청 | 질문 게시물 ID   | 열람하고자 하는 질문 게시물의 ID          |
| 페이지 생성자  | 질문 목록        | DB 커넥션에게 제공받은 질문의 목록        |
|                | 질문 게시물 내용 | DB 커넥션에게 제공받은 질문 게시물의 내용 |

##### Diagram
-------
![DM109](img/DM109.jpg)