# Generated by Django 2.0.2 on 2018-02-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180213_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]