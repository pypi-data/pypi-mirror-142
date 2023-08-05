# db-join

I realized during my personal journey using Google Datastore that I was doing something
very often on a set of DB entities.  That is, I had foreign key references on various
fields in an entity and wanted to load the entities refenced by those keys.  Additionally,
I wanted to control which entities are loaded with some syntactic sugar and I wanted to
do it efficienntly.

Hence the birth of db-join -- a NoSQL version of join semantics you get with a SQL db.


## Basics

First, create an instance of a _joiner_.  Right now, only `DatastoreJoin` class exists
but I hope overtime other NoSQL dbs wrappers can be added.

    >>> import join
    >>> joiner = join.api.DatastoreJoin()

Next, given a iterable (typically via query), _join_ against all the fields you wish.

    >>> iterable = joiner(client, iterable, ('field1', 'field2'))

What this does is discovers if the DB keys referenced by `field1` and `field2` (if any)
and does a `get_multi` on this keys and the _mutates_ the db object with those discovered
entities.  Thus, after the join both `field1` and `field2` will refer to entities (instead
of keys) assuming they are in fact keys and those keys do in fact refer to db entities.


## Dotted notation

These fields may actually be dotted patterns as documented in the `dotted-notation`
package.  Dotted notation permits you to fetch an item inside a deeply nested
datastructure.

    >>> d = {'hello': {'there': [{'a': 1, 'b': 2}, {'a': 7, 'b': 8}]}}
    >>> dotted.get(d, 'hello.there[1].b') == 8

Thus, if your DB entity has a list of keys OR something nested you can specify how to
fetch it.  For example,

    >>> joiner(client, iterable, 'list_of_keys[*]')

This will join on all keys contained in a list referenced by `list_of_keys`.


## Chaining

But that's not all.  A _pattern_ may also use chaining notation:

    >>> joiner(client, iterable, 'field1->another_field')

This will fetch the object at `field1` and then fetch that object's the object at
`another_field`.


## Replacing

Turns out sometimes you want to replace the object with a referenced object.  The `!`
operator lets you do this:

    >>> joiner(client, iterable, '!field1')

This will replace the object at yielded by iterable with whatever object was found
at `field1`.  Note that this works with chaining as well.

    >>> joiner(client, iterable, 'field1->!symlink')

This will replace `field1` with whatever was found in `symlink`.


## Recursive chaining

Similar to replacing, sometimes you want to recursively expand objects that are linked
via the same field.  The `+` operator lets you do this:

    >>> joiner(client, iterable, '+field')

This will fetch the object at `field`. If that object also has `field`, then it will
fetch the object at that object's `field` and so on until there's no more work.

## Internals

A `Join` class has a number of abstractions to help you out.  The two most important are
the `getter` and the `setter`.  These methods are called whenever you're getting a value
of a field that matches _pattern_ and when you're setting that value.

The default behavior is to just use `dotted.get` and `dotted.update` respectively.

