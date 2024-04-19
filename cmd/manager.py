import typer
from typing_extensions import Annotated
from model.Todo import Todo
import pytermgui as ptg
from repository.TodoRepository import TodoRepository

manager_app = typer.Typer(name="manager", help="Manage todos")

CONFIG = """
config:
    InputField:
        styles:
            prompt: dim italic
            cursor: '@72'
    Label:
        styles:
            value: dim bold

    Window:
        styles:
            border: '60'
            corner: '60'

    Container:
        styles:
            border: '96'
            corner: '96'
"""


# todo_repository: TodoRepository
def add_todo(name: Annotated[str, typer.Option("--name", "-n")]
             , description: Annotated[str, typer.Option("--description", "-d")]):

    todo_repository = TodoRepository()

    todo = Todo(name, description)

    todo_repository.create(todo)

    todos = todo_repository.get_all()

    for todo in todos:
        print(f"{todo.id}: {todo.name} - {todo.description}")


manager_app.command(name="add", help="Add todo")(add_todo)


def list_todos():
    todo_repository = TodoRepository()
    todos = todo_repository.get_all()
    for todo in todos:
        print(todo.id)


manager_app.command(name="list", help="List todos")(list_todos)


def remove(todo_id: Annotated[int, typer.Option("--id")]):
    todo_repository = TodoRepository()
    todo_repository.delete(todo_id)
    todos = todo_repository.get_all()

    for todo in todos:
        print(todo.name)


manager_app.command(name="remove", help="Remove todo via id")(remove)


OUTPUT = {}


def submit(manager: ptg.WindowManager, window: ptg.Window) -> None:
    for widget in window:
        if isinstance(widget, ptg.InputField):
            OUTPUT[widget.prompt] = widget.value
            continue

        if isinstance(widget, ptg.Container):
            label, field = iter(widget)
            OUTPUT[label.value] = field.value


def show_tui():
    with ptg.YamlLoader() as loader:
        loader.load(CONFIG)

    with ptg.WindowManager() as manager:
        window = (
            ptg.Window(
                "",
                ptg.InputField("Balazs", prompt="Name: "),
                ptg.InputField("Some street", prompt="Address: "),
                ptg.InputField("+11 0 123 456", prompt="Phone number: "),
                "",
                ptg.Container(
                    "Additional notes:",
                    ptg.InputField(
                        "A whole bunch of\nMeaningful notes\nand stuff", multiline=True
                    ),
                    box="EMPTY_VERTICAL",
                ),
                "",
                ["Submit", lambda *_: submit(manager, window)],
                width=60,
                box="DOUBLE",
            )
            .set_title("[210 bold]New contact")
            .center()
        )

        manager.add(window)


manager_app.command(name="show-tui-demo", help="Show tui demo")(show_tui)