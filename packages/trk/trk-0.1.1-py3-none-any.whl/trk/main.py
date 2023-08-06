from email import header
from pathlib import Path
from typing import Optional, List
from trk import ( ERRORS, __app_name__, __version__, config, database, trk
)

import pandas as pd
from tabulate import tabulate


import typer


app = typer.Typer()



def get_tracker() -> trk.Tracker:
    if config.CONFIG_FILE_PATH.exists():
        db_path = database.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please, run "trk init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    if db_path.exists():
        return trk.Tracker(db_path)
    else:
        typer.secho(
            'Database not found. Please, run "trk init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

def _version_callback(value: bool) -> None:
    if value:
        typer.echo("A time tracking cli tool created by Nick McMillan")
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def init(
    db_path: str = typer.Option(
        str(database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="time tracker database location?",
    ),
) -> None:
    """Initialize the to-do database."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"The time tracker database is {db_path}", fg=typer.colors.GREEN)
    
@app.command()
def start(event: str = typer.Argument(...), 
    start_time: str =  typer.Option(None, "--time", "-t", help = "Add a manual start time instead of current time."),
    project: str = typer.Option(None, "--project", "-p", help = "Add a project tag"),
    client: str = typer.Option(None,"--client", "-c", help = "Add a client tag")) -> None:
    ''' Start recording a task'''

    tracker = get_tracker()
    event_name = tracker.start(event, start_time, project, client)

    message_start = typer.style("Started the task: ", fg = typer.colors.GREEN)
    message_event = typer.style(event, fg = typer.colors.BRIGHT_WHITE, bold = True)
    message = message_start + message_event
    typer.echo(message)
   
@app.command()
def end(end_time: str =  typer.Option(None, "--time", "-t", help = "Add a manual end time instead of current time.")):
    """End recording a task"""
    tracker = get_tracker()
    tracker.end(end_time)

@app.command()
def list(column_name: str):
    """Get unique values of the project or client """
    tracker = get_tracker()
    values = tracker.list_unique(column_name)
    typer.echo(tabulate(values, showindex= False, headers = "keys"))

@app.command()
def summary(column_names: List[str]):
    """Return a summary table"""
    tracker = get_tracker()
    ls_column_names = []
    for i in column_names:
        ls_column_names.append(i)
    #typer.echo(type(ls_column_names))
    summary = tracker.summary(ls_column_names)
    typer.echo(tabulate(summary, showindex= False, headers = "keys" ))

