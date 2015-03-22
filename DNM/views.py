# Create your views here.
import operator

import operator

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

from DNM.apps.klotter.models import KlotterPost
from DNM.apps.static_pages.models import PageText

from DNM.apps.news.models import *
from DNM.apps.members.models import *

from DNM.apps.signup.models import SignUp


@login_required
def base(request):
    post_list = Post.objects.select_subclasses().order_by('-created')
    paginator = Paginator(post_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {'post_list': posts}

    return render(request, 'base.html', context)








@login_required
def logout_(request):
    logout(request)
    return redirect('login')





@login_required
def statistics(request):
    grader = Grad.objects.exclude(id=13)
    members = Member.objects.filter(grad__in=grader)
    # Signups
    signUps = SignUp.objects.filter(member__in=members)
    valueMap = None
    max = 0
    for signup in signUps:
        if not valueMap:
            valueMap = {signup.member.get_full_name(): 1}
        elif valueMap.has_key(signup.member.get_full_name()):
            valueMap[signup.member.get_full_name()] += 1
        else:
            valueMap[signup.member.get_full_name()] = 1
            valueMap.keys().__sizeof__()
        if valueMap[signup.member.get_full_name()] > max:
            max = valueMap[signup.member.get_full_name()]

    list_ = sorted(valueMap.iteritems(), key=operator.itemgetter(1), reverse=True)
    keys, values = map(list, zip(*list_))
    if len(keys) > 7:
        values = values[:7]
        keys = keys[:7]

    # KLotter
    klotter = KlotterPost.objects.filter(member__in=members)
    valueMap = None
    maxKlotter = 0
    for klotterPost in klotter:
        if not valueMap:
            valueMap = {klotterPost.member.get_full_name(): 1}
        elif valueMap.has_key(klotterPost.member.get_full_name()):
            valueMap[klotterPost.member.get_full_name()] += 1
        else:
            valueMap[klotterPost.member.get_full_name()] = 1
            valueMap.keys().__sizeof__()
        if valueMap[klotterPost.member.get_full_name()] > maxKlotter:
            maxKlotter = valueMap[klotterPost.member.get_full_name()]

    list_ = sorted(valueMap.iteritems(), key=operator.itemgetter(1), reverse=True)
    keysKlotter, valuesKlotter = map(list, zip(*list_))
    if len(keysKlotter) > 7:
        valuesKlotter = valuesKlotter[:7]
        keysKlotter = keysKlotter[:7]


    #Grader
    valueMap = None
    maxGrader = 0
    for member in members:
        if not valueMap:
            valueMap = {member.grad: 1}
        elif valueMap.has_key(member.grad):
            valueMap[member.grad] += 1
        else:
            valueMap[member.grad] = 1
            valueMap.keys().__sizeof__()
        if valueMap[member.grad] > maxGrader:
            maxGrader = valueMap[member.grad]
    list_ = sorted(valueMap.iteritems(), key=operator.itemgetter(1), reverse=True)
    keysGrad, valuesGrad = map(list, zip(*list_))
    context = {'max': max, 'values': values, 'keys': keys, 'maxKlotter': maxKlotter, 'valuesKlotter': valuesKlotter,
               'keysKlotter': keysKlotter, 'keysGrad': keysGrad
        , 'valuesGrad': valuesGrad, 'maxGrader': maxGrader}

    return render(request, 'statistics.html', context)


def contact(request):
    styrelsen = Member.objects.filter(Q(title__styrelsePost=True)).order_by('title__id')
    text, created = PageText.objects.get_or_create(identifier='Kontakt')
    context = {'styrelsen': styrelsen, 'text': text}
    return render(request, 'contact.html', context)