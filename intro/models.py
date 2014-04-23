from django.db import models
from django.utils.translation import ugettext as _
from utils import datetime_to_timestamp

class Menu(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    charge_value = models.CharField(max_length=200)
    distiction = models.IntegerField()
    pic = models.ImageField(upload_to='menu/')

    def __unicode__(self):
        return self.name

class ScheduleEvents(models.Model):
    CSS_CLASS_CHOICES = (
        ('event-warning', _('Warning')),
        ('event-info', _('Info')),
        ('event-success', _('Success')),
        ('event-inverse', _('Inverse')),
        ('event-special', _('Special')),
        ('event-important', _('Important')),
    )

    title = models.CharField(max_length=255, verbose_name=_('Title'))
    url = models.URLField(blank=True, null=True, verbose_name=_('URL'))
    css_class = models.CharField(max_length=20, choices=CSS_CLASS_CHOICES, verbose_name=_('Type'))
    start = models.DateTimeField(verbose_name=_('Start Date'))
    end = models.DateTimeField(verbose_name=_('End Date'))

    @property
    def start_timestamp(self):
        """
        Return start date as timestamp
        """
        return datetime_to_timestamp(self.start)

    @property
    def end_timestamp(self):
        """
        Return end date as timestamp
        """
        return datetime_to_timestamp(self.end)

    def __unicode__(self):
        return self.title
