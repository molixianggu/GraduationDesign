#!/usr/bin/env python
import os
import sys
from subprocess import call

def toHtml(p):
  for f in os.listdir(p):
    if os.path.splitext(f)[1] in ['.png', '.jpg', '.gif', '.jpge', '.html']:
      os.remove(os.path.join(os.getcwd(), p, f))

  for f in os.listdir(p):
    if os.path.splitext(f)[1] in ['.xls', '.xlsx']:
      call(['soffice', '--headless', '--convert-to', 'html', f],
           cwd=os.path.join(os.getcwd(), p))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GraduationDesign.settings")

    from django.core.management import execute_from_command_line
    if 'new' in sys.argv:
        toHtml('managementSystem/static/data/experimentalType/')
        toHtml('managementSystem/static/data/EquipmentType/')
        toHtml('managementSystem/static/data/Equipment/')
        sys.argv.remove('new')
    execute_from_command_line(sys.argv)
