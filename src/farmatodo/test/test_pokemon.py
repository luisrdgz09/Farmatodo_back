import allure
import pytest

from src.farmatodo.endpoints.endpoints_evolutions.endpoints_evolutions import EndpointsEvolutions
from src.farmatodo.task.task_get_species.task_get_species import TaskGetSpecies

@pytest.mark.test_evolutions_pokemon
def test_pokemon_evolutions():
    with allure.step("1. Se realiza el consumo del servicio de obtención de pokemones"):
        pokemons = EndpointsEvolutions()
        response_pokemon = pokemons.get_evolutions_pokemon('Squirtle')
        url_species = response_pokemon['species']['url']
    with allure.step("2. Se realiza el consumo del servicio de obtención especies"):
        response_species = pokemons.get_species_pokemon(url_species)
        url_chain = response_species['evolution_chain']['url']
    with allure.step("3. Se realiza el consumo del servicio de obtención evoluciones"):
        response_chain = pokemons.get_species_pokemon(url_chain)
        evolutions = TaskGetSpecies()
        evolutions_pokemon = evolutions.show_evolutions(response_chain)
    with allure.step("4. Se ordena alfabéticamente las evoluciones "):
        sort = evolutions.sort_alphabetically(evolutions_pokemon)
        print(f'Esta es el {sort}')

