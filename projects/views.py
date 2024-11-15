from django.shortcuts import render, get_object_or_404
from .models import Project, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def project_list(request):
    projects = Project.objects.all()

    # Search functionality
    query = request.GET.get('q')
    if query:
        projects = projects.filter(Q(title__icontains=query) | Q(description__icontains=query))

        # Pagination setup
    paginator = Paginator(projects, 5)  # Show 5 projects per page
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., negative or too high), deliver the last page.
        page_obj = paginator.page(paginator.num_pages)
    # Categories
    categories = Category.objects.all()

    return render(request, 'projects/project_list.html', {'page_obj': page_obj, 'categories': categories})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})
