import click
from rich import print
from rich.prompt import Confirm
from rich_click import RichGroup, RichCommand
import ciscotmg


@click.group(cls=RichGroup)
@click.version_option()
def cli():
    """
    Cisco TMG Matrix CLI\n
    Disclaimer: Cisco makes the data in this tool available for informational purposes.\n
    Cisco does not represent, warrant, or guarantee that it is complete, accurate, or up to date.\n
    This information is subject to change without notice.
    """
    pass


@cli.command(cls=RichCommand)
@click.option("--local", "-l", is_flag=True, help="Local pip upgrade")
@click.option("--force", "-f", is_flag=True, help="Force upgrade, no prompt")
def upgrade(local, force):
    """Upgrade software"""
    svc = ciscotmg.Services()
    online_version = svc.api.check_latest_pypi_version()
    local_version = ciscotmg.Meta.__version__
    if local_version != online_version:
        print(f"New version available: {online_version}")
        if force is False:
            ask = Confirm.ask("Do you wanna upgrade?")
            if ask:
                svc.software.upgrade(online_version, local=local)
    else:
        print(f"Up-to-date version {local_version}")


@cli.command(cls=RichCommand)
@click.argument("pid")
@click.option("--json", "-j", is_flag=True, help="Output in JSON")
@click.option("--output", "-o", type=str, help="Output to file")
def search(json, pid, output):
    """Search PIDs"""
    svc = ciscotmg.Services()
    results = svc.search(pid=pid)
    if json:
        print(results.json)
    else:
        print(results.cli)
    if output is not None:
        if json:
            ciscotmg.output.write_to_file(results.json, output)
        else:
            ciscotmg.output.write_to_file(results.cli, output)


@cli.command(cls=RichCommand)
@click.argument("pid")
@click.option("--device", "-n", is_flag=True, help="Network Device")
@click.option("-pf", type=str, help="Product Family (Network Device)")
@click.option("--json", "-j", is_flag=True, help="Output in JSON")
@click.option("--output", "-o", type=str, help="Output to file")
def lookup(device, pf, json, pid, output):
    """Lookup PID"""
    svc = ciscotmg.Services()
    results = svc.lookup(pid=pid, network_device=device, product_family=pf)
    if json:
        print(results.json)
    else:
        print(results.cli)
    if output is not None:
        if json:
            ciscotmg.output.write_to_file(results.json, output)
        else:
            ciscotmg.output.write_to_file(results.cli, output)


@cli.command(cls=RichCommand)
def url():
    """Website for Cisco TMG Matrix"""
    tmg_url = "https://tmgmatrix.cisco.com/"
    iop_url = "https://tmgmatrix.cisco.com/iop"
    print(f"Cisco TMG Optics-to-Device Matrix: {tmg_url}")
    print(f"Cisco TMG Optics-to-Optics Matrix: {iop_url}")


if __name__ == "__main__":
    cli()
