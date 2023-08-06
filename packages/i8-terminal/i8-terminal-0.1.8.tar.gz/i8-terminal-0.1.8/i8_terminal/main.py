import os
import sys

import click
import investor8_sdk
from click_repl import repl
from rich.console import Console

from i8_terminal.commands import cli
from i8_terminal.config import USER_SETTINGS
from i8_terminal.types.i8_auto_suggest import I8AutoSuggest
from i8_terminal.types.i8_completer import I8Completer


def init_commands() -> None:
    app_dir = os.path.join(os.path.join(os.path.dirname(sys.executable), "lib"), "i8_terminal")
    sys.path.append(app_dir)
    commands_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commands")
    commands_dir = commands_dir if os.path.exists(commands_dir) else os.path.join(app_dir, "commands")
    ignore_dir = ["__pycache__"]
    for cmd in [p for p in os.listdir(commands_dir) if os.path.isdir(os.path.join(commands_dir, p))]:
        if cmd not in ignore_dir:
            for sub_cmd in os.listdir(os.path.join(commands_dir, cmd)):
                sub_cmd_splitted = sub_cmd.split(".")
                if (sub_cmd_splitted[-1] in ["py", "pyc"]) and sub_cmd_splitted[0] not in ["__init__"]:
                    __import__(f"i8_terminal.commands.{cmd}.{''.join(sub_cmd_splitted[:-1])}")

    @cli.command()
    def shell() -> None:
        console = Console(force_terminal=True, color_system="truecolor")
        console.print("\n👋 Welcome to i8 Terminal!", style="yellow")
        console.print("Copyright © 2020-2022 Investoreight | https://www.i8terminal.io/\n")
        console.print("- Enter [magenta]?[/magenta] to get the list of commands.")
        console.print("- Enter [magenta]:q[/magenta] to exit the shell.\n")

        prompt_kwargs = {"completer": I8Completer(cli), "auto_suggest": I8AutoSuggest(cli)}
        repl(click.get_current_context(), prompt_kwargs=prompt_kwargs)

    @cli.command()
    def exit() -> None:
        os._exit(0)


def main() -> None:
    console = Console()
    with console.status("Starting Up...", spinner="material"):
        init_commands()

    if (not set(["user", "login"]).issubset(set(sys.argv[1:]))) and (
        not USER_SETTINGS.get("i8_core_api_key") or not USER_SETTINGS.get("i8_core_token")
    ):
        console.print(
            "Please login first to use i8 terminal using the following command:\n[magenta]i8 user login[/magenta]"
        )
        return

    investor8_sdk.ApiClient().configuration.api_key["apiKey"] = USER_SETTINGS.get("i8_core_api_key")
    investor8_sdk.ApiClient().configuration.api_key["Authorization"] = USER_SETTINGS.get("i8_core_token")
    investor8_sdk.ApiClient().configuration.api_key_prefix["Authorization"] = "Bearer"

    cli(obj={})


if __name__ == "__main__":
    main()
else:
    init_commands()
