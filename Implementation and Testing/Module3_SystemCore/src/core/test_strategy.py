from .evaluation_request import EvaluationRequest

class TestStrategy:

    def executeTest(self, request: EvaluationRequest):
        assert False, "Override me"