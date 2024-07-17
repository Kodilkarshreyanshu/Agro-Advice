from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('predi ctor', views.predictor, name='predictor'),
    path('crop_result', views.formInfo, name='crop_result'),
    
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('fert_recommend', views.fert_recommend, name='fert_recommend'),
    path('recommendation', views.fert_recommend, name='recommendation'),
    path('crop_search', views.crop_search, name='crop_search'),
    path('pair_crop_page', views.pair_crop_page, name='pair_crop_page'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/submit/', views.contact_form_submission, name='contact_form_submission'),
    path('pair-crop/', views.pair_crop_page, name='pair_crop_page'),
    path('input/<str:option>/', views.input_data, name='input_data'),
    path('form_info/', views.formInfo, name='form_info'),
    path('news/', views.news, name='news'),  # URL pattern for the news page
]
