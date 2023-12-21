from django.urls import path, include

from .views import question, qiuz, result_list, sign_up, logout_quiz, login_quiz

app_name = 'quizapp'

urlpatterns = [
    path('', qiuz, name='qiuz'),
    path('quiz/<int:pk>/', question, name='quistion'),
    path('results/', result_list, name='results'),
    path('signup/', sign_up, name='signup'),
    path('logout/', logout_quiz, name='logout'),
    path('login/', login_quiz, name='login')

]

# url_for_cbv = [
#     path('', BlogListView.as_view(), name=''), ]

# urlpatterns += url_for_cbv
