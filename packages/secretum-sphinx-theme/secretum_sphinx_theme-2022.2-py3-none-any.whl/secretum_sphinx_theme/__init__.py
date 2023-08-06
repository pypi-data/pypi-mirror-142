"""
Sphinx Read the Docs Dark Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows for toggable dark mode on the Read the Docs
theme for Sphinx.
"""

__title__ = "secretum_sphinx_theme"
__description__ = "Dark mode for the Sphinx Read the Docs theme."
__author__ = "Gerrishon Sirere"
__version__ = "2022.2"
__license__ = "MIT"

from secretum_sphinx_theme.dark_mode_loader import DarkModeLoader


def setup(app):
    app.add_config_value("default_dark_mode", True, "html")

    app.connect("config-inited", DarkModeLoader().configure)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
