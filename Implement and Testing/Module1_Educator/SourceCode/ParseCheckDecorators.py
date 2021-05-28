''' ParseCheckDecorators.py

ParseCheckDecorator_Interface.py의 인터페이스를 바탕으로 실체화된 데코레이터들.

class 이름(ParseCheckDecoratorMeta):
    ### 이름 전용 메소드
    전용 메소드
    ### 이름 데코레이터 메소드
    데코레이터 메소드

위의 형식으로 작성됨

목록:
Controller
QueryParser
ValidChecker

'''
from ParseCheckDecorator_Interface import ParseCheckDecoratorMeta

###############################################################
class Controller(ParseCheckDecoratorMeta):

    ### Controller 데코레이터 메소드

    def createPage(self, param):
        return self.next.createPage(param)

###############################################################
class QueryParser(ParseCheckDecoratorMeta):

    ### QueryParser 전용 메소드

    def parseRequest(self, query:str):
        try:
            temp = query.split("?")
            request = temp[0]
            body = temp[1]
            if '&' in body: body = body.split('&')
            else:           body = [body]
            content = {}
            for i in range(len(body)): 
                temp = body[i].split('=')
                content[temp[0]] = temp[1]
            return (request, content)
        except:
            return ('query format error', content)

    ### QueryParser 데코레이터 메소드

    def createPage(self, param):
        param = self.parseRequest(param)
        return self.next.createPage(param)

###############################################################
class ValidChecker(ParseCheckDecoratorMeta):

    ### ValidChecker 전용 메소드

    def validCheck(self, param):

        request = param[0]
        parsed = param[1]

        ## 공통 검사항목 ##

        if request == 'query format error': return 'query format error'
        if 'auth' not in parsed: return 'body: auth is not exist.'
        if 'class' not in parsed: return 'body: class is not exist.'
        #if 강의실 DB에 입력한 강의실ID에 해당하는 강의실이 없는 경우: return 'Cannot find 입력ID in Class DB'
        
        ## 메소드 별 검사 항목 ##

        ## AssignmentEditorNew
        if request == 'AssignmentEditorNew':
            if parsed['auth'] != 'educator': return 'auth violation'

        ## AssignmentEditorModify
        elif request == 'AssignmentEditorModify':
            if parsed['auth'] != 'educator': return 'auth violation'
            if 'assignment' not in parsed: return 'body: assignment is not exist.'
            #if 과제 DB에 입력한 과제ID에 해당하는 과제가 없는 경우: return 'Cannot find 입력ID in Assignment DB'
            
        ## AssignmentList
        elif request == 'AssignmentList':

            if parsed['auth'] != 'educator': return 'auth violation'
                       
        ## AssignmentContent
        elif request == 'AssignmentContent':

            if not(parsed['auth'] == 'educator' or parsed['auth'] == 'student'): return 'auth violation'

            if 'assignment' not in parsed: return 'body: assignment is not exist.'
            #if 과제 DB에 입력한 과제ID에 해당하는 과제가 없는 경우: return 'Cannot find 입력ID in Assignment DB'
             
        ## RegisterAssignment & ModifyAssignment
        elif (request == 'RegisterAssignment') or (request == 'ModifyAssignment'): 

            if parsed['auth'] != 'educator': return 'auth violation'

            if 'title' not in parsed: return 'body: title is not exist.'
            if 'cont' not in parsed: return 'body: cont is not exist.'
            if 'deadline' not in parsed: return 'body: deadline is not exist.'
            if 'score' not in parsed: return 'body: score is not exist.'
            if 'file' not in parsed: return 'body: file is not exist.'
            if 'flag' not in parsed: return 'body: flag is not exist.'
            if 'params' not in parsed: return 'body: params is not exist.'

            if request == 'ModifyAssignment':
                if 'assignment' not in parsed: return 'body: assignment is not exist'
                #if 과제 DB에 입력한 과제ID에 해당하는 과제가 없는 경우: return 'Cannot find 입력ID in Assignment DB'

            ## deadline chk
            deadline = parsed['deadline'].split('-')
            d_res = 4
            if len(deadline) == 3: d_res -= 1
            if len(deadline[0]) == 4: d_res -= 1
            if len(deadline[1]) == 2: d_res -= 1
            if len(deadline[2]) == 2: d_res -= 1
            if d_res > 0: return 'Wrong format -> body: deadline'
            #if deadline을 과거로 잡으려고 할 때: return 'Wrong date -> body: deadline=' + parsed['deadline']

            ## flag chk
            if str(parsed['flag']) == '0':
                if parsed['params'] != 'False': return 'Normal assignment cannot have body: params'

            elif str(parsed['flag']) == '1':
                if 'code' not in parsed: return 'body: code is not exist.'
                if 'openbound' not in parsed: return 'body: openbound is not exist.'

            elif str(parsed['flag']) == '2':
                if 'quiz' not in parsed: return 'body: quiz is not exist.'
                if 'openanswer' not in parsed: return 'body: quiz is not exist'

            else: return 'Wrong value -> body: flag=' + parsed['flag']          

        ## SubmissionList
        elif request == 'SubmissionList':

            if parsed['auth'] != 'educator': return 'auth violation'

            if 'assignment' not in parsed: return 'body: assignment is not exist.'
            #if 과제 DB에 입력한 과제ID에 해당하는 과제가 없는 경우: return 'Cannot find 입력ID in Assignment DB'

            
        ## SubmissionContent
        elif request == 'SubmissionContent':

            if parsed['auth'] != 'educator': return 'auth violation'

            if 'assignment' not in parsed: return 'body: assignment is not exist.'
            if 'submission' not in parsed: return 'body: submission is not exist.'
            #if 과제 DB에 입력한 과제ID에 해당하는 과제가 없는 경우: return 'Cannot find 입력ID in Assignment DB'
            #if 제출물 DB에 입력한 제출물ID에 해당하는 제출물이 없는 경우: return 'Cannot find 입력ID in Submission DB'

        else: return 'Wrong method'

        return 'accepted'

    ### ValidChecker 데코레이터 메소드
    # 데코레이터의 최심부

    def createPage(self, param):
        validChkresult = self.validCheck(param)
        return self.next.activate_event(validChkresult, param)
