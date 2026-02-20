from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_hull_hullslot"),
    ]

    operations = [
        migrations.AddField(
            model_name="hullslot",
            name="installed_module",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="api.VehicleModule"),
        ),
    ]
