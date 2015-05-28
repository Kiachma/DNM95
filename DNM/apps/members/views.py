# coding=utf-8
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from DNM.apps.members.models import *
from DNM.apps.members.forms import *
from django.template.loader import render_to_string
from django.http import HttpResponse

from django.utils.translation import ugettext as _
@login_required
def users(request):
    users = Member.objects.filter(is_active=True).order_by('last_name')
    paginator = Paginator(users, 25)  # Show 25 contacts per page
    try:
        posts = paginator.page(users)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {'users': users}

    return render(request, 'userInformation/users.html', context)


@login_required
def profile(request, user_id):
    user_ = Member()

    user_ = Member.objects.get(pk=user_id)

    context = {'user_': user_}
    return render(request, 'userInformation/profile.html', context)


@login_required
def save(request, user_id):
    if request.method == 'POST':
        oldPass = None
        if user_id == u'None':
            form = MemberForm(request.POST, request.FILES)
        else:
            user = Member.objects.get(pk=user_id)
            oldPass = user.password

            form = MemberForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if request.POST.get('password') and request.POST.get('password') != '':
                if oldPass is None or check_password(request.POST.get('password'), oldPass):
                    if request.POST.get('newPass') and request.POST.get('newPass') != '':
                        user.set_password(request.POST.get('newPass'))
                    else:
                        user.set_password(request.POST.get('password'))
                    user.save()
                    form.save_m2m()
                    # user = authenticate(username=form.instance.username, password=request.POST.get('password'))
                    #login(request, user)
                    messages.add_message(request, messages.SUCCESS, _(u'Medlem sparade!'))
                    return HttpResponseRedirect(reverse('UserInformation:profile', args=(form.instance.id,)))
                else:
                    messages.add_message(request, messages.ERROR, _(u'Felaktigt lösenord'))
            else:
                messages.add_message(request, messages.ERROR, _(u'Lösenordet får ej vara tomt'))
        else:
            messages.add_message(request, messages.ERROR, _('Korrigera felen'))
    else:
        if (get_user(request).title.styrelsePost or get_user(request).is_superuser):
            form = MemberFormSuper()
        else:
            form = MemberForm()
    c = {'form': form}
    return render(request, 'userInformation/profile.html', c)


@user_passes_test(lambda u: u.title and u.title.styrelsePost or u.is_superuser)
def delete(request, user_id):
    member = Member.objects.get(pk=user_id)
    if not ((request.user.title and request.user.title.styrelsePost) or request.user.is_superuser):
        messages.add_message(request, messages.ERROR, _(u'Du har inte rätt att ta bort användare'))
        return HttpResponseRedirect(reverse('UserInformation:users', args=()))
    Member.delete(member)
    messages.add_message(request, messages.SUCCESS, _('Medlem borttaget'))
    return HttpResponseRedirect(reverse('UserInformation:users'))


@user_passes_test(lambda u: (u.title and u.title.styrelsePost) or u.is_superuser)
def admin(request, user_id):
    user_ = Member.objects.get(pk=user_id)
    form = MemberFormSuper(instance=user_)
    context = {'form': form, 'user_': user_}
    return render(request, 'userInformation/admin.html', context)


@user_passes_test(lambda u: u.title and u.title.styrelsePost or u.is_superuser)
def adminSave(request, user_id):
    if request.method == 'POST':
        user = Member.objects.get(pk=user_id)
        form = MemberFormSuper(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _('Medlem sparad!'))
            return HttpResponseRedirect(reverse('UserInformation:profile', args=(form.instance.id,)))
    else:
        form = MemberFormSuper()
    c = {'form': form}
    return render(request, 'userInformation/profile.html', c)


def kontakt(request, user_id):
    if request.method == 'POST':
        if user_id != u"None":
            user = Member.objects.get(pk=user_id)
            form = MemberFormKontakt(request.POST, instance=user)
        else:
            user = Member()
            form = MemberFormKontakt(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if request.POST.get('newPass') and request.POST.get('newPass') != '':
                user.set_password(request.POST.get('newPass'))
            else:
                user.set_password(request.POST.get('password'))
            user.save()
            form.save_m2m()
            messages.add_message(request, messages.SUCCESS, _('Kontaktuppgifter sparad!'))
            return HttpResponse(render_to_string('components/dummy_modal.html', {'user_': user}))
        else:
            context = {'form': form, 'user_': user}
            return render(request, 'userInformation/kontakt.html', context)
    if int(user_id) != request.user.id and user_id != None:
        messages.add_message(request, messages.ERROR, _(u'Du har inte rätt att ändra dessa uppgifter'))
        HttpResponseRedirect(reverse('UserInformation:profile', args=(user_id)))
    user_ = Member.objects.get(pk=user_id)
    form = MemberFormKontakt(instance=user_)
    context = {'form': form, 'user_': user_}
    return render(request, 'userInformation/kontakt.html', context)

def medlem(request, user_id):
    if request.method == 'POST':
        user = Member.objects.get(pk=user_id)
        form = MemberFormMedlem(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _('Medlemsuppgifter sparad!'))
            return HttpResponse(render_to_string('components/dummy_modal.html', {'user_': user}))
    if int(user_id) != request.user.id and user_id != None:
        messages.add_message(request, messages.ERROR, _(u'Du har inte rätt att ändra dessa uppgifter'))
        HttpResponseRedirect(reverse('UserInformation:profile', args=(user_id)))
    user_ = Member.objects.get(pk=user_id)
    form = MemberFormMedlem(instance=user_)

    context = {'form': form, 'user_': user_}
    return render(request, 'userInformation/medlem.html', context)
def new(request):
    user_ = Member()
    form = MemberFormKontakt()
    context = {'form': form, 'user_': user_}
    return render(request, 'userInformation/kontakt.html', context)


def other(request, user_id):
    AvecInlineFormSet = inlineformset_factory(Member, Avec, form=AvecForm, extra=1)

    if request.method == 'POST':
        user = Member.objects.get(pk=user_id)
        form = MemberFormOther(request.POST, instance=user)
        formset = AvecInlineFormSet(request.POST, request.FILES, instance=user)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.add_message(request, messages.SUCCESS, _('Uppgifter sparad!'))
            return HttpResponse(render_to_string('components/dummy_modal.html', {'user_': user}))
    if int(user_id) != request.user.id and user_id != None:
        messages.add_message(request, messages.ERROR, _(u'Du har inte rätt att ändra dessa uppgifter'))
        HttpResponseRedirect(reverse('UserInformation:profile', args=(user_id)))
    user_ = Member.objects.get(pk=user_id)
    form = MemberFormOther(instance=user_)
    formset = AvecInlineFormSet(instance=user_)
    context = {'form': form, 'user_': user_, 'formset': formset}
    return render(request, 'userInformation/other.html', context)