# Generated by Django 4.1.5 on 2023-09-25 19:30

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=255, verbose_name='Name (English)')),
                ('name_ar', models.CharField(max_length=255, verbose_name='Name (Arabic)')),
                ('description_en', models.TextField(verbose_name='Description (English)')),
                ('description_ar', models.TextField(verbose_name='Description (Arabic)')),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.models.image_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=200, verbose_name='Name (English)')),
                ('name_ar', models.CharField(max_length=200, verbose_name='Name (Arabic)')),
                ('description_en', models.TextField(verbose_name='Description (English)')),
                ('description_ar', models.TextField(verbose_name='Description (Arabic)')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/products')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/products')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/products')),
                ('application', models.CharField(choices=[('Exterior', 'Exterior'), ('Interior', 'Interior')], default=None, max_length=50, null=True)),
                ('cover_type', models.CharField(choices=[('Floor', 'Floor'), ('Joint Opening', 'Joint Opening')], default=None, max_length=50, null=True)),
                ('joint_opening', models.CharField(choices=[('1', '1" [25mm]'), ('2', '2" [51mm]'), ('3', '3" [76mm]'), ('4', '4" [102mm]'), ('5', '5" [125mm]'), ('6', '6" [152mm]'), ('7', '7" [178mm]'), ('8', '8" [203mm]'), ('9', '9" [229mm]'), ('10', '10" [254mm]'), ('11', '11" [279mm]'), ('12', '12" [305mm]'), ('13', '13" [330mm]'), ('14', '14" [356mm]'), ('15', '15" [381mm]'), ('16+', '16+" [406mm+]')], default=None, max_length=50, null=True)),
                ('movement', models.CharField(choices=[('Lateral Shear Capable', 'Lateral Shear Capable'), ('Seismic - Greater than or equal to 50% (+/-)', 'Seismic - Greater than or equal to 50% (+/-)'), ('Thermal - Less than 50% (+/-)', 'Thermal - Less than 50% (+/-)')], default=None, max_length=50, null=True)),
                ('mounting_position', models.CharField(choices=[('Recessed/Flush', 'Recessed/Flush'), ('Surface Mount', 'Surface Mount')], default=None, max_length=50, null=True)),
                ('loading_class', models.CharField(choices=[('Heavy Duty', 'Heavy Duty'), ('Moderate', 'Moderate'), ('Standard', 'Standard')], default=None, max_length=50, null=True)),
                ('floor_thickness', models.CharField(choices=[('0', '0" [0mm] No finish (ie.-concrete deck)'), ('1/2', '1/2" [12.5mm] Thick or greater (ie.- terrazo/ pavers)'), ('3/8', '3/8" [9.5mm] Thick or less (ie.- ceramic tile/vinyl/carpet)'), ('Carpet', 'Carpet'), ('Granite/Marble/Pavers', 'Granite/Marble/Pavers'), ('Laminate', 'Laminate'), ('Other', 'Other'), ('Polished Concrete', 'Polished Concrete'), ('Tile/Terrazo', 'Tile/Terrazo'), ('VCT (Vinyl Composition Tile)/Sheet/Vinyl/LVT', 'VCT (Vinyl Composition Tile)/Sheet/Vinyl/LVT'), ('Wood', 'Wood')], default=None, max_length=50, null=True)),
                ('wall_type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default=None, max_length=50, null=True)),
                ('waterproofing', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default=None, max_length=50, null=True)),
                ('fire_rating', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=255, verbose_name='Name (English)')),
                ('name_ar', models.CharField(max_length=255, verbose_name='Name (Arabic)')),
                ('description_en', models.TextField(verbose_name='Description (English)')),
                ('description_ar', models.TextField(verbose_name='Description (Arabic)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/sub-categories')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('data', models.JSONField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategory'),
        ),
    ]
