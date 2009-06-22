from zope.interface import implements

from ftw.journal.interfaces import IJournalEntryEvent


class JournalEntryEvent(object):
    """Event for journal entries"""
    implements(IJournalEntryEvent)
    
    def __init__(self, obj, comment, action=None, actor=None, time=None):
        self.object = obj
        self.action = action
        self.comment = comment
        self.actor = actor
        self.time = time
