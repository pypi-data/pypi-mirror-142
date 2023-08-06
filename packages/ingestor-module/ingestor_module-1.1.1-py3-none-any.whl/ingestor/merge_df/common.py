import ast

import pandas as pd
from ingestor.common.constants import CONTENT_ID, YEAR, DURATION_MINUTE, CATEGORY_ID, \
    HOMEPAGE_ID, CONTENT_CORE_ID, SEASON_ID_LABEL, SUBCATEGORY_ID, \
    CONTENT_BUNDLE_ID, CATEGORY, SUBCATEGORY, \
    COUNTRY, ACTORS, TAGS, HOMEPAGE, \
    CONTENT_CORE, PACKAGES, PRODUCTS, PACKAGE_ID, PRODUCT_ID, TAG_ID, SEASON_ID, ID_CONTENT
from ingestor.user_profile.constants import CUSTOMER_ID, CREATED_ON, \
    COUNTRY_ID, REGION_NAME, DEVOPS, VIDEO_ID1, CATEGORY1, CATEGORY2, DURATION, \
    CONTENT_ID, RATING, BIRTHDAY, GENDER, UD_KEY, CUSTOMER_CREATED_ON, \
    CUSTOMER_MODIFIED_ON, ATTRIBUTE1, DIRECTOR_ID, LEFT, DIRECTORS, ACTOR_ID, TAGS_ID, ACTORS, PAYTVPROVIDER_ID


