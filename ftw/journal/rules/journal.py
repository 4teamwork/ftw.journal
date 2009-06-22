from Acquisition import aq_inner
from OFS.SimpleItem import SimpleItem
from zope.component import adapts
from zope.component.interfaces import ComponentLookupError
from zope.component.interfaces import IObjectEvent
from zope.interface import Interface, implements
from zope.formlib import form
from zope.event import notify 
from zope import schema

from plone.app.contentrules.browser.formhelper import AddForm, EditForm 
from plone.contentrules.rule.interfaces import IRuleElementData, IExecutable

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from ftw.journal.events.events import JournalEntryEvent
from ftw.journal import journalMessageFactory as _


class IJournalAction(Interface):
    """Definition of the configuration available for a mail action
    """
    action = schema.TextLine(title=_(u"Action"),
                             description=_(u"A title that will be used in the 'action' field of the journal entry."),
                             required=True)
    comment = schema.TextLine(title=_(u"Comment"),
                              description=_(u"A description that will be used in the 'comment' field in the journal entry."),
                              required=True)

class JournalAction(SimpleItem):
    """
    The implementation of the action defined before
    """
    implements(IJournalAction, IRuleElementData)

    action = u''
    comment = u''

    element = 'ftw.journal.JournalAction'

    @property
    def summary(self):
        return _(u"Journal action ${action}", mapping={'action' : self.action})

class JournalActionExecutor(object):
    """The executor for this action.
    """
    implements(IExecutable)
    adapts(Interface, IJournalAction, IObjectEvent)

    def __init__(self, context, element, event):
        self.context = context
        self.element = element
        self.event = event

    def __call__(self):
        action = self.element.action
        comment = self.element.comment
        obj = self.event.object

        notify(JournalEntryEvent(obj, comment, action))

        return True

class JournalAddForm(AddForm):
    """
    An add form for the journal action
    """
    form_fields = form.FormFields(IJournalAction)
    label = _(u"Add Journal Action")
    description = _(u"A journal action makes an entry into the journal of an object.")
    form_name = _(u"Configure element")

    def create(self, data):
        a = JournalAction()
        form.applyChanges(a, self.form_fields, data)
        return a

class JournalEditForm(EditForm):
    """
    An edit form for the journal action
    """
    form_fields = form.FormFields(IJournalAction)
    label = _(u"Edit Journal Action")
    description = _(u"A journal action makes an entry into the journal of an object.")
    form_name = _(u"Configure element")
