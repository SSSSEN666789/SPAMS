from SubmissionDBConnection import *
from Controller import *
from PageMaker import *

from resultParser import *


a_Controller = Controller.createPage(1)
SDBC= SubmissionsDBConnection()
a_SubmissionDBConnection = SDBC.getSubRes('0097')
pm= PageMaker()
a_PageMaker = pm.renderSubmissionResult()

a_resultParser = ResultParser()

pr= a_resultParser.parseRequest(a_SubmissionDBConnection)

print (pr)


