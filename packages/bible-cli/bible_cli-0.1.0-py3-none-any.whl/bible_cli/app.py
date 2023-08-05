# bible_cli/app.py
# Ian Kollipara
# 2022.03.10
#
# Bible Cli Application

# Imports
import requests
from rich.console import Console
from rich import table
from typer import Argument, Typer, Option, Exit
from enum import Enum


class Translation(str, Enum):
    CHEROKEE = "cherokee"
    BBE = "bbe"
    KJV = "kjv"
    WEB = "web"
    OEB_CW = "oeb-cw"
    WEBBE = "webbe"
    OEB_US = "oeb-us"
    CLEMENTINE = "clementine"
    ALMEIDA = "almeida"
    RCCV = "rccv"

def get_full_name(translation: Translation) -> str:
    ''' Convert Translation Enum values to Full Translation Title.
    
    ### get_full_name
    Given a Translation Enum Value, convert it to its full translation's title.
    '''
    
    match translation:
        case Translation.CHEROKEE:
            return "Cherokee New Testament"
        case Translation.BBE:
            return "Bible in Basic English"
        case Translation.KJV:
            return "King James Version"
        case Translation.WEB:
            return "World English Bible"
        case Translation.OEB_CW:
            return "Open English Bible, Commonwealth Edition"
        case Translation.WEBBE:
            return "World English Bible, British Edition"
        case Translation.OEB_US:
            return "Open English Bible, US Edition"
        case Translation.CLEMENTINE:
            return "Clementine Latin Vulgate"
        case Translation.ALMEIDA:
            return "João Ferreira de Almeida"
        case Translation.RCCV:
            return "Romanian Corrected Cornilescu Version"


app = Typer(name="bible-cli")
console = Console()

@app.command()
def main(
    book: str = Argument(..., help="The book of the bible"),
    chapter: str = Argument(..., help="The chapter(s) to select. Ex: 1; 1-2"),
    verses: str = Option("", help="The verse range. Ex: 1-10"),
    translation: Translation = Option(Translation.WEB, help="Translation to use"),
):
    url = f"https://bible-api.com/{book}%20{chapter}{verses if not verses else f':{verses}'}?translation={translation}"

    res = requests.get(url).json()

    if error_msg := res.get("error"):
        console.print(f"[bold red]Something went wrong: {error_msg}")
        raise Exit(1)

    v_table = table.Table(show_edge=False, show_header=False)
    v_table.add_column("Verse")
    v_table.add_column("Text")

    console.print(f"Reference: [bold green]{res.get('reference').replace(',', ', ')}")
    console.print(f"Translation: [bold blue]{get_full_name(translation)}")
    for verse in res.get("verses"):
        v_table.add_row(
            f"[bold magenta]{verse.get('verse')}", f"[italic white]{verse.get('text')}"
        )

    console.print(v_table)
