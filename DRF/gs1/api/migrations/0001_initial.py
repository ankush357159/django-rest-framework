# Generated by Django 3.2.9 on 2021-12-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll_num', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
