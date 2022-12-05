from django.views.generic import TemplateView


class MainPageView(TemplateView):

    http_method_names = ['get']
    template_name = 'guest_site/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
