# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=80)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.ForeignKey(to='b.DeliveryCountry', to_field=u'id')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShopUserAddress',
            fields=[
                (u'address_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field=u'id', serialize=False, to='a.Address')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('archived', models.BooleanField(default=False, editable=False)),
            ],
            options={
            },
            bases=('a.address',),
        ),
        migrations.CreateModel(
            name='ShopUserContact',
            fields=[
                (u'contact_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field=u'id', serialize=False, to='a.Contact')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
            ],
            options={
            },
            bases=('a.contact',),
        ),
        migrations.CreateModel(
            name='ShopUserPerson',
            fields=[
                (u'person_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field=u'id', serialize=False, to='a.Person')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('archived', models.BooleanField(default=False, editable=False)),
            ],
            options={
            },
            bases=('a.person',),
        ),
    ]
