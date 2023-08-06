"""
FreeStrange install entry
"""
import os


with open('/home/pi/.bashrc', 'r+') as path:
    path.seek(0, 2)
    path.write('\n')
    path.write('# CreatePro\n')
    path.write("alias create='python " + os.path.split(__file__)[0] + "/CreatePro/Run/__init__.py'\n")
os.system('source ~/.bashrc')
