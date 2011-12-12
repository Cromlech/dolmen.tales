# -*- coding: utf-8 -*-

import ast
from zope.schema import Dict
from zope.interface import Interface
from zope.component import getMultiAdapter
from cromlech.browser.interfaces import IViewSlot
from chameleon.codegen import template
from chameleon.astutil import Symbol


class IComposedView(Interface):

    shards = Dict(
        title=u'Slots used to render content',
        required=True)


def query_slot(econtext, name):
    """Compute the result of a slot expression
    """
    context = econtext['context']
    request = econtext['request']
    view = econtext['view']
    if IComposedView.providedBy(view):
        slot = view.shards.get(name)
    else:
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
