---

---

#### Test-case Identifier: TC-8

#### Use Case Tested: UC-104, sub success scenario - quiz

#### Pass/fail Criteria: 콘솔을 통해 쿼리를 입력했을 때 과제이름, DB에 저장, Notifier 알림, 페이지메이커의 렌더링 메시지 출력

#### Input Data: Request?Author&classID&assignmentID&title&contents&deadline dataformat&Numeric socre&filepath&flag&params&quizpath&openanswer

ex) ModifyAssignment?auth=educator&class=10&assignment=1&title=퀴즈제목&cont=퀴즈내용&deadline=2021-05-28&score=10.0&file=False&flag=2&params=True&quiz=quizpath&openanswer=True

------

#### Test Procedure:

Step 1. Type in an incorrect quizpath and  valid other input datas

Test Data: quizpath='test'
	ModifyAssignment?auth=educator&class=10&assignment=1&title=퀴즈제목&cont=퀴즈내용&deadline=2021-05-28&score=10.0&file=False&flag=2&params=True&quiz=quizpath&openanswer=True

Expected Result: 코드 경로가 잘못되었음을 시스템이 인지하고, 잘못된 코드 경로가 입력되었다는 경고 메시지 생성 및 출력

Result:

![TC-8 step1](img/TC-8%20step1.jpg)

Step 2. Type in valid other input datas

Test Date: ModifyAssignment?auth=educator&class=10&assignment=1&title=퀴즈제목&cont=퀴즈내용&deadline=2021-05-28&score=10.0&file=False&flag=2&params=True&quiz=quizpath&openanswer=True

Expected Result: 시스템이 과제를 생성, 제목 출력, 과제 DB에 저장, 학생에게 알림 발송, 과제 내용 포함한 페이지 출력

Result:

![TC-8 step2](img/TC-8%20step2.jpg)

------

#### Passed: Step2

#### Failed: Step1

quizpath가 잘못되었음을 오류로 인식 못함.