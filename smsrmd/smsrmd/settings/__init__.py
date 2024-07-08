from .base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if os.environ['SMS'] == 'prod':
    from .prod import *
    print("prod activated")
else:
    from .dev import *
    print("dev activated")