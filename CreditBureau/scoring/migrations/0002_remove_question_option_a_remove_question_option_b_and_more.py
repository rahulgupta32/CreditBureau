# Generated by Django 5.1.3 on 2024-11-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='option_a',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option_b',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option_c',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option_d',
        ),
        migrations.RemoveField(
            model_name='question',
            name='score_a',
        ),
        migrations.RemoveField(
            model_name='question',
            name='score_b',
        ),
        migrations.RemoveField(
            model_name='question',
            name='score_c',
        ),
        migrations.RemoveField(
            model_name='question',
            name='score_d',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_option',
            field=models.CharField(choices=[('A', 'Always'), ('B', 'Often'), ('C', 'Sometimes'), ('D', 'Never')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='answer',
            field=models.CharField(choices=[('A', 'Always'), ('B', 'Often'), ('C', 'Sometimes'), ('D', 'Never')], max_length=1),
        ),
    ]
