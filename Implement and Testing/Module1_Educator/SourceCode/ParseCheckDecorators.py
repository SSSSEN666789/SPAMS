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
import re
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

        queryformat = '^[^&=?]+\?[^&=?]+=[^&=?]+(&[^&=?]+=[^&=?]+)*$'
        queryformat = re.compile(queryformat) 
        if queryformat.match(query.strip()) == None: return ('query format error', {})
        
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


        ## 타입 별 포멧 체크 ##
        # TC-1 Step3, Step 4: class 
        # Tc-1 Step5        : title
        # TC-1 Step7, Stpe 8: score
        # TC-5 Step1, Step 2: assignment
        # TC는 없지만        : submission
        # TC-1 Step9        : file
        # TC-2 Step2        : code
        # TC-3 Step2        : quiz
        
        if 'class' in parsed:
            try: 
                if int(parsed['class']) < 0 : return 'body: class ID cannot be negative integer.'
            except: return 'body: class ID should be positive integer or 0.'

        if parsed['title'].strip() == '': return 'body: title cannot be blank.'

        if 'score' in parsed:
            try: 
                if float(parsed['score']) < 0 : return 'body: score cannot be negative number.'
            except: return 'body: score should be positive number or 0.'

        if 'assignment' in parsed:
            try: 
                if int(parsed['assignment']) < 0 : return 'body: assignment ID cannot be negative integer.'
            except: return 'body: assignment ID should be positive integer or 0.'

        if 'submission' in parsed:
            try: 
                if int(parsed['submission']) < 0 : return 'body: submission ID cannot be negative integer.'
            except: return 'body: submission ID should be positive integer or 0.'
        
        file_regexp = '^((?:\/[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*(?:\-[a-zA-Z0-9]+)*)+)$'
        file_regexp = re.compile(file_regexp)

        if 'file' in parsed:
            if file_regexp.match(parsed['file']) == None:
                if parsed['file'] != 'testpath': return 'body: file is Unvalid path.'

        if 'code' in parsed:
            if file_regexp.match(parsed['code']) == None:
                if parsed['code'] != 'testpath': return 'body: code is Unvalid path.'

        if 'quiz' in parsed:
            if file_regexp.match(parsed['file']) == None:
                if parsed['code'] != 'testpath': return 'body: code is Unvalid path.'

        ## 메소드 별 검사 항목 ##

        body_length = len(parsed)

        ## AssignmentEditorNew
        if request == 'AssignmentEditorNew':
            if parsed['auth'] != 'educator': return 'auth violation'
            if body_length != 2: return 'too many input.'


        ## AssignmentEditorModify
        elif request == 'AssignmentEditorModify':
            if parsed['auth'] != 'educator': return 'auth violation'
            if 'assignment' not in parsed: return 'body: assignment is not exist.'
            if body_length != 3: return 'too many input.'
            
        ## AssignmentList
        elif request == 'AssignmentList':
            if parsed['auth'] != 'educator': return 'auth violation'
            if body_length != 2: return 'too many input.'
                       
        ## AssignmentContent
        elif request == 'AssignmentContent':
            if not(parsed['auth'] == 'educator' or parsed['auth'] == 'student'): return 'auth violation'
            if 'assignment' not in parsed: return 'body: assignment is not exist.'
            if body_length != 3: return 'too many input.'
                         
        ## RegisterAssignment & ModifyAssignment
        elif (request == 'RegisterAssignment') or (request == 'ModifyAssignment'): 
            
            correct_body_length = 9

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
                correct_body_length += 1


            ## deadline chk
            deadline = parsed['deadline'].split('-')
            d_res = 4
            if len(deadline) == 3: d_res -= 1
            if len(deadline[0]) == 4: d_res -= 1
            if len(deadline[1]) == 2: d_res -= 1
            if len(deadline[2]) == 2: d_res -= 1
            if d_res > 0: return 'Wrong format -> body: deadline'

            # TC-1 Step 6
            else:
                from datetime import datetime
                try: 
                    deadline = list(map(int, deadline))
                    td = datetime.today()
                    dl = datetime(deadline[0], deadline[1], deadline[2])
                    if td > dl: return 'body: deadline should be later then today.'
                except: return 'Wrong format -> body: deadline'

            ## flag chk
            if str(parsed['flag']) == '0':
                if parsed['params'] != 'False': return 'Normal assignment cannot have body: params'

            elif str(parsed['flag']) == '1':
                if 'code' not in parsed: return 'body: code is not exist.'
                if 'openbound' not in parsed: return 'body: openbound is not exist.'
                correct_body_length += 2

            elif str(parsed['flag']) == '2':
                if 'quiz' not in parsed: return 'body: quiz is not exist.'
                if 'openanswer' not in parsed: return 'body: quiz is not exist'
                correct_body_length += 2

            else: return 'Wrong value -> body: flag=' + parsed['flag']          

            if correct_body_length != body_length: return 'too many input.'

        ## SubmissionList
        elif request == 'SubmissionList':

            if parsed['auth'] != 'educator': return 'auth violation'
            if 'assignment' not in parsed: return 'body: assignment is not exist.'
            if body_length != 3: return 'too many input.'

        ## SubmissionContent
        elif request == 'SubmissionContent':

            if parsed['auth'] != 'educator': return 'auth violation'

            if 'assignment' not in parsed: return 'body: assignment is not exist.'
            if 'submission' not in parsed: return 'body: submission is not exist.'
            if body_length != 4: return 'too many input.'

        else: return 'Wrong method'

        return 'accepted'

    ### ValidChecker 데코레이터 메소드
    # 데코레이터의 최심부

    def createPage(self, param):
        validChkresult = self.validCheck(param)
        return self.next.activate_event(validChkresult, param)
