# Generated by Django 4.0.4 on 2022-05-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_profile_options_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='group_likes',
            field=models.IntegerField(default=0, verbose_name='Количество лайков'),
        ),
        migrations.AlterField(
            model_name='historicalgroups',
            name='group_likes',
            field=models.IntegerField(default=0, verbose_name='Количество лайков'),
        ),
    ]
