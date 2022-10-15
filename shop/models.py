from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Kitchen(models.Model):
    image = models.FileField(upload_to='my_data')
    description = models.TextField(null=True, blank=True)

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class Wardrobe(models.Model):
    image = models.FileField(upload_to='my_data')
    description = models.TextField(null=True, blank=True)

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class SleepingRoom(models.Model):
    image = models.FileField(upload_to='my_data')
    description = models.TextField(null=True, blank=True)

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class Childish(models.Model):
    image = models.FileField(upload_to='my_data')
    description = models.TextField(null=True, blank=True)

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class Material(models.Model):
    image = models.FileField(upload_to='my_data')
    description = models.TextField(null=True, blank=True)

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class ShopGallery(models.Model):
    image = models.FileField(upload_to='my_data')
    name = models.CharField(max_length=100, null=True, blank=True)

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    phone_number = PhoneNumberField()
    feedback = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(default='', null=False, db_index=True)

    def get_url(self):
        return reverse('blog_detail', args=[self.slug])

    def __str__(self):
        return f'{self.title}'
