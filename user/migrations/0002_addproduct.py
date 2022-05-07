# Generated by Django 3.2.9 on 2022-03-15 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poductname', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='Product_images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.signup')),
            ],
        ),
    ]