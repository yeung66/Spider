#coding:utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ziqiang.settings")

import django
django.setup()

def main():
    from duanzi.models import Duanzi
    f=open('txt.txt')
    for line in f:
        content = line
        Duanzi.objects.create(content=content)
    f.close()

if __name__ =="__main__":
    main()
    print "Done!"