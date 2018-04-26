# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 05:16
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.hashers import make_password

def forwards_func(apps, schema_editor):
    Person = apps.get_model('pmm', 'Person')
    Member = apps.get_model('pmm', 'Member')
    User = apps.get_model('core', 'User')

    db_alias = schema_editor.connection.alias
    person = Person(first_name='Admin', last_name='Admin')
    person.save()

    member = Member(information=person)
    member.save()

    user = User(username='admin', password=make_password('qwerty123'), owner=member, is_superuser=True)
    user.save()

def reverse_func(apps, schema_editor):
    Person = apps.get_model("pmm", "Person")
    db_alias = schema_editor.connection.alias
    Person.objects.using(db_alias).filter(first_name='Admin', last_name='Admin').delete()

    with schema_editor.connection.cursor() as cursor:
        cursor.execute('ALTER SEQUENCE core_user_id_seq RESTART WITH 1;')
        cursor.execute("UPDATE core_user SET id=nextval('core_user_id_seq');")
        cursor.execute('ALTER SEQUENCE pmm_person_id_seq RESTART WITH 1;')
        cursor.execute("UPDATE pmm_person SET id=nextval('pmm_person_id_seq');")


class Migration(migrations.Migration):

    dependencies = [
        ('pmm', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
