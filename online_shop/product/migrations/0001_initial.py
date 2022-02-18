# Generated by Django 4.0.2 on 2022-02-18 18:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(help_text='Enter name of category', max_length=20, unique=True)),
                ('base_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('type', models.CharField(choices=[('percentage', 'percentage'), ('currency', 'currency')], help_text='choose type of discount', max_length=10)),
                ('value', models.PositiveIntegerField()),
                ('max_discount', models.PositiveIntegerField(blank=True, help_text='Enter max amount of discount', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(help_text='Enter name of the product ', max_length=25, unique=True)),
                ('brand', models.CharField(help_text='Enter brand of product', max_length=18)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, help_text='Upload photo of product here', null=True, upload_to='media/product')),
                ('in_stock', models.BooleanField(default=True)),
                ('price', models.PositiveIntegerField(help_text='Enter price of product')),
                ('number_in_inventory', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('discount', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.discount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('context', models.CharField(max_length=120)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
