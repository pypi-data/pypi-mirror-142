import pandas as pd
from pandas import DataFrame

from ingestor.content_profile.network.content import ContentNetworkGenerator
from ingestor.merge_df.common import CommonUtils


class FinalDfController:

    @staticmethod
    def build_content_profile_final_df(df, df_c, df_actor, df_tag, df_homepage, df_content_core,
                                       df_content_bundle_having_content, df_package_having_content_bundle,
                                       df_product_having_package) -> DataFrame:
        content_df = DataFrame()
        result_not_in_df = DataFrame()
        if not pd.isna(df["id_content"][0]):
            content_df = CommonUtils.fetch_prepare_content_id(content_df, df)

            content_df = CommonUtils.fetch_prepare_year(content_df, df)

            content_df = CommonUtils.fetch_prepare_duration(content_df, df)

            content_df = CommonUtils.fetch_prepare_country(content_df, df_c)

            content_df, result_not_in_df = CommonUtils.fetch_prepare_category(content_df, df, result_not_in_df)

            content_df, result_not_in_df = CommonUtils.fetch_prepare_subcategory(content_df, df, result_not_in_df)

            content_df, result_not_in_df = CommonUtils.fetch_prepare_actors(content_df, df, df_actor,
                                                                            result_not_in_df)

            content_df, result_not_in_df = CommonUtils.fetch_prepare_tags(content_df, df, df_tag,
                                                                          result_not_in_df)

            content_df, result_not_in_df = CommonUtils.fetch_prepare_homepages(content_df, df, df_homepage,
                                                                               result_not_in_df)

            content_df, result_not_in_df = CommonUtils.fetch_prepare_content_cores(content_df, df,
                                                                                   df_content_core,
                                                                                   result_not_in_df)

            content_df, result_not_in_df = CommonUtils.fetch_prepare_product_package(content_df, df,
                                                                                     df_content_bundle_having_content,
                                                                                     df_package_having_content_bundle,
                                                                                     df_product_having_package,
                                                                                     result_not_in_df)

        return content_df, result_not_in_df


def get_final_df_content_profile(df, df_c, df_actor,
                                 df_tag, df_homepage,
                                 df_content_core,
                                 df_product_having_package,
                                 df_content_having_bundle,
                                 df_package_having_content_bundle):
    final_df_content_profile = DataFrame()
    result_not_correct_df = DataFrame()
    cls = ContentNetworkGenerator.from_connection_uri("ws://localhost:8182/gremlin")

    for row, val in df.iterrows():
        print("dumping content profile for {0}".format(val))
        df_new = DataFrame()
        values_to_add = val.to_dict()
        row_to_add = pd.Series(values_to_add)
        new_df = df_new.append(row_to_add, ignore_index=True)
        result_df, result_not_df = FinalDfController.build_content_profile_final_df(new_df, df_c, df_actor, df_tag,
                                                                                    df_homepage,
                                                                                    df_content_core,
                                                                                    df_content_having_bundle,
                                                                                    df_package_having_content_bundle,
                                                                                    df_product_having_package)

        cls.content_creator_updater_network(payload=result_df)
        print("Successfully dumped content profile for {0}".format(val))

        final_df_content_profile = pd.concat([final_df_content_profile, result_df], axis=0)
        result_not_correct_df = pd.concat([result_not_correct_df, result_not_df], axis=0)

    return final_df_content_profile, result_not_correct_df
