## Farmatodo Back

Proyecto de automatización y consumo de la PokéAPI orientado a validar la cadena de evoluciones de un Pokémon. El código expone utilidades para consumir endpoints públicos, procesar la información obtenida y ejecutar pruebas automatizadas con PyTest y Allure.

- **Lenguaje:** Python 3.10+
- **Dependencias clave:** `requests`, `pytest`, `allure-pytest`
- **Estructura:** Arquitectura modular en `src/farmatodo` con carpetas para configuración (`conf`), consumo de servicios (`endpoints`), lógica de negocio (`task`) y pruebas (`test`).

### Requisitos previos

- Python 3.10 o superior
- [Pip](https://pip.pypa.io/) actualizado
- (Opcional) [Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline) para visualizar reportes

Se recomienda trabajar dentro de un entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate
```

### Instalación de dependencias

```powershell
pip install -U pip
pip install requests pytest allure-pytest
```

Si posteriormente se añade un archivo `requirements.txt`, bastará con ejecutar `pip install -r requirements.txt`.

### Ejecución de pruebas

Desde la raíz del proyecto, con el entorno virtual activo:

```powershell
pytest -m test_evolutions_pokemon -s
```

El marcador `test_evolutions_pokemon` está configurado en `src/pytest.ini` y ejecuta la prueba que verifica la cadena de evoluciones de `Squirtle`.

Para generar reportes con Allure:

```powershell
pytest -m test_evolutions_pokemon --alluredir=target\allure-results
allure serve target\allure-results
```

### Flujo principal

1. `EndpointsEvolutions.get_evolutions_pokemon(name)` consulta la PokéAPI obteniendo la información base del Pokémon.
2. `EndpointsEvolutions.get_species_pokemon(url)` reutiliza el mismo cliente para navegar a los endpoints de especies y cadenas de evolución.
3. `TaskGetSpecies.show_evolutions(chain_data)` procesa la cadena y muestra/retorna una lista con las evoluciones encontradas.
4. `TaskGetSpecies.sort_alphabetically(lista)` ordena alfabéticamente la lista de evoluciones.

### Estructura de carpetas destacada

```
src/
└── farmatodo/
    ├── conf/                 # Configuración de URLs base
    ├── endpoints/            # Clientes HTTP hacia la PokéAPI
    ├── task/                 # Lógica para procesar respuestas
    └── test/                 # Pruebas PyTest + Allure
```


