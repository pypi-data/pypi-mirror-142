from typing import Optional

from great_expectations.core.usage_statistics.anonymizers.anonymizer import Anonymizer
from great_expectations.core.usage_statistics.util import (
    aggregate_all_core_expectation_types,
)


class ExpectationSuiteAnonymizer(Anonymizer):
    def __init__(self, salt=None):
        super().__init__(salt=salt)
        self._ge_expectation_types = aggregate_all_core_expectation_types()

    def anonymize_expectation_suite_info(self, expectation_suite):
        anonymized_info_dict = {}
        anonymized_expectation_counts = list()

        expectations = expectation_suite.expectations
        expectation_types = [
            expectation.expectation_type for expectation in expectations
        ]
        for expectation_type in set(expectation_types):
            expectation_info = {"count": expectation_types.count(expectation_type)}
            self.anonymize_expectation(expectation_type, expectation_info)
            anonymized_expectation_counts.append(expectation_info)

        anonymized_info_dict["anonymized_name"] = self.anonymize(
            expectation_suite.expectation_suite_name
        )
        anonymized_info_dict["expectation_count"] = len(expectations)
        anonymized_info_dict[
            "anonymized_expectation_counts"
        ] = anonymized_expectation_counts

        return anonymized_info_dict

    def anonymize_expectation(
        self, expectation_type: Optional[str], info_dict: dict
    ) -> None:
        if expectation_type in self._ge_expectation_types:
            info_dict["expectation_type"] = expectation_type
        else:
            info_dict["anonymized_expectation_type"] = self.anonymize(expectation_type)
