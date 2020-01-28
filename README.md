
# expackage

ExamplePackage: demonstrates joblib/loky multiprocessing Issue in frozen executables

This repository should function as a minimal reproducible example for an issue that occurs with joblib/loky multiprocessing used in a frozen executable.

There are several branches that demonstrate different approaches, all leading to either a) a crash or b) a multiprocessing bomb

Branches:

* **pool** use of `multiprocessing.Pool`
* **threadpool** use of `multiprocessing.ThreadPool`
* **queuethread** use of `queue.Queue()`and `threading.Thread`
* **contextpool** use of `multiprocessing.get_context("spawn").Pool()`

Builds:

Download builds for each branch:

* [expackage-0.0.1-win-amd64-3.7-pool.zip][1]
* [expackage-0.0.1-win-amd64-3.7-threadpool.zip][2]
* [expackage-0.0.1-win-amd64-3.7-queuethread.zip][3]
* [expackage-0.0.1-win-amd64-3.7-contextpool.zip][4]

Logs (`expackage.exe` cli-mode):

* [pool.log](logs/pool.log)
    - cluster function returns results
    - after "Press any key to exit...": `OSError: [WinError 87] The parameter is incorrect`

* [queuethread.log](logs/queuethread.log)
    - multiprocessing bomb, failing with:
    ```
    joblib.externals.loky.process_executor.TerminatedWorkerError: A worker process managed by the executor was unexpectedly terminated.
    ...
    ERROR: The process "16800" not found.
    ERROR: The process "7964" not found.
    ERROR: The process "13552" not found.
    ERROR: The process "17616" not found.
    ```
* [threadpool.log](logs/threadpool.log)
    - equal to queuethread

* contextpool (existing pool object)
    - no error, but slow

[1]: https://www.dropbox.com/s/ia4iumvh1zsoev9/expackage-0.0.1-win-amd64-3.7-pool.zip?dl=0
[2]: https://www.dropbox.com/s/r02nn6mqhcm4arb/expackage-0.0.1-win-amd64-3.7-threadpool.zip?dl=0
[3]: https://www.dropbox.com/s/qt0sw8cjihx9wft/expackage-0.0.1-win-amd64-3.7-queuethread.zip?dl=0
[4]: https://www.dropbox.com/s/8cfuasihr1xvzc6/expackage-0.0.1-win-amd64-3.7-contextpool.zip?dl=0