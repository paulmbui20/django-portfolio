from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html', {'message': 'Thank you for contacting us!'})
