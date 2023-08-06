"""Main module printing detected numato devices on the command-line."""
import numato_gpio as ng
import typer

app = typer.Typer()


@app.command()
def discover():
    """Print out information about all discovered devices."""
    try:
        ng.discover()
        print(f"Discovered devices: {'(None)' if not ng.devices else ''}")
        for device in ng.devices.values():
            print(device)
    finally:
        ng.cleanup()


if __name__ == "__main__":
    app()
