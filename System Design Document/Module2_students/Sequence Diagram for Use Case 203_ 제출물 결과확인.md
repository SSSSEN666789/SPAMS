# Sequence Diagram for Use Case 203: 제출물 결과확인

## System Sequence Diagram
![System Sequence Diagram for UC 203](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/DM203%EC%A0%9C%EC%B6%9C%EB%AC%BC%EA%B2%B0%EA%B3%BC%ED%99%95%EC%9D%B8%20Sequence%20Diagram.png)
학생이 제출물 결과 확인 요청을 하였을때 시스템에서 제출물DB에게 해당 제출물에 대한 가공된 데이터 및 결과값을 요청하고 제출물DB는 해당 데이터를 시스템에 반환한다. 시스템은 해당 데이터를 페이지에 게시하고 제출물 결과 페이지를 학생에게 제공한다.

--------
## Object Sequence Diagram
![Object Sequence Diagram for UC 203](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/DM%20203%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EA%B2%B0%EA%B3%BC%ED%99%95%EC%9D%B8%20Object%20Sequence%20Diagram.png)
학생이 인터페이스 페이지를 통해 결과 확인 요청을 하면 이를 전달받은 Controller는 제출물DB커넥션에게 retrieve()로 결과 반환 명령을 내린다. 반환 받은 데이터를 페이지 메이커에서 렌더링하게끔 명령을 내리고 페이지 메이커는 조건문에 맞는 결과값을 렌더링하여 인터페이스 페이지에 저장. 마지막으로 컨트롤러가 인터페이스 페이지에 게시 명령을 내려 학생에게 데이터를 제공한다.


### V/a
![Object Sequence Diagram for UC 203 - Variation a](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/DM%20203%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EA%B2%B0%EA%B3%BC%ED%99%95%EC%9D%B8%20Object%20Sequence%20Diagram%20V_a.png)
1. 가공된 제출물 결과 데이터값을 Controller 말고 다른 memset에 보관하고 싶을때를 위해 결과 확인자라는 object를 추가한 디자인이다.
2. 고려해볼만 했지만 채널이 불필요하게 길어지게 되어 배제했다.
<br />=> 채택하지 않음.

### V/b
![Object Sequence Diagram for UC 203 - Variation b](https://github.com/SSSSEN666789/SPAMS/blob/Module2_ssd/System%20Design%20Document/Module2_students/img/DM%20203%20%EC%A0%9C%EC%B6%9C%EB%AC%BC%20%EA%B2%B0%EA%B3%BC%ED%99%95%EC%9D%B8%20Object%20Sequence%20Diagram%20V_b.png)
1. 제출물DB커넥션이 제출물DB로부터 받은 결과값을 페이지메이커에 바로 전달하면서 렌더링 명령을 내리는 디자인.
2. 결과 값을 전달하는것 까진 괜찮으나 렌더링 명령까지 내리는건 해당 오브젝트의 전문성이 떨어진다고 판단했다.
<br />=> 채택하지 않음.


--------
