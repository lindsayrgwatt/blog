AUTHOR = 'Lindsay Watt'
SITENAME = 'Random Dispatches'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Home", "https://www.lindsayrgwatt.com/"),
)

MARKUP = ('md')

THEME = 'themes/elegant'

# Social widget
SOCIAL = (
    ("Instagram", "https://www.instagram.com/lindsayrgwatt/"),
    ("LinkedIn", "https://www.linkedin.com/in/lindsayrgwatt/"),
    ("Github", "https://github.com/lindsayrgwatt")
)

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'

STATIC_PATHS = ['images']

DEFAULT_PAGINATION = 0

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
