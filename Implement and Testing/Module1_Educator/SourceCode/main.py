from ParseCheckDecorators import *
from Pub_EventManager import EventManager
from Subs_PageMaker import PageMaker
from Subs_AssignmentMaker import AssignmentMaker
from Subs_AssignmentsDBConnection import AssignmentsDBConnection
from Subs_SubmissionsDBConnection import SubmissionDBConnection
from Subs_Notifier import Notifier


decorator_Controller = Controller()
decorator_QueryParser = QueryParser()
decorator_ValidChecker = ValidChecker()

Pub_EventManager = EventManager()
Subs_PageMaker = PageMaker()
Subs_AssignmentMaker = AssignmentMaker()
Subs_AssignmentDBConnection = AssignmentsDBConnection()
Subs_SubmissionsDBConnection = Subs_AssignmentDBConnection()
Subs_Notifier = Notifier()

decorator_Controller.set_decorator_chain(None, decorator_QueryParser)
decorator_QueryParser.set_decorator_chain(decorator_Controller, decorator_ValidChecker)
decorator_ValidChecker.set_decorator_chain(decorator_QueryParser, Pub_EventManager)

Pub_EventManager.set_pageMaker(Subs_PageMaker)



request_number = 0

while 1:
    request_number = int(input())
