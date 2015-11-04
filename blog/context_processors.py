from blog.models import Post, Hero, Circles, Featured,Sedes,Schedule,Speakers
import datetime
from django.utils import timezone
from django.utils.timezone import utc


def list_careers(request):
    featrured = Featured.objects.all().order_by('-order')[:4]   
    post_all = Post.objects.all().order_by('created').exclude(publish=False)[:4]
    now = timezone.localtime(timezone.now())
    return (locals())

def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }