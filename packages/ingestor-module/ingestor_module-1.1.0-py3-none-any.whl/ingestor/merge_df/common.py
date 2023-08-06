import ast

import pandas as pd

from ingestor.common.constants import CONTENT_ID, YEAR, DURATION_MINUTE, CATEGORY_ID, \
    ACTOR_ID, HOMEPAGE_ID, CONTENT_CORE_ID, SEASON_ID_LABEL, SUBCATEGORY_ID, CONTENT_BUNDLE_ID, CATEGORY, SUBCATEGORY, \
    COUNTRY, ACTORS, TAGS, HOMEPAGE, \
    CONTENT_CORE, PACKAGES, PRODUCTS, PACKAGE_ID, PRODUCT_ID, TAGS_ID
from ingestor.user_profile.constants import COUNTRY_ID


class CommonUtils:

    @staticmethod
    def fetch_prepare_content_id(content_df, df):
        content_df.rename(columns={"id_content": "content_id"}, inplace=True)
        content_df[CONTENT_ID] = [int(df["id_content"].loc[0])]
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
                                       right_on="Content_id_content", how="left")
        if len(merged_with_country) > 0:
            content_df = pd.merge(content_df, df_c, left_on=CONTENT_ID,
                                  right_on="Content_id_content", how="left").drop("Content_id_content", axis=1)
            content_df.rename(columns={'Country_id_country': 'country'}, inplace=True)

            country = []
            for cc in content_df['country'].values:
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
                                                        how="left")
            package_df = pd.merge(content_bundle_having_content_df, df_package_having_content_bundle,
                                  left_on=CONTENT_BUNDLE_ID, right_on=CONTENT_BUNDLE_ID,
                                  how="left")
            packages = []
            for content_package_id in package_df['package_id'].values:
                if not pd.isna(content_package_id):
                    content_package = {PACKAGE_ID: int(content_package_id)}
                    packages.append(content_package)

            content_df[PACKAGES] = [packages]

            product_df = pd.merge(package_df, df_product_having_package,
                                  left_on='package_id', right_on='package_id',
                                  how="left")

            products = []
            for content_product_id in product_df['product_id'].values:
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
                                               how="left")

            content_cores = []
            for index, row in content_core_content_df.iterrows():
                if not pd.isna(row[CONTENT_CORE_ID]):
                    if not pd.isna(row['season_id']):
                        content_core = {CONTENT_CORE_ID: int(row[CONTENT_CORE_ID]),
                                        SEASON_ID_LABEL: int(row['season_id'])}
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
            homepage_content_df = pd.merge(content_df, df_homepage, left_on=CONTENT_ID, right_on=CONTENT_ID, how="left")

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
            tags_content_df = pd.merge(content_df, df_tag, left_on=CONTENT_ID, right_on=CONTENT_ID, how="left")

            tags = []
            for tag_id in tags_content_df['tags_id'].values:
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
            actor_content_df = pd.merge(content_df, df_actor, left_on=CONTENT_ID, right_on=CONTENT_ID, how="left")

            actors = []
            for actor_id in actor_content_df['actor_id'].values:
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
