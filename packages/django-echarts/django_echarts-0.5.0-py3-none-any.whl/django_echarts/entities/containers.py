import re
from typing import List, Union

from .chart_widgets import ChartInfo, WidgetGetterMixin, NamedCharts, merge_js_dependencies


class LayoutOpts:
    """
    Recommend layout: l8 l9 r8 r9 t6 t12 b6 b12 f4 f6 f12 a s8 s9
    """
    TOTAL_COLS = 12
    __slots__ = ['chart_pos', 'chart_span', 'info_span', 'start', 'end']

    # l=left,r=right,s=stripped,t=top,b=bottom,f=full
    _defaults = {'l': 8, 'r': 8, 's': 8, 't': 6, 'b': 6, 'f': 12}

    _rm = re.compile(r'([lrtbfsa])(([1-9]|(1[12]))?)')

    def __init__(self, chart_pos: str = 'r', chart_span: int = 8, info_span: int = 4,
                 chart_num: int = 1):
        if len(chart_pos) > 1:
            chart_pos = chart_pos[0]
        self.chart_pos = chart_pos
        self.chart_span = chart_span
        if chart_pos in 'lras':
            if chart_num == 1 and chart_span + info_span < LayoutOpts.TOTAL_COLS:
                info_span = LayoutOpts.TOTAL_COLS - chart_span
            elif chart_num > 1:
                info_span = 12
        self.info_span = info_span
        # start/end for info
        self.start = chart_pos in 'rb'
        self.end = chart_pos in 'lt'

    @classmethod
    def from_label(cls, label: str):
        m = LayoutOpts._rm.match(label)
        if m:
            pos, cols = m.group(1), m.group(2)
            if cols is None or cols == '':
                cols = LayoutOpts._defaults.get(pos, 8)
            else:
                cols = int(cols)
            return cls(pos, cols)
        else:
            raise ValueError(f'This layout can not be parsed: {label}')

    def stripped_layout(self) -> 'LayoutOpts':
        if self.chart_pos == 'r':
            return LayoutOpts(chart_pos='l', chart_span=self.chart_span)
        elif self.chart_pos == 'l':
            return LayoutOpts(chart_pos='r', chart_span=self.chart_span)
        else:
            return self

    def __str__(self):
        return f'<LOptions:{self.chart_pos},{self.chart_span}, {self.info_span}>'


class RowWidget(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = kwargs.get('title')

    def add_widget(self, widget, span):
        self.append((widget, span))


class WidgetCollection:
    widget_type = 'Collection'

    def __init__(self, name: str, title: str = None, layout: Union[str, LayoutOpts] = 'a'):
        self.name = name
        self.title = title
        self._user_defined_layout = LayoutOpts.from_label(layout)
        # [[is_chart, layout, name1, name2, name3,...]]
        self._ref_config_list = []  # type: List

        self._packed_matrix = []  # type: List[RowWidget]
        self._charts = []
        self._row_no = 0

    def start_(self):
        self._packed_matrix = []
        self._row_no = 0
        return self

    def add_chart_widget(self, chart_name: str, layout: str = 'l8'):
        self._ref_config_list.append([True, layout, chart_name])
        return self

    def add_html_widget(self, widget_names: List, layout: str = 'f'):
        self._ref_config_list.append([False, layout, *widget_names])

    def auto_mount(self, widget_container: WidgetGetterMixin):
        for is_chart, layout_str, *names in self._ref_config_list:
            if is_chart:
                chart_name = names[0]
                chart_obj, _, info = widget_container.resolve_chart_widget(chart_name)
                self.pack_chart_widget(chart_obj, info, row_no=self._row_no)
            else:
                widget_list = [widget_container.resolve_html_widget(name) for name in names]
                self.pack_html_widget(widget_list)

    def pack_chart_widget(self, chart_obj, info: ChartInfo, ignore_ref: bool = True, layout: str = 'l8',
                          row_no: int = 0):
        self._charts.append(chart_obj)
        if isinstance(chart_obj, NamedCharts):
            if chart_obj.has_ref and ignore_ref:
                return
                # raise TypeError(f'{info.name} :ChartCollection can not add a NamedCharts with is_combine=True')
            chart_widget = list(chart_obj)
        else:
            chart_widget = [chart_obj]
        row_widget = RowWidget(title=info.title)
        r_layout = self.compute_layout(LayoutOpts.from_label(layout))
        if r_layout.start:
            row_widget.add_widget(info, r_layout.info_span)
        for widget in chart_widget:
            row_widget.add_widget(widget, r_layout.chart_span)
        if r_layout.end:
            row_widget.add_widget(info, r_layout.info_span)
        self._packed_matrix.append(row_widget)
        self._row_no += 1

    def pack_html_widget(self, widget_list: List, layout: str = 'f', row_no: int = 0):
        span = int(12 / len(widget_list))
        row_widget = RowWidget()
        for widget in widget_list:
            row_widget.add_widget(widget, span)
        self._packed_matrix.append(row_widget)
        self._row_no += 1

    def compute_layout(self, row_layout: LayoutOpts):
        if self._user_defined_layout.chart_pos == 'a':
            return row_layout
        elif self._user_defined_layout.chart_pos == 's':
            if self._row_no % 2 == 1:
                return row_layout.stripped_layout()
            else:
                return row_layout
        else:
            return row_layout

    @property
    def packed_matrix(self):
        return self._packed_matrix

    @property
    def charts(self):
        return self._charts

    @property
    def js_dependencies(self):
        return merge_js_dependencies(*self.charts)
