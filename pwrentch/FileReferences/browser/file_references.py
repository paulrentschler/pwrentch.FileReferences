from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class ReferenceListView(BrowserView):

    template = ViewPageTemplateFile('reference_list.pt')

    def __call__(self):
        """"""
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        current_path = '/'.join(self.context.getPhysicalPath())
        brains = portal_catalog(
            path={'query': current_path},
            portal_type='File',
            show_inactive=True
            )
        files = { }
        for brain in brains:
            obj = brain.getObject()
            extension = obj.absolute_url().split(".")[-1].upper()
            if extension == obj.absolute_url().upper():
                extension = "unknown"

            if not files.has_key(extension):
                files[extension] = [ ]
            files[extension].append(obj)


        self.files = files
        self.file_types = sorted(files.keys())
        self.hello_name = getattr(self.context, 'hello_name', 'World')
        return self.template()

    def getReferences(self, object):
        """"""
        reference_catalog = getToolByName(self.context, 'reference_catalog')
        references = reference_catalog.getBackReferences(object)
        return [ ref.getSourceObject() for ref in references ]
