""" m delete Entrypoint """
import argparse

from mcli.cli.m_delete.delete import delete_environment_variable, delete_platform, delete_secret


def delete(**kwargs,) -> int:
    del kwargs
    mock_parser = configure_argparser(parser=argparse.ArgumentParser())
    mock_parser.print_help()
    return 0


def configure_argparser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    subparsers = parser.add_subparsers()
    parser.set_defaults(func=delete)

    # TODO: Delete Projects

    platform_parser = subparsers.add_parser(
        'platform',
        aliases=['platforms'],
        help='Delete a Platform',
    )
    platform_parser.add_argument('platform_name', help='The name of the platform to delete')
    platform_parser.set_defaults(func=delete_platform)

    environment_parser = subparsers.add_parser(
        'env',
        aliases=['environment-variable'],
        help='Delete an Environment Variable',
    )
    environment_parser.add_argument('variable_name', help='The name of the environment variable to delete')
    environment_parser.set_defaults(func=delete_environment_variable)

    secrets_parser = subparsers.add_parser(
        'secrets',
        aliases=['secret'],
        help='Delete a Secret',
    )
    secrets_parser.add_argument('secret_name', help='The name of the secret to delete')
    secrets_parser.set_defaults(func=delete_secret)

    return parser


def add_delete_argparser(subparser: argparse._SubParsersAction,) -> argparse.ArgumentParser:
    delete_parser: argparse.ArgumentParser = subparser.add_parser(
        'delete',
        aliases=['del'],
        help='Configure your local project',
    )
    delete_parser = configure_argparser(parser=delete_parser)
    return delete_parser
