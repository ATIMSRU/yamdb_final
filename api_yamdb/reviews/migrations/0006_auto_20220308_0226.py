# Generated by Django 2.2.16 on 2022-03-08 02:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_comment_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.Titles', verbose_name='название произведения'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание произведения'),
        ),
    ]
