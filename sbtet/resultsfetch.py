# # import urllib.request
# #
# # req = urllib.request.Request('https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-002&SchemeId=9&SemYearId=5')
# # with urllib.request.urlopen(req) as response:
# #    the_page = response.read()
# #    print(the_page)
# # url = 'https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-002&SchemeId=9&SemYearId=5'
# import time
#
# for i in range(1,61):
#     if i < 10 :
#         print('https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-{0}&SchemeId=9&SemYearId=5'.format('00'+str(i)))
#     else:
#         print('https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-{0}&SchemeId=9&SemYearId=5'.format('0'+str(i)))
#
# for i in range(1,61):
#     if i < 10 :
#         print('https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-{0}&SchemeId=9&SemYearId=5'.format('00'+str(i)))
#     else:
#         print('https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-{0}&SchemeId=9&SemYearId=5'.format('0'+str(i)))

# import urllib.request
# import time
# def results(url):
#     req = urllib.request.Request(url)
#     time.sleep(0.5)
#     with urllib.request.urlopen(req) as response:
#        the_page = response.read()
#        print(the_page)
#
# for i in range(1,61):
#     if i < 10 :
#         results('https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-{0}&SchemeId=9&SemYearId=5'.format('00'+str(i)))
#     else:
#         results('https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-{0}&SchemeId=9&SemYearId=5'.format('0'+str(i)))

# import json
#
# # some JSON:
# student =  '{"studentWiseReport":[{"Subject_Code":"ME-501","SubjectName":"Industrial Management and Entrepreneurship","MID1_MARKS":"9","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-502","SubjectName":"Web Designing","MID1_MARKS":"15","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-503","SubjectName":"Python Programming","MID1_MARKS":"10","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-574","SubjectName":".Net Programming Through C#","MID1_MARKS":"17","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-575","SubjectName":"Artificial Intelligence","MID1_MARKS":"17","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-506","SubjectName":"Web Designing Lab","MID1_MARKS":"16","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-507","SubjectName":"Python Programming Lab","MID1_MARKS":"17","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-578","SubjectName":".Net Programming Through C# Lab","MID1_MARKS":"19","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-509","SubjectName":"System Administration Lab","MID1_MARKS":"17","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-510","SubjectName":"Project Work","MID1_MARKS":"18","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null}],"studentInfo":[{"Pin":"21241-CS-001","StudentName":"ALLAM ANANYA","BranchName":"COMPUTER ENGINEERING","BranchCode":"CS","Sem":"5SEM","CollegeCode":"241","CollegeName":"TKR COLLEGE OF ENGINEERING AND TECHNOLOGY","ExamType":"Mid1","ExamMonthYear":null}]}'
#
# # parse x:
# studentsresult = json.loads(student)
#
# # the result is a Python dictionary:
# print(studentsresult)
# print(type(studentsresult))
# print(studentsresult['studentInfo'][0]['StudentName'])
# #print(studentsresult['studentWiseReport'][2]['SubjectName'])
# print(studentsresult['studentWiseReport'][0]['MID1_MARKS'])

import urllib.request
import time
import json

def results(url):
    req = urllib.request.Request(url)
    time.sleep(1)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        studentsresult = json.loads(the_page)

        # print(studentsresult)
        # print(type(studentsresult))
        if(len(str(the_page))>1000):
            studentsresult = studentsresult[0]
            print(studentsresult['studentInfo'][0]['StudentName'])
            #print(studentsresult['studentWiseReport'][2]['SubjectName'])
            print(studentsresult['studentWiseReport'][2]['MID1_MARKS'])

for i in range(1,61):
    if i < 10 :
        results('https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-{0}&SchemeId=9&SemYearId=5'.format('00'+str(i)))
    else:
        results('https://www.sbtet.telangana.gov.in/API/api/Results/GetC18MidStudentWiseReport?ExamTypeId=1&Pin=21241-cs-{0}&SchemeId=9&SemYearId=5'.format('0'+str(i)))

#
# the_page = b'[{"studentWiseReport":[{"Subject_Code":"ME-501","SubjectName":"Industrial Management and Entrepreneurship","MID1_MARKS":"9","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-502","SubjectName":"Web Designing","MID1_MARKS":"15","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-503","SubjectName":"Python Programming","MID1_MARKS":"10","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-574","SubjectName":".Net Programming Through C#","MID1_MARKS":"17","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-575","SubjectName":"Artificial Intelligence","MID1_MARKS":"17","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-506","SubjectName":"Web Designing Lab","MID1_MARKS":"16","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-507","SubjectName":"Python Programming Lab","MID1_MARKS":"17","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-578","SubjectName":".Net Programming Through C# Lab","MID1_MARKS":"19","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-509","SubjectName":"System Administration Lab","MID1_MARKS":"17","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null},{"Subject_Code":"CS-510","SubjectName":"Project Work","MID1_MARKS":"18","MID2_MARKS":null,"Internal_MARKS":null,"EndSemMarks":null,"HybridGrade":null,"SubjectTotal":null,"GradePoint":null,"Semester":null,"Result":null,"MaxCredits":0.0,"CreditsGained":null,"SemId":null,"TotalGradePoints":null}],"studentInfo":[{"Pin":"21241-CS-001","StudentName":"ALLAM ANANYA","BranchName":"COMPUTER ENGINEERING","BranchCode":"CS","Sem":"5SEM","CollegeCode":"241","CollegeName":"TKR COLLEGE OF ENGINEERING AND TECHNOLOGY","ExamType":"Mid1","ExamMonthYear":null}]}]'
# print(the_page.decode("utf-8"))
