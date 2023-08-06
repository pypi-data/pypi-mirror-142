from ingestor.common.constants import CONTENT_ID, YEAR, DURATION_MINUTE


# Content Node Properties

def content_node_properties(property_value):
    node_property = {CONTENT_ID: property_value[CONTENT_ID],
                     YEAR: property_value[YEAR],
                     DURATION_MINUTE: property_value[DURATION_MINUTE]}
    return node_property


'''DEFINING RELATIONSHIP NAMES'''
HAS_CATEGORY = "HAS_CATEGORY"
HAS_SUBCATEGORY = "HAS_SUBCATEGORY"
HAS_COUNTRY = "HAS_COUNTRY"
HAS_TAG = "HAS_TAG"
HAS_ACTOR = "HAS_ACTOR"
HAS_CONTENT_CORE = "HAS_CONTENT_CORE"
HAS_PRODUCT = "HAS_PRODUCT"
HAS_PACKAGE = "HAS_PACKAGE"
HAS_HOMEPAGE = "HAS_HOMEPAGE"
