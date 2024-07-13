Usage
=====

Installation
------------

To use ``python_k8s_pod_fatal`` package, first install it using ``pip``:

.. code-block:: console

   (.venv) $ pip install python_k8s_pod_fatal


Using the exception
-------------------

Then, anywhere some module from your application:

.. code-block:: python

    import requests
    from kubernetes.pod.exceptions import Fatal

    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

    if r.status_code != 200:
        raise Fatal('HTTP request to GitHub failed')

When the exception is raised, the error message will be available not only in
the respective container log, but also in the ``pod.status.message`` from the
Kubernetes API.

Customized log file
-------------------

You can also use a customized log file (see References), but in order to do
you will need to pass an additional parameter to the ``Fatal`` constructor, which
defaults to ``/dev/termination-log``. If this file is not available (the default
file does exist), the instance won't try to write to it.

In this case, you probably want to change the configuration of the Pod and also
pass the same value as an environment variable to your code, better defined in
a single place.

See the ``tests`` of this module for an example.
