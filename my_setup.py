import os
from os import remove, close
from tempfile import mkstemp
from shutil import move

import re


def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                # new_file.write(line.replace(pattern, subst))
                new_file.write(re.sub(pattern, subst, line))
    close(fh)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)

if __name__ == '__main__':
    # Changes MEDIA ROOT path
    print "Changing MEDIA_ROOT in settings.py"
    pattern = 'MEDIA_ROOT =.+'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    setting_dir = current_dir+"/mysite/settings.py"
    replace_with = "MEDIA_ROOT = '"+current_dir+"/media/'"
    replace(setting_dir, pattern, replace_with)
    user_answer = raw_input("would you like to allow full setup(y n):")
    if (user_answer is "y"):
        os.system("source venv/bin/activate")
        os.system("python manage.py migrate")
        os.system("python manage.py collectstatic")
        os.system("python manage.py runserver")