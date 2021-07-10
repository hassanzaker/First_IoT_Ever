
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('reserve/<int:slot>/', views.reserve, name='reserve'),
    path('validate/<int:ticket>/', views.validate_reserveation, name='validate'),
    path('getitem/<int:slot>/', views.get_item, name='get_item'),
    path('tempereture/<int:slot>/<int:tempereture>/', views.update_tempereture, name='tempereture'),
    path('pay/<int:cardid>/<int:password>/', views.payment, name='pay'),
]