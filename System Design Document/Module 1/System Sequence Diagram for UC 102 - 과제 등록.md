# System Sequence Diagram for UC 102 - 과제 등록

### Object Sequence Diagram

__Version 1__

![ver1](https://user-images.githubusercontent.com/51692363/117978979-65767000-b36d-11eb-8cd3-3bb58c546a42.jpg)



최초 기획안.  과제 목록을 보고 정보를 입력하면 과제 생성자가 과제를 생성하고 db에 저장하는 것까지 설계.

-------

__Version 2__

![ver2](https://user-images.githubusercontent.com/51692363/117979136-8fc82d80-b36d-11eb-822e-d4592819fa1c.jpg)



과제 생성자  모듈이 과제를 생성하고 DB에 저장명령까지 내리는 것이 cohesion이 낮다 생각.

이에 controller가 과제 객체가 생성되면 DB커넥션에 저장 명령을 내리게 함으로 coupling을 낮추고, cohesion을 증가시켰다.

------

**Version 3**

![ver3](https://user-images.githubusercontent.com/51692363/117979193-9eaee000-b36d-11eb-8ae5-c5ae115af8ac.jpg)

쿼리를 받아오고 Controller와 Pagemaker 사이에 parsing과정이 필요할 거라 판단하여 QueryParser 모듈이 파싱 작업을 실행하게 함. ValidCheck 모듈이 권한 검사와 쿼리의 결과가 유효한지 판단함.

과제 목록을 불러와 과제 정보를 입력하여 과제 객체를 생성하는 것 까지 event1이라 하면 과제 객체를 이용해 새로운 page를 만드는 일, 학생에게 생성된 과제에 대한 알림을 보내는 일, 과제DB에 새로운 과제 객체를 저장하는 일이 따라 온다. 근데 각 모듈에 컨트롤러가 따로 따로 호출하는 것보다, LEC11의 pub-sub 구조를 이용하여 과제 생성자가 과제 객체를 생성했다고 controller에게 알리면 controller는 PageMaker, DBconnection, Notifier에게 Doevent() 시그널을 보내 각각의 일을 각 모듈이 처리하게 설계. cohesion이 증가하고 유지보수가 더욱 용이. 

