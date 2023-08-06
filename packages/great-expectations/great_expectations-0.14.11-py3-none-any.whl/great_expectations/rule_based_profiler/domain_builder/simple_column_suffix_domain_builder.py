from typing import Iterable, List, Optional, Union

from great_expectations.core.batch import Batch, BatchRequest, RuntimeBatchRequest
from great_expectations.execution_engine.execution_engine import MetricDomainTypes
from great_expectations.rule_based_profiler.domain_builder import ColumnDomainBuilder
from great_expectations.rule_based_profiler.helpers.util import (
    build_simple_domains_from_column_names,
    get_parameter_value_and_validate_return_type,
)
from great_expectations.rule_based_profiler.types import Domain, ParameterContainer


class SimpleColumnSuffixDomainBuilder(ColumnDomainBuilder):
    """
    This DomainBuilder uses a column suffix to identify domains.
    """

    def __init__(
        self,
        batch_list: Optional[List[Batch]] = None,
        batch_request: Optional[Union[BatchRequest, RuntimeBatchRequest, dict]] = None,
        data_context: Optional["DataContext"] = None,  # noqa: F821
        include_column_names: Optional[Union[str, Optional[List[str]]]] = None,
        exclude_column_names: Optional[Union[str, Optional[List[str]]]] = None,
        column_name_suffixes: Optional[Union[str, Iterable, List[str]]] = None,
    ):
        """
        Args:
            batch_list: explicitly specified Batch objects for use in DomainBuilder
            batch_request: specified in DomainBuilder configuration to get Batch objects for domain computation.
            data_context: DataContext
            include_column_names: Explicitly specified desired columns (if None, it is computed based on active Batch).
            exclude_column_names: If provided, these columns are pre-filtered and excluded from consideration.
        """
        super().__init__(
            batch_list=batch_list,
            batch_request=batch_request,
            data_context=data_context,
            include_column_names=include_column_names,
            exclude_column_names=exclude_column_names,
        )

        if column_name_suffixes is None:
            column_name_suffixes = []

        self._column_name_suffixes = column_name_suffixes

    @property
    def domain_type(self) -> Union[str, MetricDomainTypes]:
        return MetricDomainTypes.COLUMN

    @property
    def column_name_suffixes(
        self,
    ) -> Optional[Union[str, Iterable, List[str]]]:
        return self._column_name_suffixes

    def _get_domains(
        self,
        variables: Optional[ParameterContainer] = None,
    ) -> List[Domain]:
        """
        Find the column suffix for each column and return all domains matching the specified suffix.
        """
        table_column_names: List[str] = self.get_effective_column_names(
            variables=variables,
        )

        # Obtain column_name_suffixes from "rule state" (i.e., variables and parameters); from instance variable otherwise.
        column_name_suffixes: Union[
            str, Iterable, List[str]
        ] = get_parameter_value_and_validate_return_type(
            domain=None,
            parameter_reference=self.column_name_suffixes,
            expected_return_type=None,
            variables=variables,
            parameters=None,
        )

        if isinstance(column_name_suffixes, str):
            column_name_suffixes = [column_name_suffixes]
        else:
            if not isinstance(column_name_suffixes, (Iterable, list)):
                raise ValueError(
                    "Unrecognized column_name_suffixes directive -- must be a list or a string."
                )

        candidate_column_names: List[str] = list(
            filter(
                lambda candidate_column_name: candidate_column_name.endswith(
                    tuple(column_name_suffixes)
                ),
                table_column_names,
            )
        )

        return build_simple_domains_from_column_names(
            column_names=candidate_column_names,
            domain_type=self.domain_type,
        )
