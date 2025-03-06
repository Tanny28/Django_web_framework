from django.http import HttpResponse

def drinks(request, drink_name):
    # Step 3: Define a dictionary with drink descriptions
    drink = {
        'mocha': 'A type of coffee',
        'tea': 'A type of beverage',
        'lemonade': 'A type of refreshment',
        'espresso': 'A strong and concentrated coffee'  # Additional drink
    }

    # Step 4: Get the drink description or show a default message
    choice_of_drink = drink.get(drink_name, "Sorry, this drink is not on the menu.")

    # Step 5: Return the response as an HTML heading
    return HttpResponse(f"<h2>{drink_name}</h2> <p>{choice_of_drink}</p>")
