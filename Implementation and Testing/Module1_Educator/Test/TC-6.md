---

---

#### Test-case Identifier: TC-6

#### Use Case Tested: UC-104, main success scenario

#### Pass/fail Criteria: 콘솔을 통해 쿼리를 입력했을 때 과제이름, DB에 저장, Notifier 알림, 페이지메이커의 렌더링 메시지 출력

#### Input Data: Request?Author&classID&assignmentID&title&contents&deadline dataformat&Numeric socre&filepath&flag&params

ex) ModifyAssignment?auth=educator&class=10&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=30.0&file=filepath&flag=0&params=False

------

#### Test Procedure:

Step 1. Type in an incorrect Request and  valid other input datas

Test Data: Modify?auth=educator&class=10&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=30.0&file=filepath&flag=0&params=False

Expected Result:  요청이 잘못되었음을 시스템이 인지하고 경고 메시지 생성 및 출력

Result:

![TC-6 step1](https://user-images.githubusercontent.com/51692363/120156423-eddd8780-c22c-11eb-97fd-61b2a8a9ec00.JPG)

Step 2. Type in an incorrect Author and  valid other input datas

Test Data: ModifyAssignment?auth=student&class=10&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=30.0&file=filepath&flag=0&params=False

Expected Result: 접근 권한이 잘못되었음을 시스템이 인지하고, 접근 권한이 없음을 경고 메시지 생성 및 출력

Result:

![TC-6 step2](https://user-images.githubusercontent.com/51692363/120156425-eddd8780-c22c-11eb-8de7-6d95d6987368.JPG)

Step 3. Type in an incorrect classID and  valid other input datas

Test Data: ModifyAssignment?auth=educator&class=test&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=30.0&file=filepath&flag=0&params=False

Expected Result: classID가 잘못되었음을 시스템이 인지하고, 접근할 수 없는 class라는 경고 메시지 생성 및 출력

Result:

![TC-6 step3](https://user-images.githubusercontent.com/51692363/120156426-ee761e00-c22c-11eb-8ca1-6f89fbca73b1.JPG)

Step 4. Type in an incorrect assignmentID and  valid other input datas

Test Data: ModifyAssignment?auth=educator&class=10&assignment=test&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=30.0&file=filepath&flag=0&params=False

Expected Result: assignmentID가 잘못되었음을 시스템이 인지하고, 접근할 수 없는 assignment라는 경고 메시지 생성 및 출력

Result:

![TC-6 step4](https://user-images.githubusercontent.com/51692363/120156428-ee761e00-c22c-11eb-9932-d6439958dd14.JPG)

Step 5. Type in blank in title and  valid other input datas

Test Data: ModifyAssignment?auth=educator&class=10&assignment=1&title=&cont=일반과제수정내용&deadline=2021-05-30&score=30.0&file=filepath&flag=0&params=False

Expected Result: 과제 제목이 입력되지 않았음을 시스템이 인지하고, 과제 제목을 입력하라는 경고 메시지 생성 및 출력

Result:

![TC-6 step5](https://user-images.githubusercontent.com/51692363/120156430-ef0eb480-c22c-11eb-9550-b7a9cc628cdc.JPG)

Step 6. Type in an incorrect deadline and  valid other input datas

Test Data: ModifyAssignment?auth=educator&class=10&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=1999-05-30&score=30.0&file=filepath&flag=0&params=False

Expected Result: 지정할 수 없는 마감일이 지정되었음을 시스템이 인지하고, 잘못된 마감일이 입력되었다는 경고 메시지 생성 및 출력

Result:

![TC-6 step6](https://user-images.githubusercontent.com/51692363/120156432-ef0eb480-c22c-11eb-9de4-38e082199cd2.JPG)

Step 7. Type in a character score value and  valid other input datas

Test Data: ModifyAssignment?auth=educator&class=10&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=test&file=filepath&flag=0&params=False

Expected Result: 잘못된 형식의 점수가 입력되었음을 시스템이 인지하고, 점수에는 숫자만 입력할 수 있다는 경고 메시지 생성 및 출력

Result:

![TC-6 step7](https://user-images.githubusercontent.com/51692363/120156435-efa74b00-c22c-11eb-9f2d-2124a9d11ce8.JPG)

Step 8. Type in an incorrect score value and  valid other input datas

Test Data: ModifyAssignment?auth=educator&class=10&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=-30.0&file=filepath&flag=0&params=False

Expected Result: 잘못된 범위의 점수가 입력되었음을 시스템이 인지하고, 점수 범위가 잘못되었다는 경고 메시지 생성 및 출력

Result:

![TC-6 step8](https://user-images.githubusercontent.com/51692363/120156437-efa74b00-c22c-11eb-991e-b1f1aab46c78.JPG)

Step 9. Type in an invalid filepath and  valid other input datas

Test Data: filepath='test'
	 ModifyAssignment?auth=educator&class=10&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=30.0&file=filepath&flag=0&params=False

Expected Result: 잘못된 파일 경로가 입력되었음을 시스템이 인지하고, 파일 경로가 잘못되었다는 경고 메시지 생성 및 출력

Result:

![TC-6 step9](https://user-images.githubusercontent.com/51692363/120156440-f03fe180-c22c-11eb-9c89-f39df4ddc21f.JPG)

------

#### Passed: Step1, Step2, Step9

#### Failed: Step3, Step4 ,Step5, Step6, Step7, Step8

TC-1과 동일.

