# Generated by Django 5.0.6 on 2024-06-10 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(default=False, verbose_name='Result')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.station', verbose_name='Station')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student', verbose_name='Student')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.title', verbose_name='Title')),
            ],
        ),
    ]