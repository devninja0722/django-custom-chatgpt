# Generated by Django 4.1.3 on 2023-01-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_aipost_corectness'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aipost',
            options={},
        ),
        migrations.AddField(
            model_name='aipost',
            name='title',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]