from helpers.templates import serve_template
from google.appengine.ext.db import ReferenceProperty


class Base(object):
    def __init__(self, model_class):
        self.model_class = model_class
        self.template_path = "%s/" % self.model_class.__name__

    def GET(self, key=None):
        if key is None:
            return serve_template(self.template_path + "index.mako", collection=self.model_class.all())
        else:
            props = sorted(self.model_class.properties().items(), key=lambda (k, v): v.creation_counter)
            if key == "0":
                return serve_template(self.template_path + "create.mako",
                                      model=self.model_class,
                                      props=props)
            else:
                instance = self.model_class.get(key)
                return serve_template(self.template_path + "edit.mako",
                                      model=instance,
                                      props=props)

    def POST(self, **kwargs):
        self._save(**kwargs)

    def PUT(self, **kwargs):
        self._save(**kwargs)

    def DELETE(self, key):
        self.model_class.get(key).delete()

    def _save(self, **kwargs):
        for name, prop in self.model_class.properties().items():
            if name in kwargs and isinstance(prop, ReferenceProperty):
                kwargs[name] = prop.reference_class.get(kwargs[name])
        instance = self.model_class(from_controller=True, **kwargs)
        instance.put()
        return "success"
