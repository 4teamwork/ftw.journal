from Acquisition import aq_inner
from ftw.journal.config import JOURNAL_ENTRIES_ANNOTATIONS_KEY
from persistent.dict import PersistentDict
from persistent.list import PersistentList
from plone.protect import utils
from uuid import uuid4
from zope.annotation.interfaces import IAnnotations, IAnnotatable
from zope.interface import alsoProvides


class AnnotationsJournalizable(object):
    """Adapter to create journal entries in an annotation"""

    def __init__(self, context):
        self.context = aq_inner(context)
        alsoProvides(self.context, IAnnotatable)

    def __call__(self, action, comment, actor, time):
        context = self.context
        annotations = IAnnotations(context)
        journal_annotations = annotations.get(JOURNAL_ENTRIES_ANNOTATIONS_KEY,
                                              None)

        if not journal_annotations:
            annotations[JOURNAL_ENTRIES_ANNOTATIONS_KEY] = PersistentList()
            journal_annotations = annotations.get(
                JOURNAL_ENTRIES_ANNOTATIONS_KEY)

        history_entry = PersistentDict({
                         'id': str(uuid4()),
                         'action': action,
                         'comments': comment,
                         'actor': actor,
                         'time': time,
                         })

        # If we have plone.protect > 3.0, mark the journal write as safe
        if 'safeWrite' in dir(utils):
            utils.safeWrite(context)
            utils.safeWrite(journal_annotations)

        journal_annotations.append(history_entry)
