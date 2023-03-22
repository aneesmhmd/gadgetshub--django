# Generated by Django 4.1.7 on 2023-03-19 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_alter_account_user_image'),
        ('store', '0007_delete_coupon'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100)),
                ('cart_total', models.PositiveIntegerField()),
                ('tax', models.PositiveIntegerField()),
                ('grand_total', models.PositiveIntegerField()),
                ('payment_method', models.CharField(default='RazorPay', max_length=30)),
                ('is_paid', models.BooleanField(default=True)),
                ('paid_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(default=None, max_length=100)),
                ('order_status', models.CharField(choices=[('Ordered', 'Ordered'), ('Shipped', 'Shipped'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded')], default='Ordered', max_length=20)),
                ('item_price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('item_total', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
