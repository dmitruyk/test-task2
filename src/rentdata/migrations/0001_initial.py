# Generated by Django 2.1 on 2019-03-25 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('contact_form_type', models.CharField(max_length=80, verbose_name='contactFormType')),
                ('remove_creation', models.DateTimeField(blank=True, null=True)),
                ('remove_id', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='id')),
                ('remove_modification', models.DateTimeField(blank=True, null=True)),
                ('remove_publishDate', models.DateTimeField(blank=True, null=True)),
                ('xlink_href', models.CharField(default=None, max_length=280, verbose_name='xlink_href')),
                ('adLinkForJSONP_xlink_href', models.TextField(default=None, verbose_name='adLinkForJSONP_xlink_href')),
                ('adLinkForXMLData_xlink_href', models.TextField(default=None, verbose_name='adLinkForXMLData_xlink_href')),
            ],
            options={
                'db_table': 'apartment',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('companyWideCustomerId', models.CharField(default=None, max_length=80, verbose_name='companyWideCustomerId')),
                ('contactDetails_id', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='contactDetails_id')),
                ('contactDetails_address_city', models.CharField(default=None, max_length=80, verbose_name='contactDetails_address_city')),
                ('contactDetails_address_houseNumber', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='contactDetails_id')),
                ('contactDetails_address_postcode', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='contactDetails_address_postcode')),
                ('contactDetails_address_street', models.CharField(default=None, max_length=180, verbose_name='contactDetails_address_street')),
                ('contactDetails_cellPhoneNumber', models.CharField(default=None, max_length=180, verbose_name='contactDetails_cellPhoneNumber')),
                ('contactDetails_cellPhoneNumberAreaCode', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='contactDetails_cellPhoneNumberAreaCode')),
                ('contactDetails_cellPhoneNumberCountryCode', models.CharField(default=None, max_length=100, verbose_name='contactDetails_cellPhoneNumberCountryCode')),
                ('contactDetails_cellPhoneNumberSubscriber', models.CharField(default=None, max_length=20, verbose_name='contactDetails_cellPhoneNumberSubscriber')),
                ('contactDetails_company', models.CharField(default=None, max_length=180, verbose_name='contactDetails_company')),
                ('contactDetails_countryCode', models.CharField(default=None, max_length=100, verbose_name='contactDetails_countryCode')),
                ('contactDetails_email', models.CharField(default=None, max_length=50, verbose_name='contactDetails_email')),
                ('contactDetails_faxNumber', models.CharField(default=None, max_length=50, verbose_name='contactDetails_faxNumber')),
                ('contactDetails_faxNumberAreaCode', models.CharField(default=None, max_length=10, verbose_name='contactDetails_faxNumberAreaCode')),
                ('contactDetails_faxNumberCountryCode', models.CharField(default=None, max_length=100, verbose_name='contactDetails_faxNumberCountryCode')),
                ('contactDetails_faxNumberSubscriber', models.CharField(default=None, max_length=100, verbose_name='contactDetails_faxNumberSubscriber')),
                ('contactDetails_firstname', models.CharField(default=None, max_length=30, verbose_name='contactDetails_firstname')),
                ('contactDetails_homepageUrl', models.CharField(default=None, max_length=150, verbose_name='contactDetails_homepageUrl')),
                ('contactDetails_lastname', models.CharField(default=None, max_length=30, verbose_name='contactDetails_lastname')),
                ('contactDetails_phoneNumber', models.CharField(default=None, max_length=50, verbose_name='contactDetails_phoneNumber')),
                ('contactDetails_phoneNumberAreaCode', models.CharField(default=None, max_length=50, verbose_name='contactDetails_phoneNumberAreaCode')),
                ('contactDetails_phoneNumberCountryCode', models.CharField(default=None, max_length=10, verbose_name='contactDetails_phoneNumberCountryCode')),
                ('contactDetails_phoneNumberSubscriber', models.CharField(default=None, max_length=20, verbose_name='contactDetails_phoneNumberSubscriber')),
                ('contactDetails_salutation', models.CharField(default=None, max_length=100, verbose_name='contactDetails_salutation')),
                ('contactFormConfiguration_addressField', models.CharField(default=None, max_length=100, verbose_name='contactFormConfiguration_addressField')),
                ('contactFormConfiguration_applicationPackageCompletedField', models.CharField(default=None, max_length=10, verbose_name='contactFormConfiguration_applicationPackageCompletedField')),
                ('contactFormConfiguration_emailAddressField', models.CharField(default=None, max_length=100, verbose_name='contactFormConfiguration_emailAddressField')),
                ('contactFormConfiguration_employmentRelationshipField', models.CharField(default=None, max_length=10, verbose_name='contactFormConfiguration_employmentRelationshipField')),
                ('contactFormConfiguration_firstnameField', models.CharField(default=None, max_length=100, verbose_name='contactFormConfiguration_firstnameField')),
                ('contactFormConfiguration_freemiumSettings_duration', models.PositiveIntegerField(default=0)),
                ('contactFormConfiguration_incomeField', models.CharField(default=None, max_length=100, verbose_name='contactFormConfiguration_incomeField')),
                ('contactFormConfiguration_lastnameField', models.CharField(default=None, max_length=100, verbose_name='contactFormConfiguration_lastnameField')),
                ('contactFormConfiguration_messageField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_messageField')),
                ('contactFormConfiguration_moveInDateField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_moveInDateField')),
                ('contactFormConfiguration_numberOfPersonsField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_numberOfPersonsField')),
                ('contactFormConfiguration_petsInHouseholdField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_petsInHouseholdField')),
                ('contactFormConfiguration_phoneNumberField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_phoneNumberField')),
                ('contactFormConfiguration_premiumProfileRequired', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_premiumProfileRequired')),
                ('contactFormConfiguration_salutationField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_salutationField')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='ImprintLink',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('imprintLink_xlink_href', models.CharField(default=None, max_length=100, verbose_name='imprintLink_xlink_href')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imprintLink_xlink_href', to='rentdata.Company')),
            ],
            options={
                'db_table': 'imprintLink',
            },
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('realEstate_id', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='id')),
                ('realEstate_xsi_type', models.CharField(default=0, max_length=50, verbose_name='realEstate_xsi_type')),
                ('realEstate_address_city', models.CharField(default=None, max_length=50, verbose_name='realEstate_address_city')),
                ('realEstate_address_geoHierarchy_city_fullGeoCodeId', models.CharField(default=None, max_length=50, verbose_name='realEstate_address_geoHierarchy_city_fullGeoCodeId')),
                ('realEstate_address_geoHierarchy_city_geoCodeId', models.CharField(default=None, max_length=50, verbose_name='realEstate_address_geoHierarchy_city_geoCodeId')),
                ('realEstate_address_geoHierarchy_city_name', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_city_name')),
                ('realEstate_address_geoHierarchy_continent_fullGeoCodeId', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_continent_fullGeoCodeId')),
                ('realEstate_address_geoHierarchy_continent_geoCodeId', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_continent_geoCodeId')),
                ('realEstate_address_geoHierarchy_country_name', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_country_name')),
                ('realEstate_address_geoHierarchy_neighbourhood_geoCodeId', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_neighbourhood_geoCodeId')),
                ('realEstate_address_geoHierarchy_quarter_fullGeoCodeId', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_quarter_fullGeoCodeId')),
                ('realEstate_address_geoHierarchy_quarter_geoCodeId', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_quarter_geoCodeId')),
                ('realEstate_address_geoHierarchy_region_geoCodeId', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_region_geoCodeId')),
                ('realEstate_address_geoHierarchy_region_name', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_region_name')),
                ('realEstate_address_postcode', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_postcode')),
                ('realEstate_address_quarter', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_quarter')),
                ('realEstate_apartmentType', models.CharField(default=None, max_length=150, verbose_name='realEstate_apartmentType')),
                ('realEstate_assistedLiving', models.CharField(default=None, max_length=150, verbose_name='realEstate_assistedLiving')),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_rent_apart', to='rentdata.Apartment')),
            ],
            options={
                'db_table': 'real_estate',
            },
        ),
        migrations.CreateModel(
            name='RealEstateAttachments',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('realEstate_attachments_xlink_href', models.CharField(default=None, max_length=150, verbose_name='realEstate_attachments_xlink_href')),
                ('xsi_type', models.CharField(default=None, max_length=150, verbose_name='xsi_type')),
                ('xlink_href', models.CharField(default=None, max_length=250, verbose_name='xlink_href')),
                ('id_achments', models.CharField(default=None, max_length=250, verbose_name='id_achments')),
                ('modification', models.DateTimeField(blank=True, null=True)),
                ('creation', models.DateTimeField(blank=True, null=True)),
                ('publishDate', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(default=None, max_length=250, verbose_name='title')),
                ('floorplan', models.BooleanField(default=False)),
                ('titlepicture', models.BooleanField(default=False)),
                ('real_estate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='real_estate_attachments', to='rentdata.RealEstate')),
            ],
            options={
                'db_table': 'realestate_attachments',
            },
        ),
        migrations.CreateModel(
            name='RealEstateNext',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('realEstate_balcony', models.BooleanField(default=False)),
                ('realEstate_baseRent', models.CharField(default=None, max_length=250, verbose_name='real_estate_baseRent')),
                ('realEstate_buildingEnergyRatingType', models.CharField(default=None, max_length=250, verbose_name='real_estate_building_energy_rating_type')),
                ('realEstate_builtInKitchen', models.BooleanField(default=False)),
                ('realEstate_calculatedTotalRent', models.CharField(default=None, max_length=250, verbose_name='real_estate_calculated_total_rent')),
                ('realEstate_calculatedTotalRentScope', models.CharField(default=None, max_length=250, verbose_name='real_estate_calculated_total_rent_scope')),
                ('realEstate_cellar', models.CharField(default=None, max_length=250, verbose_name='real_estate_cellar')),
                ('realEstate_certificateOfEligibilityNeeded', models.CharField(default=None, max_length=250, verbose_name='real_estate_certificate_of_eligibility_needed')),
                ('realEstate_condition', models.CharField(default=None, max_length=250, verbose_name='real_estate_condition')),
                ('realEstate_constructionYear', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='real_estate_construction_year')),
                ('realEstate_courtage_hasCourtage', models.CharField(default=None, max_length=250, verbose_name='realEstate_courtage_hasCourtage')),
                ('realEstate_creationDate', models.DateTimeField(blank=True, null=True)),
                ('realEstate_deposit', models.CharField(default=None, max_length=250, verbose_name='realEstate_deposit')),
                ('realEstate_descriptionNote', models.CharField(default=None, max_length=1250, verbose_name='realEstate_descriptionNote')),
                ('realEstate_energyCertificate_energyCertificateAvailability', models.CharField(default=None, max_length=250, verbose_name='realEstate_energyCertificate_energyCertificateAvailability')),
                ('realEstate_energyCertificate_energyCertificateCreationDate', models.CharField(default=None, max_length=1250, verbose_name='realEstate_energyCertificate_energyCertificateCreationDate')),
                ('realEstate_energyConsumptionContainsWarmWater', models.CharField(default=None, max_length=250, verbose_name='realEstate_energyConsumptionContainsWarmWater')),
                ('realEstate_energyPerformanceCertificate', models.BooleanField(default=False)),
                ('realEstate_externalId', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_externalId')),
                ('realEstate_floor', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_floor')),
                ('realEstate_floorplan', models.BooleanField(default=False)),
                ('realEstate_freeFrom', models.CharField(default=None, max_length=250, verbose_name='realEstate_freeFrom')),
                ('realEstate_furnishingNote', models.CharField(default=None, max_length=1250, verbose_name='realEstate_furnishingNote')),
                ('realEstate_garden', models.BooleanField(default=False)),
                ('realEstate_guestToilet', models.CharField(default=None, max_length=50, verbose_name='realEstate_guestToilet')),
                ('realEstate_handicappedAccessible', models.CharField(default=None, max_length=50, verbose_name='realEstate_handicappedAccessible')),
                ('realEstate_heatingCosts', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_heatingCosts')),
                ('realEstate_heatingCostsInServiceCharge', models.CharField(default=None, max_length=50, verbose_name='realEstate_heatingCostsInServiceCharge')),
                ('realEstate_heatingType', models.CharField(default=None, max_length=50, verbose_name='realEstate_heatingType')),
                ('realEstate_heatingTypeEnev2014', models.CharField(default=None, max_length=50, verbose_name='realEstate_heatingTypeEnev2014')),
                ('realEstate_interiorQuality', models.CharField(default=None, max_length=50, verbose_name='realEstate_interiorQuality')),
                ('realEstate_lastModificationDate', models.DateTimeField(blank=True, null=True)),
                ('realEstate_lastRefurbishment', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_lastRefurbishment')),
                ('realEstate_lift', models.BooleanField(default=False)),
                ('realEstate_livingSpace', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_livingSpace')),
                ('realEstate_locationNote', models.CharField(default=None, max_length=1250, verbose_name='realEstate_locationNote')),
                ('realEstate_numberOfFloors', models.IntegerField(blank=True, default=0, null=True, verbose_name='realEstate_numberOfFloors')),
                ('realEstate_numberOfRooms', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_numberOfRooms')),
                ('realEstate_otherNote', models.CharField(default=None, max_length=1250, verbose_name='realEstate_otherNote')),
                ('realEstate_petsAllowed', models.CharField(default=None, max_length=50, verbose_name='realEstate_petsAllowed')),
                ('realEstate_referencePriceApiCall', models.CharField(default=None, max_length=1150, verbose_name='realEstate_referencePriceApiCall')),
                ('realEstate_referencePriceServiceCall', models.CharField(default=None, max_length=1150, verbose_name='realEstate_referencePriceServiceCall')),
                ('realEstate_serviceCharge', models.IntegerField(blank=True, default=0, null=True, verbose_name='realEstate_numberOfFloors')),
                ('realEstate_state', models.CharField(default=None, max_length=1150, verbose_name='realEstate_referencePriceServiceCall')),
                ('realEstate_thermalCharacteristic', models.CharField(default=None, max_length=50, verbose_name='realEstate_thermalCharacteristic')),
                ('realEstate_title', models.CharField(default=None, max_length=250, verbose_name='realEstate_thermalCharacteristic')),
                ('realEstate_titlePicture_creation', models.DateTimeField(blank=True, null=True)),
                ('realEstate_titlePicture_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='realEstate_numberOfFloors')),
                ('realEstate_titlePicture_modification', models.DateTimeField(blank=True, null=True)),
                ('realEstate_titlePicture_publishDate', models.DateTimeField(blank=True, null=True)),
                ('realEstate_titlePicture_floorplan', models.BooleanField(default=False)),
                ('realEstate_titlePicture_title', models.CharField(default=None, max_length=250, verbose_name='realEstate_titlePicture_title')),
                ('realEstate_titlePicture_titlePicture', models.BooleanField(default=False)),
                ('realEstate_totalRent', models.CharField(default=None, max_length=250, verbose_name='realEstate_totalRent')),
                ('realEstate_useAsFlatshareRoom', models.CharField(default=None, max_length=250, verbose_name='realEstate_useAsFlatshareRoom')),
                ('realtorValuationJSONLink_xlink_href', models.CharField(default=None, max_length=550, verbose_name='realtorValuationJSONLink_xlink_href')),
                ('realtorValuationV2JSONLink_xlink_href', models.CharField(default=None, max_length=550, verbose_name='realtorValuationJSONLink_xlink_href')),
                ('realtorValuationV2JSONPLink_xlink_href', models.CharField(default=None, max_length=550, verbose_name='realtorValuationV2JSONPLink_xlink_href')),
                ('real_estate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='real_estate_attachments_nxt', to='rentdata.RealEstate')),
            ],
            options={
                'db_table': 'realestate_attachments_next',
            },
        ),
        migrations.CreateModel(
            name='RealEstateTitlePictureUrls',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('scale', models.CharField(default=None, max_length=250, verbose_name='scale')),
                ('href', models.CharField(default=None, max_length=250, verbose_name='href')),
                ('real_estate_attachments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Real_EstateTitlePictureUrls', to='rentdata.RealEstateAttachments')),
            ],
            options={
                'db_table': 'RealEstateTitlePictureUrls',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('scale', models.CharField(default=None, max_length=250, verbose_name='scale')),
                ('href', models.CharField(default=None, max_length=250, verbose_name='href')),
                ('realestate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='real_url', to='rentdata.RealEstate')),
            ],
            options={
                'db_table': 'url',
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_rent', to='rentdata.Company'),
        ),
    ]
