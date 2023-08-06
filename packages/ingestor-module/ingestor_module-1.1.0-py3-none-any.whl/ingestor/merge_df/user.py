from pandas import DataFrame
from numpy import unique
import gc
from ingestor.common.constants import INNER, CATEGORY1, ID, \
    ACTOR_NAME, DIRECTOR_NAME, CONTENT_ID, NAME, \
    TAGS_ID, TAGS_NAME, CONTENT_ID_CONTENT, CLUSTER_CATEGORY_ID, \
    ACTOR_ID, ID_ACTOR, ID_CONTENT, ID_TAGS, CATEGORY2, \
    VIDEO_ID1, PAY_TV_PROVIDER_ID, UD_KEY


class FeatureMergeController:
    @staticmethod
    def group_records(
            records_df: DataFrame,
            by_attr: str,
            get_attr: str,
            reset_attr: str
    ):
        return records_df.groupby(by_attr)[get_attr].apply(
            (lambda element: list(unique(
                element)))).reset_index(name=reset_attr)

    @staticmethod
    def merge_records(
            data1: DataFrame,
            data2: DataFrame,
            join_method: str,
            left_attr: str,
            right_attr: str,
            to_drop: [],
    ):
        data1 = data1.merge(
            data2,
            how=join_method,
            left_on=left_attr,
            right_on=right_attr)
        return data1.drop(columns=to_drop)

    def get_merged_ubd_records(self,
                               video_measure_data=None,
                               category_data=None,
                               subcategory_data=None,
                               content_having_actor_data=None,
                               content_having_director_data=None,
                               actor_data=None,
                               content_data=None,
                               content_having_tags_data=None,
                               tags_data=None,
                               cluster_category_having_content_data=None
                               ):
        """
        :param video_measure_data:
        :param category_data:
        :param subcategory_data:
        :param content_having_actor_data:
        :param content_having_director_data:
        :param actor_data:
        :param content_data:
        :param content_having_tags_data:
        :param tags_data:
        :param cluster_category_having_content_data:
        :return: dataframe
        """
        try:
            merged_df = self.merge_records(
                video_measure_data,
                category_data,
                join_method=INNER,
                left_attr=CATEGORY1,
                right_attr=ID,
                to_drop=[ID, CATEGORY1]
            )

            merged_df = self.merge_records(
                merged_df,
                subcategory_data,
                join_method=INNER,
                left_attr=CATEGORY2,
                right_attr=ID,
                to_drop=[ID, CATEGORY2]
            )

            actor_df = self.merge_records(
                content_having_actor_data,
                actor_data,
                join_method=INNER,
                left_attr=ACTOR_ID,
                right_attr=ID_ACTOR,
                to_drop=[]
            )

            group_actor_df = self.group_records(
                actor_df,
                by_attr=CONTENT_ID_CONTENT,
                get_attr=NAME,
                reset_attr=ACTOR_NAME
            )

            merged_df = self.merge_records(
                merged_df,
                group_actor_df,
                join_method=INNER,
                left_attr=VIDEO_ID1,
                right_attr=CONTENT_ID_CONTENT,
                to_drop=CONTENT_ID_CONTENT
            )

            director_df = self.merge_records(
                content_having_director_data,
                actor_data,
                join_method=INNER,
                left_attr=ACTOR_ID,
                right_attr=ID_ACTOR,
                to_drop=[]
            )

            group_director_df = self.group_records(
                director_df,
                by_attr=CONTENT_ID_CONTENT,
                get_attr=NAME,
                reset_attr=DIRECTOR_NAME
            )

            merged_df = self.merge_records(
                merged_df,
                group_director_df,
                join_method=INNER,
                left_attr=VIDEO_ID1,
                right_attr=CONTENT_ID_CONTENT,
                to_drop=CONTENT_ID_CONTENT
            )

            merged_df = self.merge_records(
                merged_df,
                content_data,
                join_method=INNER,
                left_attr=VIDEO_ID1,
                right_attr=ID_CONTENT,
                to_drop=ID_CONTENT)

            merged_tag = self.merge_records(
                content_having_tags_data,
                tags_data,
                join_method=INNER,
                left_attr=TAGS_ID,
                right_attr=ID_TAGS,
                to_drop=[])

            group_tag = self.group_records(
                merged_tag,
                by_attr=CONTENT_ID,
                get_attr=NAME,
                reset_attr=TAGS_NAME
            )

            merged_df = self.merge_records(
                merged_df,
                group_tag,
                join_method=INNER,
                left_attr=VIDEO_ID1,
                right_attr=CONTENT_ID,
                to_drop=CONTENT_ID
            )

            group_cluster_df = self.group_records(
                cluster_category_having_content_data,
                by_attr=CONTENT_ID,
                get_attr=CLUSTER_CATEGORY_ID,
                reset_attr=CLUSTER_CATEGORY_ID)

            final_df = self.merge_records(
                merged_df,
                group_cluster_df,
                join_method=INNER,
                left_attr=VIDEO_ID1,
                right_attr=CONTENT_ID,
                to_drop=CONTENT_ID)

            return final_df
        except Exception as e:
            print("Error in merging dataframe", str(e))

        finally:
            del content_having_actor_data
            del category_data, video_measure_data
            del subcategory_data
            del actor_df
            del group_actor_df
            del content_having_director_data
            del content_having_tags_data
            del group_director_df
            del content_data
            del group_tag
            del cluster_category_having_content_data
            del director_df
            del merged_df
            collect = gc.collect()
            print("Garbage collector: collected %d objects." % collect)

    def get_merged_user_vdb_records(self,
                                    customer_data=None,
                                    user_pay_tv_data=None,
                                    pay_tv_provider_data=None
                                    ):
        """
            :param customer_data:
            :param user_pay_tv_data:
            :param pay_tv_provider_data:
            :return:dataframe
            """
        try:
            merged_df = self.merge_records(
                user_pay_tv_data,
                pay_tv_provider_data,
                join_method=INNER,
                left_attr=PAY_TV_PROVIDER_ID,
                right_attr=ID,
                to_drop=[ID])

            final_user_profile_df = self.merge_records(
                customer_data,
                merged_df,
                join_method=INNER,
                left_attr=UD_KEY,
                right_attr=UD_KEY,
                to_drop=[UD_KEY, PAY_TV_PROVIDER_ID])

            return final_user_profile_df
        except Exception as e:
            print("Error in merging dataframe", str(e))
        finally:
            del user_pay_tv_data, pay_tv_provider_data,
            del customer_data, merged_df
            collect = gc.collect()
            print("Garbage collector: collected %d objects." % collect)
