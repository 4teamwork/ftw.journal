from zope.component.interfaces import IObjectEvent
from zope.interface import Interface, Attribute


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
