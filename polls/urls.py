from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^add_question/$', views.add_question, name='add_question'),
    url(r'^add_question_todb/$', views.add_question_todb, name='add_question_todb'),
    url(r'^add_choice/(?P<question_id>[0-9]+)/$', views.add_choice, name='add_choice'),
    url(r'^testchoice/$', views.testchoice, name='testchoice'),
    url(r'^add_choice_todb/$', views.add_choice_todb, name='add_choice_todb'),

]

