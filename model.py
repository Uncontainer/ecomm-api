__author__ = 'jburks'

# Created with pwiz.py
# pwiz.py -e mysql -u root converse > model_all.py
# This file is a trimmed down version of model_all.py, which is a direct dump of pwiz
# model_all.py won't run as is, so be warned...

from peewee import *

database = MySQLDatabase('converse', **{'user': 'root'})

# This might be specific to Converse, so tweak as needed for other schools.
eav_attr = {
    'item_ean': 142,
    'item_author': 140,
    'item_title': 71,
    'item_ebook': 145,
    'item_esub_duration': 144,
    'item_new': 146,
    'item_rental': 149,
    'item_used': 150,
    'no_text_required': 158,
}

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class ApiUser(BaseModel):
    api_key = CharField(max_length=40, null=True)
    created = DateTimeField()
    email = CharField(max_length=128, null=True)
    firstname = CharField(max_length=32, null=True)
    is_active = IntegerField()
    lastname = CharField(max_length=32, null=True)
    lognum = IntegerField()
    modified = DateTimeField(null=True)
    reload_acl_flag = IntegerField()
    user = PrimaryKeyField(db_column='user_id')
    username = CharField(max_length=40, null=True)

    class Meta:
        db_table = 'api_user'

class Schools(BaseModel):
    school_name = CharField(max_length=255)
    short_name = CharField(max_length=255)

    class Meta:
        db_table = 'schools'

class Departments(BaseModel):
    active = IntegerField()
    department_code = CharField(max_length=255)
    department_name = CharField(max_length=255)
    school = ForeignKeyField(db_column='school_id', rel_model=Schools)

    class Meta:
        db_table = 'departments'

class TermNames(BaseModel):
    active = IntegerField()
    school = ForeignKeyField(db_column='school_id', rel_model=Schools)
    term_name = CharField(max_length=45)

    class Meta:
        db_table = 'term_names'

class Adoptions(BaseModel):
    course_code = CharField(max_length=255)
    course_name = CharField(max_length=255)
    created_at = DateTimeField()
    department = ForeignKeyField(db_column='department_id', rel_model=Departments)
    magento_course = IntegerField(db_column='magento_course_id')
    section_code = CharField(max_length=255)
    term_name = ForeignKeyField(db_column='term_name_id', rel_model=TermNames)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'adoptions'

class CoreWebsite(BaseModel):
    code = CharField(max_length=32, null=True)
    default_group = IntegerField(db_column='default_group_id')
    is_default = IntegerField(null=True)
    name = CharField(max_length=64, null=True)
    sort_order = IntegerField()
    website = PrimaryKeyField(db_column='website_id')

    class Meta:
        db_table = 'core_website'

class CoreStoreGroup(BaseModel):
    default_store = IntegerField(db_column='default_store_id')
    group = PrimaryKeyField(db_column='group_id')
    name = CharField(max_length=255)
    root_category = IntegerField(db_column='root_category_id')
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'core_store_group'

class CoreStore(BaseModel):
    code = CharField(max_length=32, null=True)
    group = ForeignKeyField(db_column='group_id', rel_model=CoreStoreGroup)
    is_active = IntegerField()
    name = CharField(max_length=255)
    sort_order = IntegerField()
    store = PrimaryKeyField(db_column='store_id')
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'core_store'

class EavEntityType(BaseModel):
    additional_attribute_table = CharField(max_length=255, null=True)
    attribute_model = CharField(max_length=255, null=True)
    data_sharing_key = CharField(max_length=100, null=True)
    default_attribute_set = IntegerField(db_column='default_attribute_set_id')
    entity_attribute_collection = CharField(max_length=255, null=True)
    entity_id_field = CharField(max_length=255, null=True)
    entity_model = CharField(max_length=255)
    entity_table = CharField(max_length=255, null=True)
    entity_type_code = CharField(max_length=50)
    entity_type = PrimaryKeyField(db_column='entity_type_id')
    increment_model = CharField(max_length=255, null=True)
    increment_pad_char = CharField(max_length=1)
    increment_pad_length = IntegerField()
    increment_per_store = IntegerField()
    is_data_sharing = IntegerField()
    value_table_prefix = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'eav_entity_type'

class EavAttributeSet(BaseModel):
    attribute_set = PrimaryKeyField(db_column='attribute_set_id')
    attribute_set_name = CharField(max_length=255, null=True)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    sort_order = IntegerField()

    class Meta:
        db_table = 'eav_attribute_set'

