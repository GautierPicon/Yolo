import json
import importlib
import sys
from pathlib import Path

try:
    import questionary
except ImportError:
    print("Missing dependency: run `uv add questionary`")
    sys.exit(1)


def load_cli(path: str = "cli.json") -> dict:
    with open(path) as f:
        return json.load(f)


def main():
    config = load_cli()
    commands = config["commands"]

    choices = [
        questionary.Choice(title=f"{cmd['label']}  —  {cmd['description']}", value=i)
        for i, cmd in enumerate(commands)
    ]
    choices.append(questionary.Choice(title="Quit", value=-1))

    result = questionary.select(config["title"], choices=choices).ask()

    if result is None or result == -1:
        sys.exit(0)

    cmd = commands[result]
    module = importlib.import_module(cmd["module"])
    fn = getattr(module, cmd["function"])

    if cmd["function"] == "run_image":
        path = questionary.path("Image path:").ask()
        if path:
            fn(path)
    else:
        fn()


if __name__ == "__main__":
    main()