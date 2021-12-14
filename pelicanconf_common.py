#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = 'Jose Miguel Lopez'
SITENAME = 'Jose Miguel Lopez - Software Developer'
PATH = 'content'
THEME = "theme"
PLUGIN_PATHS = ["plugins"]

TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'
MARKUP = ("md",)

PLUGINS = ["i18n_subsites", "assets"]
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

DIRECT_TEMPLATES = ['index']
MENUITEMS_NAVBAR = []

###

NAME = "José Miguel López"
POSITION = "Software Developer"
LOCATION = "Granada - Remote"
DESCRIPTION = "Web developer, infinite curiosity moves me to learn more every day and be alert to innovations. In ❤️ with Python. Working on different stuff."
PROFILE_PHOTO = "/theme/images/photo.jpg"
PROFILE_PHOTO_MINI = "/theme/images/photo_mini.jpg"
BACKGROUND_PHOTO = "/theme/images/background_2.jpg"

GITHUB_URL = "https://github.com/josemlp91"
LINKEDIN_URL = "https://www.linkedin.com/in/josmilope"