# Generated by Django 3.2.13 on 2022-05-28 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authnapp', '0003_auto_20220517_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=128, verbose_name='название проекта')),
                ('repo_link', models.URLField(max_length=256, verbose_name='ссылка на репозиторий')),
                ('users_in_project', models.ManyToManyField(to='authnapp.User', verbose_name='пользователи в проекте')),
            ],
        ),
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.TextField(blank=True, max_length=512, verbose_name='текст заметки')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_web_app.project', verbose_name='проект для заметки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authnapp.user')),
            ],
        ),
    ]
