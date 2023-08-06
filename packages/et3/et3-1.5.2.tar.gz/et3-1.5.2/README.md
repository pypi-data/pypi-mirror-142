# et3

A simple library for Extracting and Transforming data, third incarnation.

## install

    $ pip install et3

## usage

You have a description of your data in the form of a dictionary, with 
each key's value being a list of transformers. This description is
applied to a list of items using the `render` and `render_item` functions.
The first transformer in the list of transformers receives the item, the
next element receives the result of the previous transformation and so on.

Examples:

* [example.py](example.py)
* [test_render.py](et3/tests/test_render.py)
* [bot-lax-adaptor](https://github.com/elifesciences/bot-lax-adaptor/blob/develop/src/main.py)
