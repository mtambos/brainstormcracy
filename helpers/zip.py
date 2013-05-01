'''
Created on Sep 16, 2011

@author: Mario Tambos
'''
from cStringIO import StringIO
import zipfile

def add_file(zipstream, fileContents, fname):
    # store the contents in a stream
    f = StringIO(fileContents)
    f.seek(0)
    # write the contents to the zip file
    while True:
        buff = f.read(len(fileContents))
        if buff == "":
            break
        zipstream.writestr(fname.encode('utf-8'), buff)
    return zipstream

def zip_files(resources = []):
    # create the zip stream
    zipstream = StringIO()
    file = zipfile.ZipFile(zipstream, "a", zipfile.ZIP_DEFLATED)

    # repeat this for every URL that should be added to the zipfile
    for resource in resources:
        file = add_file(file, resource.Data, resource.Name)

    # we have finished with the zip so package it up and write the directory
    file.close()
    zipstream.seek(0)

    return zipstream.getvalue()