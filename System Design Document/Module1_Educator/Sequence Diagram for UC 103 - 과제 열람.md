# System Sequence Diagram for UC 103 - 과제 열람

### Object Sequence Diagram

__최종 채택 시안__ : [Version 4](#version-4)</br>

##### Version 1

![ver1](img/OSD%20for%20UC103(ver1).jpg)

최초 기획안.  Lec 09 의 UC5의 OSD를 차용하여 작성. 직관적으로 흐름을 간단히 파악가능

-------

##### Version 2

![ver2](img/OSD%20for%20UC103(ver2).jpg)



과제 목록과 선택한 과제의 정보를 불러오는 get이 중복되어 각자 구분할 수 있는 메소드로 변경.

Query Paser와 Valid Checker 모듈을 추가하여 page를 만드는 과정을 더욱 상세히 묘사. 또한 유효하지 않은 접근에 대해 처리하는 방법 추가.

------

##### Version 3

![ver3](img/OSD%20for%20UC103(ver3).jpg)

OSD for UC102의 Version4와 마찬가지로 chkResult를 ValidChecker가 결과를 판단하는 버전.

역시 ValidChecker가 chkResult의 결과에 따른 메시지를 pageMaker에 보내줌으로 pageMaker는 페이지를 생성하는 메소드만 가지면 됨. cohesion을 조금 더 증가.

-------

##### Version 4

![ver4](img/OSD%20for%20UC103(ver4).png)

ValidChecker가 Publisher가 되는 것이 적절하지 않다는 피드백을 수용, EventPublisher 오브젝트를 추가하여 이벤트 중개를 담당하게 함.

