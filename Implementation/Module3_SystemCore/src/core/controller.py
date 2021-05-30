#사용자에게 notify 할 때 어떻게 할 지 모르겠어서 일단은 콘솔에 출력하는것으로 함수 생성
#autoGrade는 evalReq에서 dequeue 할 때 evalReq에 자료가 저장되어있으면
#루프 탈출하고 runTest 실행시켜서 result에 반환, result가 반환이 되었으면 반환값을 가지고 makeReport 실행시켜서
#report 생성. 반환값이 없다면 안내메세지 출력
#근데 report가 원래는 save에 인자로 들어가야 하는데 없어서 not accessed Paylance가 뜸
#testResult에 True와 False를 저장시켜 notify함수 실행시켜 안내메세지 출력함

from .test_runner import TestRunner
from .test_result_processor import TestResultProcessor
from .evaluation_queue import dequeue
from Implementation.Module3_SystemCore.src.core import test_result_processor


class contorller():
    def notify(self):
        if self == True:           
            print("AutoGrade Complete")
        elif self == False:
            print("AutoGrade Fail")
            

    def autoGrade(self):
        while True:
            evalReq = dequeue()
            if evalReq is not None:
                break
        result = TestRunner.runTest(evalReq.language)
        if result is not None:
            report = TestResultProcessor.makeReport(result)
            testResult = True
        else:
            print("runTest Failed")
            testResult = False


        self.notify(testResult)

