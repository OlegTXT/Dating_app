# Generated by Django 4.2.7 on 2023-11-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('favorite_music', models.CharField(max_length=50)),
                ('favorite_hobbies', models.CharField(max_length=50)),
                ('favorite_anime', models.CharField(max_length=50)),
            ],
        ),
    ]
