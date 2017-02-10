from django.shortcuts import render


def home(request):
    contact = {
        'name': 'myName',
        'surname': 'mySurname',
        'date_birth': '07-11-1986',
        'bio': 'Django Python developer Dublh 3 \n'
               'Junior Django Python developer',
        'email': 'email@email.com',
        'jabber': 'jabber@co',
        'skype': 'skype',
        'other_contacts': 'other contacts\n'
                          'facebook\n'
                          'phone number',
    }

    return render(request, 'hello/home.html', {'info': contact})
