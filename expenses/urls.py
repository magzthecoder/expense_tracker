from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_page,name='logout_page'),
    path('register/',views.register_page,name='register_page'),
    path('expenses/',views.expense_list,name='expense_list'),
    path('expenses/add/',views.add_expense,name='add_expense'),
    
    path('expenses/<int:id>/detail/',views.expense_detail,name='expense_detail'),
    path('expenses/<int:id>/update/',views.update_expense,name='update_expense'),
    path('expenses/<int:id>/delete/',views.delete_expense,name='delete_expense')
]