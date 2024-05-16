from django.contrib.sites import requests
from django.shortcuts import render
from .models import Passengers, DeparturePoint, ArrivalPoint, DepartureTime, ArrivalTime, Distance, TransportId, TransportType

def calculate_pollution_plain(request):
    if request.method == 'POST':
        transport_type = request.POST.get('transport_type')
        passengers = int(request.POST.get('passengers'))
        departure_point = request.POST.get('departure_point')
        arrival_point = request.POST.get('arrival_point')

        transport_obj, created = TransportType.objects.get_or_create(type=transport_type)

        api_url = "https://www.carboninterface.com/api/v1/estimates"
        headers = {
            "Authorization": "Bearer fJqKwcr9wvNEdR6GgrOkg",
            "Content-Type": "application/json"
        }
        data = {
            "type": transport_type,
            "passengers": passengers,
            "legs": [
                {"departure_airport": departure_point, "destination_airport": arrival_point}
            ]
        }
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            estimate_data = response.json().get('data', {})
            return render(request, 'resultplain.html', {'estimate_data': estimate_data})
        else:
            error_message = "Error al calcular la contaminación. Por favor, inténtalo de nuevo más tarde."
            return render(request, 'error_page.html', {'error_message': error_message})

    else:
        return render(request, 'pollution_form.html')
