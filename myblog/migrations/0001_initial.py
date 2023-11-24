# Generated by Django 4.2.7 on 2023-11-17 12:57

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
                ('name', models.CharField(max_length=45, verbose_name='Category name')),
                ('slug', models.SlugField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, max_length=100, null=True)),
                ('san', models.IntegerField()),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.category')),
            ],
        ),
    ]