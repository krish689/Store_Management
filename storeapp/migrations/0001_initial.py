# Generated by Django 2.2 on 2020-08-08 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StoreManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('new', 'new'), ('accepted', 'accepted'), ('completed', 'completed'), ('declined', 'declined')], max_length=10)),
                ('priority', models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], max_length=10)),
                ('created_by', models.CharField(max_length=50)),
                ('delivery_person', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='storeapp.DeliveryPerson')),
                ('store_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.StoreManager')),
            ],
        ),
    ]