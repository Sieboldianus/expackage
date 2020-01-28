
# expackage

ExamplePackage: demonstrates joblib/loky multiprocessing Issue in frozen executables

This repository should function as a minimal reproducible example for an issue that occurs with joblib/loky multiprocessing used in a frozen executable.

There are several branches that demonstrate different approaches, all leading to either a) a crash or b) a multiprocessing bomb

Branches:

* **pool** use of `multiprocessing.Pool`
* **threadpool** use of `multiprocessing.ThreadPool`
* **queuethread** use of `queue.Queue()`and `threading.Thread`
* **contextpool** use of `multiprocessing.get_context("spawn").Pool()`

