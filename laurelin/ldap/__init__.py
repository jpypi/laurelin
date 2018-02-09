""" laurelin.ldap

Imports base objects for user import and defines user utility functions
"""

from __future__ import absolute_import
from .base import LDAP, LDAPURI
from .constants import Scope, DerefAliases
from .controls import critical, optional
from .exceptions import LDAPError, NoSearchResults, Abandon
from .ldapobject import LDAPObject

import pyasn1.type.univ


def dc(domain):
    """Convert a DNS dotted domain name to a DN with domain components"""
    return ','.join(['dc={0}'.format(dc) for dc in domain.split('.')])


def domain(dc):
    """Convert a DN with domain components to a DNS dotted domain name"""
    return '.'.join([i.split('=')[1] for i in dc.split(',')])


__all__ = [
    'LDAP',
    'LDAPURI',
    'Scope',
    'DerefAliases',
    'critical',
    'optional',
    'LDAPError',
    'NoSearchResults',
    'Abandon',
    'LDAPObject',
    'dc',
    'domain',
]


# make pyasn1 enumerated repr() consistant

def _enum_repr(enum_obj):
    try:
        intval = int(enum_obj)
        name = enum_obj.namedValues.getName(intval)
        namerepr = repr(name)
    except Exception:
        namerepr = '<schema object>'
    return '{0}({1})'.format(enum_obj.__class__.__name__, namerepr)


pyasn1.type.univ.Enumerated.__repr__ = _enum_repr
