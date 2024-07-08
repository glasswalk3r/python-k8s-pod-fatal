Welcome to python-k8s-pod-fatal's documentation!
================================================

This package provies a Python exception that provides metadata to Kubernetes
Pods when they have a catastrophic failure.

Your Pod requires environment variables, but one of them is missing and you're
tired to go over the logs from the respective container just to figured that
out?

This package provides a customized Python exception that can help developers to
provide an appropriated error message to be logged when the application inside
a Kubernetes Pod (one or more Docker containers) has a error which is impossible
to recover, thus the Pod must be terminated.

This error message will be available when you describe the Pod with a
`kubectl describe` or `kubectl get`, which greatly helps with troubleshooting.

Usage of this module with a microsservice external dependencies failures is
even more interesting.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
