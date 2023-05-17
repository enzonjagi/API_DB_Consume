from django.shortcuts import render
from .models import Meal
import requests

def get_meals(request):
    """A view for the meals we receive from the API"""

    all_meals = {}

    if 'name' in request.GET:
        name = request.GET['name']
        url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}'
        response = requests.get(url)
        data = response.json()
        meals = data['meals']

        for meal in meals:
            meal_data = Meal(
                id = meal['idMeal'],
                name = meal['strMeal'],
                category = meal['strCategory'],
                instructions = meal['strInstructions'],
                region = meal['strArea'],
                slug = meal['idMeal'],
                image_url = meal['strMealThumb']
            )
            meal_data.save()
            all_meals = Meal.objects.all().order_by('-id')

    return render(request, 'meals/meal.html', {"all_meals": all_meals})

def meal_detail(request):
    """A view for individual meals"""
    
    meal = Meal.objects.get(id=id)

    print(meal)
    return render(request, 'meals/meal_detail.html', {'meal': meal})