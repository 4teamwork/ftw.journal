from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName


class WorkflowHistoryJournalizable(object):
    """Adapter to create journal entries in the workflow history"""
    
    def __init__(self, context):
        self.context = aq_inner(context)

    def __call__(self, action, comment, actor, time):
        context = self.context
        workflow_tool = getToolByName(context, 'portal_workflow')
        
        workflow_id = workflow_tool.getWorkflowsFor(context)[0].id
        review_state = workflow_tool.getInfoFor(context, 'review_state', None)

        history_entry = {
                         'action' : action,
                         'review_state' : review_state,
                         'comments' : comment,
                         'actor' : actor,
                         'time' : time,
                         }
    
        workflow_tool.setStatusOf(workflow_id, context, history_entry)
