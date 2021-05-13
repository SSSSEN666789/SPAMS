# Sequence Diagram for Use Case 204: 제출물 재제출

## System Sequence Diagram
![System Sequence Diagram for UC 204](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/DM204%EC%A0%9C%EC%B6%9C%EB%AC%BC%EC%9E%AC%EC%A0%9C%EC%B6%9C%20Sequence%20Diagram.png)
학생이 제출물 재제출 요청을 보냈을때 시스템은 제출물DB에 기존 제출물 object를 삭제하게 하고 새로 받은 object를 저장하게 한다. 완료되면 교육자에게 제출물이 재제출되었다고 재제출물 정보와 함께 알림을 보내도록 한다.

--------
## Object Sequence Diagram
![Object Sequence Diagram for UC 204](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/UC%20204%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EC%9E%AC%EC%A0%9C%EC%B6%9C%20Sequence%20Diagram.png)
학생이 재제출 요청을 보내면 제출물 제출때와는 달리 db에 해당 과제에 대한 제출물이 존재하는지 검사를 할 필요없이 제출을 진행한다. 대신 재제출에서는 put 메소드를 이용하여 제출물DB에 제출물 오브젝트를 갱신하여 저장하게끔 설계하였다.


### V/a
![Object Sequence Diagram for UC 204 - Variation a](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/UC%20204%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EC%9E%AC%EC%A0%9C%EC%B6%9C%20Sequence%20Diagram%20V_a.png)
1. 제출물 재제출의 초기 모델로써, 재제출 요청시 db에 먼저 기존 제출물 오브젝트를 삭제후 새로운 오브젝트를 생성하여 저장하게끔 설계했다. 
2. put이라는 메소드가 따로있기에 위 모델은 비효율적인 flow를 가져간다고 판단.
3. 추가로 알리미의 필요성이 있다고 판단.
<br />=> 채택하지 않음.

### V/b
![Object Sequence Diagram for UC 204 - Variation b](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/UC%20202%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EC%A0%9C%EC%B6%9C%20Sequence%20Diagram%20V_b.png)
1. 제출물DB커넥션이 controller로 부터 받은 제출물 object s를 활용하여 교육자에게 바로 알림을 전달하는 디자인.
2. Flow도 효율적이고 Controller의 메소드도 줄어들지만 notify 메소드를 제출물 DB커넥션이 가지고있기에는 전문성이 떨어진다고 판단하였다.
<br />=> 채택하지 않음.


--------
