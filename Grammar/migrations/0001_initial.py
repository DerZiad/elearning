# Generated by Django 3.1.4 on 2020-12-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frage', models.CharField(max_length=500)),
                ('losung', models.IntegerField()),
            ],
        ),
    ]
