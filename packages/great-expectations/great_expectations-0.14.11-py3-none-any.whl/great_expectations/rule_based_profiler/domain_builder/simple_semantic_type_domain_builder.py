from typing import Any, Dict, List, Optional, Union

import great_expectations.exceptions as ge_exceptions
from great_expectations.core.batch import Batch, BatchRequest, RuntimeBatchRequest
from great_expectations.core.profiler_types_mapping import ProfilerTypeMapping
from great_expectations.execution_engine.execution_engine import MetricDomainTypes
from great_expectations.rule_based_profiler.domain_builder import ColumnDomainBuilder
from great_expectations.rule_based_profiler.helpers.util import (
    get_parameter_value_and_validate_return_type,
)
from great_expectations.rule_based_profiler.types import (
    Domain,
    InferredSemanticDomainType,
    ParameterContainer,
    SemanticDomainTypes,
)
from great_expectations.validator.metric_configuration import MetricConfiguration


class SimpleSemanticTypeColumnDomainBuilder(ColumnDomainBuilder):
    """
    This DomainBuilder utilizes a "best-effort" semantic interpretation of ("storage") columns of a table.
    """

    def __init__(
        self,
        batch_list: Optional[List[Batch]] = None,
        batch_request: Optional[Union[BatchRequest, RuntimeBatchRequest, dict]] = None,
        data_context: Optional["DataContext"] = None,  # noqa: F821
        include_column_names: Optional[Union[str, Optional[List[str]]]] = None,
        exclude_column_names: Optional[Union[str, Optional[List[str]]]] = None,
        semantic_types: Optional[
            Union[str, SemanticDomainTypes, List[Union[str, SemanticDomainTypes]]]
        ] = None,
    ):
        """
        Args:
            batch_list: explicitly specified Batch objects for use in DomainBuilder
            batch_request: specified in DomainBuilder configuration to get Batch objects for domain computation.
            data_context: DataContext
            include_column_names: Explicitly specified desired columns (if None, it is computed based on active Batch).
            exclude_column_names: If provided, these columns are pre-filtered and excluded from consideration.
            semantic_types: single or multiple type specifications using SemanticDomainTypes (or string equivalents)
        """
        super().__init__(
            batch_list=batch_list,
            batch_request=batch_request,
            data_context=data_context,
            include_column_names=include_column_names,
            exclude_column_names=exclude_column_names,
        )

        if semantic_types is None:
            semantic_types = []

        self._semantic_types = semantic_types

    @property
    def domain_type(self) -> Union[str, MetricDomainTypes]:
        return MetricDomainTypes.COLUMN

    @property
    def semantic_types(
        self,
    ) -> Optional[
        Union[str, SemanticDomainTypes, List[Union[str, SemanticDomainTypes]]]
    ]:
        return self._semantic_types

    def _get_domains(
        self,
        variables: Optional[ParameterContainer] = None,
    ) -> List[Domain]:
        """
        Find the semantic column type for each column and return all domains matching the specified type or types.
        """
        table_column_names: List[str] = self.get_effective_column_names(
            variables=variables,
        )

        # Obtain semantic_types from "rule state" (i.e., variables and parameters); from instance variable otherwise.
        semantic_types: Union[
            str, SemanticDomainTypes, List[Union[str, SemanticDomainTypes]]
        ] = get_parameter_value_and_validate_return_type(
            domain=None,
            parameter_reference=self.semantic_types,
            expected_return_type=None,
            variables=variables,
            parameters=None,
        )

        semantic_types: List[
            SemanticDomainTypes
        ] = _parse_semantic_domain_type_argument(semantic_types=semantic_types)

        batch_ids: List[str] = self.get_batch_ids(variables=variables)
        column_types_dict_list: List[Dict[str, Any]] = self.get_validator(
            variables=variables
        ).get_metric(
            metric=MetricConfiguration(
                metric_name="table.column_types",
                metric_domain_kwargs={
                    "batch_id": batch_ids[-1],  # active_batch_id
                },
                metric_value_kwargs={
                    "include_nested": True,
                },
                metric_dependencies=None,
            )
        )

        column_name: str

        # A semantic type is distinguished from the structured column type;
        # An example structured column type would be "integer".  The inferred semantic type would be "id".
        table_column_name_to_inferred_semantic_domain_type_mapping: Dict[
            str, SemanticDomainTypes
        ] = {
            column_name: self.infer_semantic_domain_type_from_table_column_type(
                column_types_dict_list=column_types_dict_list,
                column_name=column_name,
            ).semantic_domain_type
            for column_name in table_column_names
        }
        candidate_column_names: List[str] = list(
            filter(
                lambda candidate_column_name: table_column_name_to_inferred_semantic_domain_type_mapping[
                    candidate_column_name
                ]
                in semantic_types,
                table_column_names,
            )
        )

        domains: List[Domain] = [
            Domain(
                domain_type=self.domain_type,
                domain_kwargs={
                    "column": column_name,
                },
                details={
                    "inferred_semantic_domain_type": table_column_name_to_inferred_semantic_domain_type_mapping[
                        column_name
                    ],
                },
            )
            for column_name in candidate_column_names
        ]

        return domains

    # This method (default implementation) can be overwritten (with different implementation mechanisms) by subclasses.
    # noinspection PyMethodMayBeStatic
    def infer_semantic_domain_type_from_table_column_type(
        self,
        column_types_dict_list: List[Dict[str, Any]],
        column_name: str,
    ) -> InferredSemanticDomainType:
        # Note: As of Python 3.8, specifying argument type in Lambda functions is not supported by Lambda syntax.
        column_types_dict_list = list(
            filter(
                lambda column_type_dict: column_name == column_type_dict["name"],
                column_types_dict_list,
            )
        )
        if len(column_types_dict_list) != 1:
            raise ge_exceptions.ProfilerExecutionError(
                message=f"""Error: {len(column_types_dict_list)} columns were found while obtaining semantic type \
information.  Please ensure that the specified column name refers to exactly one column.
"""
            )

        column_type: str = str(column_types_dict_list[0]["type"]).upper()

        semantic_column_type: SemanticDomainTypes
        if column_type in (
            {type_name.upper() for type_name in ProfilerTypeMapping.INT_TYPE_NAMES}
            | {type_name.upper() for type_name in ProfilerTypeMapping.FLOAT_TYPE_NAMES}
        ):
            semantic_column_type = SemanticDomainTypes.NUMERIC
        elif column_type in {
            type_name.upper() for type_name in ProfilerTypeMapping.STRING_TYPE_NAMES
        }:
            semantic_column_type = SemanticDomainTypes.TEXT
        elif column_type in {
            type_name.upper() for type_name in ProfilerTypeMapping.BOOLEAN_TYPE_NAMES
        }:
            semantic_column_type = SemanticDomainTypes.LOGIC
        elif column_type in {
            type_name.upper() for type_name in ProfilerTypeMapping.DATETIME_TYPE_NAMES
        }:
            semantic_column_type = SemanticDomainTypes.DATETIME
        elif column_type in {
            type_name.upper() for type_name in ProfilerTypeMapping.BINARY_TYPE_NAMES
        }:
            semantic_column_type = SemanticDomainTypes.BINARY
        elif column_type in {
            type_name.upper() for type_name in ProfilerTypeMapping.CURRENCY_TYPE_NAMES
        }:
            semantic_column_type = SemanticDomainTypes.CURRENCY
        elif column_type in {
            type_name.upper() for type_name in ProfilerTypeMapping.IDENTIFIER_TYPE_NAMES
        }:
            semantic_column_type = SemanticDomainTypes.IDENTIFIER
        elif column_type in (
            {
                type_name.upper()
                for type_name in ProfilerTypeMapping.MISCELLANEOUS_TYPE_NAMES
            }
            | {type_name.upper() for type_name in ProfilerTypeMapping.RECORD_TYPE_NAMES}
        ):
            semantic_column_type = SemanticDomainTypes.MISCELLANEOUS
        else:
            semantic_column_type = SemanticDomainTypes.UNKNOWN

        inferred_semantic_column_type: InferredSemanticDomainType = (
            InferredSemanticDomainType(
                semantic_domain_type=semantic_column_type,
                details={
                    "algorithm_type": "deterministic",
                    "mechanism": "lookup_table",
                    "source": "great_expectations.profile.base.ProfilerTypeMapping",
                },
            )
        )

        return inferred_semantic_column_type


