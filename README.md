# python-k8s-pod-fatal

A Python exception that provides metadata to Kubernetes Pods when they have a
catastrophic failure.

## Description

Your Pod requires environment variables, but one of them is missing and you're
tired to go over the logs from the respective container just to figured that
out?

The package `python_k8s_pod_fatal` provides a customized Python exception that
can help developers to provide an appropriated error message to be logged when
the application inside a Kubernetes Pod (one or more Docker containers) has a
error which is impossible to recover, thus the Pod must be terminated.

This error message will be available when you describe the Pod with a
`kubectl describe` or `kubectl get`, which greatly helps with troubleshooting.

Usage of this module with a microsservice external dependencies failures is
even more interesting.

## How to use

Install the module from Pypi:

```
pip install --upgrade python_k8s_pod_fatal
```

Then, anywhere some module from your application:

```python
import requests
from kubernetes.pod.exceptions import Fatal

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

if r.status_code != 200:
    raise Fatal('HTTP request to GitHub failed')

```

When the exception is raised, the error message will be available not only in
the respective container log, but also in the `pod.status.message` from the
Kubernetes API.

### Customized log file

You can also use a customized log file (see References), but in order to do
you will need to pass an additional parameter to the `Fatal` constructor, which
defaults to `/dev/termination-log`. If this file is not available (the default
file does exist), the instance won't try to write to it.

In this case, you probably want to change the configuration of the Pod and also
pass the same value as an environment variable to your code, better defined in
a single place.

See the `tests` of this module for an example.

## References

- [Determine the reason of a Pod failure](https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/#customizing-the-termination-message)
- [Python3 concrete exceptions](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)
