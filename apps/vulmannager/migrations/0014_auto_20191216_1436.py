# Generated by Django 2.2.6 on 2019-12-16 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vulmannager', '0013_auto_20191216_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='资产名')),
                ('domain', models.CharField(blank=True, max_length=72, verbose_name='域名')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('info', models.TextField(blank=True, verbose_name='资产细节')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('pics', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='vulworkflow',
            name='transactors',
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(verbose_name='端口')),
                ('service', models.CharField(blank=True, max_length=128, verbose_name='服务名')),
                ('version', models.CharField(blank=True, max_length=72, verbose_name='版本')),
                ('vulnerable', models.TextField(blank=True, verbose_name='版本漏洞信息')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ports', to='vulmannager.Asset')),
            ],
        ),
    ]