def _parse_semantic_domain_type_argument(
    semantic_types: Optional[
        Union[str, SemanticDomainTypes, List[Union[str, SemanticDomainTypes]]]
    ] = None
) -> List[SemanticDomainTypes]:
    if semantic_types is None:
        return []

    semantic_type: Union[str, SemanticDomainTypes]
    if isinstance(semantic_types, str):
        semantic_types = semantic_types.upper()
        return [
            SemanticDomainTypes[semantic_type] for semantic_type in [semantic_types]
        ]
    if isinstance(semantic_types, SemanticDomainTypes):
        return [semantic_type for semantic_type in [semantic_types]]
    elif isinstance(semantic_types, list):
        if all([isinstance(semantic_type, str) for semantic_type in semantic_types]):
            semantic_types = [semantic_type.upper() for semantic_type in semantic_types]
            return [
                SemanticDomainTypes[semantic_type] for semantic_type in semantic_types
            ]
        elif all(
            [
                isinstance(semantic_type, SemanticDomainTypes)
                for semantic_type in semantic_types
            ]
        ):
            return [semantic_type for semantic_type in semantic_types]
        else:
            raise ValueError(
                "All elements in semantic_types list must be either of str or SemanticDomainTypes type."
            )
    else:
        raise ValueError("Unrecognized semantic_types directive.")
