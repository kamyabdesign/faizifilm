from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import send_mail


from . models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, phone=phone,
                          subject=subject, message=message)

        contact.save()

        # send email
        send_mail(
            ' تماس باما ',
            ' سلام رضا جان لطفا وارد بخش ادمین شده و به تقاضای ارسال شده جواب دهید. ',
            'rezafaizi6@gmail.com',
            ['faizi.kamyabdesign@gmail.com', ],
            fail_silently=False
        )

        messages.success(request, 'پیام شما موفقانه ارسال شد!')

        return redirect("contact")
    else:

        return render(request, "film/contact.html")
