from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm
# django가 이미 만들어둔 회원가입 폼을 사용한다.(UserCreationForm)

def register(request):
    if request.method == "POST":
    # form을 통해 POST방식으로 요청이 들어올 시 아래를 실행시킨다.
        regiform = UserCreationForm(request.POST)
        # request.POST안에 담긴 정보들을 UserCreationForm에 담고,
        if regiform.is_valid():
            # 유효하면
            regiform.save()
            # 저장(유저생성)
            return redirect('index')
        else:
            # 유효하지 않으면
            return redirect('register')
            # 다시 register페이지로 보내라
    # GET방식으로 요청이 들어왔을 때 
    registerform = UserCreationForm
    return render(request, 'registration/register.html', {'registerform':registerform})
