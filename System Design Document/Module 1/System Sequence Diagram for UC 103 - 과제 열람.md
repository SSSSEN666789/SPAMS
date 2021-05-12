# System Sequence Diagram for UC 103 - 과제 열람

### Object Sequence Diagram

__Version 1__

![ver1](.\img\OSD for UC103(ver1).JPG)

최초 기획안.  Lec 09 의 UC5의 OSD를 차용하여 작성. 직관적으로 흐름을 간단히 파악가능

-------

__Version 2__

![ver2](.\img\OSD for UC103(ver2).JPG)



과제 목록과 선택한 과제의 정보를 불러오는 get이 중복되어 각자 구분할 수 있는 메소드로 변경.

Query Paser와 Valid Checker 모듈을 추가하여 page를 만드는 과정을 더욱 상세히 묘사. 또한 유효하지 않은 접근에 대해 처리하는 방법 추가.