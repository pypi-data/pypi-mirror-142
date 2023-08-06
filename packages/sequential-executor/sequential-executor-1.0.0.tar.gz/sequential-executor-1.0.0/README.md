# sequential-executor

A [concurrent.futures.Executor](https://docs.python.org/3/library/concurrent.futures.html#executor-objects) implementation that performs sequential execution.

While this micro-library may seem a little oxymoronic (Executors are, after all,
meant to execute calls asynchronously), it does have a fairly well-defined use case.

## Use case
A Python package that performs multiple operations via callback(s) defined by implementors
using that package. The package allows the implementor to define the concurrent execution environment
by passing in a `concurrent.futures.Executor` object.

This allows the implementor to tailor the execution environment based upon the work that their callback will be performing. For example, if they are making web calls (e.g. - IO bound) they could pass in a `ThreadPoolExecutor`, but if they are doing numpy analysis of large datasets (e.g. - CPU bound), they could pass in a `ProcessPoolExecutor`. But what if the implementor must enforce sequential execution, such as for ordered message processing?

The `SequentialExecutor` provided by this package allows for the implementor using the hypothetical Python package to give that package an `Executor`, but forces the execution environment into seqential ordering.

## Installation
```bash
pip install sequential-executor
```

## SequentialExecutor Example
```python
import concurrent.futures
import urllib.request

import sequential_executor

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    print('loading %r' % url)
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use in a with statement just like other Executors
with sequential_executor.SequentialExecutor() as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
```

> NOTE - Although this looks like it is submitting multiple jobs and then waiting
on each job to complete, the `concurrent.futures.Future` objects returned by the
`SequentialExecutor` *will be fully complete upon the return from the* `submit` *call!*
