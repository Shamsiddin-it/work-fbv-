from django.urls import path
from .views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("user_create/", user_create_view, name="user_create"),
    path("work_list/", work_list_view, name="work_list"),
    path("work_create/", work_create_view, name="work_create"),
    path("work_detail/<int:pk>/", work_detail_view, name="work_detail"),
    path("application_create/<int:pk>/", application_create_view, name="application_create"),
    path("application_list/", application_list_view, name="application_list"),
    path("application_detail/<int:pk>/", application_detail_view, name="application_detail"),
    path("application_update/<int:pk>/", application_update_view, name="application_update"),
    path("application_delete/<int:pk>/", application_delete_view, name="application_delete"),
    path("work_update/<int:pk>/", work_update_view, name="work_update"),
    path("work_delete/<int:pk>/", work_delete_view, name="work_delete"),
]
