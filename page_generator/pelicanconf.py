from logging import DEBUG

AUTHOR = 'bison'
SITENAME = 'Pride Versioning'
SITEURL = "http://127.0.0.1:8000/"

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
    ("on GitHub", "https://github.com/bison--/pridever"),
)

# Social widget
SOCIAL = (
    ("bison", "https://mastodon.social/@bison"),
    ("Niki Tonsky", "https://mastodon.online/@nikitonsky"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = 'themes/notmyidea'
#THEME_TEMPLATES_OVERRIDES = ['themes/override']
