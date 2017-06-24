# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oauth2', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessTokenMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='oauth2.AccessToken')),
                ('membership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserMembership')),
            ],
        ),
        migrations.CreateModel(
            name='GrantMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='oauth2.Grant')),
                ('membership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserMembership')),
            ],
        ),
    ]