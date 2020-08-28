from django.db import models

from django.utils.translation import gettext_lazy as _

from django.utils import timezone

from myuser.models import MyUser
# Create your models here.New / In Progress / Done / Invalid

class Myuser(models.Model):
    myuser = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.myuser.username


class Ticket(models.Model):    
    title = models.CharField(max_length=100)
    time_filed = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    ticket_filer = models.ForeignKey(Myuser, on_delete=models.CASCADE)
    assigned_user = models.ForeignObject(choices=Myuser.objects.all())

    completed_by_user = models.ForeignObject(choices=Myuser.objects.all())
    class Status_of_ticket(models.TextChoices):
        NEW = models.BooleanField(blank=True, null=True, default=False), _('New')
        IN_PROGRESS = models.BooleanField(blank=True, null=True, default=False), _('In_Progress')
        DONE = models.BooleanField(blank=True, null=True, default=False), _('Done')
        INVALID = models.BooleanField(blank=True, null=True, default=False), _('Invalid')

    ticket = models.CharField(
        choices = Status_of_ticket.choices,
        default = 'New',
    )

    def status(self):
        return self.ticket

