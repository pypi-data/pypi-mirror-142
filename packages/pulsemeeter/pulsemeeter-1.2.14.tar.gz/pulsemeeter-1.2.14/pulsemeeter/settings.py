import os
import platform
 

__version__ = '1.2.14'


HOME = os.getenv('HOME', os.getenv('USERPROFILE'))

USER = os.getenv('USER')
APP_DIR = os.path.dirname(os.path.realpath(__file__))
XDG_CONFIG_HOME = os.getenv('XDG_CONFIG_HOME', f'/home/{USER}/.config')
CONFIG_DIR = os.path.join(XDG_CONFIG_HOME, 'pulsemeeter')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')
ORIG_CONFIG_FILE = os.path.join(APP_DIR, 'config.json')
LAYOUT_DIR = os.path.join(APP_DIR, 'interface/layouts')
GLADEFILE = os.path.join(APP_DIR, 'interface/layouts/Tabbed.glade')
SOCK_FILE = f'/tmp/pulsemeeter.{USER}.sock'
PIDFILE = f'/tmp/pulsemeeter.{USER}.pid'
