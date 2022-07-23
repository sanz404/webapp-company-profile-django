# Generated by Django 3.2.7 on 2022-07-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_auto_20220723_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='ccreated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='categoryarticle',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='categoryarticle',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='categoryfaq',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='categoryfaq',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='categoryproject',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='categoryproject',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='emailverification',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='emailverification',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='expired_at',
            field=models.DateTimeField(null=True),
        ),
    ]
