from typing import Generic, Optional, TypeVar, Union, List

from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import transform

from spark_auto_mapper.data_types.array_base import AutoMapperArrayLikeBase
from spark_auto_mapper.data_types.data_type_base import AutoMapperDataTypeBase
from spark_auto_mapper.data_types.mixins.has_children_mixin import HasChildrenMixin
from spark_auto_mapper.type_definitions.wrapper_types import (
    AutoMapperAnyDataType,
    AutoMapperColumnOrColumnLikeType,
)

_TAutoMapperDataType = TypeVar("_TAutoMapperDataType", bound=AutoMapperAnyDataType)


class AutoMapperTransformDataType(
    AutoMapperArrayLikeBase, HasChildrenMixin, Generic[_TAutoMapperDataType]
):
    def __init__(
        self,
        column: Union[AutoMapperDataTypeBase, AutoMapperColumnOrColumnLikeType],
        value: _TAutoMapperDataType,
    ) -> None:
        super().__init__()

        self.column: Union[
            AutoMapperDataTypeBase, AutoMapperColumnOrColumnLikeType
        ] = column
        self.value: _TAutoMapperDataType = value
        # always include null properties in a transform operation
        self.include_null_properties(include_null_properties=True)

    def include_null_properties(self, include_null_properties: bool) -> None:
        if isinstance(self.value, AutoMapperDataTypeBase):
            self.value.include_null_properties(
                include_null_properties=include_null_properties
            )

    def get_column_spec(
        self, source_df: Optional[DataFrame], current_column: Optional[Column]
    ) -> Column:
        column_spec: Column = self.column.get_column_spec(
            source_df=source_df, current_column=current_column
        )

        if not isinstance(self.value, AutoMapperDataTypeBase):
            return column_spec

        def get_column_spec_for_column(x: Column) -> Column:
            if not isinstance(self.value, AutoMapperDataTypeBase):
                return x
            value_get_column_spec: Column = self.value.get_column_spec(
                source_df=source_df, current_column=x
            )
            return value_get_column_spec

        return transform(column_spec, get_column_spec_for_column)

    @property
    def children(self) -> Union[AutoMapperDataTypeBase, List[AutoMapperDataTypeBase]]:
        return self.value  # type: ignore

    def get_fields(self) -> List[str]:
        return HasChildrenMixin.get_fields(self)

    def add_missing_values_and_order(self, expected_keys: List[str]) -> None:
        HasChildrenMixin.add_missing_values_and_order(self, expected_keys=expected_keys)
