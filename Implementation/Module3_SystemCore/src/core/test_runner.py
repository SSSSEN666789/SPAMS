from .test_strategy import TestStrategy

class TestRunner:

    def __init__(self, strategy: TestStrategy):
        self._strategy = strategy

    def runTest(self):
        return self._strategy.executeTest()