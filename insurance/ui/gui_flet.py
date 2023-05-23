import flet as ft


def get_flet_args(fn, mode="web"):
    if mode == "desktop":
        return {"target": fn}
    elif mode == "web":
        return {
            "target": fn,
            "port": 8550,
            "view": ft.WEB_BROWSER
        }


def main(page: ft.Page):
    # add/update controls on Page
    pass


kwargs = get_flet_args(fn=main)
ft.app(**kwargs)
