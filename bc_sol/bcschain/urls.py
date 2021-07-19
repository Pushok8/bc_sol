from django.urls import path

from . import views


app_name = 'bcschain'
urlpatterns = [
    path('', views.BlocksView.as_view(), name='blocks'),
    path('blocks/<int:block_height>', views.BlockView.as_view(), name='block'),
]