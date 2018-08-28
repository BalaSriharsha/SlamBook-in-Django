# Generated by Django 2.1 on 2018-08-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slam', '0005_auto_20180826_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slambook',
            name='my_address',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_birth_day',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_email',
            field=models.EmailField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_favourite_actor',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_favourite_actress',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_favourite_dishes',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_favourite_festival',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_favourite_places',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_favourite_song',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_favourite_sports',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_favourite_webiste',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_happiest_moment',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_ideal',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_mobile_number',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_nickname',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='my_zodiac_sign',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='opinion_about_you',
            field=models.CharField(default='', max_length=250),
        ),
    ]
