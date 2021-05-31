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
from .evaluation_queue import EvaluationQueue
from .evaluation_request import EvaluationRequest
from .python_test_strategy import PythonTestStrategy
from .plain_text_test_strategy import PlainTextTestStrategy
from .python_report_render_strategy import PythonReportRenderStrategy
from .plain_text_report_render_strategy import PlainTextReportRenderStrategy
from .db_connection import DBConenction



class Controller():

    def __init__(self):
        # 테스트를 위해 큐에 요청을 넣어둠.
        # 실제 환경에서는 컨트롤러가 아닌 외부에서 큐에 요청을 넣게 됨.
        self.evalQueue = EvaluationQueue()
        self.evalQueue.enqueue(EvaluationRequest(1, 'example.py', 'example_test.py', 10, 1073741824, 'python'))
        self.evalQueue.enqueue(EvaluationRequest(2, 'example.txt', 'example_test.txt', 10, 1073741824, 'plaintext'))

        self.db = DBConenction()


    def notify(self, result):
        if result == True:
            print("AutoGrade Complete")
        elif result == False:
            print("AutoGrade Fail")
            

    def autoGrade(self):
        while True:
            evalReq = None
            while True:
                print('Dequeue request')
                evalReq = self.evalQueue.dequeue()
                if evalReq is not None:
                    break
            if evalReq.language == "python":
                print('Requested lang: Python')
                t_strategy = PythonTestStrategy()
                runner = TestRunner(strategy=t_strategy)
                result = runner.runTest(evalReq)
                if result is not None:
                    print('TestRunner result is not None')
                    r_strategy = PythonReportRenderStrategy()
                    processor = TestResultProcessor(strategy=r_strategy)
                    report = processor.makeReport(result)
                    self.db.save(report)
                    testResult = True
                else:
                    print("runTest Failed")
                    testResult = False
            elif evalReq.language == "plaintext":
                print('Requested lang: plain text')
                t_strategy = PlainTextTestStrategy()
                runner = TestRunner(strategy=t_strategy)
                result = runner.runTest(evalReq)
                if result is not None:
                    print('TestRunner result is not None')
                    r_strategy = PlainTextReportRenderStrategy()
                    processor = TestResultProcessor(strategy=r_strategy)
                    report = processor.makeReport(result)
                    self.db.save(report)
                    testResult = True
                else:
                    print("runTest Failed")
                    testResult = False
            self.notify(testResult)

