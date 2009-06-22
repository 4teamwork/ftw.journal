from zope.component import getMultiAdapter

from DateTime import DateTime

from ftw.journal.interfaces import IJournalizer
from ftw.journal import journalMessageFactory as _


def JournalEntryHandler(event):
    """
    """
    obj = event.object
    comment = event.comment

    try:
        journalizable = IJournalizer(obj)
    except:
        return
    
    if event.action is None:
        action = _(u"label_journal_entry", default=u"Journal Entry")
    else:
        action = event.action

    if event.actor is None:
        portal_state = getMultiAdapter((obj, obj.REQUEST), name=u'plone_portal_state')
        actor = portal_state.member().getId()
    else:
        actor = event.actor
 
    if event.time is None:
        time = DateTime()
    else:
        time = event.time
    
    journalizable(action, comment, actor, time)
