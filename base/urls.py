from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "studentLife_discipline"

urlpatterns = [
    #path('', views.caseProfile, name="case-profile"),
    path('newcase', views.NewCase, name="NewCase"),
    path('CaseList/', views.caseList, name="case-list"),
    #path('case-list/', views.caseList, name="case-list"),

    #COMMUNITY SERVICE
    path('community-service-tracker/<int:student_id>/', views.serviceTracker, name="community-service-tracker"),

    #GOOD MORAL URL
    path('RequestGoodMoral/', views.req_goodmoral, name="req_goodmoral"),
    path('goodmoral/<str:student_id>/', views.goodmoral_detail, name='goodmoral_detail'),
    path('GoodMoralTemplate/<str:student_id>/',views.GoodMoralTemplate, name="GoodMoralTemplate"),

    path('Transaction/', views.transaction, name='transaction'),
    path('approve/<int:pk>/', views.approve_request, name='approve_request'),
    path('decline/<int:pk>/', views.decline_request, name='decline_request'),

    #CRUD
    path('update-case/<str:pk>/', views.updateCase, name='update-case'),
    path('delete-case/<str:pk>/', views.deletecaserecord, name='deletecaserecord'),
    
    
    #modal part
    path('SavedSuccesfully/', views.savedcaseprofile, name="savedcaseprofile"),
     path('DeleteCaseRecord/<str:pk>/', views.deletecaserecord, name='deletecaserecord'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)