class EavAttribute(BaseModel):
    attribute_code = CharField(max_length=255, null=True)
    attribute = PrimaryKeyField(db_column='attribute_id')
    attribute_model = CharField(max_length=255, null=True)
    backend_model = CharField(max_length=255, null=True)
    backend_table = CharField(max_length=255, null=True)
    backend_type = CharField(max_length=8)
    default_value = TextField(null=True)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    frontend_class = CharField(max_length=255, null=True)
    frontend_input = CharField(max_length=50, null=True)
    frontend_label = CharField(max_length=255, null=True)
    frontend_model = CharField(max_length=255, null=True)
    is_required = IntegerField()
    is_unique = IntegerField()
    is_user_defined = IntegerField()
    note = CharField(max_length=255, null=True)
    source_model = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'eav_attribute'

class CatalogProductEntity(BaseModel):
    attribute_set = ForeignKeyField(db_column='attribute_set_id', rel_model=EavAttributeSet)
    created_at = DateTimeField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    has_options = IntegerField()
    required_options = IntegerField()
    sku = CharField(max_length=64, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'catalog_product_entity'

class CatalogProductBundleOption(BaseModel):
    option = PrimaryKeyField(db_column='option_id')
    parent = ForeignKeyField(db_column='parent_id', rel_model=CatalogProductEntity)
    position = IntegerField()
    required = IntegerField()
    type = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_product_bundle_option'

class CatalogProductBundleOptionValue(BaseModel):
    option = ForeignKeyField(db_column='option_id', rel_model=CatalogProductBundleOption)
    store = IntegerField(db_column='store_id')
    title = CharField(max_length=255, null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_bundle_option_value'

class CustomerGroup(BaseModel):
    customer_group_code = CharField(max_length=32)
    customer_group = PrimaryKeyField(db_column='customer_group_id')
    tax_class = IntegerField(db_column='tax_class_id')

    class Meta:
        db_table = 'customer_group'

class CatalogProductBundlePriceIndex(BaseModel):
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    max_price = DecimalField()
    min_price = DecimalField()
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_bundle_price_index'

class CatalogProductBundleSelection(BaseModel):
    is_default = IntegerField()
    option = ForeignKeyField(db_column='option_id', rel_model=CatalogProductBundleOption)
    parent_product = IntegerField(db_column='parent_product_id')
    position = IntegerField()
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    selection_can_change_qty = IntegerField()
    selection = PrimaryKeyField(db_column='selection_id')
    selection_price_type = IntegerField()
    selection_price_value = DecimalField()
    selection_qty = DecimalField(null=True)

    class Meta:
        db_table = 'catalog_product_bundle_selection'

class CatalogProductBundleSelectionPrice(BaseModel):
    selection = ForeignKeyField(db_column='selection_id', primary_key=True, rel_model=CatalogProductBundleSelection)
    selection_price_type = IntegerField()
    selection_price_value = DecimalField()
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_bundle_selection_price'

class CatalogProductBundleStockIndex(BaseModel):
    entity = PrimaryKeyField(db_column='entity_id')
    option = IntegerField(db_column='option_id')
    stock = IntegerField(db_column='stock_id')
    stock_status = IntegerField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_bundle_stock_index'

class CatalogProductEnabledIndex(BaseModel):
    product = ForeignKeyField(db_column='product_id', primary_key=True, rel_model=CatalogProductEntity)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    visibility = IntegerField()

    class Meta:
        db_table = 'catalog_product_enabled_index'

class CatalogProductEntityDatetime(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = DateTimeField(null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_datetime'

class CatalogProductEntityDecimal(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = DecimalField(null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_decimal'

class CatalogProductEntityGallery(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = CharField(max_length=255, null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_gallery'

class CatalogProductEntityGroupPrice(BaseModel):
    all_groups = IntegerField()
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    value = DecimalField()
    value_id = PrimaryKeyField(db_column='value_id')
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_entity_group_price'

class CatalogProductEntityInt(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = IntegerField(null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_int'

class CatalogProductEntityMediaGallery(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    value = CharField(max_length=255, null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_media_gallery'

class CatalogProductEntityMediaGalleryValue(BaseModel):
    disabled = IntegerField()
    label = CharField(max_length=255, null=True)
    position = IntegerField(null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value_id = ForeignKeyField(db_column='value_id', primary_key=True, rel_model=CatalogProductEntityMediaGallery)

    class Meta:
        db_table = 'catalog_product_entity_media_gallery_value'

class CatalogProductEntityText(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = TextField(null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_text'

class CatalogProductEntityTierPrice(BaseModel):
    all_groups = IntegerField()
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    qty = DecimalField()
    value = DecimalField()
    value_id = PrimaryKeyField(db_column='value_id')
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_entity_tier_price'

class CatalogProductEntityVarchar(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = CharField(max_length=255, null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_varchar'

class CatalogProductFlat1(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    cost = DecimalField(null=True)
    created_at = DateTimeField(null=True)
    enable_googlecheckout = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    gift_message_available = IntegerField(null=True)
    giftcard_amounts = DecimalField(null=True)
    has_options = IntegerField()
    image_label = CharField(max_length=255, null=True)
    is_recurring = IntegerField(null=True)
    links_exist = IntegerField(null=True)
    links_purchased_separately = IntegerField(null=True)
    links_title = CharField(max_length=255, null=True)
    msrp = DecimalField(null=True)
    msrp_display_actual_price_type = CharField(max_length=255, null=True)
    msrp_enabled = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    news_from_date = DateTimeField(null=True)
    news_to_date = DateTimeField(null=True)
    open_amount_max = DecimalField(null=True)
    open_amount_min = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField(null=True)
    price_view = IntegerField(null=True)
    recurring_profile = TextField(null=True)
    required_options = IntegerField()
    shipment_type = IntegerField(null=True)
    short_description = TextField(null=True)
    sku = CharField(max_length=64, null=True)
    sku_type = IntegerField(null=True)
    small_image = CharField(max_length=255, null=True)
    small_image_label = CharField(max_length=255, null=True)
    special_from_date = DateTimeField(null=True)
    special_price = DecimalField(null=True)
    special_to_date = DateTimeField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    thumbnail = CharField(max_length=255, null=True)
    thumbnail_label = CharField(max_length=255, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)
    visibility = IntegerField(null=True)
    weight = DecimalField(null=True)
    weight_type = IntegerField(null=True)

    class Meta:
        db_table = 'catalog_product_flat_1'

class CatalogProductFlat2(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    cost = DecimalField(null=True)
    created_at = DateTimeField(null=True)
    enable_googlecheckout = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    gift_message_available = IntegerField(null=True)
    giftcard_amounts = DecimalField(null=True)
    has_options = IntegerField()
    image_label = CharField(max_length=255, null=True)
    is_recurring = IntegerField(null=True)
    links_exist = IntegerField(null=True)
    links_purchased_separately = IntegerField(null=True)
    links_title = CharField(max_length=255, null=True)
    msrp = DecimalField(null=True)
    msrp_display_actual_price_type = CharField(max_length=255, null=True)
    msrp_enabled = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    news_from_date = DateTimeField(null=True)
    news_to_date = DateTimeField(null=True)
    open_amount_max = DecimalField(null=True)
    open_amount_min = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField(null=True)
    price_view = IntegerField(null=True)
    recurring_profile = TextField(null=True)
    required_options = IntegerField()
    shipment_type = IntegerField(null=True)
    short_description = TextField(null=True)
    sku = CharField(max_length=64, null=True)
    sku_type = IntegerField(null=True)
    small_image = CharField(max_length=255, null=True)
    small_image_label = CharField(max_length=255, null=True)
    special_from_date = DateTimeField(null=True)
    special_price = DecimalField(null=True)
    special_to_date = DateTimeField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    thumbnail = CharField(max_length=255, null=True)
    thumbnail_label = CharField(max_length=255, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)
    visibility = IntegerField(null=True)
    weight = DecimalField(null=True)
    weight_type = IntegerField(null=True)

    class Meta:
        db_table = 'catalog_product_flat_2'

class CatalogProductFlat3(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    cost = DecimalField(null=True)
    created_at = DateTimeField(null=True)
    enable_googlecheckout = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    gift_message_available = IntegerField(null=True)
    giftcard_amounts = DecimalField(null=True)
    has_options = IntegerField()
    image_label = CharField(max_length=255, null=True)
    is_recurring = IntegerField(null=True)
    links_exist = IntegerField(null=True)
    links_purchased_separately = IntegerField(null=True)
    links_title = CharField(max_length=255, null=True)
    msrp = DecimalField(null=True)
    msrp_display_actual_price_type = CharField(max_length=255, null=True)
    msrp_enabled = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    news_from_date = DateTimeField(null=True)
    news_to_date = DateTimeField(null=True)
    open_amount_max = DecimalField(null=True)
    open_amount_min = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField(null=True)
    price_view = IntegerField(null=True)
    recurring_profile = TextField(null=True)
    required_options = IntegerField()
    shipment_type = IntegerField(null=True)
    short_description = TextField(null=True)
    sku = CharField(max_length=64, null=True)
    sku_type = IntegerField(null=True)
    small_image = CharField(max_length=255, null=True)
    small_image_label = CharField(max_length=255, null=True)
    special_from_date = DateTimeField(null=True)
    special_price = DecimalField(null=True)
    special_to_date = DateTimeField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    thumbnail = CharField(max_length=255, null=True)
    thumbnail_label = CharField(max_length=255, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)
    visibility = IntegerField(null=True)
    weight = DecimalField(null=True)
    weight_type = IntegerField(null=True)

    class Meta:
        db_table = 'catalog_product_flat_3'

class CatalogProductFlat4(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    cost = DecimalField(null=True)
    created_at = DateTimeField(null=True)
    enable_googlecheckout = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    gift_message_available = IntegerField(null=True)
    giftcard_amounts = DecimalField(null=True)
    has_options = IntegerField()
    image_label = CharField(max_length=255, null=True)
    is_recurring = IntegerField(null=True)
    links_exist = IntegerField(null=True)
    links_purchased_separately = IntegerField(null=True)
    links_title = CharField(max_length=255, null=True)
    msrp = DecimalField(null=True)
    msrp_display_actual_price_type = CharField(max_length=255, null=True)
    msrp_enabled = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    news_from_date = DateTimeField(null=True)
    news_to_date = DateTimeField(null=True)
    open_amount_max = DecimalField(null=True)
    open_amount_min = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField(null=True)
    price_view = IntegerField(null=True)
    recurring_profile = TextField(null=True)
    required_options = IntegerField()
    shipment_type = IntegerField(null=True)
    short_description = TextField(null=True)
    sku = CharField(max_length=64, null=True)
    sku_type = IntegerField(null=True)
    small_image = CharField(max_length=255, null=True)
    small_image_label = CharField(max_length=255, null=True)
    special_from_date = DateTimeField(null=True)
    special_price = DecimalField(null=True)
    special_to_date = DateTimeField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    thumbnail = CharField(max_length=255, null=True)
    thumbnail_label = CharField(max_length=255, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)
    visibility = IntegerField(null=True)
    weight = DecimalField(null=True)
    weight_type = IntegerField(null=True)

    class Meta:
        db_table = 'catalog_product_flat_4'

class CatalogProductFlat5(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    cost = DecimalField(null=True)
    created_at = DateTimeField(null=True)
    enable_googlecheckout = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    gift_message_available = IntegerField(null=True)
    giftcard_amounts = DecimalField(null=True)
    has_options = IntegerField()
    image_label = CharField(max_length=255, null=True)
    is_recurring = IntegerField(null=True)
    links_exist = IntegerField(null=True)
    links_purchased_separately = IntegerField(null=True)
    links_title = CharField(max_length=255, null=True)
    msrp = DecimalField(null=True)
    msrp_display_actual_price_type = CharField(max_length=255, null=True)
    msrp_enabled = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    news_from_date = DateTimeField(null=True)
    news_to_date = DateTimeField(null=True)
    open_amount_max = DecimalField(null=True)
    open_amount_min = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField(null=True)
    price_view = IntegerField(null=True)
    recurring_profile = TextField(null=True)
    required_options = IntegerField()
    shipment_type = IntegerField(null=True)
    short_description = TextField(null=True)
    sku = CharField(max_length=64, null=True)
    sku_type = IntegerField(null=True)
    small_image = CharField(max_length=255, null=True)
    small_image_label = CharField(max_length=255, null=True)
    special_from_date = DateTimeField(null=True)
    special_price = DecimalField(null=True)
    special_to_date = DateTimeField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    thumbnail = CharField(max_length=255, null=True)
    thumbnail_label = CharField(max_length=255, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)
    visibility = IntegerField(null=True)
    weight = DecimalField(null=True)
    weight_type = IntegerField(null=True)

    class Meta:
        db_table = 'catalog_product_flat_5'

class CatalogProductFlat6(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    cost = DecimalField(null=True)
    created_at = DateTimeField(null=True)
    enable_googlecheckout = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    gift_message_available = IntegerField(null=True)
    giftcard_amounts = DecimalField(null=True)
    has_options = IntegerField()
    image_label = CharField(max_length=255, null=True)
    is_recurring = IntegerField(null=True)
    links_exist = IntegerField(null=True)
    links_purchased_separately = IntegerField(null=True)
    links_title = CharField(max_length=255, null=True)
    msrp = DecimalField(null=True)
    msrp_display_actual_price_type = CharField(max_length=255, null=True)
    msrp_enabled = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    news_from_date = DateTimeField(null=True)
    news_to_date = DateTimeField(null=True)
    open_amount_max = DecimalField(null=True)
    open_amount_min = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField(null=True)
    price_view = IntegerField(null=True)
    recurring_profile = TextField(null=True)
    required_options = IntegerField()
    shipment_type = IntegerField(null=True)
    short_description = TextField(null=True)
    sku = CharField(max_length=64, null=True)
    sku_type = IntegerField(null=True)
    small_image = CharField(max_length=255, null=True)
    small_image_label = CharField(max_length=255, null=True)
    special_from_date = DateTimeField(null=True)
    special_price = DecimalField(null=True)
    special_to_date = DateTimeField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    thumbnail = CharField(max_length=255, null=True)
    thumbnail_label = CharField(max_length=255, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)
    visibility = IntegerField(null=True)
    weight = DecimalField(null=True)
    weight_type = IntegerField(null=True)

    class Meta:
        db_table = 'catalog_product_flat_6'

class CatalogProductFlat7(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    cost = DecimalField(null=True)
    created_at = DateTimeField(null=True)
    enable_googlecheckout = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    gift_message_available = IntegerField(null=True)
    giftcard_amounts = DecimalField(null=True)
    has_options = IntegerField()
    image_label = CharField(max_length=255, null=True)
    is_recurring = IntegerField(null=True)
    links_exist = IntegerField(null=True)
    links_purchased_separately = IntegerField(null=True)
    links_title = CharField(max_length=255, null=True)
    msrp = DecimalField(null=True)
    msrp_display_actual_price_type = CharField(max_length=255, null=True)
    msrp_enabled = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    news_from_date = DateTimeField(null=True)
    news_to_date = DateTimeField(null=True)
    open_amount_max = DecimalField(null=True)
    open_amount_min = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField(null=True)
    price_view = IntegerField(null=True)
    recurring_profile = TextField(null=True)
    required_options = IntegerField()
    shipment_type = IntegerField(null=True)
    short_description = TextField(null=True)
    sku = CharField(max_length=64, null=True)
    sku_type = IntegerField(null=True)
    small_image = CharField(max_length=255, null=True)
    small_image_label = CharField(max_length=255, null=True)
    special_from_date = DateTimeField(null=True)
    special_price = DecimalField(null=True)
    special_to_date = DateTimeField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    thumbnail = CharField(max_length=255, null=True)
    thumbnail_label = CharField(max_length=255, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)
    visibility = IntegerField(null=True)
    weight = DecimalField(null=True)
    weight_type = IntegerField(null=True)

    class Meta:
        db_table = 'catalog_product_flat_7'

class CatalogProductFlat8(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    cost = DecimalField(null=True)
    created_at = DateTimeField(null=True)
    enable_googlecheckout = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    gift_message_available = IntegerField(null=True)
    giftcard_amounts = DecimalField(null=True)
    has_options = IntegerField()
    image_label = CharField(max_length=255, null=True)
    is_recurring = IntegerField(null=True)
    links_exist = IntegerField(null=True)
    links_purchased_separately = IntegerField(null=True)
    links_title = CharField(max_length=255, null=True)
    msrp = DecimalField(null=True)
    msrp_display_actual_price_type = CharField(max_length=255, null=True)
    msrp_enabled = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    news_from_date = DateTimeField(null=True)
    news_to_date = DateTimeField(null=True)
    open_amount_max = DecimalField(null=True)
    open_amount_min = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField(null=True)
    price_view = IntegerField(null=True)
    recurring_profile = TextField(null=True)
    required_options = IntegerField()
    shipment_type = IntegerField(null=True)
    short_description = TextField(null=True)
    sku = CharField(max_length=64, null=True)
    sku_type = IntegerField(null=True)
    small_image = CharField(max_length=255, null=True)
    small_image_label = CharField(max_length=255, null=True)
    special_from_date = DateTimeField(null=True)
    special_price = DecimalField(null=True)
    special_to_date = DateTimeField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    thumbnail = CharField(max_length=255, null=True)
    thumbnail_label = CharField(max_length=255, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)
    visibility = IntegerField(null=True)
    weight = DecimalField(null=True)
    weight_type = IntegerField(null=True)

    class Meta:
        db_table = 'catalog_product_flat_8'

class CatalogProductFlat9(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    cost = DecimalField(null=True)
    created_at = DateTimeField(null=True)
    enable_googlecheckout = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    gift_message_available = IntegerField(null=True)
    giftcard_amounts = DecimalField(null=True)
    has_options = IntegerField()
    image_label = CharField(max_length=255, null=True)
    is_recurring = IntegerField(null=True)
    links_exist = IntegerField(null=True)
    links_purchased_separately = IntegerField(null=True)
    links_title = CharField(max_length=255, null=True)
    msrp = DecimalField(null=True)
    msrp_display_actual_price_type = CharField(max_length=255, null=True)
    msrp_enabled = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    news_from_date = DateTimeField(null=True)
    news_to_date = DateTimeField(null=True)
    open_amount_max = DecimalField(null=True)
    open_amount_min = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField(null=True)
    price_view = IntegerField(null=True)
    recurring_profile = TextField(null=True)
    required_options = IntegerField()
    shipment_type = IntegerField(null=True)
    short_description = TextField(null=True)
    sku = CharField(max_length=64, null=True)
    sku_type = IntegerField(null=True)
    small_image = CharField(max_length=255, null=True)
    small_image_label = CharField(max_length=255, null=True)
    special_from_date = DateTimeField(null=True)
    special_price = DecimalField(null=True)
    special_to_date = DateTimeField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    thumbnail = CharField(max_length=255, null=True)
    thumbnail_label = CharField(max_length=255, null=True)
    type = CharField(db_column='type_id', max_length=32)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)
    visibility = IntegerField(null=True)
    weight = DecimalField(null=True)
    weight_type = IntegerField(null=True)

    class Meta:
        db_table = 'catalog_product_flat_9'

class CatalogProductIndexEav(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = IntegerField()

    class Meta:
        db_table = 'catalog_product_index_eav'

class CatalogProductIndexEavDecimal(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = DecimalField()

    class Meta:
        db_table = 'catalog_product_index_eav_decimal'

class CatalogProductIndexEavDecimalIdx(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    entity = PrimaryKeyField(db_column='entity_id')
    store = IntegerField(db_column='store_id')
    value = DecimalField()

    class Meta:
        db_table = 'catalog_product_index_eav_decimal_idx'

class CatalogProductIndexEavDecimalTmp(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    entity = PrimaryKeyField(db_column='entity_id')
    store = IntegerField(db_column='store_id')
    value = DecimalField()

    class Meta:
        db_table = 'catalog_product_index_eav_decimal_tmp'

class CatalogProductIndexEavIdx(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    entity = PrimaryKeyField(db_column='entity_id')
    store = IntegerField(db_column='store_id')
    value = IntegerField()

    class Meta:
        db_table = 'catalog_product_index_eav_idx'

class CatalogProductIndexEavTmp(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    entity = PrimaryKeyField(db_column='entity_id')
    store = IntegerField(db_column='store_id')
    value = IntegerField()

    class Meta:
        db_table = 'catalog_product_index_eav_tmp'

class CatalogProductIndexGroupPrice(BaseModel):
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    price = DecimalField(null=True)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_index_group_price'

class CatalogProductIndexPrice(BaseModel):
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    final_price = DecimalField(null=True)
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    price = DecimalField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    tier_price = DecimalField(null=True)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_index_price'

class CatalogProductIndexPriceBundleIdx(BaseModel):
    base_group_price = DecimalField(null=True)
    base_tier = DecimalField(null=True)
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    group_price_percent = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    orig_price = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField()
    special_price = DecimalField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    tier_percent = DecimalField(null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_bundle_idx'

class CatalogProductIndexPriceBundleOptIdx(BaseModel):
    alt_group_price = DecimalField(null=True)
    alt_price = DecimalField(null=True)
    alt_tier_price = DecimalField(null=True)
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    option = IntegerField(db_column='option_id')
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_bundle_opt_idx'

class CatalogProductIndexPriceBundleOptTmp(BaseModel):
    alt_group_price = DecimalField(null=True)
    alt_price = DecimalField(null=True)
    alt_tier_price = DecimalField(null=True)
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    option = IntegerField(db_column='option_id')
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_bundle_opt_tmp'

class CatalogProductIndexPriceBundleSelIdx(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    group_type = IntegerField(null=True)
    is_required = IntegerField(null=True)
    option = IntegerField(db_column='option_id')
    price = DecimalField(null=True)
    selection = IntegerField(db_column='selection_id')
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_bundle_sel_idx'

class CatalogProductIndexPriceBundleSelTmp(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    group_type = IntegerField(null=True)
    is_required = IntegerField(null=True)
    option = IntegerField(db_column='option_id')
    price = DecimalField(null=True)
    selection = IntegerField(db_column='selection_id')
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_bundle_sel_tmp'

class CatalogProductIndexPriceBundleTmp(BaseModel):
    base_group_price = DecimalField(null=True)
    base_tier = DecimalField(null=True)
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    group_price_percent = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    orig_price = DecimalField(null=True)
    price = DecimalField(null=True)
    price_type = IntegerField()
    special_price = DecimalField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    tier_percent = DecimalField(null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_bundle_tmp'

class CatalogProductIndexPriceCfgOptAgrIdx(BaseModel):
    child = IntegerField(db_column='child_id')
    customer_group = IntegerField(db_column='customer_group_id')
    group_price = DecimalField(null=True)
    parent = PrimaryKeyField(db_column='parent_id')
    price = DecimalField(null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_cfg_opt_agr_idx'

class CatalogProductIndexPriceCfgOptAgrTmp(BaseModel):
    child = IntegerField(db_column='child_id')
    customer_group = IntegerField(db_column='customer_group_id')
    group_price = DecimalField(null=True)
    parent = PrimaryKeyField(db_column='parent_id')
    price = DecimalField(null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_cfg_opt_agr_tmp'

class CatalogProductIndexPriceCfgOptIdx(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_cfg_opt_idx'

class CatalogProductIndexPriceCfgOptTmp(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_cfg_opt_tmp'

class CatalogProductIndexPriceDownlodIdx(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    max_price = DecimalField()
    min_price = DecimalField()
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_downlod_idx'

class CatalogProductIndexPriceDownlodTmp(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    max_price = DecimalField()
    min_price = DecimalField()
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_downlod_tmp'

class CatalogProductIndexPriceFinalIdx(BaseModel):
    base_group_price = DecimalField(null=True)
    base_tier = DecimalField(null=True)
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    orig_price = DecimalField(null=True)
    price = DecimalField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_final_idx'

class CatalogProductIndexPriceFinalTmp(BaseModel):
    base_group_price = DecimalField(null=True)
    base_tier = DecimalField(null=True)
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    orig_price = DecimalField(null=True)
    price = DecimalField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_final_tmp'

class CatalogProductIndexPriceIdx(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    final_price = DecimalField(null=True)
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    price = DecimalField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_idx'

class CatalogProductIndexPriceOptAgrIdx(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    option = IntegerField(db_column='option_id')
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_opt_agr_idx'

class CatalogProductIndexPriceOptAgrTmp(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    option = IntegerField(db_column='option_id')
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_opt_agr_tmp'

class CatalogProductIndexPriceOptIdx(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_opt_idx'

class CatalogProductIndexPriceOptTmp(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_opt_tmp'

class CatalogProductIndexPriceTmp(BaseModel):
    customer_group = IntegerField(db_column='customer_group_id')
    entity = PrimaryKeyField(db_column='entity_id')
    final_price = DecimalField(null=True)
    group_price = DecimalField(null=True)
    max_price = DecimalField(null=True)
    min_price = DecimalField(null=True)
    price = DecimalField(null=True)
    tax_class = IntegerField(db_column='tax_class_id', null=True)
    tier_price = DecimalField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'catalog_product_index_price_tmp'

class CatalogProductIndexTierPrice(BaseModel):
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogProductEntity)
    min_price = DecimalField(null=True)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_index_tier_price'

class CatalogProductIndexWebsite(BaseModel):
    rate = FloatField(null=True)
    website_date = DateField(null=True)
    website = ForeignKeyField(db_column='website_id', primary_key=True, rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_index_website'

class CatalogProductLinkType(BaseModel):
    code = CharField(max_length=32, null=True)
    link_type = PrimaryKeyField(db_column='link_type_id')

    class Meta:
        db_table = 'catalog_product_link_type'

class CatalogProductLink(BaseModel):
    link = PrimaryKeyField(db_column='link_id')
    link_type = ForeignKeyField(db_column='link_type_id', rel_model=CatalogProductLinkType)
    linked_product = ForeignKeyField(db_column='linked_product_id', rel_model=CatalogProductEntity, related_name="categoryproductlink_linkedproduct")
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)

    class Meta:
        db_table = 'catalog_product_link'

class CatalogProductLinkAttribute(BaseModel):
    data_type = CharField(max_length=32, null=True)
    link_type = ForeignKeyField(db_column='link_type_id', rel_model=CatalogProductLinkType)
    product_link_attribute_code = CharField(max_length=32, null=True)
    product_link_attribute = PrimaryKeyField(db_column='product_link_attribute_id')

    class Meta:
        db_table = 'catalog_product_link_attribute'

class CatalogProductLinkAttributeDecimal(BaseModel):
    link = ForeignKeyField(db_column='link_id', rel_model=CatalogProductLink)
    product_link_attribute = ForeignKeyField(db_column='product_link_attribute_id', null=True, rel_model=CatalogProductLinkAttribute)
    value = DecimalField()
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_link_attribute_decimal'

class CatalogProductLinkAttributeInt(BaseModel):
    link = ForeignKeyField(db_column='link_id', rel_model=CatalogProductLink)
    product_link_attribute = ForeignKeyField(db_column='product_link_attribute_id', null=True, rel_model=CatalogProductLinkAttribute)
    value = IntegerField()
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_link_attribute_int'

class CatalogProductLinkAttributeVarchar(BaseModel):
    link = ForeignKeyField(db_column='link_id', rel_model=CatalogProductLink)
    product_link_attribute = ForeignKeyField(db_column='product_link_attribute_id', rel_model=CatalogProductLinkAttribute)
    value = CharField(max_length=255, null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_link_attribute_varchar'

class CatalogProductOption(BaseModel):
    file_extension = CharField(max_length=50, null=True)
    image_size_x = IntegerField(null=True)
    image_size_y = IntegerField(null=True)
    is_require = IntegerField()
    max_characters = IntegerField(null=True)
    option = PrimaryKeyField(db_column='option_id')
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    sku = CharField(max_length=64, null=True)
    sort_order = IntegerField()
    type = CharField(max_length=50, null=True)

    class Meta:
        db_table = 'catalog_product_option'

class CatalogProductOptionPrice(BaseModel):
    option = ForeignKeyField(db_column='option_id', rel_model=CatalogProductOption)
    option_price = PrimaryKeyField(db_column='option_price_id')
    price = DecimalField()
    price_type = CharField(max_length=7)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'catalog_product_option_price'

class CatalogProductOptionTitle(BaseModel):
    option = ForeignKeyField(db_column='option_id', rel_model=CatalogProductOption)
    option_title = PrimaryKeyField(db_column='option_title_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    title = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_product_option_title'

class CatalogProductOptionTypeValue(BaseModel):
    option = ForeignKeyField(db_column='option_id', rel_model=CatalogProductOption)
    option_type = PrimaryKeyField(db_column='option_type_id')
    sku = CharField(max_length=64, null=True)
    sort_order = IntegerField()

    class Meta:
        db_table = 'catalog_product_option_type_value'

class CatalogProductOptionTypePrice(BaseModel):
    option_type = ForeignKeyField(db_column='option_type_id', rel_model=CatalogProductOptionTypeValue)
    option_type_price = PrimaryKeyField(db_column='option_type_price_id')
    price = DecimalField()
    price_type = CharField(max_length=7)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'catalog_product_option_type_price'

class CatalogProductOptionTypeTitle(BaseModel):
    option_type = ForeignKeyField(db_column='option_type_id', rel_model=CatalogProductOptionTypeValue)
    option_type_title = PrimaryKeyField(db_column='option_type_title_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    title = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_product_option_type_title'

class CatalogProductRelation(BaseModel):
    child = ForeignKeyField(db_column='child_id', rel_model=CatalogProductEntity, related_name="categoryproductrelation_child")
    parent = ForeignKeyField(db_column='parent_id', primary_key=True, rel_model=CatalogProductEntity, related_name="categoryproductrelation_parent")

    class Meta:
        db_table = 'catalog_product_relation'

class CatalogProductSuperAttribute(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    position = IntegerField()
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    product_super_attribute = PrimaryKeyField(db_column='product_super_attribute_id')

    class Meta:
        db_table = 'catalog_product_super_attribute'

class CatalogProductSuperAttributeLabel(BaseModel):
    product_super_attribute = ForeignKeyField(db_column='product_super_attribute_id', rel_model=CatalogProductSuperAttribute)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    use_default = IntegerField(null=True)
    value = CharField(max_length=255, null=True)
    value_id = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_super_attribute_label'

class CatalogProductSuperAttributePricing(BaseModel):
    is_percent = IntegerField(null=True)
    pricing_value = DecimalField(null=True)
    product_super_attribute = ForeignKeyField(db_column='product_super_attribute_id', rel_model=CatalogProductSuperAttribute)
    value_id = PrimaryKeyField(db_column='value_id')
    value_index = CharField(max_length=255, null=True)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_super_attribute_pricing'

class CatalogProductSuperLink(BaseModel):
    link = PrimaryKeyField(db_column='link_id')
    parent = ForeignKeyField(db_column='parent_id', rel_model=CatalogProductEntity, related_name="catalogproductsuperlink_parent")
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity, related_name="catalogproductsuperlink_product")

    class Meta:
        db_table = 'catalog_product_super_link'

class CatalogProductWebsite(BaseModel):
    product = ForeignKeyField(db_column='product_id', primary_key=True, rel_model=CatalogProductEntity)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_website'
