# Domain Model for UC - 201 과제 검색

| Responsibility Description                                   | Type | Concept Name      |
| ------------------------------------------------------------ | ---- | ----------------- |
| 각 컨셉들의 동작을 제어하고 다른 컨셉과 연결해준다.          | D    | 컨트롤러          |
| 학생이 찾고자 하는 과제의 정보                   | K    | 과제 검색 요청    |
| 과제 DB와 각 컨셉들을 연결해준다.                            | D    | 과제 DB 커넥션    |
| 학생의 화면에 표시하는 HTML 문서를 렌더링 한다.                | D    | 페이지 생성자     |
| 사용자가 보는 페이지.                                        | K    | 인터페이스 페이지 |

##### Associations

| Concept pair                       | Association Description                                  | Association name |
| ---------------------------------- | -------------------------------------------------------- | ---------------- |
| 과제 탐색요청 -> 컨트롤러          | 찾으려는 과제의 정보 전달                                           | receives         |
| 컨트롤러 -> 과제 DB 커넥션      | 찾으려는 과제를 DB 커넥션에게 검색 요청   | conveys request     |
| 컨트롤러 -> 페이지 생성자          | 컨트롤러가 페이지 생성자에게 요청 전달                   | conveys request  |
| 과제 DB 커넥션 -> 페이지 생성자    | DB 커넥션이 요청받은 과제데이터를 페이지 생성자에게 제공 | provides data    |
| 페이지 생성자 -> 인터페이스 페이지 | 페이지 생성자가 인터페이스 페이지 생성을 준비함.         | prepares         |


##### Attributes

| Concept        | Attributes              | Attribute Description                                        |
| -------------- | ----------------------- | ------------------------------------------------------------ |
| 과제 탐색 요청 | 과제 기본 파라미터      | 과제 이름, 소속 강의, 내용, 마감기한                  |
| 페이지 생성자  | 과제 파라미터 및 플래그 | 과제 탐색 요청으로 과제DB에서 제공받은 과제의 파라미터 및 플래그               |


##### Diagram
-------
![DM201](https://github.com/SSSSEN666789/SPAMS/blob/main/Domain%20Model/Module2_Students/img/DM201.jpg)