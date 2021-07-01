from .models import Category

def categories(request):
    '''
    Context pre-processor to access categories from any template 
    '''
    return {
        'categories': Category.objects.all()
    }