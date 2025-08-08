import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memo_app.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
application = get_wsgi_application()
application = WhiteNoise(application)