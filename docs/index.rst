Welcome to openaiapi's documentation!
=====================================

A light wrapper around the OpenAI API using `apiron <https://apiron.readthedocs.org>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference/modules
   glossary


Installation
------------

.. code-block:: shell

    $ python -m pip install openaiapi


Usage
-----

First, make an :envvar:`OPENAI_API_KEY` environment variable available whose value is your OpenAI API key.
Once you have an API key in place, you can use the :class:`OpenAI` class to generate content:

.. code-block:: python

    >>> from openaiapi import OpenAI
    >>> OpenAI.completions(json={"model": "text-davinci-003", "prompt": "What is your quest?"})
    {..., 'choices': [{'text': '\n\nMy quest is to find my purpose and fulfill it.', ...}], ...}}


See `the OpenAI documentation <https://beta.openai.com/docs/api-reference/introduction>`_ for the accepted/required parameters to each endpoint.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
