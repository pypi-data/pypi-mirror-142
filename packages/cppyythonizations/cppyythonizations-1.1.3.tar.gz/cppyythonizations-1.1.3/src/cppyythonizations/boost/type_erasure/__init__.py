r"""
Improves support for ``boost::type_erasure::any``.

EXAMPLES:

Let us consider a type erasure for any type that has an ``empty`` method, like
various STL containers::

    >>> import cppyy
    >>> cppyy.include("boost/type_erasure/any.hpp")
    >>> cppyy.cppdef(r"""
    ... #include <boost/type_erasure/member.hpp>
    ... BOOST_TYPE_ERASURE_MEMBER((has_member_empty), empty, 0);
    ... struct EmptyInterface : boost::mpl::vector<
    ...   boost::type_erasure::copy_constructible<>,
    ...   has_member_empty<bool() const>,
    ...   boost::type_erasure::typeid_<>,
    ...   boost::type_erasure::relaxed> {};
    ... using any_empty = boost::type_erasure::any<EmptyInterface>;
    ...
    ... template <typename T, typename S>
    ... auto wrap(S&& s) {
    ...   T t = std::forward<S>(s);
    ...   return t;
    ... }
    ... """)

Currently, cppyy fails to create such an ``any`` directly::

    >>> v = cppyy.gbl.std.vector[int]()
    >>> cppyy.gbl.any_empty(v)
    Traceback (most recent call last):
    ...
    TypeError: Template method resolution failed...

This module provides a helper to create such an ``any``::

    >>> from cppyythonizations.boost.type_erasure import any
    >>> any(cppyy.gbl.any_empty)(v)

Currently, cppyy is having trouble to detect methods on a ``boost::type_erasure::any``::

    >>> cppyy.include("vector")
    >>> erased_vector = cppyy.gbl.any_empty(cppyy.gbl.std.vector[int]())
    >>> hasattr(erased_vector, 'empty')

These methods can be explicitly made visible::
"""
# ********************************************************************
#  This file is part of cppyythonizations.
#
#        Copyright (C) 2022 Julian Rüth
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ********************************************************************
import cppyy

cppyy.cppdef(r'''
namespace cppyythonizations
namespace boost{
namespace type_erasure {

template <typename ANY>
struct any {
    template <typename T>
    static auto make(T&& value) {
        ANY x = std::forward<T>(value);
        return x;
    }
};

}
}
}
''')

def any(type):
    return cppyy.gbl.cppyythonizations.boost.type_erasure.any[type].make
