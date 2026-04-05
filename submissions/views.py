from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SubmissionForm


@login_required
def submit_poem(request):
    if not request.user.profile.is_writer:
        return HttpResponse("You are not approved as a writer yet.")
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.submitted_by = request.user
            submission.is_published = False
            submission.is_approved = False
            submission.save()

            messages.success(request, "Your poem was submitted for review 🌙")
            return redirect('home')
    else:
        form = SubmissionForm()

    return render(request, 'submit.html', {'form': form})