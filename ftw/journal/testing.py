from pkg_resources import get_distribution
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from zope.configuration import xmlconfig

IS_PLONE_5 = get_distribution('Plone').version >= '5'

class JournalFunctionalLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        from ftw import journal
        xmlconfig.file('configure.zcml', package=journal,
            context=configurationContext)
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="z3c.autoinclude" file="meta.zcml" />'
            '  <includePlugins package="plone" />'
            '  <includePluginsOverrides package="plone" />'
            '</configure>',
            context=configurationContext)

    def setUpPloneSite(self, portal):

        from plone.app.testing import setRoles, TEST_USER_ID
        setRoles(portal, TEST_USER_ID, ['Member', 'Contributor', 'Editor'])
        if IS_PLONE_5:
            applyProfile(portal, 'plone.app.contenttypes:default')

FTW_JOURNAL_FIXTURE = JournalFunctionalLayer()
FTW_JORUNAL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FTW_JOURNAL_FIXTURE, ), name="FtwJournal:Integration")
