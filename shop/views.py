from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from vk_api import vk_api

from .models import Feedback, ShopGallery, Kitchen, Wardrobe, SleepingRoom, Childish, Material, Blog
from .forms import FeedbackForm



class ShopView(ListView):
    model = ShopGallery
    template_name = 'shop/list_shop.html'
    context_object_name = 'records'


class DoneView(TemplateView):
    template_name = 'shop/done.html'


# class GalleryView(CreateView):
#     model = Gallery
#     form_class = GalleryUploadForm
#     template_name = 'shop/load_file.html'
#     success_url = 'load_image'


class FeedBackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_url = 'done'
    template_name = 'shop/list_shop.html'

    def get_success_url(self):
        vk_session = vk_api.VkApi(
            token="vk1.a.gfEstlVD5azYl1-avY5xjBq508KP-En5Stdl2u5em2Xn3hQvyeJzZyT28SHmpz7UwqZy6BWBxUoxUFeP8qTTwA3W1tFLAHt7h96gQo0fyxsNk6bcXGrDb0m89pJs4xUXquX36fbb8pgdgHVq5EIgWsq2bhWNPynFOBv_BzC8QkmyjG88LzFKL5HFinAxQ-RX")

        feed = Feedback.objects.all().order_by('-pk')[0]
        name = feed.name
        phone_number = feed.phone_number
        feedback = feed.feedback
        subject = f'Сообщение с сайта от {name} Телефон: {phone_number} Адрес: {feedback}'
        vk_session.method('messages.send', {'message': subject, "user_id": 7296951, "random_id": 0})
        vk_session.method('messages.send', {'message': subject, "user_id": 530628084, "random_id": 0})
        vk_session.method('messages.send', {'message': subject, "user_id": 27545983, "random_id": 0})
        return ('done')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = ShopGallery.objects.order_by('id')
        return super(FeedBackView, self).get_context_data(**kwargs)


class AboutUs(TemplateView):
    template_name = 'shop/aboutus.html'


class KitchenGallery(ListView):
    model = Kitchen
    template_name = 'shop/kitchen.html'
    context_object_name = 'records'


class WardrobeGallery(ListView):
    model = Wardrobe
    template_name = 'shop/wardrobe.html'
    context_object_name = 'records'


class SleepingRoomGallery(ListView):
    model = SleepingRoom
    template_name = 'shop/sleepingroom.html'
    context_object_name = 'records'


class ChildishGallery(ListView):
    model = Childish
    template_name = 'shop/childish.html'
    context_object_name = 'records'


class MaterialGallery(ListView):
    model = Material
    template_name = 'shop/material.html'
    context_object_name = 'records'

class BlogGallery(ListView):
    template_name = 'shop/blog.html'
    model = Blog
    context_object_name = 'blogs'


class OneBlog(DetailView):
    template_name = 'shop/one_blog.html'
    model = Blog


class ConfView(TemplateView):
    template_name = 'shop/conf.html'


class AcceptView(TemplateView):
    template_name = 'shop/accept.html'
