# Generated by Django 3.1.2 on 2020-11-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demoapp', '0019_auto_20201102_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
