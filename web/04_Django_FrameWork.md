# MVC & MVT

> **M**odel **V**iew **C**ontroller & **M**odel **V**iew **T**emplate
>
> 웹 프로그래밍 방법론

<br/>

<br/>

## MVC

- 일반적인 방법론

> Model : 데이터(DB)
>
> View : UI(프론트앤드)
>
> Controller : 웹 어플리케이션(백앤드)

<br/>

## MVT

- 장고 프레임워크

> Model : 데이터(DB)
>
> View : 백앤드
>
> Template : UI(프론트앤드)

<br/>

<br/>

<br/>

# Project Practice

> 질의 응답 홈페이지 만들기

- 실행환경 : Anaconda Prompt
- 프레임워크 : Django

<br/>

<br/>

## 경로 설정

```shell
cd \
cd RedBook
```

<br/>

<br/>

<br/>

## 프로젝트 생성

> `django-admin startproject <프로젝트명>`

```
django-admin startproject mysite
```

- `mysite`
  - `manage.py`
  - `mysite`
    - `__init__.py`
    - `asgi.py`
    - `settings.py`
    - `urls.py`
    - `wsgi.py`

<br/>

<br/>

<br/>

## `polls` 어플리케이션 생성

- `mysite` 폴더를 `ch3` 폴더로 변경
- `polls` 어플리케이션 생성

```bash
move mysite ch3
cd ch3
python manage.py startapp polls
```

<br/>

<br/>

<br/>

- `mysite\settings.py` 수정

```shell
cd mysite
notepad settings.py
```

```
ALLOWED_HOSTS = ['172.30.1.32', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig', # 추가
]

TIME_ZONE = 'Asia/Seoul'
```

<br/>

<br/>

## 기본 테이블 생성

```
cd ..
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

- `migrate` : 데이터베이스 변경 시 반영해주는 명령

<br/>

<br/>

## 웹 접속

- `127.0.0.1:8000` 접속

- `127.0.0.1:8000/admin` 접속

<br/>

<br/>

## 아이디 등록

- 다른 Anaconda Prompt 실행

```
cd \
cd RedBook
cd ch3
python manage.py createsuperuser

id / email / password 입력
pkw8056 / rjsdn8056@naver.com / 1234
```

<br/>

<br/>

<br/>

# Model Coding

```
notepad models.py
notepad admins.py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

<br/>

1. 테이블 정의

- `models.py`에 내용 추가

```
cd \
cd RedBook
cd cd3
cd polls
notepad models.py
```

```python
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

<br/>

- `admin.py` 에 내용 추가

```
notepad admin.py
```

```python
from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
```

<br/>

<br/>

2. 

```
cd ..
python manage.py makemigrations
dir polls\migrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

<br/>

<br/>

<br/>

# URL Config

1. `\mysite\urls.py` 내용 추가

```
cd ch3
cd mysite
notepad urls.py
```

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # shkim
    path('polls/', include('polls.urls')),
]
```

<br/>

<br/>

2. `\polls\urls.py` 파일 생성

```
cd ../polls
```

```python
from django.urls import path
from polls import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),      # /polls/
    path('<int:question_id>/', views.detail, name='detail'),       # /polls/5/
    path('<int:question_id>/results/', views.results, name='results'),     # /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),      # /polls/5/vote/
]
```

<br/>

<br/>

<br/>

# View

```
cd \RedBook\ch3\polls
mkdir templates
mkdir templates\polls
cd templates\polls

notepad index.html
```

```python
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

<br/>

```
cd ..
cd ..
notepad views.py
```

```python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from polls.models import Choice, Question


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

<br/>

```
cd templates\polls
notepad detail.html
```

```html
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
```

<br/>

```
notepad results.html
```

```html
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```











































































# 프로젝트 뼈대 만들기 : 프로젝터 및 앱 개발에 필요한 디렉토리와 파일 생성

1. 모델 코딩하기 : 테이블 관련 사항을 개발(models.py, admin.py 파일)
2. URLconf 코딩하기 : URL 및 뷰 매핑 관계를 정의(urls.py 파일 2개 : \mysite\urls.py, \polls\urls.py)
3. 템플릭 코딩하기 : 화면 UI 개발(template / 디렉토리 하위의 *.html 파일들)
4. 뷰 코딩하기 : 애플리케이션 로직 개발(views.py 파일





























