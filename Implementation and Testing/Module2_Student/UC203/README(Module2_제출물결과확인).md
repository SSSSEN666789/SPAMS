# Implement and Testing: Module 2_제출물 결과확인


### Interface 관련
Module2의 제출물 제출 및 재제출 implementation에서 있는 "제출 결과 확인"을 학생이 요청하였을 때로 가정을 하고 해당 과제와 제출물ID가 input으로 들어오는 시점부터 구현을 하였음.

### 제출물DB에 대하여
모듈3가 제공하는 제출물 결과 값들 포맷에 맞춰서 텍스트파일에 기입하여 임시로 제출물 DB로 사용하였음.

### 구동 및 작동

제출물 제출 및 재제출에서 "제출 결과 확인" 을 요청 하고 제출물 ID를 제공받는다고 가정하고 시작하기에 main에 SubmissionDBConnection 메소드에 임의로 정한 subID(제출물ID) 값을 넣어주고 시작한다. 

테스팅을 하기위해서는 subID값을 변경해주면 된다.

프로그램이 실행되면 각 클래스에서 자기역할들을 수행했다면서 임의로 메세지를 출력하게 한다. 예시로
PageMaker가 호출이되어서 작동을 하기시작하면 콘솔창에 Rendering Result를 하는중이라는 메세지를 띄운다.

### 정상 작동 결과값
![properResult](img/properResult.png)

정상적인 요청을 하였을시 이런식으로 학생이 요청한 제출물에 대한 결과값들을 제공한다. 



