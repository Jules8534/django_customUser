# Generated by Django 3.0.6 on 2020-05-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuserapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='favorite_color',
        ),
        migrations.AddField(
            model_name='myuser',
            name='display_name',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='home_page',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_name',
            field=models.CharField(max_length=30),
        ),
    ]
