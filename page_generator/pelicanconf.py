from logging import DEBUG

AUTHOR = 'bison'
SITENAME = 'Pride Versioning'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Original idea by Niki Tonsky", "https://mastodon.online/@nikitonsky/113691789641950263"),
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("bison", "https://mastodon.social/@bison"),
    ("Niki Tonsky", "https://mastodon.online/@nikitonsky"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = '../venvs/venv_3_10/Lib/site-packages/pelican/themes/notmyidea'
THEME_TEMPLATES_OVERRIDES = ['templates']
