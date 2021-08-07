#!/usr/bin/python
# -*- coding:utf-8 -*-
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os


def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
        print('Creating %s...' % (zipFilename))
        backupZip = zipfile.ZipFile(zipFilename, 'w')
        for foldername, subfolders, filenames in os.walk(folder):
            print('Adding files in %s...' % foldername)
            # Add the current folder to the ZIP file.
            # backupZip.write(os.path.basename(foldername))
            backupZip.write(foldername)
            # print(os.path.basename(foldername))
            # Add all the files in this folder to the ZIP file.
            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue  # don't backup the backup ZIP files
                # print(filename)
                # backupZip.write(os.path.join(os.path.basename(foldername), filename))
                backupZip.write(os.path.join(foldername, filename))
        backupZip.close()

    print('Done.')


# backupToZip('C:\\delicious')
backupToZip('C:\\ZZZZZZZZZZ\\python\\base1\\example')

