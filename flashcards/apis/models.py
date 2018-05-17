# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ApisSlowa(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'apis_slowa'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Definicje(models.Model):
    id_definicja = models.AutoField(primary_key=True)
    definicja = models.CharField(max_length=45, blank=True, null=True)
    autor = models.CharField(max_length=45, blank=True, null=True)
    data_dod = models.DateField(blank=True, null=True)
    sumalike = models.CharField(db_column='sumaLike', max_length=45, blank=True, null=True)  # Field name made lowercase.
    id_slowo = models.ForeignKey('Slowa', models.DO_NOTHING, db_column='id_slowo')

    class Meta:
        managed = False
        db_table = 'definicje'


class Dislikes(models.Model):
    id_dislike = models.AutoField(primary_key=True)
    uzytkownik = models.CharField(max_length=45, blank=True, null=True)
    id_slowo = models.ForeignKey('Slowa', related_name='dislikes', on_delete= models.CASCADE, db_column='id_slowo')

    class Meta:
        managed = False
        db_table = 'dislikes'

    def __unicode__(self):
        return  '%s' % (self.uzytkownik)


class DislikesDef(models.Model):
    id_dislike_def = models.AutoField(primary_key=True)
    uzytkownik = models.CharField(max_length=45, blank=True, null=True)
    id_definicja = models.ForeignKey(Definicje, related_name='dislikes', on_delete= models.CASCADE, db_column='id_definicja')

    class Meta:
        managed = False
        db_table = 'dislikes_def'

    def __unicode__(self):
        return  '%s' % (self.uzytkownik)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Likes(models.Model):
    id_like = models.AutoField(primary_key=True)
    uzytkownik = models.CharField(max_length=45, blank=True, null=True)
    id_slowo = models.ForeignKey('Slowa', related_name='likes', on_delete= models.CASCADE, db_column='id_slowo')

    class Meta:
        managed = False
        db_table = 'likes'

    def __unicode__(self):
        return  '%s' % (self.uzytkownik)


class LikesDef(models.Model):
    id_like_def = models.AutoField(primary_key=True)
    uzytkownik = models.CharField(max_length=45, blank=True, null=True)
    id_definicja = models.ForeignKey('Definicje', related_name='likes', on_delete= models.CASCADE, db_column='id_definicja')

    class Meta:
        managed = False
        db_table = 'likes_def'

    def __unicode__(self):
        return  '%s' % (self.uzytkownik)


class Slowa(models.Model):
    id_slowo = models.AutoField(primary_key=True)
    slowo = models.CharField(max_length=45, blank=True, null=True)
    autor = models.CharField(max_length=45, blank=True, null=True)
    data_dod = models.DateField(blank=True, null=True)
    sumalike = models.CharField(db_column='sumaLike', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slowa'
