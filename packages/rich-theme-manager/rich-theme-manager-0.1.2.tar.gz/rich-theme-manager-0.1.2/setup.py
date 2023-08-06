# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rich_theme_manager']

package_data = \
{'': ['*']}

install_requires = \
['rich>=11.0']

entry_points = \
{'console_scripts': ['rich_theme_manager = rich_theme_manager:main']}

setup_kwargs = {
    'name': 'rich-theme-manager',
    'version': '0.1.2',
    'description': 'Manage rich themes for CLI applications',
    'long_description': '# Rich Theme Manager\n\n## Description\nImplements a basic "theme manager" class for managing rich Themes in your [rich](https://github.com/Textualize/rich) CLI application.\n\nThe rich package provides an easy way to define custom styles and themes for use with rich.  This package provides a simple way to manage the themes: e.g. to list, add, remove themes, for the user to preview themes, and to manage themes on disk.\n\n## Synopsis\n\n```python\nfrom rich.console import Console\nfrom rich.style import Style\n\nfrom rich_theme_manager import Theme, ThemeManager\n\nTHEMES = [\n    Theme(\n        name="dark",\n        description="Dark mode theme",\n        tags=["dark"],\n        styles={\n            "error": Style(color="rgb(255,85,85)", bold=True),\n            "filepath": Style(color="rgb(80,250,123)", bold=True),\n            "time": Style(color="rgb(139,233,253)", bold=True),\n        },\n    ),\n    Theme(\n        name="light",\n        description="Light mode theme",\n        styles={\n            "error": Style(color="#b31d28", bold=True, underline=True, italic=True),\n            "filepath": Style(color="#22863a", bold=True),\n            "time": Style(color="#032f62", bold=True),\n        },\n    ),\n    Theme(\n        name="mono",\n        description="Monochromatic theme",\n        tags=["mono", "colorblind"],\n        styles={\n            "error": "reverse italic",\n            "filepath": "bold underline",\n            "time": "bold",\n        },\n    ),\n]\n\nif __name__ == "__main__":\n    theme_manager = ThemeManager(themes=THEMES)\n    theme_manager.list_themes(show_path=False)\n    theme_manager.preview_theme(THEMES[0], show_path=False)\n    console = Console(theme=THEMES[0])\n    console.print("[error]Oh No![/error]")\n```\n\n![Example output](https://github.com/RhetTbull/rich_theme_manager/raw/main/images/example1.png)\n\n## Example app\n\nA simple example app that demonstrates the ThemeManager class comes with rich_theme_manager in `__main__.py`:\n\n`python -m rich_theme_manager`:\n\n```\nusage: rich_theme_manager [-h] [--example [EXAMPLE]] [--list] [--preview THEME] [--config THEME]\n\nExample CLI usage of rich_theme_manager\n\noptional arguments:\n  -h, --help           show this help message and exit\n  --example [EXAMPLE]  Show example output for theme.\n  --list               List themes.\n  --preview THEME      Preview theme.\n  --config THEME       Print configuration for theme THEME.\n```\n\n`python -m rich_theme_manager --list`:\n\n![Example --list output](https://github.com/RhetTbull/rich_theme_manager/raw/main/images/list.png)\n\n`python -m rich_theme_manager --preview dark`:\n\n![Example --preview output](https://github.com/RhetTbull/rich_theme_manager/raw/main/images/preview_dark.png)\n\n\n## Documentation\n\nComing!\n\nIn a nutshell, use `from rich_theme_manager import Theme` instead of `from rich.theme import Theme` and use `from rich_theme_manager import ThemeManager` to create a ThemeManager instance.  \n\n`rich_theme_manager.ThemeManager(theme_dir: Optional[str] = None, themes: Optional[List[Theme]] = None)`\n\nIf you specify a `theme_dir` (for example, using [click.get_app_dir](https://click.palletsprojects.com/en/8.0.x/api/?highlight=get_app_dir#click.get_app_dir)), ThemeManager will read/write themes from/to that directory.  If you specify a `themes` list, ThemeManager will use that list of themes as the default themes and will write the defaults to the theme directory if not already present.  \n\nThis allows you to easily define default "starting" themes for your application but the user can then edit the theme files (which are INI files created by [configparser](https://docs.python.org/3/library/configparser.html)) to customize the CLI.\n\nTheme subclasses `rich.theme.Theme`.  You must specify a name and can optionally specify a description, a list of tags, and a path to save the theme to (via `Theme.save()`).\n\n`Theme(name: str, description: Optional[str] = None, styles: Optional[Mapping[str, StyleType]] = None, inherit: bool = True, tags: Optional[List[str]] = None, path: Optional[str] = None)`\n\n## License\n\nMIT License\n\n## Contributing\n\nContributions of all kinds are welcome!\n\n## Credits\n\nThank you to [Will McGugan](https://github.com/willmcgugan) for creating [rich](https://github.com/Textualize/rich) and helping to make our command line interfaces more beautiful!\n',
    'author': 'Rhet Turnbull',
    'author_email': 'rturnbull+git@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rhettbull/rich-theme-manager',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0.0',
}


setup(**setup_kwargs)
