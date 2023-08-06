import typing

from .tableconfig import TableConfig

class CellInfo:
    def __init__(self, **kwargs):
        self.width: int = kwargs['width']
        self.height: int = kwargs['height']
        self.has_border: bool = kwargs['has_border']

        self.fnc_draw_cell: typing.Callable[
            [int],
            typing.Generator[str, None, None]
        ] = kwargs['drawcell']
        self.fnc_getval: typing.Callable[
            [Table, int, int, int],
            str
        ] = kwargs.get('getval', lambda t, v, c, r: v)

class Table:
    def __init__(self, cell_info: CellInfo):
        self.data: typing.List[typing.List[int]] = [[]]
        self.cell_info: CellInfo = cell_info

        self.table_name: typing.Optional[str] = None

        self.label_sep: str = '  '
        self.label_lpad: bool = False
        self.label_left: bool = False

        self._row_labels: typing.Union[
            typing.List[str],
            typing.Dict[int, str]
        ] = {}
        self._longest_label_length: int = 0

        self.config: TableConfig = TableConfig()

    @property
    def row_labels(self):
        return self._row_labels

    @row_labels.setter
    def row_labels(self,
            value: typing.Union[
                typing.List[str],
                typing.Dict[int, str]
            ]
        ):
        self._row_labels = value
        self._longest_label_length = self._get_longest_label_length()

    @property
    def longest_label_length(self):
        return self._longest_label_length

    def draw_table(self) -> str:
        return Table.draw_tables([self])

    def draw_table_iter(self) -> typing.Generator[str, None, None]:
        row_idx = 0
        for row in self.data:
            for char_row in self.draw_row_iter(row, row_idx):
                yield char_row
            row_idx += 1

    def draw_row(self, row: typing.List[int], row_idx: int = -1) -> str:
        return '\n'.join(self.draw_row_iter(row, row_idx))

    def draw_row_iter(self, row: typing.List[int], row_idx: int = -1):
        gen_list = [ self.draw_cell_iter(row[i], col=i, row=row_idx) for i in range(len(row)) ]
        if len(gen_list) == 0:
            return

        has_labels = self.has_labels()
        did_label = False
        first_line = True

        for _ in range(self.cell_info.height):
            chars = ''
            first_col = True

            for gen in gen_list:
                res = next(gen)
                if not first_col and self.cell_info.has_border:
                    chars += res[1:]
                else:
                    chars += res

                first_col = False

            if row_idx != -1 and has_labels:
                label = self.get_row_label(row_idx) if not did_label else ''

                if not did_label and self.cell_info.has_border and first_line:
                    label = ''
                    did_label = False
                else:
                    did_label = True

                if label is None:
                    label = ''

                if self.label_left:
                    padding = ' ' * (self.longest_label_length - len(label))
                    padding_after = ' ' * (
                        self.max_length() - self.longest_label_length - len(self.label_sep) - self.row_cell_length()
                    )

                    if self.label_lpad:
                        label = padding + label
                    else:
                        label += padding

                    chars = '%s%s%s%s' % (label, self.label_sep, chars, padding_after)
                else:
                    padding = ' ' * (
                        self.max_length() - self.row_cell_length() - len(self.label_sep) - len(label)
                    )

                    if self.label_lpad:
                        label = padding + label
                    else:
                        label += padding

                    chars += self.label_sep + label
            else:
                chars += ' ' * (self.max_length() - self.row_cell_length())

            yield chars
            first_line = False

    def draw_cell_iter(self, val: int, col: int = -1, row: int = -1) -> typing.Generator[str, None, None]:
        for res in self.cell_info.fnc_draw_cell(
            self.cell_info.fnc_getval(
                self,
                val,
                col=col,
                row=row
            )
        ):
            yield res

    def get_row_label(self, row_idx: int) -> typing.Optional[str]:
        if isinstance(self.row_labels, dict):
            return self.row_labels.get(row_idx)

        if len(self.row_labels) <= row_idx:
            return None
        return self.row_labels[row_idx]

    def max_length(self, include_table_name: bool = True, include_label: bool = True) -> int:
        length = self.row_cell_length()
        name_longer = include_table_name and self.table_name is not None and len(self.table_name) > length

        if name_longer:
            length = len(self.table_name)

        if include_label and self.has_labels():
            if self.label_left:
                length += len(self.label_sep) + self.longest_label_length
            else:
                if name_longer:
                    diff = self.row_cell_length() + len(self.label_sep) + self.longest_label_length - length
                    if diff > 0:
                        length += diff
                else:
                    length += len(self.label_sep) + self.longest_label_length
        return length

    def _get_longest_label_length(self) -> int:
        val_list = self.row_labels
        if isinstance(self.row_labels, dict):
            val_list = self.row_labels.values()

        length = 0
        for val in val_list:
            if len(val) > length:
                length = len(val)
        return length

    def has_labels(self) -> bool:
        return len(self.row_labels) != 0

    def row_cell_length(self) -> int:
        length = self.col_count() * self.cell_info.width
        if self.cell_info.has_border:
            length -= self.col_count() - 1
        return length

    def row_count(self) -> int:
        return len(self.data)

    def col_count(self) -> int:
        if self.row_count() == 0:
            return 0
        return len(self.data[0])

    @staticmethod
    def draw_tables(tablelist: typing.List['Table'], **kwargs) -> str:
        tbl_count = len(tablelist)
        spacing = kwargs.get('spacing', 2)
        row_counter = [ 0 ] * tbl_count
        lne_counter = [ 0 ] * tbl_count
        result = ''
        last_result_len = 0

        gen_list = []
        gen_done: typing.Set[int] = set()
        has_table_name = False

        for tbl in tablelist:
            gen_list.append(tbl.draw_table_iter())
            if tbl.table_name is not None:
                has_table_name = True

        if has_table_name:
            for idx in range(tbl_count):
                tbl = tablelist[idx]
                if tbl.table_name is None:
                    result += ' ' * tbl.max_length()
                    if idx != tbl_count - 1:
                        result += ' ' * spacing
                    continue

                name = ''
                if tbl.has_labels() and tbl.label_left:
                    name += ' ' * (tbl.longest_label_length + len(tbl.label_sep))
                name += tbl.table_name
                name += ' ' * (tbl.max_length() - len(name))

                result += name
                if idx != tbl_count - 1:
                    result += ' ' * spacing
            result += '\n'

        while len(gen_done) != tbl_count:
            draws_done = 0

            for gidx in range(tbl_count): # pylint: disable=consider-using-enumerate
                gen = gen_list[gidx]
                tbl = tablelist[gidx]
                do_draw = gidx not in gen_done

                if do_draw:
                    while True:
                        try:
                            res = next(gen)
                            lne_counter[gidx] += 1
                            if lne_counter[gidx] == tbl.cell_info.height:
                                row_counter[gidx] += 1
                                lne_counter[gidx] = 0

                                if tbl.cell_info.has_border and tbl.row_count() != row_counter[gidx]:
                                    do_draw = True
                                    continue
                        except StopIteration:
                            do_draw = False
                            gen_done.add(gidx)
                        break

                if do_draw:
                    result += res
                    draws_done += 1
                else:
                    result += ' ' * tbl.max_length()

                if gidx != tbl_count - 1:
                    result += ' ' * spacing

            if draws_done == 0:
                result = result[:last_result_len]
            else:
                result += '\n'
            last_result_len = len(result)

        return result
