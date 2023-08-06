CUSTOMER_ID = "customer_id"
DURATION = "duration"
BIRTHDAY = "birthday"
GENDER = "gender"
CUSTOMER_CREATED_ON = "customer_created_on"
CUSTOMER_MODIFIED_ON = "customer_modified_on"
PAYTVPROVIDER_ID = "paytvprovider_id"
DEFAULT_DATE = "1970-10-10"
GENDER_VALUES ={'male': 'm', 'female': 'f', 'gender': 'na'}
AGE = "age"
MEDIAN_AGE = 52
AGE_UPPER_BOUND = 100
DEFAULT_NA = 'na'
DEFAULT_NUM = '-1'
DEFAULT_NAN = 'nan'
COUNTRY_ID = 'country_id'
VIDEO_ID2 = 'video_id2'
VIDEO_NAME2 = 'video_name2'
VIDEO_NAME1 = 'video_name1'
REDUNDANT_FEATURES = [VIDEO_ID2, VIDEO_NAME1, VIDEO_NAME2]
UNKNOWN_LABEL = 'unknown'
REGION_NAME = 'region_name'
DEVOPS = 'devops'
VIDEO_ID1 = 'video_id1'
ATTRIBUTE1 = 'attribute1'
ACTOR_NAME = 'actor_name'
DIRECTOR_NAME = 'director_name'
MOVIE = "movie"
SERIES = "series"
ABSURD_VALUE = "\\N"
CREATED_ON = 'created_on'
VOD_MOVIE = 'VOD_MOVIE'
VOD_SERIES = 'VOD_SERIES'
VOD = 'vod'
OTHER = 'other'
DASHED_LABEL = '---'
DUMMY_ATTRIBUTE_SPLIT_ON = "_"
RATING = 'rating'
CATEGORY_EN = 'category_en'
SUBCATEGORY_EN = 'subcategory_en'
TAGS = 'tags'
CHANNEL_LIVE = 'channel_live'
CATCHUP = 'catchup'
DEFAULT_FEATURE_VALUES = {
    COUNTRY_ID: DEFAULT_NAN, REGION_NAME: UNKNOWN_LABEL,
    DEVOPS: UNKNOWN_LABEL, CATEGORY_EN: DEFAULT_NAN,
    SUBCATEGORY_EN: DEFAULT_NAN, ATTRIBUTE1: DEFAULT_NAN,
    RATING: DEFAULT_NAN
    }
LOCAL_CONNECTION_URI = "ws://localhost:8182/gremlin"
USER_LABEL = "user"
CSV_EXTENSION = ".csv"
