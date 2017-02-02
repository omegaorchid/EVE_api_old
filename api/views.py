from django.shortcuts import render


class View:
    def home(self):
        context = {}
        template = 'home.html'

        return render(request=self, template_name=template, context=context)

