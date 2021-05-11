# System Sequence Diagram for UC 105 - 제출물 열람

### Object Sequence Diagram

__최종 채택 시안__ : [Version 3](#Version 3)</br>

##### Version 1

![ver1](img/OSD%20for%20UC105(ver1).png)



최초 기획안.  Lec 09 - p.27의 내용을 차용하여, 컨트롤러의 중점을 두고 생각나는대로 직감적으로 설계.

플로우가 직관적이고 이해하기 쉬우나, 컨트롤러가 하는 일이 너무 많다. 쿼리 파싱, DB에 반환 요청, 권한 검사 요청 작업이 모두 컨트롤러에게 몰려있기 때문에 유지 보수면에서 불리하다고 판단된다.

-------

##### Version 2

![ver2](img/OSD%20for%20UC105(ver2).png)



Lec 11의 설계 패턴 중, Decorator 패턴의 구조를 차용함. 메소드의 파라미터가 바뀌기 때문에 엄밀하게 Decorator 패턴에 일치하는지는 잘 모르겠다. 아무튼 결과적으로는 컨트롤러에게 과부하 되었던 responsibility를 적절히 분배하여, 각 오브젝트들의 cohesion을 높힐 수 있었음.

또 QueryParser 오브젝트를 새로이 만들어 Controller와 PageMaker 사이에서 필요한 파싱 작업을 하게 해주었음.
권한 검사 부분을 담당하는 새로운 오브젝트를 만들어야 할지 고민했었는데, 어차피 PageMaker는 파싱된 결과에 따라서 페이지를 생성하는데, 권한에 대한 부분 또한 파싱 결과에 포함되기 때문에 굳이 오브젝트를 나눠서 플로우를 늘릴 필요는 없다고 판단하였음. 
데코레이터 패턴으로 치면, PageMaker가 만들어내는 page가 real object라고 생각하면 될 듯 함.

쿼리스트링의 구조가 바뀐다든지 하는 부분에서 유지보수가 더욱 용이해질 것으로 예상된다.

-------

##### Version 3

![ver3](img/OSD%20for%20UC105(ver3).png)

첫째로, 각 요청이 유효하지 않은 경우가 있을 수 있다고 생각했음. QueryParser가 파싱한 결과를 바탕으로 해당 쿼리가 유효한지 판단하는 ValidChecker를 추가함.
둘째로, Version2에서는 권한 검사에 대한 부분을 QueryParser와 PageMaker가 진행했었는데, ValidChecker의 추가에 따라 해당 responsibility들은 ValidChecker에게 넘어갔음. 권한 검사 또한 쿼리 유효성 검사의 일환이기 때문에 해당 업무는 ValidChecker가 담당하는 것이 적절해 보인다.

결과적으로 QueryParser는 오직 쿼리를 파싱하는 일만 할 것이고, 그 쿼리를 분석하는 일은 ValidChecker가 담당할 것이고, PageMaker는 그 결과를 바탕으로 페이지를 생성하게 되어, Version2에 비해 QueryParser와 PageMaker의 응집도가 높아졌음.

'어떤 요청이 유효한 요청인가?'에 대한 정책이 바뀔 경우에 대한 유지보수성이 높아질 것으로 기대된다.