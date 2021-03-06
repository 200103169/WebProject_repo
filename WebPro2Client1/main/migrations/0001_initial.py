# Generated by Django 4.0.2 on 2022-03-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Названия')),
                ('news', models.TextField(verbose_name='Описания')),
            ],
        ),
        migrations.CreateModel(
            name='Module2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gold', models.IntegerField()),
                ('silver', models.IntegerField()),
                ('bronze', models.IntegerField()),
                ('overall', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Module3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gold', models.IntegerField()),
                ('silver', models.IntegerField()),
                ('bronze', models.IntegerField()),
                ('overall', models.IntegerField()),
            ],
        ),
    ]
