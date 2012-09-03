# -*- coding: utf-8 -*-

import ast
from zope.component import getMultiAdapter
from cromlech.browser.interfaces import IViewSlot
from chameleon.codegen import template
from chameleon.astutil import Symbol


def render_slot(slot):
    slot.update()
    return slot.render()


try:
    # We might has zope.security
    from zope.security._proxy import _Proxy as Proxy

    def resolve_slot(slot):
        """If slot is a Proxy, we need to check the security.
        If not, we render it.
        """
        if type(slot) is Proxy:
            if (zope.security.canAccess(slot, 'update') and
                zope.security.canAccess(slot, 'render')):
                return render_slot(slot)
            else:
                return u''
        else:
            return render_slot(slot)

except ImportError:
    resolve_slot = render_slot


def query_slot(econtext, name):
    """Compute the result of a slot expression
    """
    context = econtext.get('context')
    request = econtext.get('request')
    view = econtext.get('view')
    slot = getMultiAdapter((context, request, view), IViewSlot, name=name)
    return resolve_slot(slot)


class SlotExpr(object):
    """
    This is the interpreter of a slot: expression
    """
    def __init__(self, expression):
        self.expression = expression

    def __call__(self, target, engine):
        slot_name = self.expression.strip()
        value = template(
            "query_slot(econtext, name)",
            query_slot=Symbol(query_slot),  # ast of query_slot
            name=ast.Str(s=slot_name),  # our name parameter to query_slot
            mode="eval")
        return [ast.Assign(targets=[target], value=value)]
