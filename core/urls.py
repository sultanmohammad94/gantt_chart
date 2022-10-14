from django.urls import path, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r"^$",view=views.index, name="index"),
    re_path(r"^data/(.*)$",view=views.data_list, name="data_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
