from django.urls import path
from . import views


urlpatterns = [
    path('suppliers/list/', views.supplier_list, name='supplier-list'),
    path('supplier/list/<supplier_id>', views.supplier_show, name='supplier-show'),
    path('supplier/update/<supplier_id>', views.supplier_update, name='supplier-update'),
    path('supplier/delete/<supplier_id>', views.supplier_delete, name='supplier-delete'),
    path('parts/add/', views.part_add, name='part-add'),
    path('parts/list/', views.part_list, name='part-list'),
    path('parts/list/<part_id>', views.part_show, name='part-show'),
    path('parts/update/<part_id>', views.part_update, name='part-update'),
    path('parts/delete/<part_id>', views.part_delete, name='part-delete'),
    path('products/add/', views.product_add, name='product-add'),
    path('products/list/', views.product_list, name='product-list'),
    path('products/list/<product_id>', views.product_show, name='product-show'),
    path('products/update/<product_id>', views.product_update, name='product-update'),
    path('products/delete/<product_id>', views.product_delete, name='product-delete'),
    path('products/partpack/delete/<partpack_id>', views.partpack_delete, name='partpack-delete'),
]
