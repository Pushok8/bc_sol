from django.views.generic import ListView, TemplateView
from django.shortcuts import get_object_or_404

from .models import BCBlock


class BlocksView(ListView):
    model = BCBlock
    paginate_by = 50
    context_object_name = 'blocks'
    template_name = 'bcschain/index.html'


class BlockView(TemplateView):
    template_name = 'bcschain/block_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['block'] = get_object_or_404(BCBlock, height=kwargs['block_height'])

        return context
