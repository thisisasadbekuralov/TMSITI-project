from django.db import models
from django.contrib.auth import get_user_model


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True
        db_table = 'abstract_base_model'


class News(AbstractBaseModel):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='news_images/')
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['id']


class Announcement(AbstractBaseModel):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='announcement_images/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'announcement'
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'


class Management(AbstractBaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='management_images/')
    role = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    study = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    days_of_work = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'management'
        verbose_name = 'Management'
        verbose_name_plural = 'Managements'


class StructuralDivision(AbstractBaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    role = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='structural_division_images/')
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'structural_division'
        verbose_name = 'Structural Division'

        verbose_name_plural = 'Structural Divisions'


class Standard(AbstractBaseModel):
    code = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(null=False, blank=False)





