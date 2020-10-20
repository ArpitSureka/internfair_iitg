from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import internfair.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MaxValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll_number', models.IntegerField()),
                ('email', models.EmailField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StartUps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('POC', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('logo', models.ImageField(blank=True, upload_to=internfair.models.user_directory_path1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InternDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(blank=True, max_length=50)),
                ('stipend', models.IntegerField(blank=True)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('allowances', models.CharField(blank=True, max_length=150)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intern_details', to='internfair.startups')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to=internfair.models.user_directory_path)),
                ('content', models.TextField(max_length=100)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('SHORTLISTED', 'Shortlisted'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20, null=True)),
                ('intern_pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposal', to='internfair.interndetails')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to='internfair.students')),
            ],
        ),
    ]
