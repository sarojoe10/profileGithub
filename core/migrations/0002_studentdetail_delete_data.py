# Generated by Django 4.1 on 2023-12-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('github_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]