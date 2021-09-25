from django.urls import path,register_converter
from . import views,converters
register_converter(converters.fdy,'yyyy')
urlpatterns=[
    # path('stu', views.base , name='details'),
    path('del/<int:myid>', views.delete , name='delete'),
    path('edit/<int:myid>', views.edit , name='edit'),
    ]