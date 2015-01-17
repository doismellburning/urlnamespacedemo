from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

urlpatterns = patterns(
    '',
    url(r'foo$', TemplateView.as_view(template_name="foo.html"), name="foo"),
    url(r'bar$', TemplateView.as_view(template_name="bar.html"), name="bar"),
)
