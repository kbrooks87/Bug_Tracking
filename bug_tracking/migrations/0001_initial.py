# Generated by Django 3.1 on 2020-08-28 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('NEW', 'New'), ('IN PROGRESS', 'In Progess'), ('DONE', 'Done'), ('INVALID', 'Invalid')], default='NEW', max_length=200)),
                ('assignedTo', models.CharField(default='NONE', max_length=240)),
                ('completedBy', models.CharField(default='NONE', max_length=240)),
                ('markedBy', models.CharField(default='NONE', max_length=240)),
                ('filedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]