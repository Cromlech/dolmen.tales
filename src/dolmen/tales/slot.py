# -*- coding: utf-8 -*-

import ast
from crom import ComponentLookupError
from cromlech.browser.interfaces import IViewSlot
from chameleon.codegen import template
from chameleon.astutil import Symbol

try:
    from cromlech.security import getSecurityGuards

except ImportError:

    def getSecurityGuards():
        return None, None


def query_slot(econtext, name):
    """Compute the result of a slot expression
    """
    context = econtext.get('context')
    request = econtext.get('request')
    view = econtext.get('view')
    security_predict, security_check = getSecurityGuards()
    try:
        factory = IViewSlot.component(context, request, view, name=name)
        if security_predict is not None:
            factory = security_predict(factory, swallow_errors=True)
            if factory is None:
                return ''  # Security predicates failed.

        slot = factory(context, request, view)
        if security_check is not None:
            slot = security_check(slot)
            if slot is None:
                return ''  # Security checks failed.

    except ComponentLookupError:
        raise
    else:
        slot.update()
        return slot.render()
    

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
