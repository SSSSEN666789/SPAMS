# System Sequence Diagram for UC 104 - 과제 수정

### Object Sequence Diagram

__Version 1__

![ver1](.\img\OSD for UC104(ver1).JPG)



최초 기획안.  UC 104의 Domain Model을 그대로 구현하여 설계. 직관적으로 간단한 흐름을 볼 수 있음.

-------

__Version 2__

![ver2](.\img\OSD for UC104(ver2).JPG)



과제 생성자가 수정할 내용으로 과제를 생성하면 과제 생성자가 직접 저장 명령을 내리지않고 controller가 명령을 내리는 것으로 변경함으로 cohesion을 좀 더 높힘.

 

------

**Version 3**

![ver3](C:\Users\gu306\SSSSEN\SPAMS\System Design Document\Module 1\img\OSD for UC104(ver3).jpg)

UC 104는 UC 103의 sub Use Case이기에 중복되는 부분은 생략함으로 조금 더 간단히 표기.

수정할 과제의 ID는 이미 쿼리에 포함되어 있으므로 새롭게 객체를 생성하여 추가함과 동시에 기존에 있는 것을 파기하는 것보다 REST API와 같은 API에서는 PUT으로 수정이 가능하다.

그러므로 과제 수정자 모듈이 수정할 내용으로 해당 과제 ID에 put을 요청하여 과제를 수정함으로 과제 오브젝트를 새로 생성하지 않아도 되어 자원 측면에서 좀 더 효율적. 