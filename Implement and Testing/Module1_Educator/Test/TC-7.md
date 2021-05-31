---

---

#### Test-case Identifier: TC-7

#### Use Case Tested: UC-104, sub success scenario - algorithm

#### Pass/fail Criteria: 콘솔을 통해 쿼리를 입력했을 때 과제이름, DB에 저장, Notifier 알림, 페이지메이커의 렌더링 메시지 출력

#### Input Data: Request?Author&classID&assignmentID&title&contents&deadline dataformat&Numeric socre&filepath&flag&params&codepath&openbound

ex) ModifyAssignment?auth=educator&class=10&assignment=1&title=알고리즘과제제목&cont=알고리즘과제내용&deadline=2021-05-28&score=10.0&file=False&flag=1&params=True&code=codepath&openbound=False

------

#### Test Procedure:

Step 1. Type in an incorrect codepath and  valid other input datas

Test Data: codepath='test'
	ModifyAssignment?auth=educator&class=10&assignment=1&title=알고리즘과제제목&cont=알고리즘과제내용&deadline=2021-05-28&score=10.0&file=False&flag=1&params=True&code=codepath&openbound=False

Expected Result: 코드 경로가 잘못되었음을 시스템이 인지하고, 잘못된 코드 경로가 입력되었다는 경고 메시지 생성 및 출력

Result:

![TC-7 step1](https://user-images.githubusercontent.com/51692363/120156567-0fd70a00-c22d-11eb-9e9b-f4459115c480.JPG)

Step 2. Type in a correct deadline and valid other input datas

Test Date: ModifyAssignment?auth=educator&class=10&assignment=1&title=알고리즘과제제목&cont=알고리즘과제내용&deadline=2021-05-28&score=10.0&file=False&flag=1&params=True&code=codepath&openbound=False

Expected Result: 시스템이 과제를 생성, 제목 출력, 과제 DB에 저장, 학생에게 알림 발송, 과제 내용 포함한 페이지 출력

Result:

![TC-7 step2](https://user-images.githubusercontent.com/51692363/120156572-11083700-c22d-11eb-935d-416acfc90d01.JPG)

------

#### Passed: Step2

#### Failed: Step1

codepath가 잘못되었음을 오류로 인식하지 못함.