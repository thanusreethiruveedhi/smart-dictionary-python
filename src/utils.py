from rich.console import Console
from rich.panel import Panel

console = Console()


def title(text):
    console.print(Panel.fit(text, style="cyan"))


def success(text):
    console.print(f"[green]{text}[/green]")


def error(text):
    console.print(f"[red]{text}[/red]")


def info(text):
    console.print(f"[yellow]{text}[/yellow]")