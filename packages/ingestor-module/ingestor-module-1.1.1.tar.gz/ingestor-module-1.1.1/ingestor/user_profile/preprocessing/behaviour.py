import ast
from pandas import DataFrame, to_datetime
from ingestor.common.preprocessing_utils import Utils
from ingestor.user_profile.constants import ATTRIBUTE1, CUSTOMER_ID, DURATION, \
    REDUNDANT_FEATURES, DASHED_LABEL, OTHER, DEFAULT_FEATURE_VALUES, \
    CATCHUP, CHANNEL_LIVE, VOD, CREATED_ON


class PreprocessBehaviour:

    def remove_feature(
            self,
            data: DataFrame
    ) -> DataFrame:
        """
        This function drops unnecessary columns from the dataset

        :param data: dataframe object pandas
        :return: preprocessed dataframe object pandas
        """
        data = data.drop(REDUNDANT_FEATURES, axis=1)

        return data

    def preprocess_created_on(
            self,
            data: DataFrame
    ) -> DataFrame:
        """
        This function converts created on timestamp to datetime
        :param data:
        :return:
        """
        data[CREATED_ON] = to_datetime(data[CREATED_ON], unit='s')

        return data

    def attribute1_substitution(
            self,
            data: DataFrame
    ) -> DataFrame:
        """
        This function substitutes the values in attribute1 with custom values

        :param data: dataframe object pandas
        :return: dataframe object pandas
        """
        data.loc[data[ATTRIBUTE1].str.contains(
            CHANNEL_LIVE, case=False),
            ATTRIBUTE1] = CHANNEL_LIVE
        data.loc[data[ATTRIBUTE1].str.contains(
            CATCHUP, case=False),
            ATTRIBUTE1] = CATCHUP
        data.loc[data[ATTRIBUTE1].str.contains(
            VOD, case=False),
            ATTRIBUTE1] = VOD

        return data

    def preprocess_features(
            self,
            data: DataFrame,
    ) -> DataFrame:
        """
        This function takes dict of features and their default nan values
        and calls fillna_and_cast_lower function for preprocessing.

        :param data: dataframe object pandas
        :return: dataframe object pandas
        """
        data[CUSTOMER_ID] = data[CUSTOMER_ID].astype(str)
        for feature, value in DEFAULT_FEATURE_VALUES.items():
            data = Utils.fillna_and_cast_lower(
                data,
                feature=feature,
                default_val=value
            )

        return data

    def preprocess_and_explode(
            self,
            data: DataFrame,
            feature: str
    ) -> DataFrame:
        """
        This function transforms each element of a
        list-like to a row, replicating index values.

        :param data: dataframe object pandas
        :param feature: feature name
        :return: preprocessed dataframe object pandas
        """
        data = data[[CUSTOMER_ID, DURATION, feature]]
        data[feature] = data[feature].fillna("[]")
        data[feature] = data[feature].str.lower()
        data[feature] = data[feature].str.replace(DASHED_LABEL, OTHER)
        data[feature] = data[feature].str.strip()
        data[feature] = data[feature].apply(ast.literal_eval)

        return data.explode(feature).fillna('')

    def controller(
            self,
            data: DataFrame,
            to_explode: bool,
            feature=''
    ) -> DataFrame:
        """
        The driver function for PreprocessBehaviour class.
        Returns preprocessed dataframe and also breaks the list of
        feature values specified in feature parameter in
        multiple rows, as per the value specified for 'to_explode'

        :param data: dataframe object pandas
        :param to_explode: if True, split the list of value into
        separate records, ignore otherwise
        :param feature: feature to be exploded
        :return: preprocessed dataframe object pandas
        """

        data = self.remove_feature(data)

        if to_explode:
            data = self.preprocess_and_explode(data, feature)

        else:
            data = self.preprocess_created_on(data)
            data = self.attribute1_substitution(data)
            data = self.preprocess_features(data)

        return data
