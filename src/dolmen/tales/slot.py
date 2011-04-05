# -*- coding: utf-8 -*-

import ast
from chameleon.tales import TalesExpr
from zope.component import getMultiAdapter
from cromlech.browser.interfaces import IViewSlot
from chameleon.codegen import template
from chameleon.astutil import Symbol


def query_slot(econtext, name):
    """Compute the result of a slot expression
    """
    context = econtext['context']
    request = econtext['request']
    view = econtext['view']
    slot = getMultiAdapter((context, request, view), IViewSlot, name=name)
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
