# Implement and Testing: Module 1

모듈 1의 소스코드 구현과 테스팅에 관한 폴더

사용 언어 및 버전: Python 3.7.3

### 구현 관련

파이썬은 interface가 따로 없는 관계로 추상 클래스로 비슷하게 구현함.

### Source Code 구동 

SourceCode 폴더에서 main.py 실행

### Source Code API List



### 논의 사항

valid checker에서 각 DB에 커넥션 만들어줘야 될 것 같다.
Class diagram에서 어떤게 어떤 이벤트 구독하고 있는지 써둘걸...
event_createAssignmentEditor는 파라미터별로 안나눠도 될듯. 어차피 다 param으로 퉁쳤음.
pagemaker는 좀 특별히 처리해야할듯. 그냥 subs로 퉁쳐버리면 안됨. pageMaker의 결과를 받아와야함.

데코레이터들한테 이벤트 별로 메소드 따로 줄 필요 없을 것 같다. 그냥 쿼리에 요청사항 포함돼있으면 되는거 아니야?
메소드 이름은 createPage로 퉁치자. InterfacePage라는 바운더리가 Controller에게 Page 만들어 달라고 요청하는거니까.

-> 여기에 맞춰서 Class Diagram만 좀 수정하자.



쿼리스트링: 요청사항?파라미터1=값&파라미터2=값& ~~~ &파라미터n=값
요청사항에?가 들어면 안됨.
? 이후에 파라미터=값 혹은 바디 별 구분을 위한 & 외에는 =와 &이 들어가면 안됨.
바디의 순서는 바뀌어도 상관 없음.

__Request Assignment Editor:__

필요 바디
auth: 요청자 권한. 사실 리퀘스트의 헤더에 들어가는게 맞는데, 테스팅을 위해서 일단은 바디에 속해있는 것으로 간주하고 구현
class: 과제를 작성 혹은 수정할 강의실 id
assignment: 수정할 과제의 id. 새로운 과제 작성일 경우엔 없어도 되고, 기존 과제 수정일 경우 있어야함.

예시: AssignmentEditor?auth=educator&class=10

__Request Assignment List:__

필요 바디
auth: 요청자 권한
class: 과제목록을 열람할 강의실 id
예시: AssignmentList?auth=educator&class=10

__Request Assignment Content:__

필요 바디
auth: 요청자 권한
class: 과제내용을 열람할 강의실 id
assignment: 요청 과제 id
예시: AssignmentContent?auth=student&class=10&assignment=1

__Request Register Assignment:__

필요 바디

요청 과제 id는 등록할 때 서버에서 생성됨.

auth: 요청자 권한
class: 과제를 등록할 강의실 id
title: 과제 제목
cont: 과제 내용
deadline: 마감 기한(yyyy-mm-dd 형식으로 작성할 것)
score: 배정 점수
file: 과제에 첨부할 파일. 없으면 False로 작성. 있으면 경로 작성
flag: 과제 구분 플래그 (0: 일반 과제, 1: 알고리즘, 2: 퀴즈)
params: 플래그 별 특수 파라미터. 
일반 과제의 경우 False로 작성.
알고리즘 과제, 퀴즈의 경우 True로 작성.
code: 알고리즘 전용 파라미터. 테스트 케이스를 돌리기 위한 코드. 실제로는 파일 경로가 될 것 같은데, 임의의 내용이 들어간다고 가정하고 작성.
openbound: 알고리즘 전용 파라미터. 공개하는 항목들을 나열해서 작성. 없는 경우 False로 작성
ex) openbound=score,runtime,testcase
quiz: 퀴즈 전용 파라미터. 퀴즈 내용과 정답을 담고 있는 파일 path가 될 것 같음.
openanswer: 퀴즈 전용 파라미터. 정답 공개 여부를 True, False로 작성.

예시-일반 과제: 
RegisterAssignment?auth=educator&class=10&title=일반과제제목&cont=일반과제내용&deadline=2021-05-28&score=10.0&file=filepath&flag=0&params=False

예시-알고리즘 과제: 
RegisterAssignment?auth=educator&class=10&title=알고리즘과제제목&cont=알고리즘과제내용&deadline=2021-05-28&score=10.0&file=False&flag=1&params=True&code=codepath&openbound=False

예시-퀴즈:
RegisterAssignment?auth=educator&class=10&title=퀴즈제목&cont=퀴즈내용&deadline=2021-05-28&score=10.0&file=False&flag=2&params=True&quiz=quizpath&openanswer=True

__Request Modify Assignment:__

대응 메소드: modifyAssignmentObject

필요바디

Request Register Assignment와 동일하나, 
assignment: 수정할 과제의 id 

예시-일반 과제: 
ModifyAssignment?auth=educator&class=10&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=30.0&file=filepath&flag=0&params=False

__Request Submission List:__

대응 메소드: createSubList

필요바디
auth: 요청자 권한
class: 제출물 목록을 불러올 강의실 id
assignment: 제출물 목록을 불러울 과제 id
예시: SubmissionList?auth=educator&class=10&assignment=1

__Request Submission Content:__

대응 메소드: createSubCont

필요바디
auth: 요청자 권한
class: 제출물 내용을 불러올 강의실 id
assignment: 제출물 내용을 불러울 과제 id
submission: 제출물 id
예시: SubmissionContent?auth=educator&class=10&assignment=1&submission=27



ValidChecker에서 에러 유형

검사 순서:
권한 -> 바디 유무 -> DB에 유무 -> 바디별 포멧, 값

바디가 없을 때: 'body: 바디이름 is not exist.'
값 형식이 잘못되었을 때: 'Wrong format -> body: 바디이름=입력값'
값 자체가 잘못되었을 때: 'Wrong value-> body: 바디이름=입력값'
아무튼 값이 뭔가 잘못되었을 때: ex) 'Wrong date -> body: deadline=입력값'

입력한 ID에 해당하는 내용을 DB에서 못 찾았을 때: 'Cannot find 입력ID in 해당DB'
