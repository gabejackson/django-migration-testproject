# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryCountry',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_person', models.ForeignKey(to='a.ShopUserPerson', to_field=u'person_ptr')),
                ('delivery_address', models.ForeignKey(to='a.ShopUserAddress', to_field=u'address_ptr')),
                ('delivery_contact', models.ForeignKey(to='a.ShopUserContact', to_field=u'contact_ptr')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
