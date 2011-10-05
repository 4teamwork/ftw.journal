from ftw.journal.events.events import JournalEntryEvent
from ftw.journal.events.handlers import JournalEntryHandler
from ftw.journal.interfaces import IJournalizer
from plone.mocktestcase import MockTestCase
from zope.interface import Interface
from mocker import ANY
from DateTime import DateTime


class TestFtwJournalEvents(MockTestCase):

    def test_event(self):
        """ Test the events module
        """
        # Context
        mock_context = self.create_dummy()

        event = JournalEntryEvent(
            mock_context,
            'new entry',
            'save',
            'ratman',
            '15:18', )

        # Checks
        self.assertTrue(mock_context ==  event.object)
        self.assertIn('save', event.action)
        self.assertIn('new entry', event.comment)
        self.assertIn('ratman', event.actor)
        self.assertIn('15:18', event.time)

    def test_handler_not_journalizable(self):
        """ Test the handler module with no provided journalizable adapter
        """
        values = self.handler_base(journalizable=False)
        self.assertTrue(values == {})

    def test_handler_with_attrs(self):
        """ Test the handler module with all attributes"""

        values = self.handler_base(
            'new entry',
            'ratman',
            '15:18',
            'save', ).values()

        self.assertIn('save', values)
        self.assertIn('new entry', values)
        self.assertIn('ratman', values)
        self.assertIn('15:18', values)

    def test_handler_empty_attrs(self):
        """ Test the handler module with empty attrs
        """

        values = self.handler_base()

        # We just have to check the date
        time = values.get('time').Date()
        values = values.values()

        self.assertIn('label_journal_entry', values)
        self.assertIn('ratman', values)
        self.assertIn(DateTime().Date(), time)

    def handler_base(
        self,
        comment='',
        actor=None,
        time=None,
        action=None,
        journalizable=True):
        """ Basetest for the handler module
        """

        class JournalizableAdapter(object):
            """ This Class we use to store the data because we
            don't want to test the adapters and can't mock the storing
            """
            values = {}

            def __call__(self, action, comment, actor, time):
                self.values = {'action': action,
                               'comment': comment,
                               'actor': actor,
                               'time': time, }

        # Context
        mock_context = self.create_dummy()
        mock_context.REQUEST = 'portal_state'

        # Portal State
        mock_portal_state = self.mocker.mock(count=False)
        self.expect(
            mock_portal_state(ANY, mock_context.REQUEST)).result(
                mock_portal_state)
        self.expect(mock_portal_state.member().getId()).result(
            'ratman')

        self.mock_adapter(mock_portal_state, Interface, [Interface, Interface], 'plone_portal_state')

        # Adapter for IJournalizer
        mock_journalizable = self.mocker.proxy(
            JournalizableAdapter(), spec=False)
        self.expect(
            mock_journalizable(mock_context)).result(
                mock_journalizable).count(0, None)

        if journalizable:
            self.mock_adapter(mock_journalizable, IJournalizer, [Interface])

        # Event
        mock_event = self.mocker.mock(count=False)
        self.expect(mock_event.object).result(mock_context)
        self.expect(mock_event.comment).result(comment)
        self.expect(mock_event.actor).result(actor)
        self.expect(mock_event.time).result(time)
        self.expect(mock_event.action).result(action)

        self.replay()

        # Call function
        JournalEntryHandler(mock_event)

        # Return the values
        return mock_journalizable.values