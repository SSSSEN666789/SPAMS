# API List: Module1_Educator

1. [개요](#개요)
2. [API List](#API-List)
   1. [AssignmentEditorNew](#AssignmentEditorNew)
   2. [AssignmentEditorModify](#AssignmentEditorModify)
   3. [AssignmentList](#AssignmentList)
   4. [AssignmentContent](#AssignmentContent)
   5. [RegisterAssignment](#RegisterAssignment)
   6. [ModifyAssignment](#ModifyAssignment)
   7. [SubmissionList](#SubmissionList)
   8. [SubmissionContent](#SubmissionContent)

------

### 개요

Module1의 구현내용에 대한 설명 및 API List를 포함하는 문서.

사용 언어: Python 3.7.3

### 구동 및 작동

SourceCode 폴더 내 main.py를 cmd에서 실행. 

콘솔 창에 "Enter Query: "가 표시되면 테스팅할 문자열을 입력한다.
문자열이 입력되면, 입력된 문자열에 대하여 어떤 오브젝트가 어떤 업무를 하는지가 콘솔에 출력된다.

### 입력 양식

입력은 기본적으로 문자열로 받고, 이를 '쿼리'라고 가정한다.
테스팅에 사용될 쿼리는 아래의 양식을 따른다.

> 요청내용?파라미터1=값1&파라미터2=값2& ... &파라미터n=값n

해당 양식을 따르지 않는 경우 이에 대한 경고 메시지로 'query format error'가 출력된다.

파라미터와 값의 쌍을 '바디'라 칭한다.

1. 한 쿼리 내에서 바디의 순서는 관게 없다.
2. 요청 내용별로 필수로 포함해야 하는 바디의 종류가 다르다.
3. 필수로 포함해야하는 바디를 포함하지 않는 경우 이에 대한 에러 메시지를 출력한다.
4. 제공되지 않는 요청인 경우에도 에러 메러지를 출력한다.

### 기타 사항

class, assignment의 id는 지금은 int로 가정했는데, 실제 구현에서는 UUID가 될 가능성이 높다. 혹은 최종 체크포인트 이전에 수정이 될 수도 있다.

### API List

#### AssignmentEditorNew

 새로운 과제 생성을 위한 에디터 생성 요청.
예시) **AssignmentEditorNew?auth=educator&class=10**

| 바디(파라미터=값 타입) | 설명        | 비고                                                         |
| ---------------------- | ----------- | ------------------------------------------------------------ |
| auth=str               | 계정의 권한 | Educator                                                     |
| class=ID               | 강의실 ID   | **디버깅 용 테스트 id**<br />class = 0000 -> class 자체가 존재하지 않는 것으로 간주<br />class = 9999 -> class에 아직 생성된 과제 목록이 없는 것으로 간주<br />그 외의 경우는 에러 없음. |

#### AssignmentEditorModify

과제 수정을 위한 에디터 생성 요청. 
예시) **AssignmentEditorModify?auth=educator&class=10&assignment=1**

| 바디(파라미터=값 타입) | 설명           | 비고                                                         |
| ---------------------- | -------------- | ------------------------------------------------------------ |
| auth=str               | 계정의 권한    | Educator                                                     |
| class=ID               | 강의실 ID      | 상단 참고.                                                   |
| assignment=ID          | 수정할 과제 ID | **디버깅 용 테스트 id**<br />assignment= 0000 -> 해당 ID를 가진 assignment오브젝트가 DB에 없는 것으로 간주<br />그 외의 경우는 에러 없음. |

#### AssignmentList

과제 목록 요청.
예시) **AssignmentList?auth=educator&class=10**

| 바디(파라미터=값 타입) | 설명                         | 비고       |
| ---------------------- | ---------------------------- | ---------- |
| auth=str               | 계정의 권한                  | Educator   |
| class=ID               | 과제 목록을 불러올 강의실 ID | 상단 참고. |

#### AssignmentContent

과제 내용 요청.
예시) **AssignmentContent?auth=student&class=10&assignment=1**

| 바디(파라미터=값 타입) | 설명                           | 비고              |
| ---------------------- | ------------------------------ | ----------------- |
| auth=str               | 계정의 권한                    | Educator, Student |
| class=ID               | 열람할 과제가 소속된 강의실 ID | 상단 참고.        |
| assignment=ID          | 열람할 과제 ID                 | 상단 참고.        |

#### RegisterAssignment

신규 과제 등록 요청.

예시 - 일반 과제)
**RegisterAssignment?auth=educator&class=10&title=일반과제제목&cont=일반과제내용&deadline=2021-05-28&score=10.0&file=filepath&flag=0&params=False**

예시 - 알고리즘 과제)
**RegisterAssignment?auth=educator&class=10&title=알고리즘과제제목&cont=알고리즘과제내용&deadline=2021-05-28&score=10.0&file=False&flag=1&params=True&code=codepath&openbound=False**

예시 - 퀴즈)

**RegisterAssignment?auth=educator&class=10&title=퀴즈제목&cont=퀴즈내용&deadline=2021-05-28&score=10.0&file=False&flag=2&params=True&quiz=quizpath&openanswer=True**

| 바디(파라미터=값 타입) | 설명                   | 비고                                                         |
| ---------------------- | ---------------------- | ------------------------------------------------------------ |
| auth=str               | 계정의 권한            | Educator                                                     |
| class=ID               | 강의실 ID              | 상단 참고.                                                   |
| title=str              | 과제의 제목            | 신규 과제의 내용.                                            |
| cont=str               | 과제의 내용            | ..                                                           |
| deadline=date          | 과제의 마감기한        | ..<br />yyyy-mm-dd의 형식으로 작성되어야 함.                 |
| score=float            | 과제의 배정 점수       | ..                                                           |
| file=str               | 첨부 파일의 경로       | ..<br />없으면 'False'로 작성. 있으면 파일 경로 작성.        |
| flag=int               | 과제 구분 플래그       | ..<br />0: 일반과제, 1: 알고리즘, 2:퀴즈                     |
| params=boolean         | 플래그별 특수 파라미터 | ..<br />일반 과제의 경우 False로 작성, 알고리즘, 퀴즈의 경우 True로 작성 |
| code=str               | 테스트 코드의 경로     | 알고리즘 전용 바디 1. 파일 경로 작성.                        |
| openbound=str          | 공개 항목              | 알고리즘 전용 바디 2. 공개하는 항목들을 띄어쓰기 없이 나열해서 작성. 없는 경우 False로 작성.<br />예시) openbound=score,runtime,testcase |
| quiz=str               | 퀴즈 내용, 정답의 경로 | 퀴즈 전용 바디 1. 퀴즈 내용과 정답을 담고 있는 파일 경로 작성. |
| openanswer=boolean     | 정답 공개 여부         | 퀴즈 전용 바디 2. 정답 공개 여부를 True, False로 작성.       |

#### ModifyAssignment

기존 과제 수정 요청.
예시)
ModifyAssignment?auth=educator&class=10&assignment=1&title=일반과제수정제목&cont=일반과제수정내용&deadline=2021-05-30&score=30.0&file=filepath&flag=0&params=False

| 바디(파라미터=값 타입) | 설명             | 비고                                                         |
| ---------------------- | ---------------- | ------------------------------------------------------------ |
| -                      | -                | RegisterAssignment의 필요 바디에서 assignment 바디가 추가로 필요함.<br />assignment를 제외한 ModifyAssignment의 값들은 '수정된 내용'을 의미함. |
| assignment=ID          | 수정할 과제의 ID |                                                              |

#### SubmissionList

제출물 목록 요청
예시) SubmissionList?auth=educator&class=10&assignment=1

