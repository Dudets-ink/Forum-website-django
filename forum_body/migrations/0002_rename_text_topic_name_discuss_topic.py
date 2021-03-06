# Generated by Django 4.0.5 on 2022-06-19 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum_body', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='text',
            new_name='name',
        ),
        migrations.AddField(
            model_name='discuss',
            name='topic',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='forum_body.topic'),
            preserve_default=False,
        ),
    ]
