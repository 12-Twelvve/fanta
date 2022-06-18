# Generated by Django 4.0.5 on 2022-06-15 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_category', models.CharField(max_length=15)),
                ('food_title', models.CharField(max_length=20)),
                ('food_type', models.CharField(blank=True, default='', max_length=15)),
                ('food_size', models.CharField(default='', max_length=15)),
                ('food_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(max_length=15)),
                ('no_of_people', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(blank=True, max_length=15, null=True)),
                ('last_name', models.CharField(max_length=15)),
                ('code', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_code', models.CharField(max_length=10)),
                ('table_status', models.BooleanField(default=False)),
                ('table_capacity', models.IntegerField()),
                ('table_info', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_title', models.CharField(max_length=25)),
                ('Vendor_mobile', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='VendorOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=15)),
                ('total_price', models.FloatField(max_length=5)),
                ('discount', models.FloatField(default=0.0, max_length=5, null=True)),
                ('vender_request', models.TextField(blank=True, max_length=200, null=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.staff')),
                ('vernder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(default=0.0, max_length=5, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('special', models.TextField(blank=True, max_length=200, null=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
                ('vender_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendororder')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(default=0.0, max_length=5, null=True)),
                ('serverd', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('special', models.TextField(blank=True, max_length=200, null=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.staff'),
        ),
        migrations.AddField(
            model_name='order',
            name='table_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.table'),
        ),
    ]
