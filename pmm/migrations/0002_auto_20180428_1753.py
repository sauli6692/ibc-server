# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 17:53
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.hashers import make_password


lookup_tables_seeds = {
    'CivilStatus': [
        'Soltero(a)',
        'Casado(a)',
        'Divorciado(a)',
        'Viudo(a)',
        'Unión Libre',
    ],
    'FamilyRelationship': [
        'Esposo(a)',
        'Hijo(a)',
        'Mamá',
        'Papá',
        'Abuelo(a)',
        'Nieto(a)',
        'Tío(a)',
        'Primo(a)',
        'Otro',
    ],
    'IntegrationLevel': [
        'Unido Recientemente',
        'Integrado',
        'Inconstante',
        'Retirado',
    ],
    'Occupation': [
        'Estudiante Primaria',
        'Estudiante Secundaria',
        'Estudiante Universitario',
        'Empleado',
        'En Busca de Empleo',
        'Otros',
    ],
}

discipleship_seeds = [{
    'name': '4 visitas',
    'description': 'Enseñanza previa a discipulado para una persona recien convertida.',
    'lessons': [{
        'name': 'Primera visita',
        'description': '',
    }, {
        'name': 'Segunda visita',
        'description': '',
    }, {
        'name': 'Tercera visita',
        'description': '',
    }, {
        'name': 'Cuarta visita',
        'description': '',
    }]
}, {
    'name': 'Mi Nuevo Caminar',
    'description': 'Primer discipulado, brindado a nuevos miembros de la congregación.',
    'lessons': [{
        'name': 'Grada 1',
        'description': 'Esté seguro de su Salvación'
    }, {
        'name': 'Grada 2',
        'description': 'Declare su fe públicamente'
    }, {
        'name': 'Grada 3',
        'description': 'Comparta a JESÚS con otros'
    }, {
        'name': 'Grada 4',
        'description': 'Estudie su Biblia'
    }, {
        'name': 'Grada 5',
        'description': 'Aprenda a Orar'
    }, {
        'name': 'Grada 6',
        'description': 'Sea fiel a una iglesia'
    }, {
        'name': 'Grada 7',
        'description': 'Permita que JESÚS controle su vida'
    }]
}, {
    'name': '12 Lecciones',
    'description': 'Segundo discipulado, presenta los principales fundamentos de nuestra doctrina.',
    'lessons': [{
        'name': 'Lección 1',
        'description': 'La Salvación'
    }, {
        'name': 'Lección 2',
        'description': 'La Seguridad de la Salvación'
    }, {
        'name': 'Lección 3',
        'description': 'El Bautismo'
    }, {
        'name': 'Lección 4',
        'description': 'EL ESPÍRITU SANTO'
    }, {
        'name': 'Lección 5',
        'description': 'La Comunión con DIOS'
    }, {
        'name': 'Lección 6',
        'description': 'El Evangelismo Personal'
    }, {
        'name': 'Lección 7',
        'description': 'Nuestra Nueva Familia'
    }, {
        'name': 'Lección 8',
        'description': 'Buenos Administradores'
    }, {
        'name': 'Lección 9',
        'description': 'Las Relaciones Personales'
    }, {
        'name': 'Lección 10',
        'description': 'Mi Testimonio'
    }, {
        'name': 'Lección 11',
        'description': 'La voluntad de DIOS'
    }, {
        'name': 'Lección 12',
        'description': 'El Tribunal de CRISTO'
    }]
}]

def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    # Admin creation
    Person = apps.get_model('pmm', 'Person')
    Member = apps.get_model('pmm', 'Member')
    User = apps.get_model('core', 'User')

    person = Person(first_name='Admin', last_name='Admin')
    person.save()

    member = Member(information=person)
    member.save()

    user = User(username='admin', password=make_password('admin'), owner=member, is_superuser=True)
    user.save()

    # Discipleships and Lessons population
    Discipleship = apps.get_model('pmm', 'Discipleship')
    Lesson = apps.get_model('pmm', 'Lesson')

    for item in discipleship_seeds:
        discipleship = Discipleship(name=item['name'], description=item['description'])
        discipleship.save()

        Lesson.objects.using(db_alias).bulk_create([Lesson(discipleship=discipleship, lesson_number=i+1, name=l['name'], description=l['description']) for i, l in enumerate(item['lessons'])])

    # Lookup tables population
    for model, values in lookup_tables_seeds.items():
        Model = apps.get_model('pmm', model)
        Model.objects.using(db_alias).bulk_create([Model(value=value) for value in values])

def reverse_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Person = apps.get_model("pmm", "Person")
    Discipleship = apps.get_model('pmm', 'Discipleship')

    Person.objects.using(db_alias).filter(first_name='Admin', last_name='Admin').delete()

    with schema_editor.connection.cursor() as cursor:
        cursor.execute('ALTER SEQUENCE core_user_id_seq RESTART WITH 1;')
        cursor.execute("UPDATE core_user SET id=nextval('core_user_id_seq');")
        cursor.execute('ALTER SEQUENCE pmm_person_id_seq RESTART WITH 1;')
        cursor.execute("UPDATE pmm_person SET id=nextval('pmm_person_id_seq');")

    Discipleship.objects.using(db_alias).filter(name__in=[seed['name'] for seed in discipleship_seeds]).delete()

    for model, values in lookup_tables_seeds.items():
        Model = apps.get_model('pmm', model)
        Model.objects.filter(value__in=values).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pmm', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]