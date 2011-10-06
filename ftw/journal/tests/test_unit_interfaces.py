from ftw.journal.interfaces import IJournalEntryEvent, IJournalizable, \
    IWorkflowHistoryJournalizable, IAnnotationsJournalizable, IJournalizer
from plone.mocktestcase import MockTestCase
from zope.interface import directlyProvides


class TestFtwJournalInterfaces(MockTestCase):

    def test_IJournalEntryEvent(self):
        """ Test event interface
        """
        self.interface_test(IJournalEntryEvent)

        # Test attributes of event
        self.assertNotEquals(IJournalEntryEvent.get('action'), None)
        self.assertNotEquals(IJournalEntryEvent.get('comment'), None)
        self.assertNotEquals(IJournalEntryEvent.get('actor'), None)
        self.assertNotEquals(IJournalEntryEvent.get('time'), None)

    def test_IJournalizable(self):
        """ Test makrer interface
        """
        self.interface_test(IJournalizable)

    def test_IWorkflowHistoryJournalizable(self):
        """ Test makrer interface
        """
        self.interface_test(IWorkflowHistoryJournalizable)

    def test_IAnnotationsJournalizable(self):
        """ Test makrer interface
        """
        self.interface_test(IAnnotationsJournalizable)

    def test_IJournalizer(self):
        """ Test makrer interface
        """
        self.interface_test(IJournalizer)

    def interface_test(self, i):
        """ Testmethod for interfaces"""
        obj = self.create_dummy()
        directlyProvides(obj, i)

        self.assertTrue(i(obj) == obj)
