# System Sequence Diagram for UC 104 - 과제 수정

### Object Sequence Diagram

__최종 채택 시안__ : [Version 5](#version-5)</br>

##### Version 1

![ver1](img/OSD%20for%20UC104(ver1).jpg)



최초 기획안.  UC 104의 Domain Model을 그대로 구현하여 설계. 직관적으로 간단한 흐름을 볼 수 있음.

-------

##### Version 2

![ver2](img/OSD%20for%20UC104(ver2).jpg)



과제 생성자가 수정할 내용으로 과제를 생성하면 과제 생성자가 직접 저장 명령을 내리지않고 controller가 명령을 내리는 것으로 변경함으로 cohesion을 좀 더 높힘.

 

------

##### Version 3

![OSD for UC104(ver3)](img/OSD%20for%20UC104(ver3).jpg)

UC 104는 UC 103의 sub Use Case이기에 중복되는 부분은 생략함으로 조금 더 간단히 표기.

수정할 과제의 ID는 이미 쿼리에 포함되어 있으므로 새롭게 객체를 생성하여 추가함과 동시에 기존에 있는 것을 파기하는 것보다 REST API와 같은 API에서는 PUT으로 수정이 가능하다.

그러므로 과제 수정자 모듈이 수정할 내용으로 해당 과제 ID에 put을 요청하여 과제를 수정함으로 과제 오브젝트를 새로 생성하지 않아도 되어 자원 측면에서 좀 더 효율적. 

------

##### Version 4

![OSD for UC104(ver4)](img/OSD%20for%20UC104(ver4).jpg)

OSD for UC102의 Version4와 마찬가지로 chkResult를 ValidChecker가 결과를 판단하는 버전.

역시 ValidChecker가 chkResult의 결과에 따른 메시지를 pageMaker에 보내줌으로 pageMaker는 페이지를 생성하는 메소드만 가지면 됨. cohesion을 조금 더 증가.

-------

##### Version 5

![ver4](img/OSD%20for%20UC104(ver5).png)

ValidChecker가 Publisher가 되는 것이 적절하지 않다는 피드백을 수용, EventPublisher 오브젝트를 추가하여 이벤트 중개를 담당하게 함.

추가로, DB 커넥션에 수정기능을 직접 구현하는 것으로 가정하고 Assignment Modifier 오브젝트를 제거함. Assignment Maker는 Assignment 오브젝트 자체를 생성하기 위한 것인데, 그렇게 생성된 Assignment 오브젝트는 그 자체에 의미가 있다기보단, 다른 오브젝트의 매개변수로 사용하기 위한 것임. 이미 DB에 모델의 값이 들어가 있는 상황에서는 API에서 제공할 PUT 등의 리퀘스트로 값을 수정해주면 됨. 
이런 상황에서 DB 커넥션에게 부여되어도 무리가 없는 responsibility를 굳이 Assignment Modifier에게 맡겨서 coupling을 높힐 필요가 없다고 판단해 해당 object를 제거함.

