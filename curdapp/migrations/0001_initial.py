# Generated by Django 4.2.7 on 2023-11-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('fee', models.IntegerField()),
                ('iname', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('a1', models.IntegerField(max_length=50)),
                ('a2', models.IntegerField(max_length=50)),
                ('a3', models.IntegerField(max_length=50)),
                ('a4', models.IntegerField(max_length=50)),
                ('loc', models.CharField(max_length=50)),
            ],
        ),
    ]
