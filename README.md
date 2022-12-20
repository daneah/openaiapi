# openaiapi

A light wrapper around the OpenAI API using [apiron](https://apiron.readthedocs.org).

## Installation

```shell
$ python -m pip install openaiapi
```

## Usage

First, make an `OPENAI_API_KEY` environment variable available whose value is your OpenAI API key. Once you have an API key in place, you can use the `OpenAI` class to generate content:

```python
>>> from openaiapi import OpenAI
>>> OpenAI.completions(json={"model": "text-davinci-003", "prompt": "What is your quest?"})
{..., 'choices': [{'text': '\n\nMy quest is to find my purpose and fulfill it.', ...}], ...}}
```

See the package documentation for the full list of available endpoints, and see [the OpenAI documentation](https://beta.openai.com/docs/api-reference/introduction) for the accepted/required parameters to each endpoint.