class CommonUtils:

    @staticmethod
    def fetch_prepare_content_id(content_df, df):
        content_df.rename(columns={ID_CONTENT: CONTENT_ID}, inplace=True)
        content_df[CONTENT_ID] = [int(df[ID_CONTENT].loc[0])]
        return content_df

    @staticmethod
    def fetch_prepare_year(content_df, df):
        if not pd.isna(df[YEAR].loc[0]):
            content_df[YEAR] = [int(df[YEAR].loc[0])]
        return content_df

    @staticmethod
    def fetch_prepare_duration(content_df, df):
        if not pd.isna(df[DURATION_MINUTE].loc[0]):
            content_df[DURATION_MINUTE] = int(df[DURATION_MINUTE].loc[0])
        return content_df

    @staticmethod
    def fetch_prepare_country(content_df, df_c):
        merged_with_country = pd.merge(content_df, df_c, left_on=CONTENT_ID,
                                       right_on=CONTENT_ID, how=LEFT)
        if len(merged_with_country) > 0:
            content_df = pd.merge(content_df, df_c, left_on=CONTENT_ID,
                                  right_on=CONTENT_ID, how=LEFT)
            country = []
            for cc in content_df[COUNTRY_ID].values:
                if not pd.isna(cc):
                    c = {COUNTRY_ID: int(cc)}
                    country.append(c)

            content_df[COUNTRY] = [country]

        return content_df

    @staticmethod
    def fetch_prepare_product_package(content_df, df, df_content_bundle_having_content,
                                      df_package_having_content_bundle, df_product_having_package, result_not_in_df):
        try:
            content_bundle_having_content_df = pd.merge(content_df, df_content_bundle_having_content,
                                                        left_on=CONTENT_ID,
                                                        right_on=CONTENT_ID,
                                                        how=LEFT)
            package_df = pd.merge(content_bundle_having_content_df, df_package_having_content_bundle,
                                  left_on=CONTENT_BUNDLE_ID, right_on=CONTENT_BUNDLE_ID,
                                  how=LEFT)
            packages = []
            for content_package_id in package_df[PACKAGE_ID].values:
                if not pd.isna(content_package_id):
                    content_package = {PACKAGE_ID: int(content_package_id)}
                    packages.append(content_package)

            content_df[PACKAGES] = [packages]

            product_df = pd.merge(package_df, df_product_having_package,
                                  left_on=PACKAGE_ID, right_on=PACKAGE_ID,
                                  how=LEFT)

            products = []
            for content_product_id in product_df[PRODUCT_ID].values:
                if not pd.isna(content_product_id):
                    content_product = {PRODUCT_ID: int(content_product_id)}
                    products.append(content_product)

            content_df[PRODUCTS] = [products]
        except Exception:
            result_not_in_df = df
        return content_df, result_not_in_df

    @staticmethod
    def fetch_prepare_content_cores(content_df, df, df_content_core, result_not_in_df):
        try:
            content_core_content_df = pd.merge(content_df, df_content_core, left_on=CONTENT_ID, right_on=CONTENT_ID,
                                               how=LEFT)

            content_cores = []
            for index, row in content_core_content_df.iterrows():
                if not pd.isna(row[CONTENT_CORE_ID]):
                    if not pd.isna(row[SEASON_ID]):
                        content_core = {CONTENT_CORE_ID: int(row[CONTENT_CORE_ID]),
                                        SEASON_ID_LABEL: int(row[SEASON_ID])}
                        content_cores.append(content_core)
                    else:
                        content_core = {CONTENT_CORE_ID: int(row[CONTENT_CORE_ID])}
                        content_cores.append(content_core)

            content_df[CONTENT_CORE] = [content_cores]
        except Exception:
            result_not_in_df = df
        return content_df, result_not_in_df

    @staticmethod
    def fetch_prepare_homepages(content_df, df, df_homepage, result_not_in_df):
        try:
            homepage_content_df = pd.merge(content_df, df_homepage, left_on=CONTENT_ID, right_on=CONTENT_ID, how=LEFT)

            homepages = []
            for homepage_id in homepage_content_df[HOMEPAGE_ID].values:
                if not pd.isna(homepage_id):
                    homepage = {HOMEPAGE_ID: int(homepage_id)}
                    homepages.append(homepage)

            content_df[HOMEPAGE] = [homepages]

        except Exception:
            result_not_in_df = df
        return content_df, result_not_in_df

    @staticmethod
    def fetch_prepare_tags(content_df, df, df_tag, result_not_in_df):
        try:
            tags_content_df = pd.merge(content_df, df_tag, left_on=CONTENT_ID, right_on=CONTENT_ID, how=LEFT)

            tags = []
            for tag_id in tags_content_df[TAG_ID].values:
                if not pd.isna(tag_id):
                    tag = {TAGS_ID: int(tag_id)}
                    tags.append(tag)

            content_df[TAGS] = [tags]
        except Exception:
            result_not_in_df = df
        return content_df, result_not_in_df

    @staticmethod
    def fetch_prepare_actors(content_df, df, df_actor, result_not_in_df):
        try:
            actor_content_df = pd.merge(content_df, df_actor, left_on=CONTENT_ID, right_on=CONTENT_ID, how=LEFT)

            actors = []
            for actor_id in actor_content_df[ACTOR_ID].values:
                if not pd.isna(actor_id):
                    actor = {ACTOR_ID: int(actor_id)}
                    actors.append(actor)

            content_df[ACTORS] = [actors]
        except Exception:
            result_not_in_df = df
        return content_df, result_not_in_df

    @staticmethod
    def fetch_prepare_subcategory(content_df, df, result_not_in_df):
        try:
            list_sub_category_ids = []
            if not pd.isna(df[SUBCATEGORY_ID].loc[0]):
                dict_sub_category1 = {SUBCATEGORY_ID: int(df[SUBCATEGORY_ID].loc[0])}
                list_sub_category_ids.append(dict_sub_category1)

            content_df[SUBCATEGORY] = [list_sub_category_ids]

        except Exception:
            result_not_in_df = df

        return content_df, result_not_in_df

    @staticmethod
    def fetch_prepare_category(content_df, df, result_not_in_df):
        try:
            list_category_ids = []
            if not pd.isna(df[CATEGORY_ID].loc[0]):
                dict_category1 = {CATEGORY_ID: int(df[CATEGORY_ID].loc[0])}
                list_category_ids.append(dict_category1)

            content_df[CATEGORY] = [list_category_ids]
            content_df[CATEGORY] = ast.literal_eval(content_df[CATEGORY])
        except Exception:
            result_not_in_df = df
        return content_df, result_not_in_df


