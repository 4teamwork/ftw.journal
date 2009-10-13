from Acquisition import aq_inner

from zope.annotation.interfaces import IAnnotations, IAnnotatable
from zope.interface import alsoProvides

from Products.CMFCore.utils import getToolByName

from ftw.journal.config import JOURNAL_ENTRIES_ANNOTATIONS_KEY


class AnnotationsJournalizable(object):
    """Adapter to create journal entries in an annotation"""
    
    def __init__(self, context):
        self.context = aq_inner(context)
        alsoProvides(self.context, IAnnotatable)

    def __call__(self, action, comment, actor, time):
        context = self.context
        annotations = IAnnotations(context)
        journal_annotations = annotations.get(JOURNAL_ENTRIES_ANNOTATIONS_KEY, None)
        
        if not journal_annotations:
            annotations[JOURNAL_ENTRIES_ANNOTATIONS_KEY] = []
            journal_annotations = annotations.get(JOURNAL_ENTRIES_ANNOTATIONS_KEY, None)

        history_entry = {
                         'action' : action,
                         'comments' : comment,
                         'actor' : actor,
                         'time' : time,
                         }
    
        journal_annotations.append(history_entry)
        context.context._p_changed = True
