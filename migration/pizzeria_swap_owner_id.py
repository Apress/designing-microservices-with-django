def set_defaults(apps, schema_editor):
    Pizzeria = apps.get_model('pizza', 'pizzeria')
    for pizzeria in Pizzeria.objects.all().iterator():
        pizzeria.owner_user_profile_id = pizzeria.owner.id
        pizzeria.save()


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_pizzeria'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzeria',
            name='owner_user_profile_id',
            field=models.PositiveIntegerField(null=True),
            preserve_default=False,
        ),
        migrations.RunPython(set_defaults, reverse),
        migrations.AlterField(
            model_name='pizzeria',
            name='owner_user_profile_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.RemoveField(
            model_name='pizzeria',
            name='owner',
        ),
    ]
