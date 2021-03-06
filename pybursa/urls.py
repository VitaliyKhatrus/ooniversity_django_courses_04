from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings



urlpatterns = patterns('',
    
    url(r'^$','pybursa.views.index', name='index'),
    url(r'^contact/$','pybursa.views.contact', name='contact'),
    url(r'^student_list/$','pybursa.views.student_list', name='student_list'),
    url(r'^student_detail/$','pybursa.views.student_detail', name='student_detail'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^feedback/$', include('feedbacks.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

