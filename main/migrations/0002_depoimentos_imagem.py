# Generated by Django 4.0.4 on 2022-06-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='depoimentos',
            name='imagem',
            field=models.ImageField(default=1, upload_to='depoimentos'),
            preserve_default=False,
        ),
    ]
