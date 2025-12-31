from django.shortcuts import render, redirect
from .models import PerfumeReview
from .forms import ReviewForm


def review_list(request):
 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('review_list')
    
  
    else:
        form = ReviewForm()
    

    reviews = PerfumeReview.objects.all().order_by('-created_at')
    

    return render(request, 'reviews/review_list.html', {
        'reviews': reviews,
        'form': form,
    })


from django.shortcuts import get_object_or_404


def delete_review(request, pk):
    review = get_object_or_404(PerfumeReview, pk=pk)
    if request.method == 'POST':
        review.delete()
    return redirect('review_list')