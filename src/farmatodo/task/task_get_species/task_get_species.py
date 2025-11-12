class TaskGetSpecies:

    def show_evolutions(self,chain_data):
        chain = chain_data['chain']
        evolutions = []

        while chain:
            if 'species' in chain:
                species_name = chain['species']['name']
                evolutions.append(species_name)
                print(f'Pokémon: {species_name}')
            else:
                print("No se pudo encontrar información de especie.")

            if 'evolves_to' in chain and len(chain['evolves_to']) > 0:
                for evolve in chain['evolves_to']:
                    for detail in evolve['evolution_details']:
                        level = detail.get('min_level', 'N/A')
                        trigger = detail.get('trigger', {}).get('name', 'N/A')
                        print(
                            f"  Evoluciona a: {evolve['species']['name']} (Nivel mínimo: {level}, Trigger: {trigger})")
                    chain = evolve
            else:
                break

        return evolutions  # Retornamos la lista de evoluciones

    def sort_alphabetically(self, lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista
