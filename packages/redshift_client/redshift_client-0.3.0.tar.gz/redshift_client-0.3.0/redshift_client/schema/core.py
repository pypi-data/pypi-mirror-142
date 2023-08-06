from dataclasses import (
    dataclass,
)
from fa_purity.frozen import (
    FrozenDict,
)
from redshift_client.id_objs import (
    TableId,
)
from redshift_client.table.core import (
    Table,
)


@dataclass(frozen=True)
class Schema:
    tables: FrozenDict[TableId, Table]
