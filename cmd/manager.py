import typer
from typing_extensions import Annotated
from model.Todo import Todo
from repository.TodoRepository import TodoRepository

manager_app = typer.Typer(name="manager", help="Manage todos")

todo_repository = TodoRepository()


# todo_repository: TodoRepository
def add_todo(name: Annotated[str, typer.Option("--name", "-n")]
             , description: Annotated[str, typer.Option("--description", "-d")]):

    todo = Todo(name, description)

    todo_repository.create(todo)

    todos = todo_repository.get_all()

    for todo in todos:
        print(f"{todo.id}: {todo.name} - {todo.description}")


manager_app.command(name="add", help="Add todo")(add_todo)


def list_todos():
    todos = todo_repository.get_all()
    print(todos)


manager_app.command(name="list", help="List todos")(list_todos)
