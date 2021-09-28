from django.urls import path
from . import views

# app_name = 'support'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('parts/add/', views.part_add, name='part-add'),
    path('parts/list/', views.part_list, name='part-list'),
    path('parts/list/<part_id>', views.part_show, name='part-show'),
    path('parts/update/<part_id>', views.part_update, name='part-update'),
    path('parts/delete/<part_id>', views.part_delete, name='part-delete'),
]