#api/urls.py

#define url patterns
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
}
#allows us to specify data format such as raw json or html when we use the urls
#format_suffix_patterns appends the format to be used to every URL in the pattern
urlpatterns = format_suffix_patterns(urlpatterns)
