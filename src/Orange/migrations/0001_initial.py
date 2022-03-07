# Generated by Django 4.0.1 on 2022-03-07 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=100)),
                ('num_cni', models.CharField(default=0, max_length=5, unique=True)),
                ('num_agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(default=18)),
                ('num_agent', models.CharField(default='ORL0000000', max_length=10, unique=True)),
                ('country', models.CharField(max_length=100)),
                ('num_cni', models.CharField(default=0, max_length=5, unique=True)),
                ('gain', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
