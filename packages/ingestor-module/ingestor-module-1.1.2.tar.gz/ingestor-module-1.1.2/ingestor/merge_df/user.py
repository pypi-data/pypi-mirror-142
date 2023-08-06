import pandas as pd
from pandas import DataFrame
from ingestor.merge_df.common import UserBehaviourUtils, UserProfileUtils
from ingestor.user_profile.constants import CUSTOMER_ID


class FinalDfUserController:
    @staticmethod
    def build_user_behaviour_final_df(video_measure_data=None,
                                      df_content_having_tags=None,
                                      df_content_having_director=None,
                                      df_content_having_actor=None,
                                      df_content=None) -> DataFrame:
        video_measure_df = DataFrame()
        result_not_in_df = DataFrame()
        if not pd.isna(video_measure_data[CUSTOMER_ID][0]):
            video_measure_df = UserBehaviourUtils.fetch_prepare_customer_id(
                video_measure_df, video_measure_data)
            video_measure_df = UserBehaviourUtils.fetch_prepare_created_on(
                video_measure_df, video_measure_data)
            video_measure_df = UserBehaviourUtils.fetch_prepare_country_id(
                video_measure_df, video_measure_data)
            video_measure_df =UserBehaviourUtils.fetch_prepare_region_name(
                video_measure_df,video_measure_data)
            video_measure_df = UserBehaviourUtils.fetch_prepare_devops(
                video_measure_df, video_measure_data)
            video_measure_df = UserBehaviourUtils.fetch_prepare_attribute(
                video_measure_df, video_measure_data)
            video_measure_df = UserBehaviourUtils.fetch_prepare_video_id(
                video_measure_df, video_measure_data)
            video_measure_df = UserBehaviourUtils.fetch_prepare_category1(
                video_measure_df, video_measure_data)
            video_measure_df = UserBehaviourUtils.fetch_prepare_category2(
                video_measure_df, video_measure_data)
            video_measure_df = UserBehaviourUtils.fetch_prepare_duration(
                video_measure_df, video_measure_data)
            video_measure_df, result_not_in_df = UserBehaviourUtils.fetch_prepare_tags_df(
                video_measure_df, df_content_having_tags, video_measure_data, result_not_in_df)
            video_measure_df, result_not_in_df = UserBehaviourUtils.fetch_prepare_actor_df(
                video_measure_df, df_content_having_actor, video_measure_data, result_not_in_df)
            video_measure_df, result_not_in_df = UserBehaviourUtils.fetch_prepare_director_df(
                video_measure_df, df_content_having_director, video_measure_data, result_not_in_df)
            video_measure_df, result_not_in_df = UserBehaviourUtils.fetch_prepare_content_df(
                video_measure_df, df_content, video_measure_data, result_not_in_df)

        return video_measure_df, result_not_in_df

    @staticmethod
    def build_user_profile_final_df(customer=None, df_user_pay_tv=None):
        customer_df = DataFrame()
        result_not_in_df = DataFrame()
        if not pd.isna(customer[CUSTOMER_ID][0]):
            customer_df = UserProfileUtils.fetch_prepare_customer_id(
                customer_df, customer)
            customer_df = UserProfileUtils.fetch_prepare_birthday_id(
                customer_df, customer)
            customer_df = UserProfileUtils.fetch_prepare_gender(
                customer_df, customer)
            customer_df = UserProfileUtils.fetch_prepare_created_on(
                customer_df, customer)
            customer_df = UserProfileUtils.fetch_prepare_modified_on(
                customer_df, customer)
            customer_df = UserProfileUtils.fetch_prepare_ud_key(
                customer_df, customer)
            customer_df, result_not_in_df = UserProfileUtils.fetch_user_pay_tv(
                customer_df, df_user_pay_tv,
                customer, result_not_in_df)

        return customer_df, result_not_in_df


def get_final_df_user_behaviour(df_video_measure_data=None,
                                df_content_having_tags=None,
                                df_content_having_director=None,
                                df_content_having_actor=None,
                                df_content=None):
    final_df_user_behaviour = DataFrame()
    result_not_correct_df = DataFrame()

    for row, val in df_video_measure_data.iterrows():
        df_new = DataFrame()
        values_to_add = val.to_dict()
        row_to_add = pd.Series(values_to_add)
        new_df = df_new.append(row_to_add, ignore_index=True)
        result_df, result_not_df = FinalDfUserController.build_user_behaviour_final_df(
            new_df,
            df_content_having_tags,
            df_content_having_director,
            df_content_having_actor,
            df_content)

        final_df_user_behaviour = pd.concat([final_df_user_behaviour, result_df], axis=0)
        result_not_correct_df = pd.concat([result_not_correct_df, result_not_df], axis=0)

    return final_df_user_behaviour, result_not_correct_df


def get_final_df_user_profile(df_customer=None, df_user_pay_tv=None):
    final_df_user_profile = DataFrame()
    result_not_correct_df = DataFrame()

    for row, val in df_customer.iterrows():
        df_new = DataFrame()
        values_to_add = val.to_dict()
        row_to_add = pd.Series(values_to_add)
        new_df = df_new.append(row_to_add, ignore_index=True)
        result_df, result_not_df = FinalDfUserController.build_user_profile_final_df(
            new_df,
            df_user_pay_tv,
        )

        final_df_user_profile = pd.concat([final_df_user_profile, result_df], axis=0)
        result_not_correct_df = pd.concat([result_not_correct_df, result_not_df], axis=0)

    return final_df_user_profile, result_not_correct_df

