from subprocess import call
import os

p = 'managementSystem/static/data/experimentalType/'

for f in os.listdir(p):
  if os.path.splitext(f)[1] in ['.png', '.jpg', '.gif', '.jpge']:
    os.remove(os.path.join(os.getcwd(), p, f))

for f in os.listdir(p):
  if os.path.splitext(f)[1] in ['.xls', '.xlsx']:
    call(['soffice', '--headless', '--convert-to', 'html', f],
         cwd=os.path.join(os.getcwd(), p))
