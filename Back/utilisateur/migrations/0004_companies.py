# Generated by Django 4.2.6 on 2023-10-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0003_cmp_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]