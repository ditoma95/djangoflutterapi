# Generated by Django 4.2.7 on 2024-02-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=60)),
                ('mot_de_passe', models.CharField(max_length=60)),
            ],
        ),
    ]
