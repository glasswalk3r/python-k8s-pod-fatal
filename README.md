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

## More information

Please visit [readthedocs.io](https://python-k8s-pod-fatal.readthedocs.io/en/latest/)
for more details on this project.
