# Generated by Django 4.1.7 on 2023-09-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_alter_db_model_alumni_alter_db_model_release_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_email_sending_active', models.BooleanField(default=False)),
            ],
        ),
    ]
