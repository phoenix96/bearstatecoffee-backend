# Generated by Django 2.0.2 on 2018-02-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180213_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStamps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
