# Generated by Django 4.2.2 on 2023-06-15 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_thread_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thead', to='forum.subcategory', verbose_name='subcategory'),
        ),
    ]