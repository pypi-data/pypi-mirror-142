from dataclasses import (
    dataclass,
)
from fa_purity.frozen import (
    FrozenDict,
)
from fa_purity.result import (
    Result,
    ResultE,
)
from redshift_client.column import (
    Column,
    ColumnId,
)
from typing import (
    Callable,
    FrozenSet,
)


@dataclass(frozen=True)
class _Table:
    columns: FrozenDict[ColumnId, Column]
    primary_keys: FrozenSet[ColumnId]


@dataclass(frozen=True)
class Table(_Table):
    def __init__(self, obj: _Table) -> None:
        super().__init__(obj.columns, obj.primary_keys)


def new(
    columns: FrozenDict[ColumnId, Column],
    primary_keys: FrozenSet[ColumnId],
) -> ResultE[Table]:
    in_columns: Callable[[ColumnId], bool] = lambda k: k in columns
    if all(map(in_columns, primary_keys)):
        draft = _Table(columns, primary_keys)
        return Result.success(Table(draft))
    return Result.failure(Exception("All primary keys must be in columns"))
