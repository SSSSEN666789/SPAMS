# Sequence Diagram for Use Case 202: 제출물 제출

## System Sequence Diagram
![System Sequence Diagram for UC 202](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/DM202%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EC%A0%9C%EC%B6%9C%20Sequence%20Diagram.png)
학생이 제출물 제출 요청을 하였을때 시스템에서 제출물 ID를 생성하며 제출물DB에 해당 제출물을 저장하고 교육자에게 제출물이 제출되었다고 알림을 보낸다.

--------
## Object Sequence Diagram
![Object Sequence Diagram for UC 202](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/UC%20202%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EC%A0%9C%EC%B6%9C%20Sequence%20Diagram.png)
학생이 인터페이스 페이지에서 제출 요청을 하면 db에서 제출물이 이미 존재하는지 확인 후, 존재안하면 학생이 제출을 진행하도록 한다. 제출된게 파일이라면 db에 저장을하고, 그게 아니라면 파일 변환자를 통해 텍스트 파일로 변환 후 db에 저장한다. 그뒤에 알리미가 교육자에게 알림을 전달. 


### V/a
![Object Sequence Diagram for UC 202 - Variation a](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/UC%20202%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EC%A0%9C%EC%B6%9C%20Sequence%20Diagram%20V_a.png)
1. 초기에 생각했던 디자인. 
2. Control이 알림까지 할 필요없어보여서 알리미를 따로 두기로 결정함. 
<br />=> 채택하지 않음.

### V/b
![Object Sequence Diagram for UC 202 - Variation b](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/UC%20202%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EC%A0%9C%EC%B6%9C%20Sequence%20Diagram%20V_b.png)
1. Contrller의 비중을 덜고 제출물 DB 커넥션이 필요한 정보를 다 가지고있으니 교육자에게 다이렉트로 알림을 보내게 하는 설계이다.
2. Controller의 메소드 수를 줄일 수 있지만 제출물 DB 커넥션 오브젝트의 전문성이 떨어지게된다.
3. 각 오브젝트간의 전문성이 떨어지게 되는게 더 좋지 못한 디자인이라고 판단하여 이 디자인을 채택하지않았다.


--------
