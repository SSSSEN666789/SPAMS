# 테스트용 파일

# from .test_runner import TestRunner
# from .python_test_strategy import PythonTestStrategy
# from .plain_text_test_strategy import PlainTextTestStrategy
# from .test_result_processor import TestResultProcessor
# from .python_report_render_strategy import PythonReportRenderStrategy
# from .plain_text_report_render_strategy import PlainTextReportRenderStrategy

# t_strategy = PythonTestStrategy()
# runner = TestRunner(strategy=t_strategy)
# result = runner.runTest()

# r_strategy = PythonReportRenderStrategy()
# processor = TestResultProcessor(strategy=r_strategy)
# p_result = processor.makeReport(result)

# p_t_strategy = PlainTextTestStrategy()
# runner = TestRunner(strategy=p_t_strategy)
# result = runner.runTest()

# p_r_strategy = PlainTextReportRenderStrategy()
# processor = TestResultProcessor(strategy=p_r_strategy)
# p_result = processor.makeReport(result)

from .controller import Controller

controller = Controller()
controller.autoGrade()