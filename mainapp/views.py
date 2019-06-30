from django.shortcuts import render, redirect
from .models import Balance, Testt, PassedTest, History

from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime


def main(request):
    user1 = User.objects.get(username=request.user)
    print("Useeeeer", user1)
    balance = Balance.objects.filter(user=request.user)
    b = str(balance[0].money)
    test = Testt.objects.all().using('tests')
    return render(request, "main.html", {"money": b, "tests": test})


def click(request, test_id):
    if request.method == "POST":
        print(request.user.id)
        passed = PassedTest()
        passed.test = Testt.objects.get(num_id=test_id)
        for i in range(20):
            passed.test.subject_1.questions[i].chosen_ans = request.POST.get('check' + str(i + 1))
        passed.save("test")
        passed.date = datetime.today()
        passed.save()
        print(passed)

        print("----------------------------------------------------------------------------------------")
        exits = History.objects.filter(user_id=request.user.id).exists()
        print(exits)
        if exits:
            history = History.objects.get(user_id=request.user)
            print("before", len(history.ptest))
            history.ptest.append(passed)
            print("after", len(history.ptest))
            history.save()
        else:
            print("This user's history doesnt exist")
            history = History()
            history.user_id = User.objects.get(username=request.user)
            history.ptest=[]
            history.ptest.append(passed)
            history.save()
        return render(request, "last.html")
    else:

        b = Balance.objects.get(user=request.user)
        balance = int(b.money)
        print(balance)
        user = User.objects.get(username=request.user)
        print(str(user))
        print("id= ", test_id)
        t = Testt.objects.get(num_id=test_id)
        #tname = t.name
        print(int(t.cost))
        # print(tname)
        test_price = int(t.cost)
        if(balance > test_price):
            changed_balance = balance - test_price
            b.money = changed_balance
            b.save()
        return render(request, "result.html",{"balance":b.money,"test":t})
        # return render(request, "result.html",{"test":t})


def answer(request):
    print("work")
    ans = request.POST.get('check')
    print(ans)
    return render(request, "last.html")