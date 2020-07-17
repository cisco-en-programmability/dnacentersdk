# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2017-2018 Nuxt.js Team
- León Domingo ([@codevincedev](https://github.com/codevincedev))

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import json


class MyDict(dict):
    """A **Python** _dict_ subclass which tries to act like **JavaScript**
    objects, so you can use the **dot notation** (.) to access members of
    the object.
    If the member doesn't exist yet then it's created when you assign
    something to it.
    Brackets notation (d['foo']) is also possible.
    """

    def __init__(self, dict_source=None, **kw):
        if dict_source and isinstance(dict_source, (dict, MyDict)):
            for k, v in dict_source.items():
                self[k] = self._transform(v)

        for key, value in kw.items():
            self[key] = self._transform(value)

    def _transform(self, source):
        if isinstance(source, (dict, MyDict)):
            return MyDict(source)

        elif isinstance(source, list):
            return [item for item in map(self._transform, source)]

        elif isinstance(source, tuple):
            result = None
            for item in source:

                if not result:
                    result = (self._transform(item),)

                else:
                    result = result + (self._transform(item),)

            return result

        else:
            # no need for transformation (int, float, str, set, ...)
            return source

    def __getattr__(self, name):
        """
        Get a field "name" from the object in the form:
            obj.name
        """
        if name in self:
            return self[name]

    def __setattr__(self, name, value):
        """
        Sets a field into the object in the form:
            obj.name = value
        """
        self[name] = self._transform(value)

    def __getitem__(self, name):
        """
        Get a field "key" value from the object in the form:
            obj[name]
        """
        return self.get(name)

    def has_path(self, key):
        """
        Check existence of "path" in the tree.

        .. code-block:: python

            d = MyDict({'foo': {'bar': 'baz'}})
            d.has_path('foo.bar') == True

        It only supports "dot-notation" (d.foo.bar)
        """
        if super(MyDict, self).__contains__(key):
            return True

        else:
            parts = str(key).split('.')
            if len(parts) > 1:
                k = '.'.join(parts[:1])
                return self[k].has_path('.'.join(parts[1:]))

            else:
                return super(MyDict, self).__contains__(key)

    def get(self, key, default=None):
        if key in self:
            return super(MyDict, self).get(key, default)

        else:
            parts = str(key).split('.')
            if len(parts) > 1:
                try:
                    return self.get(parts[0]).get('.'.join(parts[1:]))

                except Exception:
                    return None

            else:
                return super(MyDict, self).get(key, default)

    def to_json(self):
        """Returns a JSON-like string representing this instance"""
        return json.dumps(self.get_dict())

    def get_dict(self):
        """Returns a <dict> of the <MyDict> object"""

        def _get_dict(member):

            if isinstance(member, (dict, MyDict)):
                d = {}
                for k, v in member.items():
                    d[k] = _get_dict(v)

                return d

            elif isinstance(member, (list,)):
                lst = []
                for a in member:
                    lst.append(_get_dict(a))

                return lst

            elif isinstance(member, (tuple,)):
                tpl = tuple()
                for a in member:
                    tpl = tpl + (_get_dict(a),)

                return tpl

            elif isinstance(member, (set,)):
                st = set([])
                for a in member:
                    st.add(_get_dict(a))

                return st

            else:
                return member

        return _get_dict(self)

    def __getstate__(self):
        """
        Returns a <dict> of the <MyDict> object
        - enables Pickle to work
        """
        # Uses the inherited 'copy' method from builtins.dict
        return self.copy()

    def __setstate__(self, state):
        """
        Replaces all <MyDict> items with the <dict> items
        - enables Pickle to work
        """
        #  Uses the inherited
        #  'copy', 'clear' and 'update' methods from builtins.dict.
        current_state = self.copy()
        #  Removes previous items
        self.clear()
        try:
            #  Updates items
            self.update(**state)
        except Exception as e:
            #  Restores items
            self.update(**current_state)
            raise e


def mydict_data_factory(model, json_data):
    """Data factory function with standard params."""
    # Uses kw (json_data =) to handle array responses.
    # Returns .json_data as is not important.
    return MyDict(json_data=json_data).json_data
