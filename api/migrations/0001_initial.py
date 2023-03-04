# Generated by Django 4.1.7 on 2023-03-02 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('precio', models.FloatField()),
                ('descripcion', models.TextField()),
                ('imagen', models.TextField()),
                ('disponibilidad', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='ProductosCategorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categorias')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productos')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('password', models.TextField()),
                ('tipoUsuario', models.CharField(choices=[('ADMINISTRADOR', 'ADMINISTRADOR'), ('CLIENTE', 'CLIENTE')], max_length=40)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
