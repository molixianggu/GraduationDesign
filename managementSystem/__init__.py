from subprocess import call
import os


def toHtml(p):
  for f in os.listdir(p):
    if os.path.splitext(f)[1] in ['.png', '.jpg', '.gif', '.jpge', '.html']:
      os.remove(os.path.join(os.getcwd(), p, f))

  for f in os.listdir(p):
    if os.path.splitext(f)[1] in ['.xls', '.xlsx']:
      call(['soffice', '--headless', '--convert-to', 'html', f],
           cwd=os.path.join(os.getcwd(), p))


toHtml('managementSystem/static/data/experimentalType/')
toHtml('managementSystem/static/data/EquipmentType/')
