---

---

#### Test-case Identifier: TC-3

#### Use Case Tested: UC-102, sub success scenario - quiz

#### Pass/Fail Criteria: 콘솔을 통해 쿼리를 입력했을 때 과제 이름, DB에 저장, Notifier 알림, 페이지 메이커의 랜더링 메시지 출력

#### Input Data: Request?Author&class&title&cont&deadline dataformat&Numeric score&filepath&flag&boolean params&quizpath&openbound

ex) RegisterAssignment?auth=educator&class=10&title=알고리즘과제제목&cont=알고리즘과제내용&deadline=2021-05-28&score=10.0&file=False&flag=1&params=True&code=codepath&openbound=False

------

#### Test Procedure:

Step 1. Type in an incorrect flag and  valid other input datas

Test Data: RegisterAssignment?auth=educator&class=10&title=퀴즈제목&cont=퀴즈내용&deadline=2021-05-28&score=10.0&file=False&flag=-1&params=True&quiz=quizpath&openanswer=True

Expected Result: flag가 잘못되었음 시스템이 인지하고, 잘못된 flag가 입력되었다는 경고 메시지 생성 및 출력

Result:

![TC-3 step1](https://user-images.githubusercontent.com/51692363/120154541-f634c300-c22a-11eb-9590-a686a5d6da1f.JPG)

Step 2. Type in an incorrect codepath and  valid other input datas

Test Data: Test Data: quizpath='test'
	RegisterAssignment?auth=educator&class=10&title=퀴즈제목&cont=퀴즈내용&deadline=2021-05-28&score=10.0&file=False&flag=2&params=True&quiz=quizpath&openanswer=True

Expected Result: 코드 경로가 잘못되었음을 시스템이 인지하고, 잘못된 코드 경로가 입력되었다는 경고 메시지 생성 및 출력

Result:![TC-3 step2](https://user-images.githubusercontent.com/51692363/120154545-f6cd5980-c22a-11eb-9c6c-6b1feeea66ec.JPG)

Step 3. Type in  valid other input datas

Test Date: RegisterAssignment?auth=educator&class=10&title=퀴즈제목&cont=퀴즈내용&deadline=2021-05-28&score=10.0&file=False&flag=2&params=True&quiz=quizpath&openanswer=True

Expected Result: 시스템이 과제를 생성, 제목 출력, 과제 DB에 저장, 학생에게 알림 발송, 과제 내용 포함한 페이지 출력

Result:![TC-3 step3](https://user-images.githubusercontent.com/51692363/120154548-f765f000-c22a-11eb-96dd-fc2483245e78.JPG)

------

#### Passed: Step1, Step3

#### Failed: Step2

quizpath가 올바르지 못함에도 오류로 인식 못함.