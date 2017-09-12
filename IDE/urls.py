from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getDbTree$', views.getDbTree, name='dbTree'),
    url(r'^newScriptPanel$', views.newScriptPanel, name='newScriptPanel'),
    url(r'^newScriptPanelTab$', views.newScriptPanelTab, name='newScriptPanelTab'),
    url(r'^newReportPanel$', views.newReportPanel, name='newReportPanel'),
    url(r'^newReportPanelTab$', views.newReportPanelTab, name='newReportPanelTab'),
    url(r'^executeScript$', views.executeScript, name='executeScript'),
    url(r'^executeReport$', views.executeReport, name='executeReport'),
    url(r'^showReport$', views.showReport, name='showReport'),
]