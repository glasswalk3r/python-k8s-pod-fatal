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
