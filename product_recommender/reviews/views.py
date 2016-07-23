from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review, Product
from .forms import ReviewForm
import datetime


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def Product_list(request):
    Product_list = Product.objects.order_by('-name')
    context = {'Product_list':Product_list}
    return render(request, 'reviews/Product_list.html', context)


def Product_detail(request, Product_id):
    Product = get_object_or_404(Product, pk=Product_id)
    form = ReviewForm()
    return render(request, 'reviews/Product_detail.html', {'Product': Product, 'form': form})


def add_review(request, Product_id):
    Product = get_object_or_404(Product, pk=Product_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.Product = Product
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:Product_detail', args=(Product.id,)))
    
    return render(request, 'reviews/Product_detail.html', {'Product': Product, 'form': form})