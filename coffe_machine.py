from resource import MENU, resources


# ----------------- FUNCIONES -----------------------------------

def report(election, money):
    """FUNCION PARA MOSTRAR AL USUARIO LOS RECURSOS QUE POSEE LA MAQUINA DE CAFE"""
    print(f'Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${money} ')


def drinks(election):
    """FUNCION PARA ASIGNAR INGREDIENTES DE LAS BEBIDAS Y DESCONTAR A LOS RECURSOS LO UTILIZADO"""
    if election == "espresso" or election == "latte" or election == "cappuccino":
        election = MENU[election]
        election_ingredients = election["ingredients"]
        election_water = 0
        election_milk = 0
        election_coffee = 0
        for clave in election_ingredients:
            election_water = election_ingredients["water"]
            election_coffee = election_ingredients["coffee"]
            if 'milk' in election_ingredients:
                election_milk = election_ingredients["milk"]
        return election_water,election_milk,election_coffee


def resources_left(election, election_water, election_milk, election_coffee):
    """FUNCION PARA COMPARAR SI HAY RECURSOS SUFICIENTES PARA LA BEBIDA ELEGIDA"""
    if resources["water"] < election_water:
        print('Sorry there is not enough water.')
        return False
    elif resources["milk"] < election_milk:
        print('Sorry there is not enough milk.')
        return False
    elif resources["coffee"] < election_coffee:
        print('Sorry there is not enough coffee.')
        return False


def drinks_cost(election):
    """FUNCION PARA DETERMINAR EL VALOR DE LA BEBIDA"""
    if election == 'espresso' or election == 'latte' or election == 'cappuccino':
        election = MENU[election]
        for clave in election:
            election_cost = election["cost"]
        return election_cost


def insert_money(election, cost, election_water, election_milk, election_coffee):
    """FUNCION DE INGRESO DE LAS MONEDAS, SI HAY SUFICIENTE DINERO DESCUENTA LOS RECURSOS"""
    print("Please insert coins.")
    quarters = 0.25
    cant_quarters = float(input("How many quarters: "))
    total_quarters = 0.25 * cant_quarters
    dimes = 0.10
    cant_dimes = float(input("How many dimes: "))
    total_dimes = 0.10 * cant_dimes
    nickles = 0.05
    cant_nickles = float(input("How many nickles: "))
    total_nickles = 0.05 * cant_nickles
    pennies = 0.01
    cant_pennies = float(input("How many pennies: "))
    total_pennies = 0.01 * cant_pennies

    total = total_quarters + total_dimes + total_nickles + total_pennies
    if total > cost:
        total_amount = round(total - cost, 1)
        resources["water"] -= election_water
        resources["coffee"] -= election_coffee
        resources["milk"] -= election_milk
        print(f"Here is ${total_amount} in change\nHere is your {election}. Enjoy!")
    else:
        print("Sorry that's enough money. Money refunded.")


# ----------------- PRINCIPAL -----------------------------------
# TODO: 1. input "What would you like? (espresso/latte/cappuccino), se tiene que repetir siempre."
election = input("What would you like? (espresso/latte/cappuccino/report/off): ")
money = 0

# TODO: 2. El programa tiene que tener un cierre mediante la palabra 'off'.
while election != 'off':
    # TODO: 3. Mediante la palabra 'report', el usuario puede visualizar los recursos que hay disponibles.
    if election == 'report':
        report(election,money)
    # TODO: 4. Los recursos se van restando segun a bebida elegida.
    elif election == 'espresso' or election == 'latte' or election == 'cappuccino':
        election_water, election_milk, election_coffee = drinks(election)
        recursos_disponibles = resources_left(election, election_water, election_milk, election_coffee)
        if recursos_disponibles != False:
            cost = drinks_cost(election)
            # TODO: 5. Hacer que el usuario ingrese monedas y asignar valores.
            insert_money(election, cost, election_water, election_milk, election_coffee)
    election = input("What would you like? (espresso/latte/cappuccino/report/off): ")
else:
    print("Goodbye!")






