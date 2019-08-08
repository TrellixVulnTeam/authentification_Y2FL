# Generated by Django 2.2.3 on 2019-08-08 08:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190719_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email_confirmed',
            field=models.BooleanField(default=False, verbose_name='email confirmed'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_and_last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='first and last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active status'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_confirmed',
            field=models.BooleanField(default=False, verbose_name='phone confirmed'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unconfirmed_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='unconfirmed email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unconfirmed_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='unconfirmed phone'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=10, unique=True, verbose_name='username'),
        ),
    ]
