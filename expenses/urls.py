from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_page,name='logout_page'),
    path('register/',views.register_page,name='register_page'),
    path('expenses/',views.expense_list,name='expense_list'),

    path('expenses/category/',views.category_list,name='category_list'),

    path('expenses/add/',views.add_expense,name='add_expense'),
    path('expenses/search/', views.search_expense, name='search_expense'),
    path('expenses/category/add/',views.add_category,name='add_category'),

    path('expenses/<int:id>/detail/',views.expense_detail,name='expense_detail'),
    path('expenses/local-detail/',views.local_expense_detail,name='local_expense_detail'),
    path('expenses/category/<int:id>/detail/',views.category_detail,name='category_detail'),
    path('expenses/<int:id>/update/',views.update_expense,name='update_expense'),

    path('expenses/category/<int:id>/update/',views.update_category,name='update_category'),

    path('expenses/<int:id>/delete/',views.delete_expense,name='delete_expense'),
    path('expenses/category/<int:id>/delete/',views.delete_category,name='delete_category')
]