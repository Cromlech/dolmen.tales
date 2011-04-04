# -*- coding: utf-8 -*-

import ast
from chameleon.tales import TalesExpr
from zope.component import getMultiAdapter
from cromlech.browser.interfaces import IViewSlot
from chameleon.codegen import template
from chameleon.astutil import Symbol


def query_slot(econtext, name):
    context = econtext['context']
    request = econtext['request']
    view = econtext['view']
    slot = getMultiAdapter((context, request, view), IViewSlot, name=name)
    slot.update()
    return slot.render()


class SlotExpr(object):
    """
    """
    def __init__(self, expression):
        self.expression = expression
    
    def __call__(self, target, engine):
        string = self.expression.strip()
        value = template(
            "query_slot(econtext, name)",
            query_slot=Symbol(query_slot),
            name=ast.Str(s=string),
            mode="eval"
            )
        return [ast.Assign(targets=[target], value=value)]
