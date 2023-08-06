""" mcli run Entrypoint """
import argparse
import logging
import textwrap
from typing import Optional

from mcli.models.run import RunModel
from mcli.runs import pipeline

logger = logging.getLogger(__name__)


def run(
    file: Optional[str] = None,
    **kwargs,
) -> int:
    del kwargs
    logger.info(
        textwrap.dedent("""
    ------------------------------------------------------
    Let's run this run
    ------------------------------------------------------
    """))

    partial_run_model = pipeline.create_partial_run_models(file=file,)

    # merge the partial run models into a single complete run model
    run_model = RunModel.from_partial_run_model(partial_run_model)
    #-
    # convert the run model into a mcli job object
    _ = pipeline.mcli_job_from_run_model(run_model)

    return 0


def add_run_argparser(subparser: argparse._SubParsersAction) -> None:
    run_parser: argparse.ArgumentParser = subparser.add_parser(
        'run',
        aliases=['r'],
        help='Run stuff',
    )
    run_parser.set_defaults(func=run)
    _configure_parser(run_parser)


def _configure_parser(parser: argparse.ArgumentParser):
    parser.add_argument(
        '-f',
        '--file',
        dest='file',
        help='File from which to load arguments.',
    )
