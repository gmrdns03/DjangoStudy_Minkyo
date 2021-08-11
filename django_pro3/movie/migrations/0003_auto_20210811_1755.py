# Generated by Django 3.2.6 on 2021-08-11 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0002_video_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': '주연배우', 'verbose_name_plural': '주연배우 목록'},
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
