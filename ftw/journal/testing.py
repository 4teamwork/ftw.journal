from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from zope.configuration import xmlconfig
from plone.app.testing import applyProfile


class JournalFunctionalLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        from ftw import journal
        xmlconfig.file('configure.zcml', package=journal,
            context=configurationContext)

    def setUpPloneSite(self, portal):
        pass


FTW_JOURNAL_FIXTURE = JournalFunctionalLayer()
FTW_JORUNAL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FTW_JOURNAL_FIXTURE, ), name="FtwJournal:Integration")
