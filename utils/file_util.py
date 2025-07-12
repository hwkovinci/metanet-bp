from pathlib import Path
import configparser 

config = configparser.Configparser()
config.read('config.ini')

root_home = Path( config['paths']['root_home'] )
root_proj = root_home / Path( config['paths']['root_home'] )

logs_path = root / config['paths'][logs]