| 바디(파라미터=값 타입) | 설명                                         | 비고       |
| ---------------------- | -------------------------------------------- | ---------- |
| auth=str               | 계정의 권한                                  | Educator   |
| class=ID               | 제출물 목록을 열람할 과제가 소속된 강의실 ID | 상단 참고. |
| assignment=ID          | 제출물 목록을 열람할 과제 ID                 | 상단 참고. |

#### SubmissionContent

제출물 내용 요청

| 바디(파라미터=값 타입) | 설명                                    | 비고                                                         |
| ---------------------- | --------------------------------------- | ------------------------------------------------------------ |
| auth=str               | 계정의 권한                             | Educator                                                     |
| class=ID               | 제출물이 소속된 과제가 소속된 강의실 ID | 상단 참고.                                                   |
| assignment=ID          | 제출물이 소속된 과제 ID                 | **디버깅 용 테스트 id**<br />assignment=0000 -> 해당 ID를 가진 assignment오브젝트가 DB에 없는 것으로 간주<br />assignment=9999 -> assignment에 제출된 제출물이 없는 것으로 간주<br />그 외의 경우는 에러 없음. |
| submission=ID          | 열람할 제출물 ID                        | **디버깅 용 테스트 id**<br />submission=0000 -> 해당 ID를 가진 submission오브젝트가 DB에 없는 것으로 간주<br />그 외의 경우는 에러 없음. |

