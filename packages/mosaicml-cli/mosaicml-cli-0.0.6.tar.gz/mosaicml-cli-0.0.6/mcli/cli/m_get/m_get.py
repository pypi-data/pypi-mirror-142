""" CLI Get options"""
import argparse

from mcli.config import MCLIConfig
from mcli.platform.platform_info import get_platform_list
from mcli.projects.project_info import get_projects_list


def get_entrypoint(**kwargs,) -> int:
    del kwargs
    parser = configure_argparser(argparse.ArgumentParser())
    parser.print_help()
    return 0


def get_platforms(**kwargs) -> int:
    del kwargs

    platforms = get_platform_list()
    platform_names = [
        f'Name: { x.name }, '
        f'Context: {x.kubernetes_context}, '
        f'Namespace: {x.namespace}' for x in platforms
    ]
    print('PLATFORMS:')
    if platform_names:
        print('\n'.join(platform_names))
    else:
        print('None')
    return 0


def get_environment_variables(**kwargs) -> int:
    del kwargs

    conf: MCLIConfig = MCLIConfig.load_config()
    var_names = [f'Name: {x.name}, Key: {x.env_key}' for x in conf.environment_variables]
    print('ENV Variables:')
    if var_names:
        print('\n'.join(var_names))
    else:
        print('None')
    return 0


def get_secrets(**kwargs) -> int:
    del kwargs

    conf: MCLIConfig = MCLIConfig.load_config()
    var_names = [f'Name: {x.name}, Type: {x.secret_type.value}' for x in conf.secrets]
    print('Secrets:')
    if var_names:
        print('\n'.join(var_names))
    else:
        print('None')
    return 0


def get_projects(**kwargs) -> int:
    del kwargs
    all_projects = sorted(get_projects_list(), reverse=True)
    print('Projects:')

    for project in all_projects:
        print(f'Project: {project.project}  (last used {project.get_last_accessed_string()})')
    if len(all_projects) == 0:
        print('None')

    return 0


def configure_argparser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    subparsers = parser.add_subparsers()
    parser.set_defaults(func=get_entrypoint)

    projects_parser = subparsers.add_parser('projects', aliases=['project'], help='Get Project')
    projects_parser.set_defaults(func=get_projects)
    platform_parser = subparsers.add_parser('platforms', aliases=['platform'], help='Get Platforms')
    platform_parser.set_defaults(func=get_platforms)
    environment_parser = subparsers.add_parser('env', aliases=['environment'], help='Get Environment Variables')
    environment_parser.set_defaults(func=get_environment_variables)
    secrets_parser = subparsers.add_parser('secrets', aliases=['secret'], help='Get Secrets')
    secrets_parser.set_defaults(func=get_secrets)
    return parser


def add_get_argparser(subparser: argparse._SubParsersAction,) -> argparse.ArgumentParser:
    """Adds the get parser to a subparser

    Args:
        subparser: the Subparser to add the Get parser to
    """
    get_parser: argparse.ArgumentParser = subparser.add_parser(
        'get',
        aliases=['g'],
        help='Get info about your MCLI setup',
    )
    get_parser = configure_argparser(parser=get_parser)
    return get_parser
