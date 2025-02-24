#!/usr/bin/python3
from typing import Union

import click
from pygitguardian import GGClient
from pygitguardian.models import Detail, Quota, QuotaResponse

from ggshield.core.client import retrieve_client
from ggshield.core.utils import json_output_option_decorator
from ggshield.output.text.message import format_quota_color


@click.command()
@json_output_option_decorator
@click.pass_context
def quota(ctx: click.Context, json_output: bool) -> int:
    """Command to show quotas overview."""
    client: GGClient = retrieve_client(ctx.obj["config"])
    response: Union[Detail, QuotaResponse] = client.quota_overview()

    if not isinstance(response, (Detail, QuotaResponse)):
        raise click.ClickException("Unexpected quota response")

    if isinstance(response, Detail):
        raise click.ClickException(response.detail)

    quota: Quota = response.content

    click.echo(
        quota.to_json()
        if json_output
        else (
            f"Quota available: {format_quota_color(quota.remaining, quota.limit)}\n"
            f"Quota used in the last 30 days: {quota.count}\n"
            f"Total Quota of the workspace: {quota.limit}\n"
        )
    )

    return 0
