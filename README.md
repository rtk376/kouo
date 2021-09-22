DESCRIPTION
-----------
This project contains the coding task set by Kouo as part of the interview process.

This project is a simple Python 3 CLI interface to retrieve top N starred repositories
of a given Github user, sorted by the highest star count.

REQUIREMENTS    
------------
For this project the following packages are required:

PyGithub, version 1.55

To install the dependencies, run

```
pip install -r requirements.txt
```

or install PyGithub manually.

USAGE
-----
The program can take in up to two arguments, `-u, --username` and
`-t, --top`. 

`--username` is  a required argument and takes in a Github username.

`--top` is an optional argument that takes in a integer, N, to show
the top N starred repositories of the given user. Default N=5.

Please clone the repository, e.g. `git clone https://github.com/rtk376/kouo.git`, 
and install the dependencies.
## Example

```
python kouo -u fabpot -t 6
```
Output:
```
Username: fabpot

Top 6 starred repositories:
Repository: local-php-security-checker, Star Count: 700
Repository: symfony, Star Count: 369
Repository: sphinx-php, Star Count: 163
Repository: Silex, Star Count: 116
Repository: Twig, Star Count: 80
Repository: Pimple, Star Count: 77

```

NOTES
-----
`setup.py` is not provided and the installation of this package is not supported
due to the simplicity of the task.
