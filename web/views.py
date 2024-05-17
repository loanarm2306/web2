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
