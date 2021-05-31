from .test_strategy import TestStrategy
from .evaluation_request import EvaluationRequest

class TestRunner:

    def __init__(self, strategy: TestStrategy):
        self._strategy = strategy

    def runTest(self, request: EvaluationRequest):
        return self._strategy.executeTest(request)