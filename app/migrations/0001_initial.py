# Generated by Django 3.1.6 on 2021-02-18 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=50)),
                ('Company_address', models.CharField(max_length=50)),
                ('Company_state', models.CharField(max_length=50)),
                ('Founded', models.IntegerField(default='2001')),
                ('Company_city', models.CharField(max_length=50)),
                ('Company_contact', models.BigIntegerField(default='123')),
                ('Company_Email', models.EmailField(max_length=50)),
                ('Company_link', models.CharField(max_length=50)),
                ('Company_desp', models.TextField(max_length=150)),
                ('open_job', models.IntegerField(default='5')),
                ('Company_logo', models.ImageField(default='/static/default-user.jpg', upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Master_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('OTP', models.IntegerField()),
                ('Role', models.CharField(max_length=50)),
                ('is_verifed', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_title', models.CharField(max_length=50)),
                ('Job_desp', models.TextField(max_length=500)),
                ('Job_type', models.CharField(max_length=50)),
                ('Job_category', models.CharField(max_length=50)),
                ('Job_respon', models.TextField(max_length=500)),
                ('Job_edu_exp', models.TextField(max_length=500)),
                ('Job_benefit', models.TextField(max_length=500)),
                ('Vacancy', models.IntegerField(default='5')),
                ('Education', models.CharField(max_length=50)),
                ('Experience', models.CharField(max_length=50)),
                ('Job_loc', models.CharField(max_length=50)),
                ('start_salary', models.CharField(default='5k', max_length=50)),
                ('end_salary', models.CharField(default='8k', max_length=50)),
                ('Gender', models.CharField(default='Any', max_length=50)),
                ('App_deadline', models.DateField(default='2020-12-01')),
                ('Published', models.DateField(auto_now_add=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Contact', models.BigIntegerField(default='123')),
                ('DOB', models.DateField(default='2020-12-01')),
                ('Gender', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(default='/static/default-user.jpg', upload_to='img/')),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.master_table')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employer'),
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Contact', models.BigIntegerField(default='123')),
                ('DOB', models.DateField(default='2020-12-01')),
                ('Gender', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(default='/static/default-user.jpg', upload_to='img/')),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.master_table')),
            ],
        ),
    ]