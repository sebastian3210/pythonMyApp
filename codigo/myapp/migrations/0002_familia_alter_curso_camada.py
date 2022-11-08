# Generated by Django 4.1.2 on 2022-11-07 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(),
        ),
    ]
