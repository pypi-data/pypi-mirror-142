import logging
import sys
from typing import Any, Optional, TextIO, Tuple

import click
import rich.console
import rich.logging
import rich.progress
import sentry_sdk
import yaml

from . import __title__, __version__
from . import api as clink


logger = logging.getLogger(__name__)


sentry_sdk.init(release=f"{__title__}@{__version__}")


@click.group()
@click.pass_context
@click.version_option(__version__)
def main(context: click.Context) -> None:
    logging.basicConfig(
        datefmt=f"[{logging.Formatter.default_time_format}]",
        format="%(message)s",
        level=logging.INFO,
        handlers=[rich.logging.RichHandler(show_path=False)],
    )
    logging.getLogger(name="clink").setLevel(logging.DEBUG)

    console = rich.console.Console()

    console.print(
        r"""
           _                    _ _      _
   __ _ __| |____ _ _ __ ___ __| (_)_ _ | |__
  / _` (_-< / / _` | '_ \___/ _| | | ' \| / /
  \__,_/__/_\_\__,_| .__/   \__|_|_|_||_|_\_\
                   |_|

    """,
        highlight=False,
        overflow="crop",
        style="bold #c837ab",
    )

    context.ensure_object(dict)
    context.obj["component"] = clink.Participant("clink.cli")


@main.command()
@click.argument("type_", metavar="type", required=False, type=str)
@click.option(
    "--input",
    "input",
    help="JSON event object.",
    required=False,
    type=click.File(),
)
@click.option("--subject", "subject", required=False, type=str)
@click.option("--dry-run", "dry_run", is_flag=True)
@click.pass_context
def emit_event(
    context: click.Context,
    type_: Optional[str],
    input: Optional[TextIO],
    subject: Optional[str],
    dry_run: bool,
) -> None:
    if (input and type_) or (not input and not type_):
        raise click.BadOptionUsage(
            option_name="type",
            message='Either "type" OR "--input" parameter must be provided.',
            ctx=context,
        )

    context.ensure_object(dict)
    component = context.obj["component"]

    if input:
        data = yaml.safe_load(input)
        event = clink.Event.from_dict(data)
        component.emit_event(event, dry_run=dry_run)
    else:
        component.emit_event(type=type_, subject=subject, dry_run=dry_run)


@main.command()
@click.option(
    "--topic",
    "-t",
    "topics",
    type=str,
    multiple=True,
    default=["#"],
    show_default=True,
)
@click.pass_context
def consume(context: click.Context, topics: Tuple[str]) -> None:
    context.ensure_object(dict)
    component: clink.Participant = context.obj["component"]

    @component.on_event(*topics, supports_dry_run=True)
    def noop(event: clink.Event, **kwargs: Any) -> None:  # pragma: no cover
        pass

    logging.info(f"Listening for events on topics: {', '.join(topics)}")

    component.consume()


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(prog_name=__title__))
