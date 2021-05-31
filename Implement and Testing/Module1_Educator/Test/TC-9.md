---

---

#### Test-case Identifier: TC-8

#### Use Case Tested: UC 공통, sub success scenario

#### Pass/fail Criteria: 콘솔을 통해 쿼리를 입력했을 때 쿼리에 해당하는 페이지 출력

#### Input Data: Request?Author&classID&assignmentID

ex) SubmissionList?auth=educator&class=10&assignment=1

------

#### Test Procedure:

Step 1. Type in more body.

ex)AssignmentList?auth=educator&class=10&assignment=1

Expected Result: 필요 이상의 body가 입력되었음을 시스템이 감지하고 body가 너무 많다는 경고 메시지 출력

Result:

![TC-9 step1](https://user-images.githubusercontent.com/51692363/120173369-ee7f1980-c23e-11eb-86e2-1a7610732653.JPG)

Step 2. Type in incorrect query format

ex)asdczmxnjknad;

Expected Result: classID 형식이 잘못되었음을 시스템이 인지하고, 잘못된 쿼리 라는 경고 메시지 생성 및 출력

Result:

![TC-9 step2](https://user-images.githubusercontent.com/51692363/120173591-1ec6b800-c23f-11eb-8d14-46d0120ce00d.JPG)





------

#### 

#### Failed: Step1, Step2

불필요한 body가 입력되었음에도 오류로 인식못함.

쿼리가 잘못된 형식이 들어오면 작동이 안되고 프로그램이 터짐.