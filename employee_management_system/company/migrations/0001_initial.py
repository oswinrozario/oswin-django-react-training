# Generated by Django 5.0.1 on 2024-01-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('Technology', 'Technology'), ('Finance', 'Finance'), ('Healthcare', 'Healthcare'), ('Manufacturing', 'Manufacturing'), ('Retail', 'Retail'), ('Telecommunications', 'Telecommunications')], max_length=100)),
                ('revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('employees_count', models.PositiveIntegerField(blank=True, null=True)),
                ('founded_date', models.DateField(blank=True, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
