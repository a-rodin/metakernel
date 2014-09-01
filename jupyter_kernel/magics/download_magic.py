# Copyright (c) Calico Development Team.
# Distributed under the terms of the Modified BSD License.
# http://calicoproject.org/

from jupyter_kernel import Magic
import urllib
try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse
import os

class DownloadMagic(Magic):

    def line_download(self, url, filename=None):
        """%download URL [FILENAME] - download file from URL"""
        opener = urllib.URLopener()
        if filename is None:
            parts = urlparse.urlsplit(url)
            #('http', 'example.com', '/somefile.zip', '', '')
            path = parts[2]
            filename = os.path.basename(path)
        try:
            opener.retrieve(url, filename)
            self.kernel.Print("Downloaded '%s'." % filename)
        except Exception as e:
            self.kernel.Error(str(e))


def register_magics(kernel):
    kernel.register_magics(DownloadMagic)