from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="заголовок")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "разделы"


class Item(models.Model):
    title = models.CharField(max_length=50, verbose_name="заголовок")
    short_description = models.CharField(max_length=100, verbose_name='краткое описание')
    description = RichTextField(verbose_name="описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="раздел")
    price = models.IntegerField(verbose_name="цена")

    def __str__(self):
        return self.title

    def all_images(self):
        return ItemImage.objects.filter(item=self)

    def title_image(self):
        return self.all_images()[0]

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class ItemImage(models.Model):
    image = models.ImageField(verbose_name="картинка")
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE, verbose_name="товар")
