## [git-crawler](https://github.com/eif0/git-crawler/) - Git email Crawler, and Information Disclosure Tool

Many times amateur git users (and sadly some experienced users too) make mistakes while commiting/pulling/merging from different workstations and some private information become public without the programmer's will.

Also, quite often new github/bitbucket/gitcloud/whatever users use to think that their emails accounts remain private/hidden if they don't publish them in their public profile.

In order to __audit missconfigured repos__, and find someone's information leaks I created git-crawler.

__git-crawler__ is an auditing tool that find and disclosure all the __email accounts__ related to a git project (both autor's mail and contributor's mail).

It doesn't mind if you noticed about the leak and solved your configuration issue by pushing again with a _.mailmap_ file _(see [git-shortlog](http://git-scm.com/docs/git-shortlog) or [git-blame](http://git-scm.com/docs/git-blame))_ to replace your previously leaked email. It's too late!, git-crawler will find your leaked mail without hesitation!


####_git-crawler has two major ways of use:_
* __"Remote Repo"__ mode: Find email leaks within a remote repo not abailable locally (works great both with public and private repos).

* __"Local Repo"__ mode: Find email leaks within a local repo downloaded at your workstation.


## Technical details

The app is written in pure Python2 (migration to Python3 is planned for the future). 


### Running locally

You can clone this repo with a simple:
``$ git clone https://github.com/eif0/git-crawler.git``

#### Usage

_(example auditing [Xibalba](https://github.com/eif0/xibalba)'s leaked emails)_

In order to audit a __remote repo__:
* ``python git-crawler.py -r https://github.com/eif0/xibalba.git``

In order to audit a __local repo__:
* ``python git-crawler.py -l /path/to/xibalba`` 


### Licensing

The source code is licensed under GPLv3. License is available [here](/LICENSE).

## Contribute

You can help this project by reporting problems, suggestions, or contributing to the code.

Also, you can always contact me at eif0@hush.com

### Report a problem or suggestions/ideas

Go to git-crawler's [issue tracker](https://github.com/eif0/git-crawler/issues) and check if your problem/suggestion is already reported. If not, create a new issue with a descriptive title and detail your suggestion or steps to reproduce the problem.

Also, as said before, my email is always available for suggestions, ideas and cat pictures.

### Invite me a beer

Last, but not least, if you like this project and find it useful you can buy me a beer

* __BitCoin__: _12toiKBQG8NukypFSd5qKvWCp1rtoPqyur_
* __LiteCoin__: _LXtAKuXqCKWD6AWnGqZ6iw7HduqCgsXMhR_
