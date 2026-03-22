from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SubmissionForm


@login_required
def submit_poem(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.submitted_by = request.user
            submission.save()

            messages.success(request, "Your poem was submitted for review 🌙")
            return redirect('home')
    else:
        form = SubmissionForm()

    return render(request, 'submit.html', {'form': form})