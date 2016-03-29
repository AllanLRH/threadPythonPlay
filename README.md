# threadPlay

This branch uses the multiprocessing.dummy features to provide threading.

Used for obtaining results from `brew info PACKAGENAME` throught the _subprocessing_ module, since the call is places outside of the GIL.

Testing for speed (_concurrent.features_ module method seems faster):

```
threadPythonPlay git/master
(py35)❯ time ./threadPlay.py > /dev/null
./threadPlay.py > /dev/null  1.78s user 0.34s system 241% cpu 0.880 total

threadPythonPlay git/master
(py35)❯ git checkout multiprocessing_dummy_pool
Switched to branch 'multiprocessing_dummy_pool'

threadPythonPlay git/multiprocessing_dummy_pool
(py35)❯ time ./threadPlay.py > /dev/null
./threadPlay.py > /dev/null  1.97s user 0.37s system 228% cpu 1.024 total
```
