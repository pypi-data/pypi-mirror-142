from cement.core.output import OutputHandler
from rich.console import Console
from rich.table import Table


class AkinonOutputHandler(OutputHandler):
    class Meta:
        label = 'akinon_output_handler'

    def _render_data(self, rows: dict, headers: dict):
        table = Table()
        for column_header in headers.values():
            table.add_column(column_header)

        for datum in rows:
            row = list()
            for col in headers.keys():
                value = datum[col]
                if isinstance(value, bool):
                    value = 'Yes' if value else 'No'
                row.append(str(value))
            table.add_row(*row)

        console = Console(highlight=False)
        console.print(table)

    def render(self, data, *args, **kwargs):
        is_text = kwargs.get('is_text', False)
        if is_text:
            print(kwargs.get('custom_text'))
            return

        rows = kwargs.get('rows')
        assert rows is not None
        assert isinstance(rows, list)

        is_succeed = kwargs.get('is_succeed', False)
        if is_succeed:
            is_log = kwargs.get('is_log', False)
            if is_log:
                self._render_logs(rows)
            else:
                headers = kwargs.get('headers')
                assert headers is not None
                assert isinstance(headers, dict)
                self._render_data(rows, headers)
        else:
            # self._render_error()
            self.app.log.error(data)

    def _render_logs(self, rows: dict):
        text = ''
        for row in rows:
            text += f'[bold]{row.get("application_type")}:[/bold] {row.get("message")}\n'

        console = Console(highlight=False)
        console.print(text)
