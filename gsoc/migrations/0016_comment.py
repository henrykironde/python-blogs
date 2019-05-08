# Generated by Django 2.1.8 on 2019-05-08 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aldryn_newsblog', '0016_auto_20180329_1417'),
        ('gsoc', '0015_auto_20190423_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              to='aldryn_newsblog.Article')),
                ('parent', models.ForeignKey(null=True,
                                             on_delete=django.db.models.deletion.CASCADE,
                                             related_name='replies', to='gsoc.Comment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
