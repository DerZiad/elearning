# Generated by Django 3.1.4 on 2021-01-12 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
                ('niveau', models.CharField(default='A1', max_length=3)),
                ('note', models.IntegerField(default=0)),
                ('imagedemodel', models.ImageField(default='pictures/user_200_200.jpg', max_length=255, upload_to='pics/')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackname', models.CharField(default=None, max_length=30)),
                ('track', models.FileField(upload_to='Track/')),
                ('modeltest', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Horen.modeltest')),
            ],
        ),
        migrations.CreateModel(
            name='ReponseHoren',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid', models.BooleanField(default=False)),
                ('modeltest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Horen.modeltest')),
                ('personnes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personnetrack', to='Auth.personne')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.CharField(max_length=150)),
                ('reponse', models.CharField(max_length=150)),
                ('audio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Horen.track')),
            ],
        ),
        migrations.CreateModel(
            name='Choix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.CharField(max_length=150)),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Horen.question')),
            ],
        ),
    ]
