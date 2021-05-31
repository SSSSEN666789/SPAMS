#사용자에게 notify 할 때 어떻게 할 지 모르겠어서 일단은 콘솔에 출력하는것으로 함수 생성
#autoGrade는 evalReq에서 dequeue 할 때 evalReq에 자료가 저장되어있으면
#루프 탈출하고 runTest 실행시켜서 result에 반환, result가 반환이 되었으면 반환값을 가지고 makeReport 실행시켜서
#report 생성. 반환값이 없다면 안내메세지 출력
#근데 report가 원래는 save에 인자로 들어가야 하는데 없어서 not accessed Paylance가 뜸
#testResult에 True와 False를 저장시켜 notify함수 실행시켜 안내메세지 출력함

#main.py 참조해서 testrunner와 testresultprocessor 인스턴스 생성 후
#함수 호출하고, strategy 패턴 삽입

from .test_runner import TestRunner
from .test_result_processor import TestResultProcessor
from .evaluation_queue import dequeue
from .python_test_strategy import PythonTestStrategy
from .plain_text_test_strategy import PlainTextTestStrategy
from .python_report_render_strategy import PythonReportRenderStrategy
from .plain_text_report_render_strategy import PlainTextReportRenderStrategy
from Implementation.Module3_SystemCore.src.core import test_result_processor



class contorller():
    def notify(self):
        if self == True:           
            print("AutoGrade Complete")
        elif self == False:
            print("AutoGrade Fail")
            

    def autoGrade(self):
        while True:
            while True:
                evalReq = dequeue()
                if evalReq is not None:
                    break
            if evalReq.language == "python":
                t_strategy = PythonTestStrategy()
                runner = TestRunner(strategy=t_strategy)
                result = runner.runTest()
                if result is not None:
                    r_strategy = PythonReportRenderStrategy()
                    processor = TestResultProcessor(strategy=r_strategy)
                    report = processor.makeReport(result)
                    testResult = True
                else:
                    print("runTest Failed")
                    testResult = False
            elif evalReq.language == "plaintext":
                t_strategy = PlainTextTestStrategy()
                runner = TestRunner(strategy=t_strategy)
                result = runner.runTest()
                if result is not None:
                    r_strategy = PlainTextReportRenderStrategy()
                    processor = TestResultProcessor(strategy=r_strategy)
                    report = processor.makeReport(result)
                    testResult = True
                else:
                    print("runTest Failed")
                    testResult = False
            self.notify(testResult)

