# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='infected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_water', models.IntegerField()),
                ('item_food', models.IntegerField()),
                ('item_medication', models.IntegerField()),
                ('item_ammunition', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='survivor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survivor_name', models.CharField(max_length=20, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='survivor_control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_title', models.CharField(max_length=50)),
                ('last_location', models.CharField(max_length=50)),
                ('status_message', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('survivor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survivor_control.survivor')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='survivor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='survivor_control.survivor'),
        ),
        migrations.AddField(
            model_name='infected',
            name='postby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survivor_control.survivor'),
        ),
        migrations.AddField(
            model_name='infected',
            name='survivor_infected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infected_reports', to='survivor_control.survivor'),
        ),
    ]
