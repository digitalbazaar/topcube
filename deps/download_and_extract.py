import os
import sys
import urllib
import tarfile

# hardcoded here otherwise gyp on windows will incorrectly try to relativize the path
source_url = 'https://www.dropbox.com/s/1hyt9q3zac0fbua/cefclient-0.0.2.tar.gz?dl=1'

target_file = os.path.abspath(os.path.basename(source_url))
dirname = os.path.abspath(sys.argv[1])

if not os.path.exists(target_file):
    urllib.urlretrieve(source_url, target_file)

tfile = tarfile.open(target_file,'r:gz');
tfile.extractall(dirname)
sys.exit(0)
