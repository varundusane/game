# Generated by Django 4.1 on 2022-08-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='niickname',
            new_name='nickname',
        ),
        migrations.AddField(
            model_name='player',
            name='username',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]