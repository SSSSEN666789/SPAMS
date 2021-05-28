from .report_render_strategy import ReportRenderStrategy

class TestResultProcessor:

    def __init__(self, strategy: ReportRenderStrategy):
        self._strategy = strategy
    
    def makeReport(self, testResult: str):
        return self._strategy.render(testResult)
