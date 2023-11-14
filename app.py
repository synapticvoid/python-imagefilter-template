from textual import on, work
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Header, Footer, Label, Input, Static, Button, RichLog


class TextField(Static):
    """Simple text field with a top label. The initial value of the field is optional.
    To retrieve the value of the field, use the `value` attribute:
    field = TextField("My label", initial_value="My initial value")
    print(field.input.value) # prints "My initial value"
    """
    value = reactive("")

    def __init__(self, label: str, initial_value: str = ""):
        super().__init__()
        self.label = label
        self.input = Input(placeholder=self.label, value=initial_value)

    def compose(self) -> ComposeResult:
        yield Label(self.label)
        yield self.input


class ImageFilterApp(App):
    DEFAULT_CSS = """
    #process {
        dock: bottom;
        margin-bottom: 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.input_dir = TextField("Input directory",
                                   initial_value="")
        self.rich_log = RichLog(highlight=True)

    def compose(self) -> ComposeResult:
        yield Header()
        yield self.input_dir
        yield Button("Process", id="process", variant="primary")
        yield Footer()
        yield self.rich_log

    @on(Button.Pressed, "#process")
    def on_process_pressed(self, event):
        self.rich_log.write("Process pressed")

        # --------------------------------------------------
        # Ajouter les paramètres de configuration ici
        # --------------------------------------------------
        self.start_process()

    @work(exclusive=True, thread=True)
    def start_process(self):
        # --------------------------------------------------
        # Appeler votre code de traitement ici
        # --------------------------------------------------
        pass
