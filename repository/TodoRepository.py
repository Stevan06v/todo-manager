import os
from typing import List, Type
from model.Todo import Todo
from repository.IRepository import IRepository
import json


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class TodoRepository(IRepository):  # implements IRepo

    def __init__(self, file_path: str = "./data/todos.json"):
        self.todos: List[Todo] = []
        self.file_path = file_path
        self.load_from_json()

    def load_from_json(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.todos = [Todo(todo_data['name'], todo_data['description']) for todo_data in data]
        except FileNotFoundError:
            with open(self.file_path, 'w') as fp:
                pass
            print(f"File created successfully: '{self.file_path}'.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON file '{self.file_path}'.")

    def save_to_json(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump([{'name': todo.name, 'description': todo.description} for todo in self.todos], file, indent=4)
            print("Todos saved successfully to JSON file.")
        except Exception as e:
            print(f"Error saving todos to JSON file: {e}")

    def get_all(self):
        return self.todos

    def get_by_id(self, id):
        for todo in self.get_all():
            if todo.id == id:
                return todo
        return None

    def create(self, todo):
        self.todos.append(todo)
        self.save_to_json()

    def update(self, updated_todo):
        for i, todo in enumerate(self.todos):
            if todo.id == updated_todo.id:
                self.todos[i] = updated_todo
                return
        raise ValueError("Todo item not found")

    def delete(self, id):
        pass


