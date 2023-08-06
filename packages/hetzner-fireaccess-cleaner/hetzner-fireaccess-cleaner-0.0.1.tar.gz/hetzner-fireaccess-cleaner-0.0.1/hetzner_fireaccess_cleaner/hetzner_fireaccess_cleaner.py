import re
import sys
import time
from pathlib import Path

import click
import pkg_resources  # part of setuptools
import toml
from hcloud import Client


def print_error(message):
    print('Error: {}'.format(message))
    sys.exit(1)


def get_token(context=None):

    config_file = str(Path.home().joinpath('.config/hcloud/cli.toml'))
    try:
        config = toml.load(config_file)
    except FileNotFoundError:
        print_error(f'Failed to find {config_file}, have you setup hcloud?')

    # Check if context is provided, if not, lets use the current active one
    if context is None:
        context = config.get('active_context')
        if context is None:
            print_error('No context provided or configured')
        print(f'No context provided, using {context}')

    try:
        context = next(x for x in config.get('contexts') if x.get('name') == context)
    except StopIteration:
        print_error('Could not find context config')

    token = context.get('token')

    if token == '' or token is None:
        print_error('No token, bad hcloud config?')

    return token


VERSION = pkg_resources.get_distribution("hetzner-fireaccess-cleaner").version
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VERSION)
@click.option('--context', help='context to use. [default: current active]')
@click.pass_context
def cli(ctx, context):
    """A simple CLI for cleaning automated access to hetzner firewalls"""
    ctx.ensure_object(dict)
    ctx.obj['context'] = context if context else None


@cli.command()
@click.argument('firewall')
@click.pass_context
def clean(ctx, firewall):
    """Clean the firewall from expired rules"""
    context = ctx.obj['context']

    token = get_token(context)

    try:
        client = Client(token=token)
        firewall = client.firewalls.get_by_name(firewall)
        # Get firewall rules
        rules = firewall.data_model.rules
    except Exception as err:
        print_error(err)

    prog = re.compile(r".*auto-expire-\[([0-9]+)].*")

    rules_to_remove = []

    for idx, rule in enumerate(rules):

        # find rules which has our tag expire-[]
        match = prog.match(rule.description)
        if match:
            # Check if the rule has expired
            time_to_expire = match[1]

            if int(time_to_expire) <= int(time.time()):
                print(f'Rule marked for removal: {rule.description}')
                rules_to_remove.append(idx)

    if len(rules_to_remove) < 1:
        print('No rules to remove')
        sys.exit()

    for idx in rules_to_remove:
        rules.pop(idx)

    print('Removing rules')
    firewall.set_rules(rules)
    print('Finished')

    sys.exit()
