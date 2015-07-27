#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import os
import hashlib

class Newspaper(object):

    def __init__(self, name, frequency, url, filename, folder, text):
        self.name = name
        self.frequency = frequency
        self.url = url
        self.filename = filename
        self.folder = "/home/nicolas/NewspaperCover/" + folder + "/"
        self.folder = folder + "/"
        self.text = text

    def ensure_dir(self,f):
        d = os.path.dirname(f)
        if not os.path.exists(d):
            os.makedirs(d)

    def downloadImage(self):
        self.ensure_dir(self.folder)
        urllib.urlretrieve(self.url, self.folder + "tmp-" + self.filename)

    def md5(self,full_path):
        return hashlib.md5(open(full_path, 'rb').read()).hexdigest()

    def compareMd5(self):
        if not os.path.isfile(self.folder + self.filename):
            os.rename(self.folder + "tmp-" + self.filename, self.folder + self.filename)
        elif self.md5(self.folder + "tmp-" + self.filename) != self.md5(self.folder + self.filename):
            os.rename(self.folder + "tmp-" + self.filename, self.folder + self.filename)
        else:
            os.remove(self.folder + "tmp-" + self.filename)
            return 0
        return 1
