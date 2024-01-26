from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse # HttpResponseRedirect, reverse는 새로고침과 관련된 모듈이다.
from .models import *


# Create your views here.
# def index(request):
#     return HttpResponse("my_to_do_app first page")

def index(request):
    # DB에서 데이터를 받아서 index.html 뿌려줘야한다.
    todos = Todo.objects.all()
    content = {
        "todos": todos
    }
    return render(request, "my_to_do_app/index.html",content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    # POST는 객체방식으로 들어오기 때문에 key값과 value값이 필요한대 우리가 html파일에서 메모란에 작성하는 id값을 'todoContent'으로줬다. 입력하는 사람의 id와 그에대한 내용이 value로 들어오고 그것이 객체(dobject)가 되어
    # 그것에 대한 키값을 POST로 들고오면 그것에 대한 value값이 출력된다. 즉 그 id에 해당하는 사람이 쓴 내용이 출력되게 된다.
    new_todo =Todo(content = user_input_str)
    #데이터 DB에 저장
    new_todo.save()
    return HttpResponseRedirect(reverse('index')) # reverse() 메서드는 안에 매개변수로 다시 돌리겠다라는 메서드이다.

def deleteTodo(request):
    delete_todo_id = request.GET['todoNum']
    # print("삭제할 todo의 id :", delete_todo_id)
    todo = Todo.objects.get(id=delete_todo_id)
    
    #데이터 삭제
    todo.delete()
    
    return HttpResponseRedirect(reverse('index'))