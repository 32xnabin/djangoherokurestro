# Generated by Django 2.2 on 2019-04-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('logo', models.CharField(max_length=255, verbose_name='Logo')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('rating', models.IntegerField(verbose_name='Rating')),
            ],
        ),
    ]