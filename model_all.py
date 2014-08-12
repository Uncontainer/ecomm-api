__author__ = 'jburks'
#pwiz.py -e mysql -u root converse > model.py

from peewee import *

database = MySQLDatabase('converse', **{'user': 'root'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class AdminAssert(BaseModel):
    assert_data = TextField(null=True)
    assert_ = PrimaryKeyField(db_column='assert_id')
    assert_type = CharField(max_length=20, null=True)

    class Meta:
        db_table = 'admin_assert'

class AdminRole(BaseModel):
    parent = IntegerField(db_column='parent_id')
    role = PrimaryKeyField(db_column='role_id')
    role_name = CharField(max_length=50, null=True)
    role_type = CharField(max_length=1)
    sort_order = IntegerField()
    tree_level = IntegerField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'admin_role'

class AdminRule(BaseModel):
    assert_ = IntegerField(db_column='assert_id')
    permission = CharField(max_length=10, null=True)
    privileges = CharField(max_length=20, null=True)
    resource = CharField(db_column='resource_id', max_length=255, null=True)
    role = ForeignKeyField(db_column='role_id', rel_model=AdminRole)
    role_type = CharField(max_length=1, null=True)
    rule = PrimaryKeyField(db_column='rule_id')

    class Meta:
        db_table = 'admin_rule'

class AdminUser(BaseModel):
    created = DateTimeField()
    email = CharField(max_length=128, null=True)
    extra = TextField(null=True)
    firstname = CharField(max_length=32, null=True)
    is_active = IntegerField()
    lastname = CharField(max_length=32, null=True)
    logdate = DateTimeField(null=True)
    lognum = IntegerField()
    modified = DateTimeField(null=True)
    password = CharField(max_length=40, null=True)
    reload_acl_flag = IntegerField()
    rp_token = TextField(null=True)
    rp_token_created_at = DateTimeField(null=True)
    user = PrimaryKeyField(db_column='user_id')
    username = CharField(max_length=40, null=True)

    class Meta:
        db_table = 'admin_user'

class AdminnotificationInbox(BaseModel):
    date_added = DateTimeField()
    description = TextField(null=True)
    is_read = IntegerField()
    is_remove = IntegerField()
    notification = PrimaryKeyField(db_column='notification_id')
    severity = IntegerField()
    title = CharField(max_length=255)
    url = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'adminnotification_inbox'

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

class Api2AclAttribute(BaseModel):
    allowed_attributes = TextField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    operation = CharField(max_length=20)
    resource = CharField(db_column='resource_id', max_length=255)
    user_type = CharField(max_length=20)

    class Meta:
        db_table = 'api2_acl_attribute'

class Api2AclRole(BaseModel):
    created_at = DateTimeField()
    entity = PrimaryKeyField(db_column='entity_id')
    role_name = CharField(max_length=255)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'api2_acl_role'

class Api2AclRule(BaseModel):
    entity = PrimaryKeyField(db_column='entity_id')
    privilege = CharField(max_length=20, null=True)
    resource = CharField(db_column='resource_id', max_length=255)
    role = ForeignKeyField(db_column='role_id', rel_model=Api2AclRole)

    class Meta:
        db_table = 'api2_acl_rule'

class Api2AclUser(BaseModel):
    admin = ForeignKeyField(db_column='admin_id', rel_model=AdminUser)
    role = ForeignKeyField(db_column='role_id', rel_model=Api2AclRole)

    class Meta:
        db_table = 'api2_acl_user'

class ApiAssert(BaseModel):
    assert_data = TextField(null=True)
    assert_ = PrimaryKeyField(db_column='assert_id')
    assert_type = CharField(max_length=20, null=True)

    class Meta:
        db_table = 'api_assert'

class ApiRole(BaseModel):
    parent = IntegerField(db_column='parent_id')
    role = PrimaryKeyField(db_column='role_id')
    role_name = CharField(max_length=50, null=True)
    role_type = CharField(max_length=1)
    sort_order = IntegerField()
    tree_level = IntegerField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'api_role'

class ApiRule(BaseModel):
    api_permission = CharField(max_length=10, null=True)
    api_privileges = CharField(max_length=20, null=True)
    assert_ = IntegerField(db_column='assert_id')
    resource = CharField(db_column='resource_id', max_length=255, null=True)
    role = ForeignKeyField(db_column='role_id', rel_model=ApiRole)
    role_type = CharField(max_length=1, null=True)
    rule = PrimaryKeyField(db_column='rule_id')

    class Meta:
        db_table = 'api_rule'

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

class ApiSession(BaseModel):
    logdate = DateTimeField()
    sessid = CharField(max_length=40, null=True)
    user = ForeignKeyField(db_column='user_id', rel_model=ApiUser)

    class Meta:
        db_table = 'api_session'

class CaptchaLog(BaseModel):
    count = IntegerField()
    type = CharField(max_length=32, primary_key=True)
    updated_at = DateTimeField(null=True)
    value = CharField(max_length=32)

    class Meta:
        db_table = 'captcha_log'

class CatalogCategoryAncCategsIndexIdx(BaseModel):
    category = IntegerField(db_column='category_id')
    path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_anc_categs_index_idx'

class CatalogCategoryAncCategsIndexTmp(BaseModel):
    category = IntegerField(db_column='category_id')
    path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_anc_categs_index_tmp'

class CatalogCategoryAncProductsIndexIdx(BaseModel):
    category = IntegerField(db_column='category_id')
    position = IntegerField(null=True)
    product = IntegerField(db_column='product_id')

    class Meta:
        db_table = 'catalog_category_anc_products_index_idx'

class CatalogCategoryAncProductsIndexTmp(BaseModel):
    category = IntegerField(db_column='category_id')
    position = IntegerField(null=True)
    product = IntegerField(db_column='product_id')

    class Meta:
        db_table = 'catalog_category_anc_products_index_tmp'

class CatalogCategoryEntity(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    entity_type = IntegerField(db_column='entity_type_id')
    level = IntegerField()
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    position = IntegerField()
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'catalog_category_entity'

EavAttribute(BaseModel):
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

class CatalogCategoryEntityDatetime(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogCategoryEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = DateTimeField(null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_category_entity_datetime'

class CatalogCategoryEntityDecimal(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogCategoryEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = DecimalField(null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_category_entity_decimal'

class CatalogCategoryEntityInt(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogCategoryEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = IntegerField(null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_category_entity_int'

class CatalogCategoryEntityText(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogCategoryEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = TextField(null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_category_entity_text'

class CatalogCategoryEntityVarchar(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogCategoryEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = CharField(max_length=255, null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_category_entity_varchar'

class CatalogCategoryFlatStore1(BaseModel):
    all_children = TextField(null=True)
    available_sort_by = TextField(null=True)
    children = TextField(null=True)
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    custom_apply_to_products = IntegerField(null=True)
    custom_design = CharField(max_length=255, null=True)
    custom_design_from = DateTimeField(null=True)
    custom_design_to = DateTimeField(null=True)
    custom_layout_update = TextField(null=True)
    custom_use_parent_settings = IntegerField(null=True)
    default_sort_by = CharField(max_length=255, null=True)
    description = TextField(null=True)
    display_mode = CharField(max_length=255, null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogCategoryEntity)
    filter_price_range = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    include_in_menu = IntegerField(null=True)
    is_active = IntegerField(null=True)
    is_anchor = IntegerField(null=True)
    landing_page = IntegerField(null=True)
    level = IntegerField()
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    meta_title = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    page_layout = CharField(max_length=255, null=True)
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    path_in_store = TextField(null=True)
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    thumbnail = CharField(max_length=255, null=True)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_flat_store_1'

class CatalogCategoryFlatStore2(BaseModel):
    all_children = TextField(null=True)
    available_sort_by = TextField(null=True)
    children = TextField(null=True)
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    custom_apply_to_products = IntegerField(null=True)
    custom_design = CharField(max_length=255, null=True)
    custom_design_from = DateTimeField(null=True)
    custom_design_to = DateTimeField(null=True)
    custom_layout_update = TextField(null=True)
    custom_use_parent_settings = IntegerField(null=True)
    default_sort_by = CharField(max_length=255, null=True)
    description = TextField(null=True)
    display_mode = CharField(max_length=255, null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogCategoryEntity)
    filter_price_range = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    include_in_menu = IntegerField(null=True)
    is_active = IntegerField(null=True)
    is_anchor = IntegerField(null=True)
    landing_page = IntegerField(null=True)
    level = IntegerField()
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    meta_title = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    page_layout = CharField(max_length=255, null=True)
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    path_in_store = TextField(null=True)
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    thumbnail = CharField(max_length=255, null=True)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_flat_store_2'

class CatalogCategoryFlatStore3(BaseModel):
    all_children = TextField(null=True)
    available_sort_by = TextField(null=True)
    children = TextField(null=True)
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    custom_apply_to_products = IntegerField(null=True)
    custom_design = CharField(max_length=255, null=True)
    custom_design_from = DateTimeField(null=True)
    custom_design_to = DateTimeField(null=True)
    custom_layout_update = TextField(null=True)
    custom_use_parent_settings = IntegerField(null=True)
    default_sort_by = CharField(max_length=255, null=True)
    description = TextField(null=True)
    display_mode = CharField(max_length=255, null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogCategoryEntity)
    filter_price_range = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    include_in_menu = IntegerField(null=True)
    is_active = IntegerField(null=True)
    is_anchor = IntegerField(null=True)
    landing_page = IntegerField(null=True)
    level = IntegerField()
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    meta_title = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    page_layout = CharField(max_length=255, null=True)
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    path_in_store = TextField(null=True)
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    thumbnail = CharField(max_length=255, null=True)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_flat_store_3'

class CatalogCategoryFlatStore4(BaseModel):
    all_children = TextField(null=True)
    available_sort_by = TextField(null=True)
    children = TextField(null=True)
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    custom_apply_to_products = IntegerField(null=True)
    custom_design = CharField(max_length=255, null=True)
    custom_design_from = DateTimeField(null=True)
    custom_design_to = DateTimeField(null=True)
    custom_layout_update = TextField(null=True)
    custom_use_parent_settings = IntegerField(null=True)
    default_sort_by = CharField(max_length=255, null=True)
    description = TextField(null=True)
    display_mode = CharField(max_length=255, null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogCategoryEntity)
    filter_price_range = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    include_in_menu = IntegerField(null=True)
    is_active = IntegerField(null=True)
    is_anchor = IntegerField(null=True)
    landing_page = IntegerField(null=True)
    level = IntegerField()
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    meta_title = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    page_layout = CharField(max_length=255, null=True)
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    path_in_store = TextField(null=True)
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    thumbnail = CharField(max_length=255, null=True)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_flat_store_4'

class CatalogCategoryFlatStore5(BaseModel):
    all_children = TextField(null=True)
    available_sort_by = TextField(null=True)
    children = TextField(null=True)
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    custom_apply_to_products = IntegerField(null=True)
    custom_design = CharField(max_length=255, null=True)
    custom_design_from = DateTimeField(null=True)
    custom_design_to = DateTimeField(null=True)
    custom_layout_update = TextField(null=True)
    custom_use_parent_settings = IntegerField(null=True)
    default_sort_by = CharField(max_length=255, null=True)
    description = TextField(null=True)
    display_mode = CharField(max_length=255, null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogCategoryEntity)
    filter_price_range = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    include_in_menu = IntegerField(null=True)
    is_active = IntegerField(null=True)
    is_anchor = IntegerField(null=True)
    landing_page = IntegerField(null=True)
    level = IntegerField()
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    meta_title = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    page_layout = CharField(max_length=255, null=True)
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    path_in_store = TextField(null=True)
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    thumbnail = CharField(max_length=255, null=True)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_flat_store_5'

class CatalogCategoryFlatStore6(BaseModel):
    all_children = TextField(null=True)
    available_sort_by = TextField(null=True)
    children = TextField(null=True)
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    custom_apply_to_products = IntegerField(null=True)
    custom_design = CharField(max_length=255, null=True)
    custom_design_from = DateTimeField(null=True)
    custom_design_to = DateTimeField(null=True)
    custom_layout_update = TextField(null=True)
    custom_use_parent_settings = IntegerField(null=True)
    default_sort_by = CharField(max_length=255, null=True)
    description = TextField(null=True)
    display_mode = CharField(max_length=255, null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogCategoryEntity)
    filter_price_range = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    include_in_menu = IntegerField(null=True)
    is_active = IntegerField(null=True)
    is_anchor = IntegerField(null=True)
    landing_page = IntegerField(null=True)
    level = IntegerField()
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    meta_title = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    page_layout = CharField(max_length=255, null=True)
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    path_in_store = TextField(null=True)
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    thumbnail = CharField(max_length=255, null=True)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_flat_store_6'

class CatalogCategoryFlatStore7(BaseModel):
    all_children = TextField(null=True)
    available_sort_by = TextField(null=True)
    children = TextField(null=True)
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    custom_apply_to_products = IntegerField(null=True)
    custom_design = CharField(max_length=255, null=True)
    custom_design_from = DateTimeField(null=True)
    custom_design_to = DateTimeField(null=True)
    custom_layout_update = TextField(null=True)
    custom_use_parent_settings = IntegerField(null=True)
    default_sort_by = CharField(max_length=255, null=True)
    description = TextField(null=True)
    display_mode = CharField(max_length=255, null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogCategoryEntity)
    filter_price_range = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    include_in_menu = IntegerField(null=True)
    is_active = IntegerField(null=True)
    is_anchor = IntegerField(null=True)
    landing_page = IntegerField(null=True)
    level = IntegerField()
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    meta_title = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    page_layout = CharField(max_length=255, null=True)
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    path_in_store = TextField(null=True)
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    thumbnail = CharField(max_length=255, null=True)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_flat_store_7'

class CatalogCategoryFlatStore8(BaseModel):
    all_children = TextField(null=True)
    available_sort_by = TextField(null=True)
    children = TextField(null=True)
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    custom_apply_to_products = IntegerField(null=True)
    custom_design = CharField(max_length=255, null=True)
    custom_design_from = DateTimeField(null=True)
    custom_design_to = DateTimeField(null=True)
    custom_layout_update = TextField(null=True)
    custom_use_parent_settings = IntegerField(null=True)
    default_sort_by = CharField(max_length=255, null=True)
    description = TextField(null=True)
    display_mode = CharField(max_length=255, null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogCategoryEntity)
    filter_price_range = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    include_in_menu = IntegerField(null=True)
    is_active = IntegerField(null=True)
    is_anchor = IntegerField(null=True)
    landing_page = IntegerField(null=True)
    level = IntegerField()
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    meta_title = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    page_layout = CharField(max_length=255, null=True)
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    path_in_store = TextField(null=True)
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    thumbnail = CharField(max_length=255, null=True)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_flat_store_8'

class CatalogCategoryFlatStore9(BaseModel):
    all_children = TextField(null=True)
    available_sort_by = TextField(null=True)
    children = TextField(null=True)
    children_count = IntegerField()
    created_at = DateTimeField(null=True)
    custom_apply_to_products = IntegerField(null=True)
    custom_design = CharField(max_length=255, null=True)
    custom_design_from = DateTimeField(null=True)
    custom_design_to = DateTimeField(null=True)
    custom_layout_update = TextField(null=True)
    custom_use_parent_settings = IntegerField(null=True)
    default_sort_by = CharField(max_length=255, null=True)
    description = TextField(null=True)
    display_mode = CharField(max_length=255, null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=CatalogCategoryEntity)
    filter_price_range = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    include_in_menu = IntegerField(null=True)
    is_active = IntegerField(null=True)
    is_anchor = IntegerField(null=True)
    landing_page = IntegerField(null=True)
    level = IntegerField()
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    meta_title = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    page_layout = CharField(max_length=255, null=True)
    parent = IntegerField(db_column='parent_id')
    path = CharField(max_length=255)
    path_in_store = TextField(null=True)
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    thumbnail = CharField(max_length=255, null=True)
    updated_at = DateTimeField(null=True)
    url_key = CharField(max_length=255, null=True)
    url_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'catalog_category_flat_store_9'

class EavAttributeSet(BaseModel):
    attribute_set = PrimaryKeyField(db_column='attribute_set_id')
    attribute_set_name = CharField(max_length=255, null=True)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    sort_order = IntegerField()

    class Meta:
        db_table = 'eav_attribute_set'

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

class CatalogCategoryProduct(BaseModel):
    category = ForeignKeyField(db_column='category_id', primary_key=True, rel_model=CatalogCategoryEntity)
    position = IntegerField()
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)

    class Meta:
        db_table = 'catalog_category_product'

class CatalogCategoryProductIndex(BaseModel):
    category = ForeignKeyField(db_column='category_id', primary_key=True, rel_model=CatalogCategoryEntity)
    is_parent = IntegerField()
    position = IntegerField(null=True)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    visibility = IntegerField()

    class Meta:
        db_table = 'catalog_category_product_index'

class CatalogCategoryProductIndexEnblIdx(BaseModel):
    product = IntegerField(db_column='product_id')
    visibility = IntegerField()

    class Meta:
        db_table = 'catalog_category_product_index_enbl_idx'

class CatalogCategoryProductIndexEnblTmp(BaseModel):
    product = IntegerField(db_column='product_id')
    visibility = IntegerField()

    class Meta:
        db_table = 'catalog_category_product_index_enbl_tmp'

class CatalogCategoryProductIndexIdx(BaseModel):
    category = IntegerField(db_column='category_id')
    is_parent = IntegerField()
    position = IntegerField()
    product = IntegerField(db_column='product_id')
    store = IntegerField(db_column='store_id')
    visibility = IntegerField()

    class Meta:
        db_table = 'catalog_category_product_index_idx'

class CatalogCategoryProductIndexTmp(BaseModel):
    category = IntegerField(db_column='category_id')
    is_parent = IntegerField()
    position = IntegerField()
    product = IntegerField(db_column='product_id')
    store = IntegerField(db_column='store_id')
    visibility = IntegerField()

    class Meta:
        db_table = 'catalog_category_product_index_tmp'

class CustomerEntity(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    created_at = DateTimeField()
    disable_auto_group_change = IntegerField()
    email = CharField(max_length=255, null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    entity_type = IntegerField(db_column='entity_type_id')
    group = IntegerField(db_column='group_id')
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    is_active = IntegerField()
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    updated_at = DateTimeField()
    website = ForeignKeyField(db_column='website_id', null=True, rel_model=CoreWebsite)

    class Meta:
        db_table = 'customer_entity'

class CatalogCompareItem(BaseModel):
    catalog_compare_item = PrimaryKeyField(db_column='catalog_compare_item_id')
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    visitor = IntegerField(db_column='visitor_id')

    class Meta:
        db_table = 'catalog_compare_item'

class CatalogEavAttribute(BaseModel):
    apply_to = CharField(max_length=255, null=True)
    attribute = ForeignKeyField(db_column='attribute_id', primary_key=True, rel_model=EavAttribute)
    frontend_input_renderer = CharField(max_length=255, null=True)
    is_comparable = IntegerField()
    is_configurable = IntegerField()
    is_filterable = IntegerField()
    is_filterable_in_search = IntegerField()
    is_global = IntegerField()
    is_html_allowed_on_front = IntegerField()
    is_searchable = IntegerField()
    is_used_for_price_rules = IntegerField()
    is_used_for_promo_rules = IntegerField()
    is_visible = IntegerField()
    is_visible_in_advanced_search = IntegerField()
    is_visible_on_front = IntegerField()
    is_wysiwyg_enabled = IntegerField()
    position = IntegerField()
    used_for_sort_by = IntegerField()
    used_in_product_listing = IntegerField()

    class Meta:
        db_table = 'catalog_eav_attribute'

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
    value = PrimaryKeyField(db_column='value_id')

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
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_datetime'

class CatalogProductEntityDecimal(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = DecimalField(null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_decimal'

class CatalogProductEntityGallery(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    position = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = CharField(max_length=255, null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_gallery'

class CatalogProductEntityGroupPrice(BaseModel):
    all_groups = IntegerField()
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    value = DecimalField()
    value = PrimaryKeyField(db_column='value_id')
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_entity_group_price'

class CatalogProductEntityInt(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = IntegerField(null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_int'

class CatalogProductEntityMediaGallery(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    value = CharField(max_length=255, null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_media_gallery'

class CatalogProductEntityMediaGalleryValue(BaseModel):
    disabled = IntegerField()
    label = CharField(max_length=255, null=True)
    position = IntegerField(null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = ForeignKeyField(db_column='value_id', primary_key=True, rel_model=CatalogProductEntityMediaGallery)

    class Meta:
        db_table = 'catalog_product_entity_media_gallery_value'

class CatalogProductEntityText(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = TextField(null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_entity_text'

class CatalogProductEntityTierPrice(BaseModel):
    all_groups = IntegerField()
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    qty = DecimalField()
    value = DecimalField()
    value = PrimaryKeyField(db_column='value_id')
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_entity_tier_price'

class CatalogProductEntityVarchar(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = CharField(max_length=255, null=True)
    value = PrimaryKeyField(db_column='value_id')

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
    linked_product = ForeignKeyField(db_column='linked_product_id', rel_model=CatalogProductEntity)
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
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_link_attribute_decimal'

class CatalogProductLinkAttributeInt(BaseModel):
    link = ForeignKeyField(db_column='link_id', rel_model=CatalogProductLink)
    product_link_attribute = ForeignKeyField(db_column='product_link_attribute_id', null=True, rel_model=CatalogProductLinkAttribute)
    value = IntegerField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_link_attribute_int'

class CatalogProductLinkAttributeVarchar(BaseModel):
    link = ForeignKeyField(db_column='link_id', rel_model=CatalogProductLink)
    product_link_attribute = ForeignKeyField(db_column='product_link_attribute_id', rel_model=CatalogProductLinkAttribute)
    value = CharField(max_length=255, null=True)
    value = PrimaryKeyField(db_column='value_id')

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
    child = ForeignKeyField(db_column='child_id', rel_model=CatalogProductEntity)
    parent = ForeignKeyField(db_column='parent_id', primary_key=True, rel_model=CatalogProductEntity)

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
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'catalog_product_super_attribute_label'

class CatalogProductSuperAttributePricing(BaseModel):
    is_percent = IntegerField(null=True)
    pricing_value = DecimalField(null=True)
    product_super_attribute = ForeignKeyField(db_column='product_super_attribute_id', rel_model=CatalogProductSuperAttribute)
    value = PrimaryKeyField(db_column='value_id')
    value_index = CharField(max_length=255, null=True)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_super_attribute_pricing'

class CatalogProductSuperLink(BaseModel):
    link = PrimaryKeyField(db_column='link_id')
    parent = ForeignKeyField(db_column='parent_id', rel_model=CatalogProductEntity)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)

    class Meta:
        db_table = 'catalog_product_super_link'

class CatalogProductWebsite(BaseModel):
    product = ForeignKeyField(db_column='product_id', primary_key=True, rel_model=CatalogProductEntity)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalog_product_website'

class CataloginventoryStock(BaseModel):
    stock = PrimaryKeyField(db_column='stock_id')
    stock_name = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'cataloginventory_stock'

class CataloginventoryStockItem(BaseModel):
    backorders = IntegerField()
    enable_qty_increments = IntegerField()
    is_decimal_divided = IntegerField()
    is_in_stock = IntegerField()
    is_qty_decimal = IntegerField()
    item = PrimaryKeyField(db_column='item_id')
    low_stock_date = DateTimeField(null=True)
    manage_stock = IntegerField()
    max_sale_qty = DecimalField()
    min_qty = DecimalField()
    min_sale_qty = DecimalField()
    notify_stock_qty = DecimalField(null=True)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    qty = DecimalField()
    qty_increments = DecimalField()
    stock = ForeignKeyField(db_column='stock_id', rel_model=CataloginventoryStock)
    stock_status_changed_auto = IntegerField()
    use_config_backorders = IntegerField()
    use_config_enable_qty_inc = IntegerField()
    use_config_manage_stock = IntegerField()
    use_config_max_sale_qty = IntegerField()
    use_config_min_qty = IntegerField()
    use_config_min_sale_qty = IntegerField()
    use_config_notify_stock_qty = IntegerField()
    use_config_qty_increments = IntegerField()

    class Meta:
        db_table = 'cataloginventory_stock_item'

class CataloginventoryStockStatus(BaseModel):
    product = ForeignKeyField(db_column='product_id', primary_key=True, rel_model=CatalogProductEntity)
    qty = DecimalField()
    stock = ForeignKeyField(db_column='stock_id', rel_model=CataloginventoryStock)
    stock_status = IntegerField()
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'cataloginventory_stock_status'

class CataloginventoryStockStatusIdx(BaseModel):
    product = PrimaryKeyField(db_column='product_id')
    qty = DecimalField()
    stock = IntegerField(db_column='stock_id')
    stock_status = IntegerField()
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'cataloginventory_stock_status_idx'

class CataloginventoryStockStatusTmp(BaseModel):
    product = PrimaryKeyField(db_column='product_id')
    qty = DecimalField()
    stock = IntegerField(db_column='stock_id')
    stock_status = IntegerField()
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'cataloginventory_stock_status_tmp'

class Catalogrule(BaseModel):
    actions_serialized = TextField(null=True)
    conditions_serialized = TextField(null=True)
    description = TextField(null=True)
    discount_amount = DecimalField()
    from_date = DateField(null=True)
    is_active = IntegerField()
    name = CharField(max_length=255, null=True)
    rule = PrimaryKeyField(db_column='rule_id')
    simple_action = CharField(max_length=32, null=True)
    sort_order = IntegerField()
    stop_rules_processing = IntegerField()
    sub_discount_amount = DecimalField()
    sub_is_enable = IntegerField()
    sub_simple_action = CharField(max_length=32, null=True)
    to_date = DateField(null=True)

    class Meta:
        db_table = 'catalogrule'

class CatalogruleAffectedProduct(BaseModel):
    product = PrimaryKeyField(db_column='product_id')

    class Meta:
        db_table = 'catalogrule_affected_product'

class CatalogruleCustomerGroup(BaseModel):
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    rule = ForeignKeyField(db_column='rule_id', primary_key=True, rel_model=Catalogrule)

    class Meta:
        db_table = 'catalogrule_customer_group'

class CatalogruleGroupWebsite(BaseModel):
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    rule = ForeignKeyField(db_column='rule_id', primary_key=True, rel_model=Catalogrule)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalogrule_group_website'

class CatalogruleProduct(BaseModel):
    action_amount = DecimalField()
    action_operator = CharField(max_length=10, null=True)
    action_stop = IntegerField()
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    from_time = IntegerField()
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    rule = ForeignKeyField(db_column='rule_id', rel_model=Catalogrule)
    rule_product = PrimaryKeyField(db_column='rule_product_id')
    sort_order = IntegerField()
    sub_discount_amount = DecimalField()
    sub_simple_action = CharField(max_length=32, null=True)
    to_time = IntegerField()
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalogrule_product'

class CatalogruleProductPrice(BaseModel):
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    earliest_end_date = DateField(null=True)
    latest_start_date = DateField(null=True)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    rule_date = DateField()
    rule_price = DecimalField()
    rule_product_price = PrimaryKeyField(db_column='rule_product_price_id')
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalogrule_product_price'

class CatalogruleWebsite(BaseModel):
    rule = ForeignKeyField(db_column='rule_id', primary_key=True, rel_model=Catalogrule)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'catalogrule_website'

class CatalogsearchFulltext(BaseModel):
    data_index = TextField(null=True)
    fulltext = PrimaryKeyField(db_column='fulltext_id')
    product = IntegerField(db_column='product_id')
    store = IntegerField(db_column='store_id')

    class Meta:
        db_table = 'catalogsearch_fulltext'

class CatalogsearchQuery(BaseModel):
    display_in_terms = IntegerField()
    is_active = IntegerField(null=True)
    is_processed = IntegerField(null=True)
    num_results = IntegerField()
    popularity = IntegerField()
    query = PrimaryKeyField(db_column='query_id')
    query_text = CharField(max_length=255, null=True)
    redirect = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    synonym_for = CharField(max_length=255, null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'catalogsearch_query'

class CatalogsearchResult(BaseModel):
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    query = ForeignKeyField(db_column='query_id', primary_key=True, rel_model=CatalogsearchQuery)
    relevance = DecimalField()

    class Meta:
        db_table = 'catalogsearch_result'

class CheckoutAgreement(BaseModel):
    agreement = PrimaryKeyField(db_column='agreement_id')
    checkbox_text = TextField(null=True)
    content = TextField(null=True)
    content_height = CharField(max_length=25, null=True)
    is_active = IntegerField()
    is_html = IntegerField()
    name = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'checkout_agreement'

class CheckoutAgreementStore(BaseModel):
    agreement = ForeignKeyField(db_column='agreement_id', primary_key=True, rel_model=CheckoutAgreement)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'checkout_agreement_store'

class CmsBlock(BaseModel):
    block = PrimaryKeyField(db_column='block_id')
    content = TextField(null=True)
    creation_time = DateTimeField(null=True)
    identifier = CharField(max_length=255)
    is_active = IntegerField()
    title = CharField(max_length=255)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'cms_block'

class CmsBlockStore(BaseModel):
    block = ForeignKeyField(db_column='block_id', primary_key=True, rel_model=CmsBlock)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'cms_block_store'

class CmsPage(BaseModel):
    content = TextField(null=True)
    content_heading = CharField(max_length=255, null=True)
    creation_time = DateTimeField(null=True)
    custom_layout_update_xml = TextField(null=True)
    custom_root_template = CharField(max_length=255, null=True)
    custom_theme = CharField(max_length=100, null=True)
    custom_theme_from = DateField(null=True)
    custom_theme_to = DateField(null=True)
    identifier = CharField(max_length=100, null=True)
    is_active = IntegerField()
    layout_update_xml = TextField(null=True)
    meta_description = TextField(null=True)
    meta_keywords = TextField(null=True)
    page = PrimaryKeyField(db_column='page_id')
    root_template = CharField(max_length=255, null=True)
    sort_order = IntegerField()
    title = CharField(max_length=255, null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'cms_page'

class CmsPageStore(BaseModel):
    page = ForeignKeyField(db_column='page_id', primary_key=True, rel_model=CmsPage)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'cms_page_store'

class CoreCache(BaseModel):
    create_time = IntegerField(null=True)
    data = TextField(null=True)
    expire_time = IntegerField(null=True)
    id = CharField(max_length=200, primary_key=True)
    update_time = IntegerField(null=True)

    class Meta:
        db_table = 'core_cache'

class CoreCacheOption(BaseModel):
    code = CharField(max_length=32, primary_key=True)
    value = IntegerField(null=True)

    class Meta:
        db_table = 'core_cache_option'

class CoreCacheTag(BaseModel):
    cache = CharField(db_column='cache_id', max_length=200)
    tag = CharField(max_length=100, primary_key=True)

    class Meta:
        db_table = 'core_cache_tag'

class CoreConfigData(BaseModel):
    config = PrimaryKeyField(db_column='config_id')
    path = CharField(max_length=255)
    scope = CharField(max_length=8)
    scope = IntegerField(db_column='scope_id')
    value = TextField(null=True)

    class Meta:
        db_table = 'core_config_data'

class CoreEmailTemplate(BaseModel):
    added_at = DateTimeField(null=True)
    modified_at = DateTimeField(null=True)
    orig_template_code = CharField(max_length=200, null=True)
    orig_template_variables = TextField(null=True)
    template_code = CharField(max_length=150)
    template = PrimaryKeyField(db_column='template_id')
    template_sender_email = CharField(max_length=200, null=True)
    template_sender_name = CharField(max_length=200, null=True)
    template_styles = TextField(null=True)
    template_subject = CharField(max_length=200)
    template_text = TextField()
    template_type = IntegerField(null=True)

    class Meta:
        db_table = 'core_email_template'

class CoreFlag(BaseModel):
    flag_code = CharField(max_length=255)
    flag_data = TextField(null=True)
    flag = PrimaryKeyField(db_column='flag_id')
    last_update = DateTimeField()
    state = IntegerField()

    class Meta:
        db_table = 'core_flag'

class CoreLayoutUpdate(BaseModel):
    handle = CharField(max_length=255, null=True)
    layout_update = PrimaryKeyField(db_column='layout_update_id')
    sort_order = IntegerField()
    xml = TextField(null=True)

    class Meta:
        db_table = 'core_layout_update'

class CoreLayoutLink(BaseModel):
    area = CharField(max_length=64, null=True)
    layout_link = PrimaryKeyField(db_column='layout_link_id')
    layout_update = ForeignKeyField(db_column='layout_update_id', rel_model=CoreLayoutUpdate)
    package = CharField(max_length=64, null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    theme = CharField(max_length=64, null=True)

    class Meta:
        db_table = 'core_layout_link'

class CoreResource(BaseModel):
    code = CharField(max_length=50, primary_key=True)
    data_version = CharField(max_length=50, null=True)
    version = CharField(max_length=50, null=True)

    class Meta:
        db_table = 'core_resource'

class CoreSession(BaseModel):
    session_data = TextField()
    session_expires = IntegerField()
    session = CharField(db_column='session_id', max_length=255, primary_key=True)

    class Meta:
        db_table = 'core_session'

class CoreTranslate(BaseModel):
    key = PrimaryKeyField(db_column='key_id')
    locale = CharField(max_length=20)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    string = CharField(max_length=255)
    translate = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'core_translate'

class CoreUrlRewrite(BaseModel):
    category = ForeignKeyField(db_column='category_id', null=True, rel_model=CatalogCategoryEntity)
    description = CharField(max_length=255, null=True)
    id_path = CharField(max_length=255, null=True)
    is_system = IntegerField(null=True)
    options = CharField(max_length=255, null=True)
    product = ForeignKeyField(db_column='product_id', null=True, rel_model=CatalogProductEntity)
    request_path = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    target_path = CharField(max_length=255, null=True)
    url_rewrite = PrimaryKeyField(db_column='url_rewrite_id')

    class Meta:
        db_table = 'core_url_rewrite'

class CoreVariable(BaseModel):
    code = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    variable = PrimaryKeyField(db_column='variable_id')

    class Meta:
        db_table = 'core_variable'

class CoreVariableValue(BaseModel):
    html_value = TextField(null=True)
    plain_value = TextField(null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = PrimaryKeyField(db_column='value_id')
    variable = ForeignKeyField(db_column='variable_id', rel_model=CoreVariable)

    class Meta:
        db_table = 'core_variable_value'

class CouponAggregated(BaseModel):
    coupon_code = CharField(max_length=50, null=True)
    coupon_uses = IntegerField()
    discount_amount = DecimalField()
    discount_amount_actual = DecimalField()
    order_status = CharField(max_length=50, null=True)
    period = DateField()
    rule_name = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    subtotal_amount = DecimalField()
    subtotal_amount_actual = DecimalField()
    total_amount = DecimalField()
    total_amount_actual = DecimalField()

    class Meta:
        db_table = 'coupon_aggregated'

class CouponAggregatedOrder(BaseModel):
    coupon_code = CharField(max_length=50, null=True)
    coupon_uses = IntegerField()
    discount_amount = DecimalField()
    order_status = CharField(max_length=50, null=True)
    period = DateField()
    rule_name = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    subtotal_amount = DecimalField()
    total_amount = DecimalField()

    class Meta:
        db_table = 'coupon_aggregated_order'

class CouponAggregatedUpdated(BaseModel):
    coupon_code = CharField(max_length=50, null=True)
    coupon_uses = IntegerField()
    discount_amount = DecimalField()
    discount_amount_actual = DecimalField()
    order_status = CharField(max_length=50, null=True)
    period = DateField()
    rule_name = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    subtotal_amount = DecimalField()
    subtotal_amount_actual = DecimalField()
    total_amount = DecimalField()
    total_amount_actual = DecimalField()

    class Meta:
        db_table = 'coupon_aggregated_updated'

class CronSchedule(BaseModel):
    created_at = DateTimeField()
    executed_at = DateTimeField(null=True)
    finished_at = DateTimeField(null=True)
    job_code = CharField(max_length=255)
    messages = TextField(null=True)
    schedule = PrimaryKeyField(db_column='schedule_id')
    scheduled_at = DateTimeField(null=True)
    status = CharField(max_length=7)

    class Meta:
        db_table = 'cron_schedule'

class CustomerAddressEntity(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    created_at = DateTimeField()
    entity = PrimaryKeyField(db_column='entity_id')
    entity_type = IntegerField(db_column='entity_type_id')
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    is_active = IntegerField()
    parent = ForeignKeyField(db_column='parent_id', null=True, rel_model=CustomerEntity)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'customer_address_entity'

class CustomerAddressEntityDatetime(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerAddressEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = DateTimeField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_address_entity_datetime'

class CustomerAddressEntityDecimal(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerAddressEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = DecimalField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_address_entity_decimal'

class CustomerAddressEntityInt(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerAddressEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = IntegerField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_address_entity_int'

class CustomerAddressEntityText(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerAddressEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = TextField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_address_entity_text'

class CustomerAddressEntityVarchar(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerAddressEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = CharField(max_length=255, null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_address_entity_varchar'

class CustomerEavAttribute(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', primary_key=True, rel_model=EavAttribute)
    data_model = CharField(max_length=255, null=True)
    input_filter = CharField(max_length=255, null=True)
    is_system = IntegerField()
    is_visible = IntegerField()
    multiline_count = IntegerField()
    sort_order = IntegerField()
    validate_rules = TextField(null=True)

    class Meta:
        db_table = 'customer_eav_attribute'

class CustomerEavAttributeWebsite(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', primary_key=True, rel_model=EavAttribute)
    default_value = TextField(null=True)
    is_required = IntegerField(null=True)
    is_visible = IntegerField(null=True)
    multiline_count = IntegerField(null=True)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'customer_eav_attribute_website'

class CustomerEntityDatetime(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = DateTimeField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_entity_datetime'

class CustomerEntityDecimal(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = DecimalField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_entity_decimal'

class CustomerEntityInt(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = IntegerField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_entity_int'

class CustomerEntityText(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = TextField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_entity_text'

class CustomerEntityVarchar(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CustomerEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    value = CharField(max_length=255, null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'customer_entity_varchar'

class CustomerFormAttribute(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    form_code = CharField(max_length=32, primary_key=True)

    class Meta:
        db_table = 'customer_form_attribute'

class CustomercreditCode(BaseModel):
    code = CharField(max_length=255)
    code = PrimaryKeyField(db_column='code_id')
    created_date = DateTimeField(null=True)
    credit = DecimalField()
    from_date = DateField(null=True)
    is_active = IntegerField()
    owner = IntegerField(db_column='owner_id', null=True)
    to_date = DateField(null=True)
    updated_date = DateTimeField(null=True)
    used_date = DateField(null=True)
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'customercredit_code'

class CustomercreditCodeLog(BaseModel):
    action_date = DateTimeField(null=True)
    action_type = IntegerField()
    code = IntegerField(db_column='code_id')
    comment = TextField()
    credit = DecimalField()
    log = PrimaryKeyField(db_column='log_id')

    class Meta:
        db_table = 'customercredit_code_log'

class CustomercreditCredit(BaseModel):
    credit = PrimaryKeyField(db_column='credit_id')
    customer = IntegerField(db_column='customer_id')
    value = DecimalField()
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'customercredit_credit'

class CustomercreditCreditLog(BaseModel):
    action_date = DateTimeField(null=True)
    action_type = IntegerField()
    comment = TextField()
    credit = IntegerField(db_column='credit_id')
    log = PrimaryKeyField(db_column='log_id')
    order = IntegerField(db_column='order_id', null=True)
    rule = IntegerField(db_column='rule_id')
    rules_customer = IntegerField(db_column='rules_customer_id', null=True)
    value = DecimalField()
    value_change = DecimalField()

    class Meta:
        db_table = 'customercredit_credit_log'

class CustomercreditRules(BaseModel):
    actions_serialized = TextField(null=True)
    conditions_serialized = TextField(null=True)
    credit = DecimalField()
    customer_group_ids = CharField(max_length=255)
    description = CharField(max_length=255)
    is_active = IntegerField()
    is_onetime = IntegerField()
    name = CharField(max_length=255)
    rule = PrimaryKeyField(db_column='rule_id')
    rule_type = IntegerField()
    website_ids = CharField(max_length=255)

    class Meta:
        db_table = 'customercredit_rules'

class CustomercreditRulesCustomer(BaseModel):
    customer = IntegerField(db_column='customer_id')
    rule = IntegerField(db_column='rule_id')

    class Meta:
        db_table = 'customercredit_rules_customer'

class CustomercreditRulesCustomerAction(BaseModel):
    action_tag = IntegerField()
    customer = IntegerField(db_column='customer_id')
    rule = IntegerField(db_column='rule_id')
    value = IntegerField()

    class Meta:
        db_table = 'customercredit_rules_customer_action'

class CustomercreditRulesCustomerLog(BaseModel):
    action_tag = IntegerField()
    customer = IntegerField(db_column='customer_id')
    rule = IntegerField(db_column='rule_id')
    value = CharField(max_length=255)

    class Meta:
        db_table = 'customercredit_rules_customer_log'

class DataflowProfile(BaseModel):
    actions_xml = TextField(null=True)
    created_at = DateTimeField(null=True)
    data_transfer = CharField(max_length=11, null=True)
    direction = CharField(max_length=6, null=True)
    entity_type = CharField(max_length=64, null=True)
    gui_data = TextField(null=True)
    name = CharField(max_length=255, null=True)
    profile = PrimaryKeyField(db_column='profile_id')
    store = IntegerField(db_column='store_id')
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'dataflow_profile'

class DataflowBatch(BaseModel):
    adapter = CharField(max_length=128, null=True)
    batch = PrimaryKeyField(db_column='batch_id')
    created_at = DateTimeField(null=True)
    params = TextField(null=True)
    profile = ForeignKeyField(db_column='profile_id', rel_model=DataflowProfile)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'dataflow_batch'

class DataflowBatchExport(BaseModel):
    batch_data = TextField(null=True)
    batch_export = BigIntegerField(db_column='batch_export_id', primary_key=True)
    batch = ForeignKeyField(db_column='batch_id', rel_model=DataflowBatch)
    status = IntegerField()

    class Meta:
        db_table = 'dataflow_batch_export'

class DataflowBatchImport(BaseModel):
    batch_data = TextField(null=True)
    batch = ForeignKeyField(db_column='batch_id', rel_model=DataflowBatch)
    batch_import = BigIntegerField(db_column='batch_import_id', primary_key=True)
    status = IntegerField()

    class Meta:
        db_table = 'dataflow_batch_import'

class DataflowSession(BaseModel):
    comment = CharField(max_length=255, null=True)
    created_date = DateTimeField(null=True)
    direction = CharField(max_length=32, null=True)
    file = CharField(max_length=255, null=True)
    session = PrimaryKeyField(db_column='session_id')
    type = CharField(max_length=32, null=True)
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'dataflow_session'

class DataflowImportData(BaseModel):
    import_ = PrimaryKeyField(db_column='import_id')
    serial_number = IntegerField()
    session = ForeignKeyField(db_column='session_id', null=True, rel_model=DataflowSession)
    status = IntegerField()
    value = TextField(null=True)

    class Meta:
        db_table = 'dataflow_import_data'

class DataflowProfileHistory(BaseModel):
    action_code = CharField(max_length=64, null=True)
    history = PrimaryKeyField(db_column='history_id')
    performed_at = DateTimeField(null=True)
    profile = ForeignKeyField(db_column='profile_id', rel_model=DataflowProfile)
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'dataflow_profile_history'

class DesignChange(BaseModel):
    date_from = DateField(null=True)
    date_to = DateField(null=True)
    design = CharField(max_length=255, null=True)
    design_change = PrimaryKeyField(db_column='design_change_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'design_change'

class DirectoryCountry(BaseModel):
    country = CharField(db_column='country_id', max_length=2, primary_key=True)
    iso2_code = CharField(max_length=2, null=True)
    iso3_code = CharField(max_length=3, null=True)

    class Meta:
        db_table = 'directory_country'

class DirectoryCountryFormat(BaseModel):
    country_format = PrimaryKeyField(db_column='country_format_id')
    country = CharField(db_column='country_id', max_length=2, null=True)
    format = TextField()
    type = CharField(max_length=30, null=True)

    class Meta:
        db_table = 'directory_country_format'

class DirectoryCountryRegion(BaseModel):
    code = CharField(max_length=32, null=True)
    country = CharField(db_column='country_id', max_length=4)
    default_name = CharField(max_length=255, null=True)
    region = PrimaryKeyField(db_column='region_id')

    class Meta:
        db_table = 'directory_country_region'

class DirectoryCountryRegionName(BaseModel):
    locale = CharField(max_length=8, primary_key=True)
    name = CharField(max_length=255, null=True)
    region = ForeignKeyField(db_column='region_id', rel_model=DirectoryCountryRegion)

    class Meta:
        db_table = 'directory_country_region_name'

class DirectoryCurrencyRate(BaseModel):
    currency_from = CharField(max_length=3, primary_key=True)
    currency_to = CharField(max_length=3)
    rate = DecimalField()

    class Meta:
        db_table = 'directory_currency_rate'

class DownloadableLink(BaseModel):
    is_shareable = IntegerField()
    link_file = CharField(max_length=255, null=True)
    link = PrimaryKeyField(db_column='link_id')
    link_type = CharField(max_length=20, null=True)
    link_url = CharField(max_length=255, null=True)
    number_of_downloads = IntegerField(null=True)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    sample_file = CharField(max_length=255, null=True)
    sample_type = CharField(max_length=20, null=True)
    sample_url = CharField(max_length=255, null=True)
    sort_order = IntegerField()

    class Meta:
        db_table = 'downloadable_link'

class DownloadableLinkPrice(BaseModel):
    link = ForeignKeyField(db_column='link_id', rel_model=DownloadableLink)
    price = DecimalField()
    price = PrimaryKeyField(db_column='price_id')
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'downloadable_link_price'

class SalesFlatOrder(BaseModel):
    adjustment_negative = DecimalField(null=True)
    adjustment_positive = DecimalField(null=True)
    applied_rule_ids = CharField(max_length=255, null=True)
    base_adjustment_negative = DecimalField(null=True)
    base_adjustment_positive = DecimalField(null=True)
    base_currency_code = CharField(max_length=3, null=True)
    base_customer_credit_amount = DecimalField(null=True)
    base_customer_credit_invoiced = DecimalField(null=True)
    base_customer_credit_refunded = DecimalField(null=True)
    base_discount_amount = DecimalField(null=True)
    base_discount_canceled = DecimalField(null=True)
    base_discount_invoiced = DecimalField(null=True)
    base_discount_refunded = DecimalField(null=True)
    base_grand_total = DecimalField(null=True)
    base_hidden_tax_amount = DecimalField(null=True)
    base_hidden_tax_invoiced = DecimalField(null=True)
    base_hidden_tax_refunded = DecimalField(null=True)
    base_shipping_amount = DecimalField(null=True)
    base_shipping_canceled = DecimalField(null=True)
    base_shipping_discount_amount = DecimalField(null=True)
    base_shipping_hidden_tax_amnt = DecimalField(null=True)
    base_shipping_incl_tax = DecimalField(null=True)
    base_shipping_invoiced = DecimalField(null=True)
    base_shipping_refunded = DecimalField(null=True)
    base_shipping_tax_amount = DecimalField(null=True)
    base_shipping_tax_refunded = DecimalField(null=True)
    base_subtotal = DecimalField(null=True)
    base_subtotal_canceled = DecimalField(null=True)
    base_subtotal_incl_tax = DecimalField(null=True)
    base_subtotal_invoiced = DecimalField(null=True)
    base_subtotal_refunded = DecimalField(null=True)
    base_tax_amount = DecimalField(null=True)
    base_tax_canceled = DecimalField(null=True)
    base_tax_invoiced = DecimalField(null=True)
    base_tax_refunded = DecimalField(null=True)
    base_to_global_rate = DecimalField(null=True)
    base_to_order_rate = DecimalField(null=True)
    base_total_canceled = DecimalField(null=True)
    base_total_due = DecimalField(null=True)
    base_total_invoiced = DecimalField(null=True)
    base_total_invoiced_cost = DecimalField(null=True)
    base_total_offline_refunded = DecimalField(null=True)
    base_total_online_refunded = DecimalField(null=True)
    base_total_paid = DecimalField(null=True)
    base_total_qty_ordered = DecimalField(null=True)
    base_total_refunded = DecimalField(null=True)
    billing_address = IntegerField(db_column='billing_address_id', null=True)
    can_ship_partially = IntegerField(null=True)
    can_ship_partially_item = IntegerField(null=True)
    coupon_code = CharField(max_length=255, null=True)
    coupon_rule_name = CharField(max_length=255, null=True)
    created_at = DateTimeField(null=True)
    customer_credit_amount = DecimalField(null=True)
    customer_credit_invoiced = DecimalField(null=True)
    customer_credit_refunded = DecimalField(null=True)
    customer_dob = DateTimeField(null=True)
    customer_email = CharField(max_length=255, null=True)
    customer_firstname = CharField(max_length=255, null=True)
    customer_gender = IntegerField(null=True)
    customer_group = IntegerField(db_column='customer_group_id', null=True)
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    customer_is_guest = IntegerField(null=True)
    customer_lastname = CharField(max_length=255, null=True)
    customer_middlename = CharField(max_length=255, null=True)
    customer_note = TextField(null=True)
    customer_note_notify = IntegerField(null=True)
    customer_prefix = CharField(max_length=255, null=True)
    customer_suffix = CharField(max_length=255, null=True)
    customer_taxvat = CharField(max_length=255, null=True)
    datass_amount = DecimalField(null=True)
    datass_transaction = CharField(max_length=39, null=True)
    discount_amount = DecimalField(null=True)
    discount_canceled = DecimalField(null=True)
    discount_description = CharField(max_length=255, null=True)
    discount_invoiced = DecimalField(null=True)
    discount_refunded = DecimalField(null=True)
    edit_increment = IntegerField(null=True)
    email_sent = IntegerField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    ext_customer = CharField(db_column='ext_customer_id', max_length=255, null=True)
    ext_order = CharField(db_column='ext_order_id', max_length=255, null=True)
    forced_shipment_with_invoice = IntegerField(null=True)
    gift_message = IntegerField(db_column='gift_message_id', null=True)
    global_currency_code = CharField(max_length=3, null=True)
    grand_total = DecimalField(null=True)
    hidden_tax_amount = DecimalField(null=True)
    hidden_tax_invoiced = DecimalField(null=True)
    hidden_tax_refunded = DecimalField(null=True)
    hold_before_state = CharField(max_length=255, null=True)
    hold_before_status = CharField(max_length=255, null=True)
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    is_virtual = IntegerField(null=True)
    order_currency_code = CharField(max_length=255, null=True)
    original_increment = CharField(db_column='original_increment_id', max_length=50, null=True)
    payment_auth_expiration = IntegerField(null=True)
    payment_authorization_amount = DecimalField(null=True)
    paypal_ipn_customer_notified = IntegerField(null=True)
    protect_code = CharField(max_length=255, null=True)
    quote_address = IntegerField(db_column='quote_address_id', null=True)
    quote = IntegerField(db_column='quote_id', null=True)
    relation_child = CharField(db_column='relation_child_id', max_length=32, null=True)
    relation_child_real = CharField(db_column='relation_child_real_id', max_length=32, null=True)
    relation_parent = CharField(db_column='relation_parent_id', max_length=32, null=True)
    relation_parent_real = CharField(db_column='relation_parent_real_id', max_length=32, null=True)
    remote_ip = CharField(max_length=255, null=True)
    shipping_address = IntegerField(db_column='shipping_address_id', null=True)
    shipping_amount = DecimalField(null=True)
    shipping_canceled = DecimalField(null=True)
    shipping_description = CharField(max_length=255, null=True)
    shipping_discount_amount = DecimalField(null=True)
    shipping_hidden_tax_amount = DecimalField(null=True)
    shipping_incl_tax = DecimalField(null=True)
    shipping_invoiced = DecimalField(null=True)
    shipping_method = CharField(max_length=255, null=True)
    shipping_refunded = DecimalField(null=True)
    shipping_tax_amount = DecimalField(null=True)
    shipping_tax_refunded = DecimalField(null=True)
    state = CharField(max_length=32, null=True)
    status = CharField(max_length=32, null=True)
    store_currency_code = CharField(max_length=3, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    store_name = CharField(max_length=255, null=True)
    store_to_base_rate = DecimalField(null=True)
    store_to_order_rate = DecimalField(null=True)
    subtotal = DecimalField(null=True)
    subtotal_canceled = DecimalField(null=True)
    subtotal_incl_tax = DecimalField(null=True)
    subtotal_invoiced = DecimalField(null=True)
    subtotal_refunded = DecimalField(null=True)
    tax_amount = DecimalField(null=True)
    tax_canceled = DecimalField(null=True)
    tax_invoiced = DecimalField(null=True)
    tax_refunded = DecimalField(null=True)
    total_canceled = DecimalField(null=True)
    total_due = DecimalField(null=True)
    total_invoiced = DecimalField(null=True)
    total_item_count = IntegerField()
    total_offline_refunded = DecimalField(null=True)
    total_online_refunded = DecimalField(null=True)
    total_paid = DecimalField(null=True)
    total_qty_ordered = DecimalField(null=True)
    total_refunded = DecimalField(null=True)
    updated_at = DateTimeField(null=True)
    weight = DecimalField(null=True)
    x_forwarded_for = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'sales_flat_order'

class DownloadableLinkPurchased(BaseModel):
    created_at = DateTimeField()
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    link_section_title = CharField(max_length=255, null=True)
    order = ForeignKeyField(db_column='order_id', null=True, rel_model=SalesFlatOrder)
    order_increment = CharField(db_column='order_increment_id', max_length=50, null=True)
    order_item = IntegerField(db_column='order_item_id')
    product_name = CharField(max_length=255, null=True)
    product_sku = CharField(max_length=255, null=True)
    purchased = PrimaryKeyField(db_column='purchased_id')
    updated_at = DateTimeField()

    class Meta:
        db_table = 'downloadable_link_purchased'

class SalesFlatOrderItem(BaseModel):
    additional_data = TextField(null=True)
    amount_refunded = DecimalField(null=True)
    applied_rule_ids = TextField(null=True)
    base_amount_refunded = DecimalField(null=True)
    base_cost = DecimalField(null=True)
    base_discount_amount = DecimalField(null=True)
    base_discount_invoiced = DecimalField(null=True)
    base_discount_refunded = DecimalField(null=True)
    base_hidden_tax_amount = DecimalField(null=True)
    base_hidden_tax_invoiced = DecimalField(null=True)
    base_hidden_tax_refunded = DecimalField(null=True)
    base_original_price = DecimalField(null=True)
    base_price = DecimalField()
    base_price_incl_tax = DecimalField(null=True)
    base_row_invoiced = DecimalField()
    base_row_total = DecimalField()
    base_row_total_incl_tax = DecimalField(null=True)
    base_tax_amount = DecimalField(null=True)
    base_tax_before_discount = DecimalField(null=True)
    base_tax_invoiced = DecimalField(null=True)
    base_tax_refunded = DecimalField(null=True)
    base_weee_tax_applied_amount = DecimalField(null=True)
    base_weee_tax_applied_row_amnt = DecimalField(null=True)
    base_weee_tax_disposition = DecimalField(null=True)
    base_weee_tax_row_disposition = DecimalField(null=True)
    created_at = DateTimeField()
    description = TextField(null=True)
    discount_amount = DecimalField(null=True)
    discount_invoiced = DecimalField(null=True)
    discount_percent = DecimalField(null=True)
    discount_refunded = DecimalField(null=True)
    ext_order_item = CharField(db_column='ext_order_item_id', max_length=255, null=True)
    free_shipping = IntegerField()
    gift_message_available = IntegerField(null=True)
    gift_message = IntegerField(db_column='gift_message_id', null=True)
    hidden_tax_amount = DecimalField(null=True)
    hidden_tax_canceled = DecimalField(null=True)
    hidden_tax_invoiced = DecimalField(null=True)
    hidden_tax_refunded = DecimalField(null=True)
    is_nominal = IntegerField()
    is_qty_decimal = IntegerField(null=True)
    is_virtual = IntegerField(null=True)
    item = PrimaryKeyField(db_column='item_id')
    locked_do_invoice = IntegerField(null=True)
    locked_do_ship = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    no_discount = IntegerField()
    order = ForeignKeyField(db_column='order_id', rel_model=SalesFlatOrder)
    original_price = DecimalField(null=True)
    parent_item = IntegerField(db_column='parent_item_id', null=True)
    price = DecimalField()
    price_incl_tax = DecimalField(null=True)
    product = IntegerField(db_column='product_id', null=True)
    product_options = TextField(null=True)
    product_type = CharField(max_length=255, null=True)
    qty_backordered = DecimalField(null=True)
    qty_canceled = DecimalField(null=True)
    qty_invoiced = DecimalField(null=True)
    qty_ordered = DecimalField(null=True)
    qty_refunded = DecimalField(null=True)
    qty_shipped = DecimalField(null=True)
    quote_item = IntegerField(db_column='quote_item_id', null=True)
    row_invoiced = DecimalField()
    row_total = DecimalField()
    row_total_incl_tax = DecimalField(null=True)
    row_weight = DecimalField(null=True)
    sku = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    tax_amount = DecimalField(null=True)
    tax_before_discount = DecimalField(null=True)
    tax_canceled = DecimalField(null=True)
    tax_invoiced = DecimalField(null=True)
    tax_percent = DecimalField(null=True)
    tax_refunded = DecimalField(null=True)
    updated_at = DateTimeField()
    weee_tax_applied = TextField(null=True)
    weee_tax_applied_amount = DecimalField(null=True)
    weee_tax_applied_row_amount = DecimalField(null=True)
    weee_tax_disposition = DecimalField(null=True)
    weee_tax_row_disposition = DecimalField(null=True)
    weight = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_order_item'

class DownloadableLinkPurchasedItem(BaseModel):
    created_at = DateTimeField()
    is_shareable = IntegerField()
    item = PrimaryKeyField(db_column='item_id')
    link_file = CharField(max_length=255, null=True)
    link_hash = CharField(max_length=255, null=True)
    link = IntegerField(db_column='link_id')
    link_title = CharField(max_length=255, null=True)
    link_type = CharField(max_length=255, null=True)
    link_url = CharField(max_length=255, null=True)
    number_of_downloads_bought = IntegerField()
    number_of_downloads_used = IntegerField()
    order_item = ForeignKeyField(db_column='order_item_id', null=True, rel_model=SalesFlatOrderItem)
    product = IntegerField(db_column='product_id', null=True)
    purchased = ForeignKeyField(db_column='purchased_id', rel_model=DownloadableLinkPurchased)
    status = CharField(max_length=50, null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'downloadable_link_purchased_item'

class DownloadableLinkTitle(BaseModel):
    link = ForeignKeyField(db_column='link_id', rel_model=DownloadableLink)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    title = CharField(max_length=255, null=True)
    title = PrimaryKeyField(db_column='title_id')

    class Meta:
        db_table = 'downloadable_link_title'

class DownloadableSample(BaseModel):
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    sample_file = CharField(max_length=255, null=True)
    sample = PrimaryKeyField(db_column='sample_id')
    sample_type = CharField(max_length=20, null=True)
    sample_url = CharField(max_length=255, null=True)
    sort_order = IntegerField()

    class Meta:
        db_table = 'downloadable_sample'

class DownloadableSampleTitle(BaseModel):
    sample = ForeignKeyField(db_column='sample_id', rel_model=DownloadableSample)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    title = CharField(max_length=255, null=True)
    title = PrimaryKeyField(db_column='title_id')

    class Meta:
        db_table = 'downloadable_sample_title'

class EavAttributeGroup(BaseModel):
    attribute_group = PrimaryKeyField(db_column='attribute_group_id')
    attribute_group_name = CharField(max_length=255, null=True)
    attribute_set = ForeignKeyField(db_column='attribute_set_id', rel_model=EavAttributeSet)
    default = IntegerField(db_column='default_id', null=True)
    sort_order = IntegerField()

    class Meta:
        db_table = 'eav_attribute_group'

class EavAttributeLabel(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    attribute_label = PrimaryKeyField(db_column='attribute_label_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'eav_attribute_label'

class EavAttributeOption(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    option = PrimaryKeyField(db_column='option_id')
    sort_order = IntegerField()

    class Meta:
        db_table = 'eav_attribute_option'

class EavAttributeOptionValue(BaseModel):
    option = ForeignKeyField(db_column='option_id', rel_model=EavAttributeOption)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = CharField(max_length=255, null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'eav_attribute_option_value'

class EavEntity(BaseModel):
    attribute_set = IntegerField(db_column='attribute_set_id')
    created_at = DateTimeField()
    entity = PrimaryKeyField(db_column='entity_id')
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    is_active = IntegerField()
    parent = IntegerField(db_column='parent_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'eav_entity'

class EavEntityAttribute(BaseModel):
    attribute_group = ForeignKeyField(db_column='attribute_group_id', rel_model=EavAttributeGroup)
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    attribute_set = IntegerField(db_column='attribute_set_id')
    entity_attribute = PrimaryKeyField(db_column='entity_attribute_id')
    entity_type = IntegerField(db_column='entity_type_id')
    sort_order = IntegerField()

    class Meta:
        db_table = 'eav_entity_attribute'

class EavEntityDatetime(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    entity = ForeignKeyField(db_column='entity_id', rel_model=EavEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = DateTimeField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'eav_entity_datetime'

class EavEntityDecimal(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    entity = ForeignKeyField(db_column='entity_id', rel_model=EavEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = DecimalField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'eav_entity_decimal'

class EavEntityInt(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    entity = ForeignKeyField(db_column='entity_id', rel_model=EavEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = IntegerField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'eav_entity_int'

class EavEntityStore(BaseModel):
    entity_store = PrimaryKeyField(db_column='entity_store_id')
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    increment_last = CharField(db_column='increment_last_id', max_length=50, null=True)
    increment_prefix = CharField(max_length=20, null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'eav_entity_store'

class EavEntityText(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    entity = ForeignKeyField(db_column='entity_id', rel_model=EavEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = TextField()
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'eav_entity_text'

class EavEntityVarchar(BaseModel):
    attribute = IntegerField(db_column='attribute_id')
    entity = ForeignKeyField(db_column='entity_id', rel_model=EavEntity)
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = CharField(max_length=255, null=True)
    value = PrimaryKeyField(db_column='value_id')

    class Meta:
        db_table = 'eav_entity_varchar'

class EavFormType(BaseModel):
    code = CharField(max_length=64)
    is_system = IntegerField()
    label = CharField(max_length=255)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    theme = CharField(max_length=64, null=True)
    type = PrimaryKeyField(db_column='type_id')

    class Meta:
        db_table = 'eav_form_type'

class EavFormFieldset(BaseModel):
    code = CharField(max_length=64)
    fieldset = PrimaryKeyField(db_column='fieldset_id')
    sort_order = IntegerField()
    type = ForeignKeyField(db_column='type_id', rel_model=EavFormType)

    class Meta:
        db_table = 'eav_form_fieldset'

class EavFormElement(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    element = PrimaryKeyField(db_column='element_id')
    fieldset = ForeignKeyField(db_column='fieldset_id', null=True, rel_model=EavFormFieldset)
    sort_order = IntegerField()
    type = ForeignKeyField(db_column='type_id', rel_model=EavFormType)

    class Meta:
        db_table = 'eav_form_element'

class EavFormFieldsetLabel(BaseModel):
    fieldset = ForeignKeyField(db_column='fieldset_id', primary_key=True, rel_model=EavFormFieldset)
    label = CharField(max_length=255)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'eav_form_fieldset_label'

class EavFormTypeEntity(BaseModel):
    entity_type = ForeignKeyField(db_column='entity_type_id', rel_model=EavEntityType)
    type = ForeignKeyField(db_column='type_id', primary_key=True, rel_model=EavFormType)

    class Meta:
        db_table = 'eav_form_type_entity'

class GiftMessage(BaseModel):
    customer = IntegerField(db_column='customer_id')
    gift_message = PrimaryKeyField(db_column='gift_message_id')
    message = TextField(null=True)
    recipient = CharField(max_length=255, null=True)
    sender = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'gift_message'

class GooglecheckoutNotification(BaseModel):
    serial_number = CharField(max_length=64, primary_key=True)
    started_at = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'googlecheckout_notification'

class ImportexportImportdata(BaseModel):
    behavior = CharField(max_length=10)
    data = TextField(null=True)
    entity = CharField(max_length=50)

    class Meta:
        db_table = 'importexport_importdata'

class IndexEvent(BaseModel):
    created_at = DateTimeField()
    entity = CharField(max_length=64)
    entity_pk = BigIntegerField(null=True)
    event = BigIntegerField(db_column='event_id', primary_key=True)
    new_data = TextField(null=True)
    old_data = TextField(null=True)
    type = CharField(max_length=64)

    class Meta:
        db_table = 'index_event'

class IndexProcess(BaseModel):
    ended_at = DateTimeField(null=True)
    indexer_code = CharField(max_length=32)
    mode = CharField(max_length=9)
    process = PrimaryKeyField(db_column='process_id')
    started_at = DateTimeField(null=True)
    status = CharField(max_length=15)

    class Meta:
        db_table = 'index_process'

class IndexProcessEvent(BaseModel):
    event = ForeignKeyField(db_column='event_id', rel_model=IndexEvent)
    process = ForeignKeyField(db_column='process_id', primary_key=True, rel_model=IndexProcess)
    status = CharField(max_length=7)

    class Meta:
        db_table = 'index_process_event'

class LogCustomer(BaseModel):
    customer = IntegerField(db_column='customer_id')
    log = PrimaryKeyField(db_column='log_id')
    login_at = DateTimeField()
    logout_at = DateTimeField(null=True)
    store = IntegerField(db_column='store_id')
    visitor = BigIntegerField(db_column='visitor_id', null=True)

    class Meta:
        db_table = 'log_customer'

class LogQuote(BaseModel):
    created_at = DateTimeField()
    deleted_at = DateTimeField(null=True)
    quote = PrimaryKeyField(db_column='quote_id')
    visitor = BigIntegerField(db_column='visitor_id', null=True)

    class Meta:
        db_table = 'log_quote'

class LogSummary(BaseModel):
    add_date = DateTimeField()
    customer_count = IntegerField()
    store = IntegerField(db_column='store_id')
    summary = BigIntegerField(db_column='summary_id', primary_key=True)
    type = IntegerField(db_column='type_id', null=True)
    visitor_count = IntegerField()

    class Meta:
        db_table = 'log_summary'

class LogSummaryType(BaseModel):
    period = IntegerField()
    period_type = CharField(max_length=6)
    type_code = CharField(max_length=64, null=True)
    type = PrimaryKeyField(db_column='type_id')

    class Meta:
        db_table = 'log_summary_type'

class LogUrl(BaseModel):
    url = BigIntegerField(db_column='url_id', primary_key=True)
    visit_time = DateTimeField()
    visitor = BigIntegerField(db_column='visitor_id', null=True)

    class Meta:
        db_table = 'log_url'

class LogUrlInfo(BaseModel):
    referer = CharField(max_length=255, null=True)
    url = CharField(max_length=255, null=True)
    url = BigIntegerField(db_column='url_id', primary_key=True)

    class Meta:
        db_table = 'log_url_info'

class LogVisitor(BaseModel):
    first_visit_at = DateTimeField(null=True)
    last_url = BigIntegerField(db_column='last_url_id')
    last_visit_at = DateTimeField()
    session = CharField(db_column='session_id', max_length=64, null=True)
    store = IntegerField(db_column='store_id')
    visitor = BigIntegerField(db_column='visitor_id', primary_key=True)

    class Meta:
        db_table = 'log_visitor'

class LogVisitorInfo(BaseModel):
    http_accept_charset = CharField(max_length=255, null=True)
    http_accept_language = CharField(max_length=255, null=True)
    http_referer = CharField(max_length=255, null=True)
    http_user_agent = CharField(max_length=255, null=True)
    remote_addr = BigIntegerField(null=True)
    server_addr = BigIntegerField(null=True)
    visitor = BigIntegerField(db_column='visitor_id', primary_key=True)

    class Meta:
        db_table = 'log_visitor_info'

class LogVisitorOnline(BaseModel):
    customer = IntegerField(db_column='customer_id', null=True)
    first_visit_at = DateTimeField(null=True)
    last_url = CharField(max_length=255, null=True)
    last_visit_at = DateTimeField(null=True)
    remote_addr = BigIntegerField()
    visitor = BigIntegerField(db_column='visitor_id', primary_key=True)
    visitor_type = CharField(max_length=1)

    class Meta:
        db_table = 'log_visitor_online'

class NewsletterTemplate(BaseModel):
    added_at = DateTimeField(null=True)
    modified_at = DateTimeField(null=True)
    template_actual = IntegerField(null=True)
    template_code = CharField(max_length=150, null=True)
    template = PrimaryKeyField(db_column='template_id')
    template_sender_email = CharField(max_length=200, null=True)
    template_sender_name = CharField(max_length=200, null=True)
    template_styles = TextField(null=True)
    template_subject = CharField(max_length=200, null=True)
    template_text = TextField(null=True)
    template_text_preprocessed = TextField(null=True)
    template_type = IntegerField(null=True)

    class Meta:
        db_table = 'newsletter_template'

class NewsletterQueue(BaseModel):
    newsletter_sender_email = CharField(max_length=200, null=True)
    newsletter_sender_name = CharField(max_length=200, null=True)
    newsletter_styles = TextField(null=True)
    newsletter_subject = CharField(max_length=200, null=True)
    newsletter_text = TextField(null=True)
    newsletter_type = IntegerField(null=True)
    queue_finish_at = DateTimeField(null=True)
    queue = PrimaryKeyField(db_column='queue_id')
    queue_start_at = DateTimeField(null=True)
    queue_status = IntegerField()
    template = ForeignKeyField(db_column='template_id', rel_model=NewsletterTemplate)

    class Meta:
        db_table = 'newsletter_queue'

class NewsletterSubscriber(BaseModel):
    change_status_at = DateTimeField(null=True)
    customer = IntegerField(db_column='customer_id')
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    subscriber_confirm_code = CharField(max_length=32, null=True)
    subscriber_email = CharField(max_length=150, null=True)
    subscriber = PrimaryKeyField(db_column='subscriber_id')
    subscriber_status = IntegerField()

    class Meta:
        db_table = 'newsletter_subscriber'

class NewsletterProblem(BaseModel):
    problem_error_code = IntegerField(null=True)
    problem_error_text = CharField(max_length=200, null=True)
    problem = PrimaryKeyField(db_column='problem_id')
    queue = ForeignKeyField(db_column='queue_id', rel_model=NewsletterQueue)
    subscriber = ForeignKeyField(db_column='subscriber_id', null=True, rel_model=NewsletterSubscriber)

    class Meta:
        db_table = 'newsletter_problem'

class NewsletterQueueLink(BaseModel):
    letter_sent_at = DateTimeField(null=True)
    queue = ForeignKeyField(db_column='queue_id', rel_model=NewsletterQueue)
    queue_link = PrimaryKeyField(db_column='queue_link_id')
    subscriber = ForeignKeyField(db_column='subscriber_id', rel_model=NewsletterSubscriber)

    class Meta:
        db_table = 'newsletter_queue_link'

class NewsletterQueueStoreLink(BaseModel):
    queue = ForeignKeyField(db_column='queue_id', primary_key=True, rel_model=NewsletterQueue)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'newsletter_queue_store_link'

class OauthConsumer(BaseModel):
    callback_url = CharField(max_length=255, null=True)
    created_at = DateTimeField()
    entity = PrimaryKeyField(db_column='entity_id')
    key = CharField(max_length=32)
    name = CharField(max_length=255)
    rejected_callback_url = CharField(max_length=255)
    secret = CharField(max_length=32)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'oauth_consumer'

class OauthNonce(BaseModel):
    nonce = CharField(max_length=32)
    timestamp = IntegerField()

    class Meta:
        db_table = 'oauth_nonce'

class OauthToken(BaseModel):
    admin = ForeignKeyField(db_column='admin_id', null=True, rel_model=AdminUser)
    authorized = IntegerField()
    callback_url = CharField(max_length=255)
    consumer = ForeignKeyField(db_column='consumer_id', rel_model=OauthConsumer)
    created_at = DateTimeField()
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    entity = PrimaryKeyField(db_column='entity_id')
    revoked = IntegerField()
    secret = CharField(max_length=32)
    token = CharField(max_length=32)
    type = CharField(max_length=16)
    verifier = CharField(max_length=32, null=True)

    class Meta:
        db_table = 'oauth_token'

class PaypalCert(BaseModel):
    cert = PrimaryKeyField(db_column='cert_id')
    content = TextField(null=True)
    updated_at = DateTimeField(null=True)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'paypal_cert'

class PaypalPaymentTransaction(BaseModel):
    additional_information = TextField(null=True)
    created_at = DateTimeField(null=True)
    transaction = PrimaryKeyField(db_column='transaction_id')
    txn = CharField(db_column='txn_id', max_length=100, null=True)

    class Meta:
        db_table = 'paypal_payment_transaction'

class PaypalSettlementReport(BaseModel):
    account = CharField(db_column='account_id', max_length=64, null=True)
    filename = CharField(max_length=24, null=True)
    last_modified = DateTimeField(null=True)
    report_date = DateTimeField(null=True)
    report = PrimaryKeyField(db_column='report_id')

    class Meta:
        db_table = 'paypal_settlement_report'

class PaypalSettlementReportRow(BaseModel):
    consumer = CharField(db_column='consumer_id', max_length=127, null=True)
    custom_field = CharField(max_length=255, null=True)
    fee_amount = DecimalField()
    fee_currency = CharField(max_length=3, null=True)
    fee_debit_or_credit = CharField(max_length=2, null=True)
    gross_transaction_amount = DecimalField()
    gross_transaction_currency = CharField(max_length=3, null=True)
    invoice = CharField(db_column='invoice_id', max_length=127, null=True)
    payment_tracking = CharField(db_column='payment_tracking_id', max_length=255, null=True)
    paypal_reference = CharField(db_column='paypal_reference_id', max_length=19, null=True)
    paypal_reference_id_type = CharField(max_length=3, null=True)
    report = ForeignKeyField(db_column='report_id', rel_model=PaypalSettlementReport)
    row = PrimaryKeyField(db_column='row_id')
    transaction_completion_date = DateTimeField(null=True)
    transaction_debit_or_credit = CharField(max_length=2)
    transaction_event_code = CharField(max_length=5, null=True)
    transaction = CharField(db_column='transaction_id', max_length=19, null=True)
    transaction_initiation_date = DateTimeField(null=True)

    class Meta:
        db_table = 'paypal_settlement_report_row'

class PersistentSession(BaseModel):
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    info = TextField(null=True)
    key = CharField(max_length=50)
    persistent = PrimaryKeyField(db_column='persistent_id')
    updated_at = DateTimeField(null=True)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'persistent_session'

class Poll(BaseModel):
    active = IntegerField()
    answers_display = IntegerField(null=True)
    closed = IntegerField()
    date_closed = DateTimeField(null=True)
    date_posted = DateTimeField()
    poll = PrimaryKeyField(db_column='poll_id')
    poll_title = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    votes_count = IntegerField()

    class Meta:
        db_table = 'poll'

class PollAnswer(BaseModel):
    answer = PrimaryKeyField(db_column='answer_id')
    answer_order = IntegerField()
    answer_title = CharField(max_length=255, null=True)
    poll = ForeignKeyField(db_column='poll_id', rel_model=Poll)
    votes_count = IntegerField()

    class Meta:
        db_table = 'poll_answer'

class PollStore(BaseModel):
    poll = ForeignKeyField(db_column='poll_id', primary_key=True, rel_model=Poll)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'poll_store'

class PollVote(BaseModel):
    customer = IntegerField(db_column='customer_id', null=True)
    ip_address = BigIntegerField(null=True)
    poll_answer = ForeignKeyField(db_column='poll_answer_id', rel_model=PollAnswer)
    poll = IntegerField(db_column='poll_id')
    vote = PrimaryKeyField(db_column='vote_id')
    vote_time = DateTimeField(null=True)

    class Meta:
        db_table = 'poll_vote'

class ProductAlertPrice(BaseModel):
    add_date = DateTimeField()
    alert_price = PrimaryKeyField(db_column='alert_price_id')
    customer = ForeignKeyField(db_column='customer_id', rel_model=CustomerEntity)
    last_send_date = DateTimeField(null=True)
    price = DecimalField()
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    send_count = IntegerField()
    status = IntegerField()
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'product_alert_price'

class ProductAlertStock(BaseModel):
    add_date = DateTimeField()
    alert_stock = PrimaryKeyField(db_column='alert_stock_id')
    customer = ForeignKeyField(db_column='customer_id', rel_model=CustomerEntity)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    send_count = IntegerField()
    send_date = DateTimeField(null=True)
    status = IntegerField()
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'product_alert_stock'

class RatingEntity(BaseModel):
    entity_code = CharField(max_length=64)
    entity = PrimaryKeyField(db_column='entity_id')

    class Meta:
        db_table = 'rating_entity'

class Rating(BaseModel):
    entity = ForeignKeyField(db_column='entity_id', rel_model=RatingEntity)
    position = IntegerField()
    rating_code = CharField(max_length=64)
    rating = PrimaryKeyField(db_column='rating_id')

    class Meta:
        db_table = 'rating'

class RatingOption(BaseModel):
    code = CharField(max_length=32)
    option = PrimaryKeyField(db_column='option_id')
    position = IntegerField()
    rating = ForeignKeyField(db_column='rating_id', rel_model=Rating)
    value = IntegerField()

    class Meta:
        db_table = 'rating_option'

class ReviewEntity(BaseModel):
    entity_code = CharField(max_length=32)
    entity = PrimaryKeyField(db_column='entity_id')

    class Meta:
        db_table = 'review_entity'

class ReviewStatus(BaseModel):
    status_code = CharField(max_length=32)
    status = PrimaryKeyField(db_column='status_id')

    class Meta:
        db_table = 'review_status'

class Review(BaseModel):
    created_at = DateTimeField()
    entity = ForeignKeyField(db_column='entity_id', rel_model=ReviewEntity)
    entity_pk_value = IntegerField()
    review = BigIntegerField(db_column='review_id', primary_key=True)
    status = ForeignKeyField(db_column='status_id', rel_model=ReviewStatus)

    class Meta:
        db_table = 'review'

class RatingOptionVote(BaseModel):
    customer = IntegerField(db_column='customer_id', null=True)
    entity_pk_value = BigIntegerField()
    option = ForeignKeyField(db_column='option_id', rel_model=RatingOption)
    percent = IntegerField()
    rating = IntegerField(db_column='rating_id')
    remote_ip = CharField(max_length=16)
    remote_ip_long = BigIntegerField()
    review = ForeignKeyField(db_column='review_id', null=True, rel_model=Review)
    value = IntegerField()
    vote = BigIntegerField(db_column='vote_id', primary_key=True)

    class Meta:
        db_table = 'rating_option_vote'

class RatingOptionVoteAggregated(BaseModel):
    entity_pk_value = BigIntegerField()
    percent = IntegerField()
    percent_approved = IntegerField(null=True)
    primary = PrimaryKeyField(db_column='primary_id')
    rating = ForeignKeyField(db_column='rating_id', rel_model=Rating)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    vote_count = IntegerField()
    vote_value_sum = IntegerField()

    class Meta:
        db_table = 'rating_option_vote_aggregated'

class RatingStore(BaseModel):
    rating = ForeignKeyField(db_column='rating_id', primary_key=True, rel_model=Rating)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'rating_store'

class RatingTitle(BaseModel):
    rating = ForeignKeyField(db_column='rating_id', primary_key=True, rel_model=Rating)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    value = CharField(max_length=255)

    class Meta:
        db_table = 'rating_title'

class ReportComparedProductIndex(BaseModel):
    added_at = DateTimeField()
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    index = BigIntegerField(db_column='index_id', primary_key=True)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    visitor = IntegerField(db_column='visitor_id', null=True)

    class Meta:
        db_table = 'report_compared_product_index'

class ReportEventTypes(BaseModel):
    customer_login = IntegerField()
    event_name = CharField(max_length=64)
    event_type = PrimaryKeyField(db_column='event_type_id')

    class Meta:
        db_table = 'report_event_types'

class ReportEvent(BaseModel):
    event = BigIntegerField(db_column='event_id', primary_key=True)
    event_type = ForeignKeyField(db_column='event_type_id', rel_model=ReportEventTypes)
    logged_at = DateTimeField()
    object = IntegerField(db_column='object_id')
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    subject = IntegerField(db_column='subject_id')
    subtype = IntegerField()

    class Meta:
        db_table = 'report_event'

class ReportViewedProductAggregatedDaily(BaseModel):
    period = DateField(null=True)
    product = ForeignKeyField(db_column='product_id', null=True, rel_model=CatalogProductEntity)
    product_name = CharField(max_length=255, null=True)
    product_price = DecimalField()
    rating_pos = IntegerField()
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    views_num = IntegerField()

    class Meta:
        db_table = 'report_viewed_product_aggregated_daily'

class ReportViewedProductAggregatedMonthly(BaseModel):
    period = DateField(null=True)
    product = ForeignKeyField(db_column='product_id', null=True, rel_model=CatalogProductEntity)
    product_name = CharField(max_length=255, null=True)
    product_price = DecimalField()
    rating_pos = IntegerField()
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    views_num = IntegerField()

    class Meta:
        db_table = 'report_viewed_product_aggregated_monthly'

class ReportViewedProductAggregatedYearly(BaseModel):
    period = DateField(null=True)
    product = ForeignKeyField(db_column='product_id', null=True, rel_model=CatalogProductEntity)
    product_name = CharField(max_length=255, null=True)
    product_price = DecimalField()
    rating_pos = IntegerField()
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    views_num = IntegerField()

    class Meta:
        db_table = 'report_viewed_product_aggregated_yearly'

class ReportViewedProductIndex(BaseModel):
    added_at = DateTimeField()
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    index = BigIntegerField(db_column='index_id', primary_key=True)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    visitor = IntegerField(db_column='visitor_id', null=True)

    class Meta:
        db_table = 'report_viewed_product_index'

class ReviewDetail(BaseModel):
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    detail = TextField()
    detail = BigIntegerField(db_column='detail_id', primary_key=True)
    nickname = CharField(max_length=128)
    review = ForeignKeyField(db_column='review_id', rel_model=Review)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    title = CharField(max_length=255)

    class Meta:
        db_table = 'review_detail'

class ReviewEntitySummary(BaseModel):
    entity_pk_value = BigIntegerField()
    entity_type = IntegerField()
    primary = BigIntegerField(db_column='primary_id', primary_key=True)
    rating_summary = IntegerField()
    reviews_count = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'review_entity_summary'

class ReviewStore(BaseModel):
    review = ForeignKeyField(db_column='review_id', primary_key=True, rel_model=Review)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'review_store'

class SalesBestsellersAggregatedDaily(BaseModel):
    period = DateField(null=True)
    product = ForeignKeyField(db_column='product_id', null=True, rel_model=CatalogProductEntity)
    product_name = CharField(max_length=255, null=True)
    product_price = DecimalField()
    qty_ordered = DecimalField()
    rating_pos = IntegerField()
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)

    class Meta:
        db_table = 'sales_bestsellers_aggregated_daily'

class SalesBestsellersAggregatedMonthly(BaseModel):
    period = DateField(null=True)
    product = ForeignKeyField(db_column='product_id', null=True, rel_model=CatalogProductEntity)
    product_name = CharField(max_length=255, null=True)
    product_price = DecimalField()
    qty_ordered = DecimalField()
    rating_pos = IntegerField()
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)

    class Meta:
        db_table = 'sales_bestsellers_aggregated_monthly'

class SalesBestsellersAggregatedYearly(BaseModel):
    period = DateField(null=True)
    product = ForeignKeyField(db_column='product_id', null=True, rel_model=CatalogProductEntity)
    product_name = CharField(max_length=255, null=True)
    product_price = DecimalField()
    qty_ordered = DecimalField()
    rating_pos = IntegerField()
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)

    class Meta:
        db_table = 'sales_bestsellers_aggregated_yearly'

class SalesBillingAgreement(BaseModel):
    agreement = PrimaryKeyField(db_column='agreement_id')
    agreement_label = CharField(max_length=255, null=True)
    created_at = DateTimeField()
    customer = ForeignKeyField(db_column='customer_id', rel_model=CustomerEntity)
    method_code = CharField(max_length=32)
    reference = CharField(db_column='reference_id', max_length=32)
    status = CharField(max_length=20)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'sales_billing_agreement'

class SalesBillingAgreementOrder(BaseModel):
    agreement = ForeignKeyField(db_column='agreement_id', primary_key=True, rel_model=SalesBillingAgreement)
    order = ForeignKeyField(db_column='order_id', rel_model=SalesFlatOrder)

    class Meta:
        db_table = 'sales_billing_agreement_order'

class SalesFlatCreditmemo(BaseModel):
    adjustment = DecimalField(null=True)
    adjustment_negative = DecimalField(null=True)
    adjustment_positive = DecimalField(null=True)
    base_adjustment = DecimalField(null=True)
    base_adjustment_negative = DecimalField(null=True)
    base_adjustment_positive = DecimalField(null=True)
    base_currency_code = CharField(max_length=3, null=True)
    base_customer_credit_amount = DecimalField(null=True)
    base_discount_amount = DecimalField(null=True)
    base_grand_total = DecimalField(null=True)
    base_hidden_tax_amount = DecimalField(null=True)
    base_shipping_amount = DecimalField(null=True)
    base_shipping_hidden_tax_amnt = DecimalField(null=True)
    base_shipping_incl_tax = DecimalField(null=True)
    base_shipping_tax_amount = DecimalField(null=True)
    base_subtotal = DecimalField(null=True)
    base_subtotal_incl_tax = DecimalField(null=True)
    base_tax_amount = DecimalField(null=True)
    base_to_global_rate = DecimalField(null=True)
    base_to_order_rate = DecimalField(null=True)
    billing_address = IntegerField(db_column='billing_address_id', null=True)
    created_at = DateTimeField(null=True)
    creditmemo_status = IntegerField(null=True)
    customer_credit_amount = DecimalField(null=True)
    discount_amount = DecimalField(null=True)
    email_sent = IntegerField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    global_currency_code = CharField(max_length=3, null=True)
    grand_total = DecimalField(null=True)
    hidden_tax_amount = DecimalField(null=True)
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    invoice = IntegerField(db_column='invoice_id', null=True)
    order_currency_code = CharField(max_length=3, null=True)
    order = ForeignKeyField(db_column='order_id', rel_model=SalesFlatOrder)
    shipping_address = IntegerField(db_column='shipping_address_id', null=True)
    shipping_amount = DecimalField(null=True)
    shipping_hidden_tax_amount = DecimalField(null=True)
    shipping_incl_tax = DecimalField(null=True)
    shipping_tax_amount = DecimalField(null=True)
    state = IntegerField(null=True)
    store_currency_code = CharField(max_length=3, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    store_to_base_rate = DecimalField(null=True)
    store_to_order_rate = DecimalField(null=True)
    subtotal = DecimalField(null=True)
    subtotal_incl_tax = DecimalField(null=True)
    tax_amount = DecimalField(null=True)
    transaction = CharField(db_column='transaction_id', max_length=255, null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'sales_flat_creditmemo'

class SalesFlatCreditmemoComment(BaseModel):
    comment = TextField(null=True)
    created_at = DateTimeField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    is_customer_notified = IntegerField(null=True)
    is_visible_on_front = IntegerField()
    parent = ForeignKeyField(db_column='parent_id', rel_model=SalesFlatCreditmemo)

    class Meta:
        db_table = 'sales_flat_creditmemo_comment'

class SalesFlatCreditmemoGrid(BaseModel):
    base_currency_code = CharField(max_length=3, null=True)
    base_customer_credit_amount = DecimalField(null=True)
    base_grand_total = DecimalField(null=True)
    base_to_global_rate = DecimalField(null=True)
    base_to_order_rate = DecimalField(null=True)
    billing_name = CharField(max_length=255, null=True)
    created_at = DateTimeField(null=True)
    creditmemo_status = IntegerField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=SalesFlatCreditmemo)
    global_currency_code = CharField(max_length=3, null=True)
    grand_total = DecimalField(null=True)
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    invoice = IntegerField(db_column='invoice_id', null=True)
    order_created_at = DateTimeField(null=True)
    order_currency_code = CharField(max_length=3, null=True)
    order = IntegerField(db_column='order_id')
    order_increment = CharField(db_column='order_increment_id', max_length=50, null=True)
    state = IntegerField(null=True)
    store_currency_code = CharField(max_length=3, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    store_to_base_rate = DecimalField(null=True)
    store_to_order_rate = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_creditmemo_grid'

class SalesFlatCreditmemoItem(BaseModel):
    additional_data = TextField(null=True)
    base_cost = DecimalField(null=True)
    base_discount_amount = DecimalField(null=True)
    base_hidden_tax_amount = DecimalField(null=True)
    base_price = DecimalField(null=True)
    base_price_incl_tax = DecimalField(null=True)
    base_row_total = DecimalField(null=True)
    base_row_total_incl_tax = DecimalField(null=True)
    base_tax_amount = DecimalField(null=True)
    base_weee_tax_applied_amount = DecimalField(null=True)
    base_weee_tax_applied_row_amnt = DecimalField(null=True)
    base_weee_tax_disposition = DecimalField(null=True)
    base_weee_tax_row_disposition = DecimalField(null=True)
    description = TextField(null=True)
    discount_amount = DecimalField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    hidden_tax_amount = DecimalField(null=True)
    name = CharField(max_length=255, null=True)
    order_item = IntegerField(db_column='order_item_id', null=True)
    parent = ForeignKeyField(db_column='parent_id', rel_model=SalesFlatCreditmemo)
    price = DecimalField(null=True)
    price_incl_tax = DecimalField(null=True)
    product = IntegerField(db_column='product_id', null=True)
    qty = DecimalField(null=True)
    row_total = DecimalField(null=True)
    row_total_incl_tax = DecimalField(null=True)
    sku = CharField(max_length=255, null=True)
    tax_amount = DecimalField(null=True)
    weee_tax_applied = TextField(null=True)
    weee_tax_applied_amount = DecimalField(null=True)
    weee_tax_applied_row_amount = DecimalField(null=True)
    weee_tax_disposition = DecimalField(null=True)
    weee_tax_row_disposition = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_creditmemo_item'

class SalesFlatInvoice(BaseModel):
    base_currency_code = CharField(max_length=3, null=True)
    base_customer_credit_amount = DecimalField(null=True)
    base_discount_amount = DecimalField(null=True)
    base_grand_total = DecimalField(null=True)
    base_hidden_tax_amount = DecimalField(null=True)
    base_shipping_amount = DecimalField(null=True)
    base_shipping_hidden_tax_amnt = DecimalField(null=True)
    base_shipping_incl_tax = DecimalField(null=True)
    base_shipping_tax_amount = DecimalField(null=True)
    base_subtotal = DecimalField(null=True)
    base_subtotal_incl_tax = DecimalField(null=True)
    base_tax_amount = DecimalField(null=True)
    base_to_global_rate = DecimalField(null=True)
    base_to_order_rate = DecimalField(null=True)
    base_total_refunded = DecimalField(null=True)
    billing_address = IntegerField(db_column='billing_address_id', null=True)
    can_void_flag = IntegerField(null=True)
    created_at = DateTimeField(null=True)
    customer_credit_amount = DecimalField(null=True)
    discount_amount = DecimalField(null=True)
    email_sent = IntegerField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    global_currency_code = CharField(max_length=3, null=True)
    grand_total = DecimalField(null=True)
    hidden_tax_amount = DecimalField(null=True)
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    is_used_for_refund = IntegerField(null=True)
    order_currency_code = CharField(max_length=3, null=True)
    order = ForeignKeyField(db_column='order_id', rel_model=SalesFlatOrder)
    shipping_address = IntegerField(db_column='shipping_address_id', null=True)
    shipping_amount = DecimalField(null=True)
    shipping_hidden_tax_amount = DecimalField(null=True)
    shipping_incl_tax = DecimalField(null=True)
    shipping_tax_amount = DecimalField(null=True)
    state = IntegerField(null=True)
    store_currency_code = CharField(max_length=3, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    store_to_base_rate = DecimalField(null=True)
    store_to_order_rate = DecimalField(null=True)
    subtotal = DecimalField(null=True)
    subtotal_incl_tax = DecimalField(null=True)
    tax_amount = DecimalField(null=True)
    total_qty = DecimalField(null=True)
    transaction = CharField(db_column='transaction_id', max_length=255, null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'sales_flat_invoice'

class SalesFlatInvoiceComment(BaseModel):
    comment = TextField(null=True)
    created_at = DateTimeField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    is_customer_notified = IntegerField(null=True)
    is_visible_on_front = IntegerField()
    parent = ForeignKeyField(db_column='parent_id', rel_model=SalesFlatInvoice)

    class Meta:
        db_table = 'sales_flat_invoice_comment'

class SalesFlatInvoiceGrid(BaseModel):
    base_currency_code = CharField(max_length=3, null=True)
    base_customer_credit_amount = DecimalField(null=True)
    base_grand_total = DecimalField(null=True)
    billing_name = CharField(max_length=255, null=True)
    created_at = DateTimeField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=SalesFlatInvoice)
    global_currency_code = CharField(max_length=3, null=True)
    grand_total = DecimalField(null=True)
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    order_created_at = DateTimeField(null=True)
    order_currency_code = CharField(max_length=3, null=True)
    order = IntegerField(db_column='order_id')
    order_increment = CharField(db_column='order_increment_id', max_length=50, null=True)
    state = IntegerField(null=True)
    store_currency_code = CharField(max_length=3, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)

    class Meta:
        db_table = 'sales_flat_invoice_grid'

class SalesFlatInvoiceItem(BaseModel):
    additional_data = TextField(null=True)
    base_cost = DecimalField(null=True)
    base_discount_amount = DecimalField(null=True)
    base_hidden_tax_amount = DecimalField(null=True)
    base_price = DecimalField(null=True)
    base_price_incl_tax = DecimalField(null=True)
    base_row_total = DecimalField(null=True)
    base_row_total_incl_tax = DecimalField(null=True)
    base_tax_amount = DecimalField(null=True)
    base_weee_tax_applied_amount = DecimalField(null=True)
    base_weee_tax_applied_row_amnt = DecimalField(null=True)
    base_weee_tax_disposition = DecimalField(null=True)
    base_weee_tax_row_disposition = DecimalField(null=True)
    description = TextField(null=True)
    discount_amount = DecimalField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    hidden_tax_amount = DecimalField(null=True)
    name = CharField(max_length=255, null=True)
    order_item = IntegerField(db_column='order_item_id', null=True)
    parent = ForeignKeyField(db_column='parent_id', rel_model=SalesFlatInvoice)
    price = DecimalField(null=True)
    price_incl_tax = DecimalField(null=True)
    product = IntegerField(db_column='product_id', null=True)
    qty = DecimalField(null=True)
    row_total = DecimalField(null=True)
    row_total_incl_tax = DecimalField(null=True)
    sku = CharField(max_length=255, null=True)
    tax_amount = DecimalField(null=True)
    weee_tax_applied = TextField(null=True)
    weee_tax_applied_amount = DecimalField(null=True)
    weee_tax_applied_row_amount = DecimalField(null=True)
    weee_tax_disposition = DecimalField(null=True)
    weee_tax_row_disposition = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_invoice_item'

class SalesFlatOrderAddress(BaseModel):
    address_type = CharField(max_length=255, null=True)
    city = CharField(max_length=255, null=True)
    company = CharField(max_length=255, null=True)
    country = CharField(db_column='country_id', max_length=2, null=True)
    customer_address = IntegerField(db_column='customer_address_id', null=True)
    customer = IntegerField(db_column='customer_id', null=True)
    email = CharField(max_length=255, null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    fax = CharField(max_length=255, null=True)
    firstname = CharField(max_length=255, null=True)
    lastname = CharField(max_length=255, null=True)
    middlename = CharField(max_length=255, null=True)
    parent = ForeignKeyField(db_column='parent_id', null=True, rel_model=SalesFlatOrder)
    postcode = CharField(max_length=255, null=True)
    prefix = CharField(max_length=255, null=True)
    quote_address = IntegerField(db_column='quote_address_id', null=True)
    region = CharField(max_length=255, null=True)
    region = IntegerField(db_column='region_id', null=True)
    street = CharField(max_length=255, null=True)
    suffix = CharField(max_length=255, null=True)
    telephone = CharField(max_length=255, null=True)
    vat = TextField(db_column='vat_id', null=True)
    vat_is_valid = IntegerField(null=True)
    vat_request_date = TextField(null=True)
    vat_request = TextField(db_column='vat_request_id', null=True)
    vat_request_success = IntegerField(null=True)

    class Meta:
        db_table = 'sales_flat_order_address'

class SalesFlatOrderGrid(BaseModel):
    base_currency_code = CharField(max_length=3, null=True)
    base_grand_total = DecimalField(null=True)
    base_total_paid = DecimalField(null=True)
    billing_name = CharField(max_length=255, null=True)
    created_at = DateTimeField(null=True)
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=SalesFlatOrder)
    grand_total = DecimalField(null=True)
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    order_currency_code = CharField(max_length=255, null=True)
    shipping_name = CharField(max_length=255, null=True)
    status = CharField(max_length=32, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    store_name = CharField(max_length=255, null=True)
    total_paid = DecimalField(null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'sales_flat_order_grid'

class SalesFlatOrderPayment(BaseModel):
    account_status = CharField(max_length=255, null=True)
    additional_data = TextField(null=True)
    additional_information = TextField(null=True)
    address_status = CharField(max_length=255, null=True)
    amount_authorized = DecimalField(null=True)
    amount_canceled = DecimalField(null=True)
    amount_ordered = DecimalField(null=True)
    amount_paid = DecimalField(null=True)
    amount_refunded = DecimalField(null=True)
    anet_trans_method = CharField(max_length=255, null=True)
    base_amount_authorized = DecimalField(null=True)
    base_amount_canceled = DecimalField(null=True)
    base_amount_ordered = DecimalField(null=True)
    base_amount_paid = DecimalField(null=True)
    base_amount_paid_online = DecimalField(null=True)
    base_amount_refunded = DecimalField(null=True)
    base_amount_refunded_online = DecimalField(null=True)
    base_shipping_amount = DecimalField(null=True)
    base_shipping_captured = DecimalField(null=True)
    base_shipping_refunded = DecimalField(null=True)
    cc_approval = CharField(max_length=255, null=True)
    cc_avs_status = CharField(max_length=255, null=True)
    cc_cid_status = CharField(max_length=255, null=True)
    cc_debug_request_body = CharField(max_length=255, null=True)
    cc_debug_response_body = CharField(max_length=255, null=True)
    cc_debug_response_serialized = CharField(max_length=255, null=True)
    cc_exp_month = CharField(max_length=255, null=True)
    cc_exp_year = CharField(max_length=255, null=True)
    cc_last4 = CharField(max_length=255, null=True)
    cc_number_enc = CharField(max_length=255, null=True)
    cc_owner = CharField(max_length=255, null=True)
    cc_secure_verify = CharField(max_length=255, null=True)
    cc_ss_issue = CharField(max_length=255, null=True)
    cc_ss_start_month = CharField(max_length=255, null=True)
    cc_ss_start_year = CharField(max_length=255, null=True)
    cc_status = CharField(max_length=255, null=True)
    cc_status_description = CharField(max_length=255, null=True)
    cc_trans = CharField(db_column='cc_trans_id', max_length=255, null=True)
    cc_type = CharField(max_length=255, null=True)
    echeck_account_name = CharField(max_length=255, null=True)
    echeck_account_type = CharField(max_length=255, null=True)
    echeck_bank_name = CharField(max_length=255, null=True)
    echeck_routing_number = CharField(max_length=255, null=True)
    echeck_type = CharField(max_length=255, null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    last_trans = CharField(db_column='last_trans_id', max_length=255, null=True)
    method = CharField(max_length=255, null=True)
    parent = ForeignKeyField(db_column='parent_id', rel_model=SalesFlatOrder)
    paybox_request_number = CharField(max_length=255, null=True)
    po_number = CharField(max_length=255, null=True)
    protection_eligibility = CharField(max_length=255, null=True)
    quote_payment = IntegerField(db_column='quote_payment_id', null=True)
    shipping_amount = DecimalField(null=True)
    shipping_captured = DecimalField(null=True)
    shipping_refunded = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_order_payment'

class SalesFlatOrderStatusHistory(BaseModel):
    comment = TextField(null=True)
    created_at = DateTimeField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    entity_name = CharField(max_length=32, null=True)
    is_customer_notified = IntegerField(null=True)
    is_visible_on_front = IntegerField()
    parent = ForeignKeyField(db_column='parent_id', rel_model=SalesFlatOrder)
    status = CharField(max_length=32, null=True)

    class Meta:
        db_table = 'sales_flat_order_status_history'

class SalesFlatQuote(BaseModel):
    applied_rule_ids = CharField(max_length=255, null=True)
    base_currency_code = CharField(max_length=255, null=True)
    base_customer_credit_total = DecimalField(null=True)
    base_grand_total = DecimalField(null=True)
    base_subtotal = DecimalField(null=True)
    base_subtotal_with_discount = DecimalField(null=True)
    base_to_global_rate = DecimalField(null=True)
    base_to_quote_rate = DecimalField(null=True)
    checkout_method = CharField(max_length=255, null=True)
    converted_at = DateTimeField(null=True)
    coupon_code = CharField(max_length=255, null=True)
    created_at = DateTimeField()
    customer_credit_total = DecimalField(null=True)
    customer_dob = DateTimeField(null=True)
    customer_email = CharField(max_length=255, null=True)
    customer_firstname = CharField(max_length=255, null=True)
    customer_gender = CharField(max_length=255, null=True)
    customer_group = IntegerField(db_column='customer_group_id', null=True)
    customer = IntegerField(db_column='customer_id', null=True)
    customer_is_guest = IntegerField(null=True)
    customer_lastname = CharField(max_length=255, null=True)
    customer_middlename = CharField(max_length=40, null=True)
    customer_note = CharField(max_length=255, null=True)
    customer_note_notify = IntegerField(null=True)
    customer_prefix = CharField(max_length=40, null=True)
    customer_suffix = CharField(max_length=40, null=True)
    customer_tax_class = IntegerField(db_column='customer_tax_class_id', null=True)
    customer_taxvat = CharField(max_length=255, null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    ext_shipping_info = TextField(null=True)
    gift_message = IntegerField(db_column='gift_message_id', null=True)
    global_currency_code = CharField(max_length=255, null=True)
    grand_total = DecimalField(null=True)
    is_active = IntegerField(null=True)
    is_changed = IntegerField(null=True)
    is_multi_shipping = IntegerField(null=True)
    is_persistent = IntegerField(null=True)
    is_virtual = IntegerField(null=True)
    items_count = IntegerField(null=True)
    items_qty = DecimalField(null=True)
    orig_order = IntegerField(db_column='orig_order_id', null=True)
    password_hash = CharField(max_length=255, null=True)
    quote_currency_code = CharField(max_length=255, null=True)
    remote_ip = CharField(max_length=32, null=True)
    reserved_order = CharField(db_column='reserved_order_id', max_length=64, null=True)
    store_currency_code = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    store_to_base_rate = DecimalField(null=True)
    store_to_quote_rate = DecimalField(null=True)
    subtotal = DecimalField(null=True)
    subtotal_with_discount = DecimalField(null=True)
    trigger_recollect = IntegerField()
    updated_at = DateTimeField()

    class Meta:
        db_table = 'sales_flat_quote'

class SalesFlatQuoteAddress(BaseModel):
    address = PrimaryKeyField(db_column='address_id')
    address_type = CharField(max_length=255, null=True)
    applied_taxes = TextField(null=True)
    base_customer_credit_amount = DecimalField(null=True)
    base_discount_amount = DecimalField()
    base_grand_total = DecimalField()
    base_hidden_tax_amount = DecimalField(null=True)
    base_shipping_amount = DecimalField()
    base_shipping_discount_amount = DecimalField(null=True)
    base_shipping_hidden_tax_amnt = DecimalField(null=True)
    base_shipping_incl_tax = DecimalField(null=True)
    base_shipping_tax_amount = DecimalField(null=True)
    base_subtotal = DecimalField()
    base_subtotal_total_incl_tax = DecimalField(null=True)
    base_subtotal_with_discount = DecimalField()
    base_tax_amount = DecimalField()
    city = CharField(max_length=255, null=True)
    collect_shipping_rates = IntegerField()
    company = CharField(max_length=255, null=True)
    country = CharField(db_column='country_id', max_length=255, null=True)
    created_at = DateTimeField()
    customer_address = IntegerField(db_column='customer_address_id', null=True)
    customer_credit_amount = DecimalField(null=True)
    customer = IntegerField(db_column='customer_id', null=True)
    customer_notes = TextField(null=True)
    discount_amount = DecimalField()
    discount_description = CharField(max_length=255, null=True)
    email = CharField(max_length=255, null=True)
    fax = CharField(max_length=255, null=True)
    firstname = CharField(max_length=255, null=True)
    free_shipping = IntegerField()
    gift_message = IntegerField(db_column='gift_message_id', null=True)
    grand_total = DecimalField()
    hidden_tax_amount = DecimalField(null=True)
    lastname = CharField(max_length=255, null=True)
    middlename = CharField(max_length=40, null=True)
    postcode = CharField(max_length=255, null=True)
    prefix = CharField(max_length=40, null=True)
    quote = ForeignKeyField(db_column='quote_id', rel_model=SalesFlatQuote)
    region = CharField(max_length=255, null=True)
    region = IntegerField(db_column='region_id', null=True)
    same_as_billing = IntegerField()
    save_in_address_book = IntegerField(null=True)
    shipping_amount = DecimalField()
    shipping_description = CharField(max_length=255, null=True)
    shipping_discount_amount = DecimalField(null=True)
    shipping_hidden_tax_amount = DecimalField(null=True)
    shipping_incl_tax = DecimalField(null=True)
    shipping_method = CharField(max_length=255, null=True)
    shipping_tax_amount = DecimalField(null=True)
    street = CharField(max_length=255, null=True)
    subtotal = DecimalField()
    subtotal_incl_tax = DecimalField(null=True)
    subtotal_with_discount = DecimalField()
    suffix = CharField(max_length=40, null=True)
    tax_amount = DecimalField()
    telephone = CharField(max_length=255, null=True)
    updated_at = DateTimeField()
    vat = TextField(db_column='vat_id', null=True)
    vat_is_valid = IntegerField(null=True)
    vat_request_date = TextField(null=True)
    vat_request = TextField(db_column='vat_request_id', null=True)
    vat_request_success = IntegerField(null=True)
    weight = DecimalField()

    class Meta:
        db_table = 'sales_flat_quote_address'

class SalesFlatQuoteItem(BaseModel):
    additional_data = TextField(null=True)
    applied_rule_ids = TextField(null=True)
    base_cost = DecimalField(null=True)
    base_discount_amount = DecimalField(null=True)
    base_hidden_tax_amount = DecimalField(null=True)
    base_price = DecimalField()
    base_price_incl_tax = DecimalField(null=True)
    base_row_total = DecimalField()
    base_row_total_incl_tax = DecimalField(null=True)
    base_tax_amount = DecimalField(null=True)
    base_tax_before_discount = DecimalField(null=True)
    base_weee_tax_applied_amount = DecimalField(null=True)
    base_weee_tax_applied_row_amnt = DecimalField(null=True)
    base_weee_tax_disposition = DecimalField(null=True)
    base_weee_tax_row_disposition = DecimalField(null=True)
    created_at = DateTimeField()
    custom_price = DecimalField(null=True)
    description = TextField(null=True)
    discount_amount = DecimalField(null=True)
    discount_percent = DecimalField(null=True)
    free_shipping = IntegerField()
    gift_message = IntegerField(db_column='gift_message_id', null=True)
    hidden_tax_amount = DecimalField(null=True)
    is_qty_decimal = IntegerField(null=True)
    is_virtual = IntegerField(null=True)
    item = PrimaryKeyField(db_column='item_id')
    name = CharField(max_length=255, null=True)
    no_discount = IntegerField(null=True)
    original_custom_price = DecimalField(null=True)
    parent_item = ForeignKeyField(db_column='parent_item_id', null=True, rel_model='self')
    price = DecimalField()
    price_incl_tax = DecimalField(null=True)
    product = ForeignKeyField(db_column='product_id', null=True, rel_model=CatalogProductEntity)
    product_type = CharField(max_length=255, null=True)
    qty = DecimalField()
    quote = ForeignKeyField(db_column='quote_id', rel_model=SalesFlatQuote)
    redirect_url = CharField(max_length=255, null=True)
    row_total = DecimalField()
    row_total_incl_tax = DecimalField(null=True)
    row_total_with_discount = DecimalField(null=True)
    row_weight = DecimalField(null=True)
    sku = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    tax_amount = DecimalField(null=True)
    tax_before_discount = DecimalField(null=True)
    tax_percent = DecimalField(null=True)
    updated_at = DateTimeField()
    weee_tax_applied = TextField(null=True)
    weee_tax_applied_amount = DecimalField(null=True)
    weee_tax_applied_row_amount = DecimalField(null=True)
    weee_tax_disposition = DecimalField(null=True)
    weee_tax_row_disposition = DecimalField(null=True)
    weight = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_quote_item'

class SalesFlatQuoteAddressItem(BaseModel):
    additional_data = TextField(null=True)
    address_item = PrimaryKeyField(db_column='address_item_id')
    applied_rule_ids = TextField(null=True)
    base_cost = DecimalField(null=True)
    base_discount_amount = DecimalField(null=True)
    base_hidden_tax_amount = DecimalField(null=True)
    base_price = DecimalField(null=True)
    base_price_incl_tax = DecimalField(null=True)
    base_row_total = DecimalField()
    base_row_total_incl_tax = DecimalField(null=True)
    base_tax_amount = DecimalField(null=True)
    created_at = DateTimeField()
    description = TextField(null=True)
    discount_amount = DecimalField(null=True)
    discount_percent = DecimalField(null=True)
    free_shipping = IntegerField(null=True)
    gift_message = IntegerField(db_column='gift_message_id', null=True)
    hidden_tax_amount = DecimalField(null=True)
    image = CharField(max_length=255, null=True)
    is_qty_decimal = IntegerField(null=True)
    name = CharField(max_length=255, null=True)
    no_discount = IntegerField(null=True)
    parent_item = ForeignKeyField(db_column='parent_item_id', null=True, rel_model='self')
    parent_product = IntegerField(db_column='parent_product_id', null=True)
    price = DecimalField(null=True)
    price_incl_tax = DecimalField(null=True)
    product = IntegerField(db_column='product_id', null=True)
    qty = DecimalField()
    quote_address = ForeignKeyField(db_column='quote_address_id', rel_model=SalesFlatQuoteAddress)
    quote_item = ForeignKeyField(db_column='quote_item_id', rel_model=SalesFlatQuoteItem)
    row_total = DecimalField()
    row_total_incl_tax = DecimalField(null=True)
    row_total_with_discount = DecimalField(null=True)
    row_weight = DecimalField(null=True)
    sku = CharField(max_length=255, null=True)
    super_product = IntegerField(db_column='super_product_id', null=True)
    tax_amount = DecimalField(null=True)
    tax_percent = DecimalField(null=True)
    updated_at = DateTimeField()
    weight = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_quote_address_item'

class SalesFlatQuoteItemOption(BaseModel):
    code = CharField(max_length=255)
    item = ForeignKeyField(db_column='item_id', rel_model=SalesFlatQuoteItem)
    option = PrimaryKeyField(db_column='option_id')
    product = IntegerField(db_column='product_id')
    value = TextField(null=True)

    class Meta:
        db_table = 'sales_flat_quote_item_option'

class SalesFlatQuotePayment(BaseModel):
    additional_data = TextField(null=True)
    additional_information = TextField(null=True)
    cc_cid_enc = CharField(max_length=255, null=True)
    cc_exp_month = IntegerField(null=True)
    cc_exp_year = IntegerField(null=True)
    cc_last4 = CharField(max_length=255, null=True)
    cc_number_enc = CharField(max_length=255, null=True)
    cc_owner = CharField(max_length=255, null=True)
    cc_ss_issue = CharField(max_length=255, null=True)
    cc_ss_owner = CharField(max_length=255, null=True)
    cc_ss_start_month = IntegerField(null=True)
    cc_ss_start_year = IntegerField(null=True)
    cc_type = CharField(max_length=255, null=True)
    created_at = DateTimeField()
    method = CharField(max_length=255, null=True)
    payment = PrimaryKeyField(db_column='payment_id')
    paypal_correlation = CharField(db_column='paypal_correlation_id', max_length=255, null=True)
    paypal_payer = CharField(db_column='paypal_payer_id', max_length=255, null=True)
    paypal_payer_status = CharField(max_length=255, null=True)
    po_number = CharField(max_length=255, null=True)
    quote = ForeignKeyField(db_column='quote_id', rel_model=SalesFlatQuote)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'sales_flat_quote_payment'

class SalesFlatQuoteShippingRate(BaseModel):
    address = ForeignKeyField(db_column='address_id', rel_model=SalesFlatQuoteAddress)
    carrier = CharField(max_length=255, null=True)
    carrier_title = CharField(max_length=255, null=True)
    code = CharField(max_length=255, null=True)
    created_at = DateTimeField()
    error_message = TextField(null=True)
    method = CharField(max_length=255, null=True)
    method_description = TextField(null=True)
    method_title = TextField(null=True)
    price = DecimalField()
    rate = PrimaryKeyField(db_column='rate_id')
    updated_at = DateTimeField()

    class Meta:
        db_table = 'sales_flat_quote_shipping_rate'

class SalesFlatShipment(BaseModel):
    billing_address = IntegerField(db_column='billing_address_id', null=True)
    created_at = DateTimeField(null=True)
    customer = IntegerField(db_column='customer_id', null=True)
    email_sent = IntegerField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    order = ForeignKeyField(db_column='order_id', rel_model=SalesFlatOrder)
    packages = TextField(null=True)
    shipment_status = IntegerField(null=True)
    shipping_address = IntegerField(db_column='shipping_address_id', null=True)
    shipping_label = TextField(null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    total_qty = DecimalField(null=True)
    total_weight = DecimalField(null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'sales_flat_shipment'

class SalesFlatShipmentComment(BaseModel):
    comment = TextField(null=True)
    created_at = DateTimeField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    is_customer_notified = IntegerField(null=True)
    is_visible_on_front = IntegerField()
    parent = ForeignKeyField(db_column='parent_id', rel_model=SalesFlatShipment)

    class Meta:
        db_table = 'sales_flat_shipment_comment'

class SalesFlatShipmentGrid(BaseModel):
    created_at = DateTimeField(null=True)
    entity = ForeignKeyField(db_column='entity_id', primary_key=True, rel_model=SalesFlatShipment)
    increment = CharField(db_column='increment_id', max_length=50, null=True)
    order_created_at = DateTimeField(null=True)
    order = IntegerField(db_column='order_id')
    order_increment = CharField(db_column='order_increment_id', max_length=50, null=True)
    shipment_status = IntegerField(null=True)
    shipping_name = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    total_qty = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_shipment_grid'

class SalesFlatShipmentItem(BaseModel):
    additional_data = TextField(null=True)
    description = TextField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    name = CharField(max_length=255, null=True)
    order_item = IntegerField(db_column='order_item_id', null=True)
    parent = ForeignKeyField(db_column='parent_id', rel_model=SalesFlatShipment)
    price = DecimalField(null=True)
    product = IntegerField(db_column='product_id', null=True)
    qty = DecimalField(null=True)
    row_total = DecimalField(null=True)
    sku = CharField(max_length=255, null=True)
    weight = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_shipment_item'

class SalesFlatShipmentTrack(BaseModel):
    carrier_code = CharField(max_length=32, null=True)
    created_at = DateTimeField(null=True)
    description = TextField(null=True)
    entity = PrimaryKeyField(db_column='entity_id')
    order = IntegerField(db_column='order_id')
    parent = ForeignKeyField(db_column='parent_id', rel_model=SalesFlatShipment)
    qty = DecimalField(null=True)
    title = CharField(max_length=255, null=True)
    track_number = TextField(null=True)
    updated_at = DateTimeField(null=True)
    weight = DecimalField(null=True)

    class Meta:
        db_table = 'sales_flat_shipment_track'

class SalesInvoicedAggregated(BaseModel):
    invoiced = DecimalField(null=True)
    invoiced_captured = DecimalField(null=True)
    invoiced_not_captured = DecimalField(null=True)
    order_status = CharField(max_length=50, null=True)
    orders_count = IntegerField()
    orders_invoiced = DecimalField(null=True)
    period = DateField(null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)

    class Meta:
        db_table = 'sales_invoiced_aggregated'

class SalesInvoicedAggregatedOrder(BaseModel):
    invoiced = DecimalField(null=True)
    invoiced_captured = DecimalField(null=True)
    invoiced_not_captured = DecimalField(null=True)
    order_status = CharField(max_length=50)
    orders_count = IntegerField()
    orders_invoiced = DecimalField(null=True)
    period = DateField(null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)

    class Meta:
        db_table = 'sales_invoiced_aggregated_order'

class SalesOrderAggregatedCreated(BaseModel):
    order_status = CharField(max_length=50)
    orders_count = IntegerField()
    period = DateField(null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    total_canceled_amount = DecimalField()
    total_discount_amount = DecimalField()
    total_discount_amount_actual = DecimalField()
    total_income_amount = DecimalField()
    total_invoiced_amount = DecimalField()
    total_paid_amount = DecimalField()
    total_profit_amount = DecimalField()
    total_qty_invoiced = DecimalField()
    total_qty_ordered = DecimalField()
    total_refunded_amount = DecimalField()
    total_revenue_amount = DecimalField()
    total_shipping_amount = DecimalField()
    total_shipping_amount_actual = DecimalField()
    total_tax_amount = DecimalField()
    total_tax_amount_actual = DecimalField()

    class Meta:
        db_table = 'sales_order_aggregated_created'

class SalesOrderAggregatedUpdated(BaseModel):
    order_status = CharField(max_length=50)
    orders_count = IntegerField()
    period = DateField(null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    total_canceled_amount = DecimalField()
    total_discount_amount = DecimalField()
    total_discount_amount_actual = DecimalField()
    total_income_amount = DecimalField()
    total_invoiced_amount = DecimalField()
    total_paid_amount = DecimalField()
    total_profit_amount = DecimalField()
    total_qty_invoiced = DecimalField()
    total_qty_ordered = DecimalField()
    total_refunded_amount = DecimalField()
    total_revenue_amount = DecimalField()
    total_shipping_amount = DecimalField()
    total_shipping_amount_actual = DecimalField()
    total_tax_amount = DecimalField()
    total_tax_amount_actual = DecimalField()

    class Meta:
        db_table = 'sales_order_aggregated_updated'

class SalesOrderStatus(BaseModel):
    label = CharField(max_length=128)
    status = CharField(max_length=32, primary_key=True)

    class Meta:
        db_table = 'sales_order_status'

class SalesOrderStatusLabel(BaseModel):
    label = CharField(max_length=128)
    status = ForeignKeyField(db_column='status', primary_key=True, rel_model=SalesOrderStatus)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'sales_order_status_label'

class SalesOrderStatusState(BaseModel):
    is_default = IntegerField()
    state = CharField(max_length=32)
    status = ForeignKeyField(db_column='status', primary_key=True, rel_model=SalesOrderStatus)

    class Meta:
        db_table = 'sales_order_status_state'

class SalesOrderTax(BaseModel):
    amount = DecimalField(null=True)
    base_amount = DecimalField(null=True)
    base_real_amount = DecimalField(null=True)
    code = CharField(max_length=255, null=True)
    hidden = IntegerField()
    order = IntegerField(db_column='order_id')
    percent = DecimalField(null=True)
    position = IntegerField()
    priority = IntegerField()
    process = IntegerField()
    tax = PrimaryKeyField(db_column='tax_id')
    title = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'sales_order_tax'

class SalesOrderTaxItem(BaseModel):
    item = ForeignKeyField(db_column='item_id', rel_model=SalesFlatOrderItem)
    tax = ForeignKeyField(db_column='tax_id', rel_model=SalesOrderTax)
    tax_item = PrimaryKeyField(db_column='tax_item_id')
    tax_percent = DecimalField()

    class Meta:
        db_table = 'sales_order_tax_item'

class SalesPaymentTransaction(BaseModel):
    additional_information = TextField(null=True)
    created_at = DateTimeField(null=True)
    is_closed = IntegerField()
    order = ForeignKeyField(db_column='order_id', rel_model=SalesFlatOrder)
    parent = ForeignKeyField(db_column='parent_id', null=True, rel_model='self')
    parent_txn = CharField(db_column='parent_txn_id', max_length=100, null=True)
    payment = ForeignKeyField(db_column='payment_id', rel_model=SalesFlatOrderPayment)
    transaction = PrimaryKeyField(db_column='transaction_id')
    txn = CharField(db_column='txn_id', max_length=100, null=True)
    txn_type = CharField(max_length=15, null=True)

    class Meta:
        db_table = 'sales_payment_transaction'

class SalesRecurringProfile(BaseModel):
    additional_info = TextField(null=True)
    bill_failed_later = IntegerField()
    billing_address_info = TextField()
    billing_amount = DecimalField()
    created_at = DateTimeField()
    currency_code = CharField(max_length=3)
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    init_amount = DecimalField(null=True)
    init_may_fail = IntegerField()
    internal_reference = CharField(db_column='internal_reference_id', max_length=42)
    method_code = CharField(max_length=32)
    order_info = TextField()
    order_item_info = TextField()
    period_frequency = IntegerField(null=True)
    period_max_cycles = IntegerField(null=True)
    period_unit = CharField(max_length=20)
    profile = PrimaryKeyField(db_column='profile_id')
    profile_vendor_info = TextField(null=True)
    reference = CharField(db_column='reference_id', max_length=32, null=True)
    schedule_description = CharField(max_length=255)
    shipping_address_info = TextField(null=True)
    shipping_amount = DecimalField(null=True)
    start_datetime = DateTimeField()
    state = CharField(max_length=20)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    subscriber_name = CharField(max_length=150, null=True)
    suspension_threshold = IntegerField(null=True)
    tax_amount = DecimalField(null=True)
    trial_billing_amount = TextField(null=True)
    trial_period_frequency = IntegerField(null=True)
    trial_period_max_cycles = IntegerField(null=True)
    trial_period_unit = CharField(max_length=20, null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'sales_recurring_profile'

class SalesRecurringProfileOrder(BaseModel):
    link = PrimaryKeyField(db_column='link_id')
    order = ForeignKeyField(db_column='order_id', rel_model=SalesFlatOrder)
    profile = ForeignKeyField(db_column='profile_id', rel_model=SalesRecurringProfile)

    class Meta:
        db_table = 'sales_recurring_profile_order'

class SalesRefundedAggregated(BaseModel):
    offline_refunded = DecimalField(null=True)
    online_refunded = DecimalField(null=True)
    order_status = CharField(max_length=50)
    orders_count = IntegerField()
    period = DateField(null=True)
    refunded = DecimalField(null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)

    class Meta:
        db_table = 'sales_refunded_aggregated'

class SalesRefundedAggregatedOrder(BaseModel):
    offline_refunded = DecimalField(null=True)
    online_refunded = DecimalField(null=True)
    order_status = CharField(max_length=50, null=True)
    orders_count = IntegerField()
    period = DateField(null=True)
    refunded = DecimalField(null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)

    class Meta:
        db_table = 'sales_refunded_aggregated_order'

class SalesShippingAggregated(BaseModel):
    order_status = CharField(max_length=50, null=True)
    orders_count = IntegerField()
    period = DateField(null=True)
    shipping_description = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    total_shipping = DecimalField(null=True)
    total_shipping_actual = DecimalField(null=True)

    class Meta:
        db_table = 'sales_shipping_aggregated'

class SalesShippingAggregatedOrder(BaseModel):
    order_status = CharField(max_length=50, null=True)
    orders_count = IntegerField()
    period = DateField(null=True)
    shipping_description = CharField(max_length=255, null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    total_shipping = DecimalField(null=True)
    total_shipping_actual = DecimalField(null=True)

    class Meta:
        db_table = 'sales_shipping_aggregated_order'

class Salesrule(BaseModel):
    actions_serialized = TextField(null=True)
    apply_to_shipping = IntegerField()
    conditions_serialized = TextField(null=True)
    coupon_type = IntegerField()
    description = TextField(null=True)
    discount_amount = DecimalField()
    discount_qty = DecimalField(null=True)
    discount_step = IntegerField()
    from_date = DateField(null=True)
    is_active = IntegerField()
    is_advanced = IntegerField()
    is_rss = IntegerField()
    name = CharField(max_length=255, null=True)
    product_ids = TextField(null=True)
    rule = PrimaryKeyField(db_column='rule_id')
    simple_action = CharField(max_length=32, null=True)
    simple_free_shipping = IntegerField()
    sort_order = IntegerField()
    stop_rules_processing = IntegerField()
    times_used = IntegerField()
    to_date = DateField(null=True)
    use_auto_generation = IntegerField()
    uses_per_coupon = IntegerField()
    uses_per_customer = IntegerField()

    class Meta:
        db_table = 'salesrule'

class SalesruleCoupon(BaseModel):
    code = CharField(max_length=255, null=True)
    coupon = PrimaryKeyField(db_column='coupon_id')
    created_at = DateTimeField()
    expiration_date = DateTimeField(null=True)
    is_primary = IntegerField(null=True)
    rule = ForeignKeyField(db_column='rule_id', rel_model=Salesrule)
    times_used = IntegerField()
    type = IntegerField(null=True)
    usage_limit = IntegerField(null=True)
    usage_per_customer = IntegerField(null=True)

    class Meta:
        db_table = 'salesrule_coupon'

class SalesruleCouponUsage(BaseModel):
    coupon = ForeignKeyField(db_column='coupon_id', primary_key=True, rel_model=SalesruleCoupon)
    customer = ForeignKeyField(db_column='customer_id', rel_model=CustomerEntity)
    times_used = IntegerField()

    class Meta:
        db_table = 'salesrule_coupon_usage'

class SalesruleCustomer(BaseModel):
    customer = ForeignKeyField(db_column='customer_id', rel_model=CustomerEntity)
    rule_customer = PrimaryKeyField(db_column='rule_customer_id')
    rule = ForeignKeyField(db_column='rule_id', rel_model=Salesrule)
    times_used = IntegerField()

    class Meta:
        db_table = 'salesrule_customer'

class SalesruleCustomerGroup(BaseModel):
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    rule = ForeignKeyField(db_column='rule_id', primary_key=True, rel_model=Salesrule)

    class Meta:
        db_table = 'salesrule_customer_group'

class SalesruleLabel(BaseModel):
    label = CharField(max_length=255, null=True)
    label = PrimaryKeyField(db_column='label_id')
    rule = ForeignKeyField(db_column='rule_id', rel_model=Salesrule)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'salesrule_label'

class SalesruleProductAttribute(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    rule = ForeignKeyField(db_column='rule_id', primary_key=True, rel_model=Salesrule)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'salesrule_product_attribute'

class SalesruleWebsite(BaseModel):
    rule = ForeignKeyField(db_column='rule_id', primary_key=True, rel_model=Salesrule)
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'salesrule_website'

class Schoolselector(BaseModel):
    created_time = DateTimeField(null=True)
    school_state = CharField(max_length=2)
    schoolselector = PrimaryKeyField(db_column='schoolselector_id')
    status = IntegerField()
    store = IntegerField(db_column='store_id')
    title = CharField(max_length=100)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'schoolselector'

class SendfriendLog(BaseModel):
    ip = BigIntegerField()
    log = PrimaryKeyField(db_column='log_id')
    time = IntegerField()
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'sendfriend_log'

class ShippingTablerate(BaseModel):
    condition_name = CharField(max_length=20)
    condition_value = DecimalField()
    cost = DecimalField()
    dest_country = CharField(db_column='dest_country_id', max_length=4)
    dest_region = IntegerField(db_column='dest_region_id')
    dest_zip = CharField(max_length=10)
    pk = PrimaryKeyField()
    price = DecimalField()
    website = IntegerField(db_column='website_id')

    class Meta:
        db_table = 'shipping_tablerate'

class Sitemap(BaseModel):
    sitemap_filename = CharField(max_length=32, null=True)
    sitemap = PrimaryKeyField(db_column='sitemap_id')
    sitemap_path = CharField(max_length=255, null=True)
    sitemap_time = DateTimeField(null=True)
    sitemap_type = CharField(max_length=32, null=True)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)

    class Meta:
        db_table = 'sitemap'

class Stores(BaseModel):
    store_name_code = CharField(max_length=255)

    class Meta:
        db_table = 'stores'

class StoreSchools(BaseModel):
    created_at = DateTimeField()
    school = ForeignKeyField(db_column='school_id', rel_model=Schools)
    store = ForeignKeyField(db_column='store_id', rel_model=Stores)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'store_schools'

class Tag(BaseModel):
    first_customer = ForeignKeyField(db_column='first_customer_id', null=True, rel_model=CustomerEntity)
    first_store = ForeignKeyField(db_column='first_store_id', null=True, rel_model=CoreStore)
    name = CharField(max_length=255, null=True)
    status = IntegerField()
    tag = PrimaryKeyField(db_column='tag_id')

    class Meta:
        db_table = 'tag'

class TagProperties(BaseModel):
    base_popularity = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    tag = ForeignKeyField(db_column='tag_id', primary_key=True, rel_model=Tag)

    class Meta:
        db_table = 'tag_properties'

class TagRelation(BaseModel):
    active = IntegerField()
    created_at = DateTimeField(null=True)
    customer = ForeignKeyField(db_column='customer_id', null=True, rel_model=CustomerEntity)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    tag = ForeignKeyField(db_column='tag_id', rel_model=Tag)
    tag_relation = PrimaryKeyField(db_column='tag_relation_id')

    class Meta:
        db_table = 'tag_relation'

class TagSummary(BaseModel):
    base_popularity = IntegerField()
    customers = IntegerField()
    historical_uses = IntegerField()
    popularity = IntegerField()
    products = IntegerField()
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    tag = ForeignKeyField(db_column='tag_id', primary_key=True, rel_model=Tag)
    uses = IntegerField()

    class Meta:
        db_table = 'tag_summary'

class TaxClass(BaseModel):
    class_ = PrimaryKeyField(db_column='class_id')
    class_name = CharField(max_length=255)
    class_type = CharField(max_length=8)

    class Meta:
        db_table = 'tax_class'

class TaxCalculationRate(BaseModel):
    code = CharField(max_length=255)
    rate = DecimalField()
    tax_calculation_rate = PrimaryKeyField(db_column='tax_calculation_rate_id')
    tax_country = CharField(db_column='tax_country_id', max_length=2)
    tax_postcode = CharField(max_length=21, null=True)
    tax_region = IntegerField(db_column='tax_region_id')
    zip_from = IntegerField(null=True)
    zip_is_range = IntegerField(null=True)
    zip_to = IntegerField(null=True)

    class Meta:
        db_table = 'tax_calculation_rate'

class TaxCalculationRule(BaseModel):
    code = CharField(max_length=255)
    position = IntegerField()
    priority = IntegerField()
    tax_calculation_rule = PrimaryKeyField(db_column='tax_calculation_rule_id')

    class Meta:
        db_table = 'tax_calculation_rule'

class TaxCalculation(BaseModel):
    customer_tax_class = ForeignKeyField(db_column='customer_tax_class_id', rel_model=TaxClass)
    product_tax_class = ForeignKeyField(db_column='product_tax_class_id', rel_model=TaxClass)
    tax_calculation = PrimaryKeyField(db_column='tax_calculation_id')
    tax_calculation_rate = ForeignKeyField(db_column='tax_calculation_rate_id', rel_model=TaxCalculationRate)
    tax_calculation_rule = ForeignKeyField(db_column='tax_calculation_rule_id', rel_model=TaxCalculationRule)

    class Meta:
        db_table = 'tax_calculation'

class TaxCalculationRateTitle(BaseModel):
    store = ForeignKeyField(db_column='store_id', rel_model=CoreStore)
    tax_calculation_rate = ForeignKeyField(db_column='tax_calculation_rate_id', rel_model=TaxCalculationRate)
    tax_calculation_rate_title = PrimaryKeyField(db_column='tax_calculation_rate_title_id')
    value = CharField(max_length=255)

    class Meta:
        db_table = 'tax_calculation_rate_title'

class TaxOrderAggregatedCreated(BaseModel):
    code = CharField(max_length=255)
    order_status = CharField(max_length=50)
    orders_count = IntegerField()
    percent = FloatField(null=True)
    period = DateField(null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    tax_base_amount_sum = FloatField(null=True)

    class Meta:
        db_table = 'tax_order_aggregated_created'

class TaxOrderAggregatedUpdated(BaseModel):
    code = CharField(max_length=255)
    order_status = CharField(max_length=50)
    orders_count = IntegerField()
    percent = FloatField(null=True)
    period = DateField(null=True)
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    tax_base_amount_sum = FloatField(null=True)

    class Meta:
        db_table = 'tax_order_aggregated_updated'

class WeeeDiscount(BaseModel):
    customer_group = ForeignKeyField(db_column='customer_group_id', rel_model=CustomerGroup)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    value = DecimalField()
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'weee_discount'

class WeeeTax(BaseModel):
    attribute = ForeignKeyField(db_column='attribute_id', rel_model=EavAttribute)
    country = ForeignKeyField(db_column='country', null=True, rel_model=DirectoryCountry)
    entity = ForeignKeyField(db_column='entity_id', rel_model=CatalogProductEntity)
    entity_type = IntegerField(db_column='entity_type_id')
    state = CharField(max_length=255)
    value = DecimalField()
    value = PrimaryKeyField(db_column='value_id')
    website = ForeignKeyField(db_column='website_id', rel_model=CoreWebsite)

    class Meta:
        db_table = 'weee_tax'

class Widget(BaseModel):
    parameters = TextField(null=True)
    widget_code = CharField(max_length=255, null=True)
    widget = PrimaryKeyField(db_column='widget_id')
    widget_type = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'widget'

class WidgetInstance(BaseModel):
    instance = PrimaryKeyField(db_column='instance_id')
    instance_type = CharField(max_length=255, null=True)
    package_theme = CharField(max_length=255, null=True)
    sort_order = IntegerField()
    store_ids = CharField(max_length=255)
    title = CharField(max_length=255, null=True)
    widget_parameters = TextField(null=True)

    class Meta:
        db_table = 'widget_instance'

class WidgetInstancePage(BaseModel):
    block_reference = CharField(max_length=255, null=True)
    entities = TextField(null=True)
    instance = ForeignKeyField(db_column='instance_id', rel_model=WidgetInstance)
    layout_handle = CharField(max_length=255, null=True)
    page_for = CharField(max_length=25, null=True)
    page_group = CharField(max_length=25, null=True)
    page = PrimaryKeyField(db_column='page_id')
    page_template = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'widget_instance_page'

class WidgetInstancePageLayout(BaseModel):
    layout_update = ForeignKeyField(db_column='layout_update_id', rel_model=CoreLayoutUpdate)
    page = ForeignKeyField(db_column='page_id', rel_model=WidgetInstancePage)

    class Meta:
        db_table = 'widget_instance_page_layout'

class Wishlist(BaseModel):
    customer = ForeignKeyField(db_column='customer_id', rel_model=CustomerEntity)
    shared = IntegerField()
    sharing_code = CharField(max_length=32, null=True)
    updated_at = DateTimeField(null=True)
    wishlist = PrimaryKeyField(db_column='wishlist_id')

    class Meta:
        db_table = 'wishlist'

class WishlistItem(BaseModel):
    added_at = DateTimeField(null=True)
    description = TextField(null=True)
    product = ForeignKeyField(db_column='product_id', rel_model=CatalogProductEntity)
    qty = DecimalField()
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    wishlist = ForeignKeyField(db_column='wishlist_id', rel_model=Wishlist)
    wishlist_item = PrimaryKeyField(db_column='wishlist_item_id')

    class Meta:
        db_table = 'wishlist_item'

class WishlistItemOption(BaseModel):
    code = CharField(max_length=255)
    option = PrimaryKeyField(db_column='option_id')
    product = IntegerField(db_column='product_id')
    value = TextField(null=True)
    wishlist_item = ForeignKeyField(db_column='wishlist_item_id', rel_model=WishlistItem)

    class Meta:
        db_table = 'wishlist_item_option'

class XmlconnectApplication(BaseModel):
    active_from = DateField(null=True)
    active_to = DateField(null=True)
    application = PrimaryKeyField(db_column='application_id')
    browsing_mode = IntegerField(null=True)
    code = CharField(max_length=32)
    name = CharField(max_length=255)
    status = IntegerField()
    store = ForeignKeyField(db_column='store_id', null=True, rel_model=CoreStore)
    type = CharField(max_length=32)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'xmlconnect_application'

class XmlconnectConfigData(BaseModel):
    application = ForeignKeyField(db_column='application_id', rel_model=XmlconnectApplication)
    category = CharField(max_length=60)
    path = CharField(max_length=250)
    value = TextField()

    class Meta:
        db_table = 'xmlconnect_config_data'

class XmlconnectHistory(BaseModel):
    activation_key = CharField(max_length=255)
    application = ForeignKeyField(db_column='application_id', rel_model=XmlconnectApplication)
    code = CharField(max_length=32)
    created_at = DateTimeField(null=True)
    history = PrimaryKeyField(db_column='history_id')
    name = CharField(max_length=255)
    params = TextField(null=True)
    store = IntegerField(db_column='store_id', null=True)
    title = CharField(max_length=200)

    class Meta:
        db_table = 'xmlconnect_history'

class XmlconnectNotificationTemplate(BaseModel):
    application = ForeignKeyField(db_column='application_id', rel_model=XmlconnectApplication)
    content = TextField()
    created_at = DateTimeField(null=True)
    message_title = CharField(max_length=255)
    modified_at = DateTimeField(null=True)
    name = CharField(max_length=255)
    push_title = CharField(max_length=140)
    template = PrimaryKeyField(db_column='template_id')

    class Meta:
        db_table = 'xmlconnect_notification_template'

class XmlconnectQueue(BaseModel):
    content = TextField(null=True)
    create_time = DateTimeField(null=True)
    exec_time = DateTimeField(null=True)
    message_title = CharField(max_length=255, null=True)
    push_title = CharField(max_length=140)
    queue = PrimaryKeyField(db_column='queue_id')
    status = IntegerField()
    template = ForeignKeyField(db_column='template_id', rel_model=XmlconnectNotificationTemplate)
    type = CharField(max_length=12)

    class Meta:
        db_table = 'xmlconnect_queue'

