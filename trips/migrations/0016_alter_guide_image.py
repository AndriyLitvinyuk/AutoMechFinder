# Generated by Django 3.2 on 2021-06-18 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0015_alter_guide_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]
