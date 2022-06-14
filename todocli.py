import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()

@app.command(short_help="adds an item")
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    show()

@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    show()

@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    show()

@app.command()
def show():
    tasks = [("Task 1", "Study"), ("Task 2", "Work")]
    console.print("Todos")
    
    table = Table(show_header=True, header_style="bold")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    for i, task in enumerate(tasks, start=1):
        is_done_str = "Y" if True == 2 else "N"
        table.add_row(str(i), task[0], f"{task[1]}", is_done_str)
    console.print(table)

if __name__ == "__main__":
    app()