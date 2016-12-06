from Acquisition import aq_inner
from plone.protect import utils
from Products.CMFCore.utils import getToolByName


class WorkflowHistoryJournalizable(object):
    """Adapter to create journal entries in the workflow history"""

    def __init__(self, context):
        self.context = aq_inner(context)

    def __call__(self, action, comment, actor, time):
        context = self.context
        workflow_tool = getToolByName(context, 'portal_workflow')

        workflows = workflow_tool.getWorkflowsFor(context)

        if not workflows:
            return

        workflow_id = workflows[0].id
        review_state = workflow_tool.getInfoFor(context, 'review_state', None)

        history_entry = {
                         'action': action,
                         'review_state': review_state,
                         'comments': comment,
                         'actor': actor,
                         'time': time,
                         }

        # If we have plone.protect > 3.0, mark the journal write as safe
        if 'safeWrite' in dir(utils):
            utils.safeWrite(context)
            utils.safeWrite(review_state)

        workflow_tool.setStatusOf(workflow_id, context, history_entry)
