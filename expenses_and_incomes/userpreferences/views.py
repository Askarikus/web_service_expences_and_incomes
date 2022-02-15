import json
import os

from django.contrib import messages

from .models import UserPreference
from django.conf import settings
from django.shortcuts import render


def index(request):
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    currency_data = [{'name': k, 'value': v} for k, v in data.items()]
    # import pdb
    # pdb.set_trace()
    exists = UserPreference.objects.filter(user=request.user).exists()
    user_preferences = None
    if exists:
        user_preferences = UserPreference.objects.get(user=request.user)

    if request.method == 'GET':
        return render(request, 'preferences/index.html', {'currencies': currency_data,
                                                          'user_preferences': user_preferences})

    else:
        currency = request.POST['currency']
        if exists:
            user_preferences.currency = currency
            user_preferences.save()
        else:
            UserPreference.objects.create(user=request.user, currency=currency)
        messages.success(request, 'Changes saved')
        return render(request, 'preferences/index.html',
                      {'currencies': currency_data, 'user_preferences': user_preferences})
