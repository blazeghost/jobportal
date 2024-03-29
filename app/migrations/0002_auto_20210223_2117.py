# Generated by Django 3.1.6 on 2021-02-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='profile_pic',
            field=models.ImageField(default='/img/default-user.jpg', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='Company_logo',
            field=models.ImageField(default='/img/default-user.jpg', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='profile_pic',
            field=models.ImageField(default='/img/default-user.jpg', upload_to='img/'),
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
