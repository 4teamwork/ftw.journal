from ftw.journal.adapters.annotations_journal import AnnotationsJournalizable
from ftw.journal.adapters.workflow_history_journal import \
    WorkflowHistoryJournalizable
from ftw.journal.config import JOURNAL_ENTRIES_ANNOTATIONS_KEY
from mocker import ANY
from persistent.list import PersistentList
from plone.mocktestcase import MockTestCase
from Products.CMFCore.WorkflowTool import WorkflowTool
from zope.annotation.interfaces import IAnnotations
from zope.interface import Interface


class TestFtwJournalAdapters(MockTestCase):

    def test_annotations_journal(self):
        """ Test annotations journal adapter
        """
        # Context
        mock_context = self.create_dummy()

        # Annotation-Adapter
        annotation_adapter = dict()
        annotation_adapter['ftw.journal.journal_entries_annotations_key'] = []
        mock_annotation_adapter = self.mocker.proxy(
            annotation_adapter, spec=None)
        self.expect(
            mock_annotation_adapter(mock_context)).call(
                lambda a: mock_annotation_adapter).count(0, None)
        self.expect(
            mock_annotation_adapter.get(ANY, ANY)).result(PersistentList())
        self.mock_adapter(mock_annotation_adapter, IAnnotations, [Interface])


        self.replay()

        adapter = AnnotationsJournalizable(mock_context)
        adapter('save', 'saved new file', 'ratman', '15:18', )

        # Checks
        values = mock_annotation_adapter.get(
            JOURNAL_ENTRIES_ANNOTATIONS_KEY)[0].values()
        self.assertIn('save', values)
        self.assertIn('saved new file', values)
        self.assertIn('ratman', values)
        self.assertIn('15:18', values)
        self.assertTrue(adapter.context._p_changed)

    def test_workflow_history_journal(self):
        """ Test workflow history journal adapter
        """
        # Context
        mock_context = self.create_dummy()

        # Workflow
        mock_wf = self.mocker.mock()
        self.expect(mock_wf.id).result('wf-published')

        # Workflowtool
        wftool = WorkflowTool()
        mock_wftool = self.mocker.proxy(wftool, spec=None)
        self.expect(mock_wftool.getWorkflowsFor(ANY)).result([mock_wf])
        self.expect(mock_wftool.getInfoFor(ANY, ANY, ANY)).result('published')

        self.mock_tool(mock_wftool, 'portal_workflow')

        self.replay()

        adapter = WorkflowHistoryJournalizable(mock_context)
        adapter('save', 'saved new file', 'ratman', '15:18', )

        # Get the saved values
        values = mock_context.workflow_history.get('wf-published')[0].values()

        # Checks
        self.assertIn('save', values)
        self.assertIn('published', values)
        self.assertIn('saved new file', values)
        self.assertIn('ratman', values)
        self.assertIn('15:18', values)
