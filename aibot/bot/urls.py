from django.urls import path
from .views import chatbot_view, chat_response,payment_view,home,login_view,sign_up,logout_view,success,admin_view

urlpatterns = [
    path('chatbot/', chatbot_view, name='chatbot_view'),
    path('chat/', chat_response, name='chat_response'),
    path('payment',payment_view,name="payment"),
    path('',home,name="home"),
    path("login",login_view,name="login"),
    path('signup',sign_up,name="signup"),
    path('logout',logout_view,name="logout"),
    path('success/<str:booking_id>/', success, name='success'),
    path('admin_view',admin_view,name="admin_view"),
]
