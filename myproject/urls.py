"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url
from first_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^',include('django.contrib.auth.urls')),
    url(r'^hello$',views.hello,name='hello17'),
    path('consult_doc/<str:username>/',views.consult1,name='consult_doc'),
    path('replytoques/<int:consult_id>/',views.replyques,name='replytoques'),
    url(r'^consultations$',views.consultation,name='consultations'),
    path('updateexpertreply/<int:id>/',views.updateexpertreply,name='updateexpertreply'),
    
    
    url(r'^home$',views.home,name='hello'),
    url(r'^about$',views.about,name='hello1'),
    url(r'^contact$',views.contact,name='hello2'),
    url(r'^user_login$',views.usr_login,name='user_login'),
    url(r'^breast_cancer$',views.breast_cancer_form,name='breast_cancer'),
    
    url(r'^kidney_disease$',views.kidney_form1,name='kidney_disease'),
    url(r'^register$',views.register,name='hello4'),
    url(r'^blog$',views.blogs,name='hello5'),
    url(r'^doctor$',views.doctors,name='hello6'),
    url(r'^breast_form$',views.breast_cancer,name='hello7'),
    url(r'^kidney_form$',views.kidney_form,name='hello8'),
    url(r'^liver_form$',views.liver_form,name='hello9'),
    url(r'^diabetes_form$',views.diabetes_form,name='hello10'),
    url(r'^lung_form$',views.lung_form,name='hello11'),
    url(r'^heart_form1$',views.heart,name='heart_form1'),
    url(r'^heartform$',views.heart_form_open,name='heartform'),
    url(r'^df$',views.diabetes_form1,name='df'),
    url(r'^dash2$',views.user_dash,name='hello13'),
    url(r'^bc_dash$',views.bc1,name='hello14'),
    url(r'^dashboard$',views.dash,name='dash'),
    url(r'^dash$',views.dash1,name='dash2'),
    url(r'^user_logout$',views.user_logout,name='dash3'),
    url(r'^view_profile1$',views.view1,name='view_profile1'),
    url(r'^edit_profile$',views.doctor_edit,name='edit_profile'),
    url(r'^expert_login$',views.doctor_login,name='expert_login'),
    url(r'^change$',views.changepassword,name='dash4'),
    url(r'^diabetes_info$',views.diabetes_info,name='dash5'),
    url(r'^heart_visual$',views.heart_visual,name='dash6'),
    url(r'^kidney_visual$',views.kidney_visual,name='dash7'),
    url(r'^liver_visual$',views.liver_visual,name='dash8'),
    url(r'^lung_visual$',views.lung_visual,name='dash9'),
    url(r'^breastcancer_visual$',views.breastcancer_visual,name='dash10'),
    url(r'^diabetes_visual$',views.diabetes_visual,name='dash11'),
    url(r'^signup$',views.signuppage,name='signup'),
    url(r'^expert_logout$',views.signuppage,name='expert_logout'),
    url(r'^update_expert_profile$',views.updateexpertprofile,name='update_expert_profile'),
    url(r'^doctor_profile$',views.doctorprofile,name='doctor_profile'),
    url(r'^view_experts$',views.viewexperts,name='view_experts'),
    url(r'^diabetes$',views.diabetes_d,name='diabetes'),
    url(r'^heart$',views.heart_d,name='heart'),
    url(r'^liver$',views.liver_d,name='liver'),
    url(r'^lung$',views.liver_d,name='lung'),
    url(r'^kidney$',views.kidney_d,name='kidney'),
    url(r'^hospital$',views.hospitals,name='hospital'),
    url(r'^breasti$',views.breast_info,name='breasti'),
    url(r'^diabetesi$',views.diabetes_info,name='diai'),
    url(r'^hearti$',views.heart_info,name='hearti'),
    url(r'^kidneyi$',views.kidney_info,name='kidneyi'),
    url(r'^liveri$',views.liver_info,name='liveri'),
    url(r'^lungi$',views.lung_info,name='lungi'),
    url(r'^lungform$',views.lungform1,name='lungform'),
    url(r'^liver_disease$',views.liverform,name='liver_disease'),
    url(r'^asthma$',views.asthma,name='asthma'),
    url(r'^coldflu$',views.coldflu,name='coldflu'),
    url(r'^mental$',views.mental,name='mental'),
    url(r'^forgot_password$',views.forgot,name='forgot_password'),
    url(r'^fp$',views.forgot,name='fp'),
    url(r'^forgot_password1$',views.forgot1,name='forgot_password1'),
    url(r'^fp1$',views.fp2,name='fp1'),
    url(r'^contactus$',views.contact,name='contactus'),
    url(r'^appointment$',views.appointment,name='appointment'),
    url(r'^thankyou$',views.thankyou,name='thankyou'),
    url(r'^sent$',views.sentpage,name='sent'),
    path('view_expert_detail/<str:username>/',views.view_expert_detail,name='view_expert_detail'),
    path('viewreply/<str:username>/',views.view_reply,name='viewreply'),


    


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

























