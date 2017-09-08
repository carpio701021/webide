from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getDbTree$', views.getDbTree, name='dbTree'),
    url(r'^newScriptPanel$', views.newScriptPanel, name='newScriptPanel'),
    url(r'^newScriptPanelTab$', views.newScriptPanelTab, name='newScriptPanelTab'),
    url(r'^executeScript$', views.executeScript, name='executeScript'),
]