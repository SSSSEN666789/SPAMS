from ParseCheckDecorators import *

decorator_Controller = Controller()
decorator_QueryParser = QueryParser()
decorator_ValidChecker = ValidChecker()

decorator_Controller.set_decorator_chain(None, decorator_QueryParser)
decorator_QueryParser.set_decorator_chain(decorator_Controller, decorator_ValidChecker)
decorator_ValidChecker.set_decorator_chain(decorator_QueryParser, None)



request_number = 0

while 1:
    request_number = int(input())
