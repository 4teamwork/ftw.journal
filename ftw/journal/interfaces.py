from zope import schema
from zope.interface import Interface, Attribute
from zope.component.interfaces import IObjectEvent

from ftw.journal import journalMessageFactory as _


class IJournalEntryEvent(IObjectEvent):
    """An event that can be fired to make a journal entry
    """

    action = Attribute("")
    comment = Attribute("")
    actor = Attribute("")
    time = Attribute("")


class IJournalizable(Interface):
    """Marker interface for objects that can have journal entries set on themselves
    """


class IWorkflowHistoryJournalizable(IJournalizable):
    """Marker interface for objects that store journal entries in the workflow history
    """


class IAnnotationsJournalizable(IJournalizable):
    """Marker interface for objects that store journal entries in an annotation
    """


class IJournalizer(Interface):
    """Interface for 
    """
