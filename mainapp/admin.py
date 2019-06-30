from django.contrib import admin
from .models import Balance
from .models import Question,Text,Subject,SubjectWithEightAnswer,Test,Testt,SubjectWithTexts,PassedTest,History
    #,Text,SubjectWithEightAnswer,Subject
admin.site.register(Balance)
admin.site.register(Test)
admin.site.register(Testt)

admin.site.register(Text)
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(SubjectWithEightAnswer)
admin.site.register(SubjectWithTexts)
admin.site.register(PassedTest)
admin.site.register(History)
