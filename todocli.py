import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import delete_todo, get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

console = Console()

app = typer.Typer()

@app.command(short_help="adds an item")
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)
    show()

@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    delete_todo(position-1)
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    update_todo(position-1, task, category)
    show()

@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    complete_todo(position-1)
    show()

@app.command()
def show():
    tasks = get_all_todos()
    console.print("Todos")
    
    table = Table(show_header=True, header_style="bold")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    for i, task in enumerate(tasks, start=1):
        is_done_str = "Y" if task.status == 2 else "N"
        table.add_row(str(i), task.task, f"{task.category}", is_done_str)
    console.print(table)

if __name__ == "__main__":
    app()