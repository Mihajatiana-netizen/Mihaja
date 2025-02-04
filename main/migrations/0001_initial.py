# Generated by Django 5.0.4 on 2024-08-14 06:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.CharField(default='', max_length=10000)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_message', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_telephone', models.CharField(default='0387377789', max_length=20)),
                ('niveau', models.CharField(default='Première années', max_length=50)),
                ('adresse', models.CharField(default='Vontovorona Bloc 16 porte 565', max_length=225)),
                ('age', models.PositiveIntegerField(default=18)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(default=None, upload_to='profile/')),
                ('type_etablissement', models.BooleanField(default=False)),
                ('carrier_reve', models.CharField(default='Ingenieur', max_length=255)),
                ('etablissement_freq', models.CharField(default='ESPA', max_length=255)),
                ('ecoles_origine', models.TextField(default='Ingenieur')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legend', models.CharField(default=' ', max_length=5000)),
                ('image_1', models.ImageField(default=None, upload_to='publicatio/')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='main.profil')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coms', models.CharField(default=' ', max_length=1000)),
                ('sender_coms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_coms', to=settings.AUTH_USER_MODEL)),
                ('pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conex_pub', to='main.publication')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_reaction', models.PositiveIntegerField(default=0)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='react', to=settings.AUTH_USER_MODEL)),
                ('pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conex_react', to='main.publication')),
                ('sender_react', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_react', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
