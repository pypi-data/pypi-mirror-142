from typing import Iterable, Optional
from explainaboard.info import SysOutputInfo, BucketPerformance, Performance, Table
from explainaboard.utils import analysis
from explainaboard.builders import ExplainaboardBuilder
from explainaboard.utils.eval_bucket import *  # noqa
from explainaboard.utils.feature_funcs import get_similarity_by_sacrebleu
from tqdm import tqdm

"""TODO
"""


class HellaswagExplainaboardBuilder(ExplainaboardBuilder):
    """
    Input: System Output file List[dict];  Metadata info
    Output: Analysis
    """

    def __init__(
        self,
        info: SysOutputInfo,
        system_output_object: Iterable[dict],
        feature_table: Optional[Table] = {},
        user_defined_feature_config = None
    ):
        super().__init__(info, system_output_object, feature_table, user_defined_feature_config)


    # --- Feature functions accessible by ExplainaboardBuilder._get_feature_func()
    def _get_similarity_ctx_true_answer(self, existing_features: dict):
        true_label = int(existing_features["true_label"])
        true_answer = existing_features["endings"][true_label]

        return get_similarity_by_sacrebleu(existing_features["ctx"], true_answer)

    # define function for incomplete features
    def _get_ctx_length(self, existing_features: dict):
        return len(existing_features["ctx"].split(" "))

    # define function for incomplete features
    def _get_ctx_a_length_divided_b(self, existing_features: dict):
        return (
            len(existing_features["ctx_a"].split(" "))
            * 1.0
            / len(existing_features["ctx_b"].split(" "))
        )

    def _get_true_answer_length(self, existing_features: dict):
        true_label = int(existing_features["true_label"])
        true_answer = existing_features["endings"][true_label]
        return len(true_answer.split(" "))

    def _get_activity_label(self, existing_feature: dict):
        return str(existing_feature["activity_label"])

    def _get_ind(self, existing_feature: dict):
        return float(existing_feature["ind"])
    # --- End feature functions

    def _complete_feature(self):
        """
        This function is used to calculate features used for bucekting, such as sentence_length
        :param feature_table_iterator:
        :return:
        """
        # Get names of bucketing features
        # print(f"self._info.features.get_bucket_features()\n {self._info.features.get_bucket_features()}")
        bucket_features = self._info.features.get_bucket_features()
        for _id, dict_sysout in tqdm(
            enumerate(self._system_output), desc="featurizing"
        ):
            # Get values of bucketing features
            for bucket_feature in bucket_features:
                feature_value = eval(
                    HellaswagExplainaboardBuilder.get_bucket_feature_value(
                        bucket_feature
                    )
                )(dict_sysout)
                dict_sysout[bucket_feature] = feature_value
            # if self._data is None:
            #     self._data = {}
            self._data[_id] = dict_sysout
            yield _id, dict_sysout

    def get_overall_performance(self):
        predicted_labels, true_labels = [], []

        for _id, feature_table in self._data.items():

            predicted_labels.append(feature_table["predicted_label"])
            true_labels.append(feature_table["true_label"])

        for metric_name in self._info.metric_names:
            one_metric = eval(metric_name)(
                true_labels=true_labels,
                predicted_labels=predicted_labels,
                is_print_confidence_interval=self._info.results.is_print_confidence_interval,
            )
            overall_value_json = one_metric.evaluate()

            overall_value = overall_value_json["value"]
            confidence_score_low = overall_value_json["confidence_score_low"]
            confidence_score_up = overall_value_json["confidence_score_up"]
            overall_performance = Performance(
                metric_name=metric_name,
                value=float(format(overall_value, '.4g')),
                confidence_score_low=float(format(confidence_score_low, '.4g')),
                confidence_score_up=float(format(confidence_score_up, '.4g')),
            )
            if self._info.results.overall is None:
                self._info.results.overall = {}
                self._info.results.overall[metric_name] = overall_performance
            else:
                self._info.results.overall[metric_name] = overall_performance

    def _bucketing_samples(self, sysout_iterator):

        sample_address = ""
        feature_to_sample_address_to_value = {}

        # Preparation for bucketing
        for _id, dict_sysout in sysout_iterator:

            sample_address = str(_id)  # this could be abstracted later
            for feature_name in self._info.features.get_bucket_features():
                if feature_name not in feature_to_sample_address_to_value.keys():
                    feature_to_sample_address_to_value[feature_name] = {}
                else:
                    feature_to_sample_address_to_value[feature_name][
                        sample_address
                    ] = dict_sysout[feature_name]

        # Bucketing
        for feature_name in tqdm(
            self._info.features.get_bucket_features(), desc="bucketing"
        ):

            # print(f"Feature Name: {feature_name}\n"
            #       f"Bucket Hyper:\n function_name: {self._info.features[feature_name].bucket_info._method} \n"
            #       f"bucket_number: {self._info.features[feature_name].bucket_info._number}\n"
            #       f"bucket_setting: {self._info.features[feature_name].bucket_info._setting}\n")

            self._samples_over_bucket[feature_name] = eval(
                self._info.features[feature_name].bucket_info._method
            )(
                dict_obj=feature_to_sample_address_to_value[feature_name],
                bucket_number=self._info.features[feature_name].bucket_info._number,
                bucket_setting=self._info.features[feature_name].bucket_info._setting,
            )

            # print(f"self._samples_over_bucket.keys():\n{self._samples_over_bucket.keys()}")

            # evaluating bucket: get bucket performance
            self._performances_over_bucket[feature_name] = self.get_bucket_performance(
                feature_name
            )

    def get_bucket_performance(self, feature_name: str):
        """
        This function defines how to get bucket-level performance w.r.t a given feature (e.g., sentence length)
        :param feature_name: the name of a feature, e.g., sentence length
        :return: bucket_name_to_performance: a dictionary that maps bucket names to bucket performance
        """

        bucket_name_to_performance = {}
        for bucket_interval, sample_ids in self._samples_over_bucket[
            feature_name
        ].items():

            bucket_true_labels = []
            bucket_predicted_labels = []
            bucket_cases = []

            for sample_id in sample_ids:

                true_label = self._data[int(sample_id)]["true_label"]
                predicted_label = self._data[int(sample_id)]["predicted_label"]
                s_id = self._data[int(sample_id)]["id"]

                # get a bucket of true/predicted labels
                bucket_true_labels.append(true_label)
                bucket_predicted_labels.append(predicted_label)
                # get a bucket of cases (e.g., errors)
                if self._info.results.is_print_case:
                    if true_label != predicted_label:
                        bucket_case = str(s_id)
                        bucket_cases.append(bucket_case)

            bucket_name_to_performance[bucket_interval] = []
            for metric_name in self._info.metric_names:

                one_metric = eval(metric_name)(
                    true_labels=bucket_true_labels,
                    predicted_labels=bucket_predicted_labels,
                    is_print_confidence_interval=self._info.results.is_print_confidence_interval,
                )
                bucket_value_json = one_metric.evaluate()

                bucket_value = bucket_value_json["value"]
                confidence_score_low = bucket_value_json["confidence_score_low"]
                confidence_score_up = bucket_value_json["confidence_score_up"]

                # print(f"name:\t {one_metric._name} \n"
                #       f"value:\t {bucket_value}\n"
                #       f"confidence low\t {confidence_score_low}\n"
                #       f"confidence up \t {confidence_score_up}\n"
                #       f"---------------------------------")

                bucket_performance = BucketPerformance(
                    bucket_name=bucket_interval,
                    metric_name=metric_name,
                    value=format(bucket_value, '.4g'),
                    confidence_score_low=format(confidence_score_low, '.4g'),
                    confidence_score_up=format(confidence_score_up, '.4g'),
                    n_samples=len(bucket_true_labels),
                    bucket_samples=bucket_cases,
                )

                bucket_name_to_performance[bucket_interval].append(bucket_performance)

        return sort_dict(bucket_name_to_performance)  # noqa

    def _generate_report(self):
        dict_fine_grained = {}
        for feature_name, metadata in self._performances_over_bucket.items():
            dict_fine_grained[feature_name] = []
            for bucket_name, bucket_performance in metadata.items():
                bucket_name = analysis.beautify_interval(bucket_name)

                # instantiation
                dict_fine_grained[feature_name].append(bucket_performance)

        self._info.results.fine_grained = dict_fine_grained

    def _print_bucket_info(self):
        for feature_name in self._performances_over_bucket.keys():
            print_dict(  # noqa
                self._performances_over_bucket[feature_name], feature_name
            )

    def run(self) -> SysOutputInfo:
        eb_generator = self._complete_feature()
        self._bucketing_samples(eb_generator)
        self.get_overall_performance()
        self._print_bucket_info()
        self._generate_report()
        return self._info
