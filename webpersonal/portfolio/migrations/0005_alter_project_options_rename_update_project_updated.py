# Generated by Django 4.1.2 on 2023-02-04 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_update_project_updated_alter_project_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='update',
            new_name='updated',
        ),
    ]