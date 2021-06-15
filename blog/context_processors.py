from . models import Alls


def Alldata(request):
    all = Alls.objects.all()
    return {'all': all}
