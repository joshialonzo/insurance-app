"""Insurance entry point script."""
# insurance/__main__.py

from insurance.ui.cli import app, __app_name__


def main():
    app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
