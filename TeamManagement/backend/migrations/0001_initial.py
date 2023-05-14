# Generated by Django 4.2.1 on 2023-05-14 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('admin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserTeamRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('teamName', models.CharField(max_length=50)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.team')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='userteamrequest',
            constraint=models.UniqueConstraint(fields=('userId', 'teamName'), name='pk_userteam_request'),
        ),
        migrations.AddConstraint(
            model_name='userteam',
            constraint=models.UniqueConstraint(fields=('userId', 'teamName'), name='pk_userteam'),
        ),
    ]
