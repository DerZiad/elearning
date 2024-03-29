# Generated by Django 3.1.4 on 2021-01-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=80)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('datedenaissance', models.DateField()),
                ('username', models.CharField(max_length=18)),
                ('Address', models.CharField(default='Maroc/Meknes/Umi', max_length=80)),
                ('Sexe', models.CharField(default='Femme', max_length=5)),
                ('photo', models.ImageField(default='pictures/user_200_200.jpg', max_length=255, upload_to='pictures/')),
                ('valid', models.BooleanField(default=False)),
                ('succes_lesen', models.IntegerField(default=0)),
                ('succes_horen', models.IntegerField(default=0)),
                ('succes_grammar', models.IntegerField(default=0)),
                ('datecreationaccount', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