class UserBehaviourUtils:

    @staticmethod
    def fetch_prepare_customer_id(video_measure_df, vm_df):
        video_measure_df[CUSTOMER_ID] = [str(vm_df[CUSTOMER_ID].loc[0])]
        return video_measure_df

    @staticmethod
    def fetch_prepare_created_on(video_measure_df, vm_df):
        video_measure_df[CREATED_ON] = [pd.to_datetime(vm_df[CREATED_ON].loc[0], unit='s')]

        return video_measure_df

    @staticmethod
    def fetch_prepare_country_id(video_measure_df, vm_df):
        video_measure_df[COUNTRY_ID] = [str(vm_df[COUNTRY_ID].loc[0])]
        return video_measure_df

    @staticmethod
    def fetch_prepare_region_name(video_measure_df, vm_df):
        video_measure_df[REGION_NAME] = [str(vm_df[REGION_NAME].loc[0])]
        return video_measure_df

    @staticmethod
    def fetch_prepare_devops(video_measure_df, vm_df):
        video_measure_df[DEVOPS] = [str(vm_df[DEVOPS].loc[0])]
        return video_measure_df

    @staticmethod
    def fetch_prepare_attribute(video_measure_df, vm_df):
        video_measure_df[ATTRIBUTE1] = [str(vm_df[ATTRIBUTE1].loc[0])]
        return video_measure_df

    @staticmethod
    def fetch_prepare_video_id(video_measure_df, vm_df):
        video_measure_df[VIDEO_ID1] = [int(vm_df[VIDEO_ID1].loc[0])]
        return video_measure_df

    @staticmethod
    def fetch_prepare_category1(video_measure_df, vm_df):
        if not pd.isna(vm_df[CATEGORY1].loc[0]):
            category = []
            for category_id in vm_df[CATEGORY1]:
                if not pd.isna(category_id):
                    category_id = {CATEGORY_ID: int(category_id)}
                    category.append(category_id)

            video_measure_df[CATEGORY] = [category]

        return video_measure_df

    @staticmethod
    def fetch_prepare_category2(video_measure_df, vm_df):
        if not pd.isna(vm_df[CATEGORY2].loc[0]):
            subcategory = []
            for subcategory_id in vm_df[CATEGORY2]:
                if not pd.isna(subcategory_id):
                    subcategory_id = {SUBCATEGORY_ID: int(subcategory_id)}
                    subcategory.append(subcategory_id)

            video_measure_df[SUBCATEGORY] = [subcategory]

        return video_measure_df

    @staticmethod
    def fetch_prepare_duration(video_measure_df, vm_df):
        if not pd.isna(vm_df[DURATION].loc[0]) and vm_df[DURATION].values is not None:
            video_measure_df[DURATION] = [int(vm_df[DURATION].loc[0])]
        return video_measure_df

    @staticmethod
    def fetch_prepare_tags_df(video_measure_df, df_content_having_tag, vm_df, result_not_in_df):
        try:
            tags_content_df = pd.merge(video_measure_df, df_content_having_tag, left_on=VIDEO_ID1, right_on=CONTENT_ID,
                                       how=LEFT)

            tags = []
            for tag_id in tags_content_df[TAGS_ID].values:
                if not pd.isna(tag_id):
                    tag = {TAGS_ID: int(tag_id)}
                    tags.append(tag)

            video_measure_df[TAGS] = [tags]
        except Exception:
            result_not_in_df = vm_df
        return video_measure_df, result_not_in_df

    @staticmethod
    def fetch_prepare_actor_df(video_measure_df, df_content_having_actor, vm_df, result_not_in_df):
        try:
            actor_content_df = pd.merge(video_measure_df, df_content_having_actor, left_on=VIDEO_ID1,
                                        right_on=CONTENT_ID, how=LEFT)

            actors = []
            for actor_id in actor_content_df[ACTOR_ID].values:
                if not pd.isna(actor_id):
                    actor = {ACTOR_ID: int(actor_id)}
                    actors.append(actor)

            video_measure_df[ACTORS] = [actors]
        except Exception:
            result_not_in_df = vm_df
        return video_measure_df, result_not_in_df

    @staticmethod
    def fetch_prepare_director_df(video_measure_df, df_content_having_director, vm_df, result_not_in_df):
        try:
            df_content_having_director = df_content_having_director.rename({ACTOR_ID: DIRECTOR_ID}, axis=1)
            director_content_df = pd.merge(video_measure_df, df_content_having_director, left_on=VIDEO_ID1,
                                           right_on=CONTENT_ID, how=LEFT)

            directors = []
            for director_id in director_content_df[DIRECTOR_ID].values:
                if not pd.isna(director_id):
                    director = {DIRECTOR_ID: int(director_id)}
                    directors.append(director)

            video_measure_df[DIRECTORS] = [directors]
        except Exception:
            result_not_in_df = vm_df
        return video_measure_df, result_not_in_df

    @staticmethod
    def fetch_prepare_content_df(video_measure_df, df_content, vm_df, result_not_in_df):
        try:
            df_content = df_content[[CONTENT_ID, RATING]]
            video_measure_df = pd.merge(video_measure_df, df_content, left_on=VIDEO_ID1,
                                        right_on=CONTENT_ID, how=LEFT)

            video_measure_df = video_measure_df.drop(CONTENT_ID, axis=1)
        except Exception:
            result_not_in_df = vm_df
        return video_measure_df, result_not_in_df


