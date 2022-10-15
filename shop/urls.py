from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedBackView.as_view()),
    path('done', views.DoneView.as_view()),
    path('conf', views.ConfView.as_view()),
    path('accept', views.AcceptView.as_view()),
    path('aboutus', views.AboutUs.as_view()),
    path('kitchen', views.KitchenGallery.as_view()),
    path('wardrobe', views.WardrobeGallery.as_view()),
    path('sleepingroom', views.SleepingRoomGallery.as_view()),
    path('childish', views.ChildishGallery.as_view()),
    path('material', views.MaterialGallery.as_view()),
    path('blog', views.BlogGallery.as_view()),
    path('blog/<str:slug>', views.OneBlog.as_view(), name="blog_detail"),
]
