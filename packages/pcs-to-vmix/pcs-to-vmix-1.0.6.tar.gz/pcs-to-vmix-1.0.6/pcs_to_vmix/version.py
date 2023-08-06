''' Keep a VERSION file in the package root 
Kepp this in the root of your source
from pkg_name.version import VERSION
from pkg_name.version import VER
VER is short form and VERSION is with git Sha and dirty flag if gitpython installed'''


import logging
log = logging.getLogger('')

import pathlib
PKG_ROOT = pathlib.Path(__file__).parent

try:
    VERSION = (PKG_ROOT / "../VERSION").read_text()
except FileNotFoundError:
    VERSION = '99.0.0'

# And to improve with a VER and VERSION 
gitsha = None

try:
    import git
    
    repo = git.Repo(search_parent_directories=True)
    remoteBranch = repo.active_branch.tracking_branch()
    remote = repo.remote(remoteBranch.remote_name)
    for url in remote.urls:
        break
    log.info(
        f'Latest commit:{repo.commit()}| Dirty:{repo.is_dirty()}| Branch:{repo.active_branch}| Remote Branch:{remoteBranch}| Remote url:{url}'
    )
    gitsha = repo.head.object.hexsha
    if repo.is_dirty():
        gitsha += 'M'
    
except ModuleNotFoundError:
    log.warning(f'`gitpython` not installed - Not a problem if running in production enviroment.')
    pass

# TODO - Make recursivly walk up your tree until you find a repo / what are we actually trying to do here?
# Guess we are trying to catch deviation from a sha on a dev machine that does not have gitpython installed
if pathlib.Path(PKG_ROOT / '../../.git').is_dir():
    log.debug('We are in a repo so should have a sha')
    if not gitsha:
        log.error('We are in a repo so should have a sha')
        # raise ValueError('No sha and in a repo - probably not installed with `pip install -r requirements.txt` which installs `gitpython`')

if gitsha:
    VERSION += ('.' + gitsha)

VER = VERSION.rpartition('.')[0]

log.info(f'VER:{VER}|VERSION:{VERSION}')
pass
