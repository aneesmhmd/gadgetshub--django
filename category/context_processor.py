from category.models import Category,Brand

def menu_links(request):
    categories = Category.objects.all().order_by('id')
    brands = Brand.objects.all().order_by('id')
    return dict(categories=categories,brands=brands)