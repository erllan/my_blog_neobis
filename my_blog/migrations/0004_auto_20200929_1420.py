# Generated by Django 3.0.2 on 2020-09-29 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_auto_20200928_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_set', to='my_blog.User'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_blog.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentSet', to='my_blog.Blog'),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
                ('blog', models.ManyToManyField(blank=True, to='my_blog.Blog')),
            ],
        ),
    ]
