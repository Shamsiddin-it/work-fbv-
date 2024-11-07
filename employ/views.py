from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from .models import User, Work, Application
from django.urls import reverse_lazy
from .forms import UserForm, WorkForm, ApplicationForm  


def home_view(request):
    return render(request, "home.html")


def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("home"))
    else:
        form = UserForm()
    
    return render(request, "user_create.html", {'form': form})


def work_create_view(request):
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("work_list"))
    else:
        form = WorkForm()

    return render(request, "work_create.html", {'form': form})


def work_list_view(request):
    works = Work.objects.all()
    return render(request, "work_list.html", {'works': works})


def work_detail_view(request, pk):
    work = get_object_or_404(Work, pk=pk)
    applications = Application.objects.filter(work=work)
    return render(request, "work_detail.html", {'work': work, 'application_work': applications})


def work_update_view(request, pk):
    work = get_object_or_404(Work, pk=pk)
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("work_list"))
    else:
        form = WorkForm(instance=work)

    return render(request, "work_update.html", {'form': form, 'work': work})


def work_delete_view(request, pk):
    work = get_object_or_404(Work, pk=pk)
    if request.method == 'POST':
        work.delete()
        return redirect(reverse_lazy("work_list"))
    return render(request, "work_delete.html", {'work': work})


def application_create_view(request, pk):
    work = get_object_or_404(Work, pk=pk)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.work = work
            application.save()
            return redirect(reverse_lazy("home"))
    else:
        form = ApplicationForm()

    return render(request, "application_create.html", {'form': form, 'work': work})


def application_list_view(request):
    applications = Application.objects.all()
    return render(request, "application_list.html", {'applications': applications})


def application_detail_view(request, pk):
    application = get_object_or_404(Application, pk=pk)
    return render(request, "application_detail.html", {'application': application})


def application_update_view(request, pk):
    application = get_object_or_404(Application, pk=pk)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("work_detail", kwargs={'pk': application.work.pk}))
    else:
        form = ApplicationForm(instance=application)

    return render(request, "application_update.html", {'form': form, 'application': application})


def application_delete_view(request, pk):
    application = get_object_or_404(Application, pk=pk)
    
    if request.method == 'POST':
        application.delete()
        return redirect(reverse_lazy("work_detail", kwargs={'pk': application.work.pk}))

    return render(request, "application_delete.html", {'application': application})
