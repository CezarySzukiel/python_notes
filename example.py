from dataclasses import dataclass
import dataclasses


@dataclass(frozen=True)
class Todo:
    name: str
    status: str = 'pending'


@dataclass(frozen=True)
class TodoList:
    todos: tuple[Todo, ...]


t1 = Todo('Python', 'Failed')
t2 = Todo('Data Science')
t3 = Todo('MLOPS')

t_coll = TodoList((t1, t2, t3))


def change_todo_name(todo: Todo, name: str) -> Todo:
    return dataclasses.replace(todo, name=name)


def update_todos(todo_list: TodoList, prev_todo: Todo, next_todo: Todo) -> TodoList:
    def replace_todo(todo: Todo) -> Todo:
        if todo is not prev_todo:
            return todo
        return next_todo

    return TodoList(tuple(map(replace_todo, todo_list.todos)))


print(t_coll)
tx = change_todo_name(t2, "learn async")
t_coll = update_todos(t_coll, t2, tx)
print(t_coll)



