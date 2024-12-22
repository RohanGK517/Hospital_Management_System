"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.say_home),
    path('admit/',views.patient_admission),
    path('doctors/', views.say_doc),
    path('patients/', views.say_pat),
    path('admins/', views.say_admin),
    path('userlogin/', views.userlogin),
    path('signup/', views.signup),
    path('signup_admin/', views.signup_admin),
    path('signup_doctor/', views.signup_doc),
    path('signup_patient/', views.signup_patient),
    path('comment', views.handlecomment),
    path('logout/', views.handlelogout),
    path('contact/', views.contact),
    path('patients/<int:id>/update/', views.pat_update),
    path('doctors/<int:id>/', views.doc_profile),
    path('admins/<int:id>/', views.admin_profile),
    path('patients/<int:id>/', views.pat_profile),
    path('patients/<int:id>/delete/', views.pat_delete),
    path('doctors/<int:id>/delete/', views.doc_delete),

    path('generator/', views.billGenerator),
    path('generated/', views.generated),
    path('patients/<int:id>/invoice/', views.invoice),
    path('NewInvoice/', views.NewInvoice),

]
