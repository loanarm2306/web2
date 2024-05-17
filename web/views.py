from django.shortcuts import render, get_object_or_404, redirect
from .models import PollutionResult
import requests


def calculate_pollution_plain(request):
    if request.method == 'POST':
        transport_type = request.POST.get('transport_type')
        passengers = request.POST.get('passengers')
        departure_point = request.POST.get('departure_point')
        arrival_point = request.POST.get('arrival_point')
        carbon_emission = request.POST.get('carbon_emission')

        api_url = "https://www.carboninterface.com/api/v1/estimates"
        headers = {
            "Authorization": "Bearer Kjd6ggkR8x8KkftIe3SPQ",
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
            carbon_emission = estimate_data['attributes']['carbon_g']

            result = PollutionResult.objects.create(
                transport_type=transport_type,
                passengers=passengers,
                departure_point=departure_point,
                arrival_point=arrival_point,
                carbon_emission=carbon_emission
            )

            return render(request, 'results.html', {'estimate_data': estimate_data})
        else:
            error_message = "Error!"
            return render(request, 'error.html', {'error_message': error_message})

    else:
        return render(request, 'results.html')


def calculate_pollution_car(request):
    if request.method == 'POST':
        transport_type = request.POST.get('transport_type')
        departure_point = request.POST.get('departure_point')
        arrival_point = request.POST.get('arrival_point')
        distance_travelled = int(request.POST.get('distance_travelled'))
        passengers = int(request.POST.get('passengers'))

        emission_per_km = 120
        total_emission = emission_per_km * distance_travelled * passengers

        result = PollutionResult.objects.create(
            transport_type=transport_type,
            passengers=passengers,
            departure_point=departure_point,
            arrival_point=arrival_point,
            carbon_emission=total_emission
        )

        return render(request, 'results.html', {'estimate_data': {'carbon_g': total_emission}})
    else:
        return render(request, 'results.html')


def calculate_pollution_train(request):
    if request.method == 'POST':
        transport_type = request.POST.get('transport_type')
        departure_point = request.POST.get('departure_point')
        arrival_point = request.POST.get('arrival_point')
        passengers = int(request.POST.get('passengers'))

        distances = {
            'StationA-StationB': 100,
            'StationA-StationC': 200,
            'StationB-StationC': 150
        }

        distance_key = f'{departure_point}-{arrival_point}'
        distance = distances.get(distance_key, 0)

        if distance == 0:
            error_message = 'Distancia desconocida entre las estaciones proporcionadas.'
            return render(request, 'error.html', {'error_message': error_message})

        emission_per_passenger_per_km = 50
        total_emission = emission_per_passenger_per_km * distance * passengers

        result = PollutionResult.objects.create(
            transport_type=transport_type,
            passengers=passengers,
            departure_point=departure_point,
            arrival_point=arrival_point,
            carbon_emission=total_emission
        )

        return render(request, 'results.html', {'estimate_data': {'carbon_g': total_emission}})

    else:
        return render(request, 'results.html')


def calculate_pollution_subway(request):
    if request.method == 'POST':
        transport_type = request.POST.get('transport_type')
        departure_station = request.POST.get('departure_station')
        arrival_station = request.POST.get('arrival_station')
        passengers = int(request.POST.get('passengers'))

        distances = {
            'Station1-Station2': 5,
            'Station1-Station3': 10,
            'Station2-Station3': 7
        }

        distance_key = f'{departure_station}-{arrival_station}'
        distance = distances.get(distance_key, 0)

        if distance == 0:
            error_message = 'Distancia desconocida entre las estaciones proporcionadas.'
            return render(request, 'error.html', {'error_message': error_message})

        emission_per_passenger_per_km = 30
        total_emission = emission_per_passenger_per_km * distance * passengers

        result = PollutionResult.objects.create(
            transport_type=transport_type,
            passengers=passengers,
            departure_station=departure_station,
            arrival_station=arrival_station,
            carbon_emission=total_emission
        )

        return render(request, 'results.html', {'estimate_data': {'carbon_g': total_emission}})

    else:
        return render(request, 'calculate.html')


def calculate_pollution_motorbike(request):
    if request.method == 'POST':
        transport_type = request.POST.get('transport_type')
        distance_travelled = float(request.POST.get('distance'))
        passengers = int(request.POST.get('passengers'))

        emission_per_passenger_per_km = 100
        total_emission = emission_per_passenger_per_km * distance_travelled * passengers

        result = PollutionResult.objects.create(
            transport_type=transport_type,
            passengers=passengers,
            distance=distance_travelled,
            carbon_emission=total_emission
        )

        return render(request, 'results.html', {'estimate_data': {'carbon_g': total_emission}})

    else:
        return render(request, 'calculate.html')


def calculate_pollution_boat(request):
    if request.method == 'POST':
        transport_type = request.POST.get('transport_type')
        departure_port = request.POST.get('departure_port')
        arrival_port = request.POST.get('arrival_port')
        passengers = int(request.POST.get('passengers'))

        distances = {
            'Port1-Port2': 50,
            'Port1-Port3': 120,
            'Port2-Port3': 90
        }

        distance_key = f'{departure_port}-{arrival_port}'
        distance = distances.get(distance_key, 0)

        if distance == 0:
            error_message = 'Distancia desconocida entre los puertos proporcionados.'
            return render(request, 'error.html', {'error_message': error_message})

        emission_per_passenger_per_km = 250
        total_emission = emission_per_passenger_per_km * distance * passengers

        result = PollutionResult.objects.create(
            transport_type=transport_type,
            passengers=passengers,
            departure_point=departure_port,
            arrival_point=arrival_port,
            carbon_emission=total_emission
        )

        return render(request, 'results.html', {'estimate_data': {'carbon_g': total_emission}})

    else:
        return render(request, 'calculate.html')


def results_list(request):
    results = PollutionResult.objects.all()
    return render(request, 'results.html', {'results': results})


def edit_result_plain(request, result_id):
    result = get_object_or_404(PollutionResult, pk=result_id)
    if request.method == 'POST':
        result.passengers = int(request.POST.get('passengers'))
        result.departure_point = request.POST.get('departure_point')
        result.arrival_point = request.POST.get('arrival_point')
        result.save()
        return redirect('results')
    return render(request, 'edit_result.html', {'result': result})


def delete_result(request, result_id):
    result = get_object_or_404(PollutionResult, pk=result_id)
    if request.method == 'POST':
        result.delete()
        return redirect('results')
    return render(request, 'confirm_delete.html', {'result': result})
