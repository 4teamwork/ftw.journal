from DateTime import DateTime
from ftw.journal.config import JOURNAL_ENTRIES_ANNOTATIONS_KEY
from ftw.journal.events.events import JournalEntryEvent
from ftw.journal.interfaces import \
    IAnnotationsJournalizable, IWorkflowHistoryJournalizable
from ftw.journal.testing import FTW_JORUNAL_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID
from zope.annotation.interfaces import IAnnotations
from zope.event import notify
from zope.interface import alsoProvides
import unittest2 as unittest
from Products.CMFCore.utils import getToolByName


class TestFtwJournalIntegration(unittest.TestCase):

    layer = FTW_JORUNAL_INTEGRATION_TESTING

    def test_event_annotation(self):
        """ Test the event with IAnnotationsJournalizable interface
        """

        portal = self.layer['portal']
        folder = portal[portal.invokeFactory('Folder', 'f1', )]
        doc = folder[folder.invokeFactory('Document', 'd1', )]

        alsoProvides(doc, IAnnotationsJournalizable)

        notify(JournalEntryEvent(doc, "added new line", "modified"))

        journal = IAnnotations(doc).get(JOURNAL_ENTRIES_ANNOTATIONS_KEY)[0]

        self.assertTrue('modified' in journal.get('action'))
        self.assertTrue('added new line' in journal.get('comments'))
        self.assertTrue(TEST_USER_ID in journal.get('actor'))
        self.assertTrue(DateTime().Date() in journal.get('time').Date())

    def test_event_workflow_history(self):
        """ Test the event with IWorkflowHistoryJournalizable interface
        """

        portal = self.layer['portal']
        folder = portal[portal.invokeFactory('Folder', 'f1', )]
        doc = folder[folder.invokeFactory('Document', 'd1', )]

        wftool = getToolByName(doc, 'portal_workflow')
        wftool.manage_changeWorkflows('simple_publication_workflow')

        alsoProvides(doc, IWorkflowHistoryJournalizable)

        notify(JournalEntryEvent(doc, "new workflow", "modified"))

        journal = wftool.getStatusOf('simple_publication_workflow', doc)

        self.assertTrue('modified' in journal.get('action'))
        self.assertTrue('new workflow' in journal.get('comments'))
        self.assertTrue('private' in journal.get('review_state'))
        self.assertTrue(TEST_USER_ID in journal.get('actor'))
        self.assertTrue(DateTime().Date() in journal.get('time').Date())

    def test_journal_is_none_if_no_workflow_defined(self):
        """ Test the event with IWorkflowHistoryJournalizable interface
        """

        portal = self.layer['portal']
        folder = portal[portal.invokeFactory('Folder', 'f1', )]
        doc = folder[folder.invokeFactory('Document', 'd1', )]

        alsoProvides(doc, IWorkflowHistoryJournalizable)

        notify(JournalEntryEvent(doc, "new workflow", "modified"))

        wftool = getToolByName(doc, 'portal_workflow')
        journal = wftool.getStatusOf('simple_publication_workflow', doc)
        self.assertIsNone(journal)