class UserProfileUtils:

    @staticmethod
    def fetch_prepare_customer_id(customer_df, cm_df):

        customer_df[CUSTOMER_ID] = [str(cm_df[CUSTOMER_ID].loc[0])]
        return customer_df

    @staticmethod
    def fetch_prepare_birthday_id(customer_df, cm_df):

        customer_df[BIRTHDAY] = [pd.to_datetime(cm_df[BIRTHDAY].loc[0])]
        return customer_df

    @staticmethod
    def fetch_prepare_gender(customer_df, cm_df):
        customer_df[GENDER] = [str(cm_df[GENDER].loc[0])]
        return customer_df

    @staticmethod
    def fetch_prepare_created_on(customer_df, cm_df):
        customer_df[CUSTOMER_CREATED_ON] = [pd.to_datetime(cm_df[CUSTOMER_CREATED_ON].loc[0])]
        print(type(customer_df[CUSTOMER_CREATED_ON].loc[0]))
        return customer_df

    @staticmethod
    def fetch_prepare_modified_on(customer_df, cm_df):
        customer_df[CUSTOMER_MODIFIED_ON] = [pd.to_datetime(cm_df[CUSTOMER_MODIFIED_ON].loc[0])]
        print(type(customer_df[CUSTOMER_MODIFIED_ON].loc[0]))
        return customer_df

    @staticmethod
    def fetch_prepare_ud_key(customer_df, cm_df):
        customer_df[UD_KEY] = [int(cm_df[UD_KEY].loc[0])]
        return customer_df

    @staticmethod
    def fetch_user_pay_tv(customer_df, df_user_pay_tv, cm_df, result_not_in_df):
        try:
            customer_df = pd.merge(customer_df, df_user_pay_tv, left_on=UD_KEY,
                                   right_on=UD_KEY, how=LEFT)

            customer_df = customer_df.drop(UD_KEY, axis=1)
            if not pd.isna(customer_df[PAYTVPROVIDER_ID].loc[0]):
                    customer_df[PAYTVPROVIDER_ID] = [int(customer_df[PAYTVPROVIDER_ID].loc[0])]

        except Exception :
            result_not_in_df = cm_df
        return customer_df, result_not_in_df
