from django.conf import settings 
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(_('título'), max_length=200)
    text = models.TextField(_('texto'))
    created_date = models.DateTimeField(_('criado em'), default=timezone.now)
    published_date = models.DateTimeField(_('publicar em'), blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PostEn(Post):
    language = models.CharField(_('idioma'), max_length=2, default='en')

    class Meta:
        verbose_name = _('Post EN')
        verbose_name_plural = _('Posts EN')

    def __str__(self):
        return self.title

class PostEs(Post):
    language = models.CharField(_('idioma'), max_length=2, default='es')

    class Meta:
        verbose_name = _('Post ES')
        verbose_name_plural = _('Posts ES')

    def __str__(self):
        return self.title

class PostPt(Post):
    language = models.CharField(_('idioma'), max_length=5, default='pt-br')
    post_en = models.OneToOneField(PostEn, verbose_name=_('Post em Inglês'), on_delete=models.SET_NULL,
                                      null=True, blank=True, related_name='post_pt_en')
    post_es = models.OneToOneField(PostEs, verbose_name=_('Post em Espanhol'), on_delete=models.SET_NULL,
                                      null=True, blank=True, related_name='post_pt_es')

    class Meta:
        verbose_name = _('Post PT')
        verbose_name_plural = _('Posts PT')

    def __str__(self):
        return self.title