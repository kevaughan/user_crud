import os, subprocess, sys


DEFAULT_URL="http://dl.dropbox.com/u/1004432/"
PACKAGE = "virtualenv.py"

def download(
    download_base=DEFAULT_URL, to_dir=os.curdir,
    delay = 15, package = PACKAGE
):
    """Download setuptools from a specified location and return its filename

    `version` should be a valid setuptools version number that is available
    as an egg for download under the `download_base` URL (which should end
    with a '/'). `to_dir` is the directory where the egg will be downloaded.
    `delay` is the number of seconds to pause before an actual download attempt.
    """
    import urllib2, shutil
    url = download_base + package
    saveto = os.path.join(to_dir, package)
    src = dst = None
    if not os.path.exists(saveto):  # Avoid repeated downloads
        try:
            from distutils import log
            if delay:
                log.warn("""
---------------------------------------------------------------------------
If this script fails 
You may need to enable firewall access for this script first.
or define your http_proxy

(Note: if this machine does not have network access, this script will not work )
---------------------------------------------------------------------------"""

                ); 
            log.warn("Downloading %s", url)
            src = urllib2.urlopen(url)
            # Read/write all in one block, so we don't create a corrupt file
            # if the download is interrupted.
            # data = _validate_md5(egg_name, src.read())
            data = src.read()
            dst = open(saveto,"wb"); dst.write(data)
        finally:
            if src: src.close()
            if dst: dst.close()
    return os.path.realpath(saveto)

def create():
    success = subprocess.call(["python", "virtualenv.py", "--no-site-packages","venv"])
    if sys.platform == 'win32':
        success = subprocess.call(["venv/Scripts/pip", "install","--use-mirrors","flask"])
    else:
        success = subprocess.call(["venv/bin/pip", "install","--use-mirrors","flask"])

def install():
    download()
    download(package="helloflask.py")
    create()
if __name__=='__main__':
    install()
