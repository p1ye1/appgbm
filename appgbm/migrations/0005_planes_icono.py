# Generated by Django 4.0.1 on 2022-03-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgbm', '0004_delete_seccion_1_alter_planes_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planes',
            name='icono',
            field=models.ImageField(null=True, upload_to='img_planes'),
        ),
    ]