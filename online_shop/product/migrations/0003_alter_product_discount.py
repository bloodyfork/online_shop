# Generated by Django 4.0.2 on 2022-02-15 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_options_alter_category_base_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.discount'),
        ),
    ]
