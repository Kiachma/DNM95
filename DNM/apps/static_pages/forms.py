from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import ModelForm
from django.shortcuts import render
from DNM.apps.static_pages.models import PageText
from django_summernote.widgets import SummernoteWidget

__author__ = 'eaura'


class PageTextInputForm(ModelForm):
    class Meta:
        model = PageText
        exclude = ('identifier',)
        widgets = {
            'text': SummernoteWidget(attrs={'width': '100%'}),
        }


@login_required
@user_passes_test(lambda u: u.title and u.title.styrelsePost or u.is_superuser)
def editpage(request, page_id):
    text, created = PageText.objects.get_or_create(identifier=page_id)

    if request.method == 'POST':
        form = PageTextInputForm(request.POST, instance=text)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            context = {'text': text}
            return render(request, 'simplePage.html', context)
    form = PageTextInputForm(instance=text)
    context = {'form': form, 'identifier': text.identifier}
    return render(request, 'editSimplePage.html', context)