from django_components import component

@component.register("hello")
class Hello(component.Component):
    template_name = "template.html"

    def get_context_data(self, name):
        return {
            "name": name,
        }

    def post(self, request, *args, **kwargs):
        return self.render_to_response(context={"name": "bobby"}, name="bo")

    class Media:
        css = "style.css"
        js = "script.js"
