from .models import Category

def categories(request):
    '''
    Context pre-processor to access categories from any template (Site-wide access) 
    '''
    return {
        'categories': Category.objects.all()
    }