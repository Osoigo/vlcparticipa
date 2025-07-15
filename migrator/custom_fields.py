# taken from https://github.com/tortoise/tortoise-orm/issues/569
import datetime
from typing import Any, Optional, Type, Union

from tortoise import fields
from tortoise.contrib.postgres.fields import TSVectorField
from tortoise.models import Model


class DecimalField(fields.Field[str], str):
    SQL_TYPE = "DECIMAL"

    def to_python_value(self, value: Any) -> Optional[int]:
        self.validate(value)
        if value is not None:
            value = str(value)
        return value

    def to_db_value(self, value: Any, instance: Type[Model] | Model) -> Optional[str]:
        if value is not None:
            value = str(value)
        self.validate(value)
        return value


class NaiveDatetimeField(fields.DatetimeField):
    skip_to_python_if_native = True

    class _db_postgres:  # noqa
        SQL_TYPE = "TIMESTAMP"

    def _to_naive(self, value: datetime.datetime) -> datetime.datetime:
        if value.tzinfo is None:
            return value

        value = value.astimezone(datetime.timezone.utc)

        return value.replace(tzinfo=None)

    def to_python_value(self, value: Any) -> Optional[datetime.datetime]:
        value = super().to_python_value(value)

        if value is None:
            return value

        return self._to_naive(value)

    def to_db_value(
        self,
        value: Optional[datetime.datetime],
        instance: "Union[Type[Model], Model]",
    ) -> Optional[datetime.datetime]:
        value = super().to_db_value(value, instance)

        if value is None:
            return value

        return self._to_naive(value)


class TSVectorField(TSVectorField):
    field_type = str


__all__ = [
    "DecimalField",
    "NaiveDatetimeField",
    "TSVectorField",
]
