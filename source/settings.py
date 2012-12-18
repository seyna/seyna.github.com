# ===============
# Basic settings
# ===============
AUTHOR = 'Seyna'
DEFAULT_CATEGORY = 'blog'
SITENAME = 'Seyna - On the Road to Be a Web Architect'
SITEURL = 'http://seyna.github.com'
SITE_URL = SITEURL
STATIC_PATHS = ['images', ]
TIMEZONE = 'Asia/Taipei'


# =============
# URL settings
# =============
PERMALINK_STRUCTURE = '{date:%Y}/{date:%m}/'
ARTICLE_URL = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_URL = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_URL = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_URL = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE
ARTICLE_SAVE_AS = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_SAVE_AS = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_SAVE_AS = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_SAVE_AS = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE


# ===========
# Pagination
# ===========
WITH_PAGINATION = True
DEFAULT_PAGINATION = 10


# =================
# Ordering content
# =================
REVERSE_ARCHIVE_ORDER = True


# =================
# Tuples (Title, URL) to appear
# =================
SOCIAL= (('twitter', "http://twitter.com/closetu"),
         ('github' , "http://github.com/seyna"),)
LINKS = (('smallWrite', "http://smallwrite.blogspot.tw/"),
         ('seyna said', "http://seyna.tumblr.com/"),)


# =================
# Theming
# =================
THEME = 'notmyidea'

GOOGLE_ANALYTICS = 'UA-18732293-7'
DISQUS_SITENAME = 'seynasblog'
FLATTR = True
GITHUB_URL = 'http://github.com/seyna/seyna.github.com'
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
    )
TWITTER_USERNAME = 'closetu'

# =================
# What I added (modify default template)
# =================
FACEBOOK_LIKE = True
