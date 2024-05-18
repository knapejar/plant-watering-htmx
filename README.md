# Plant Watering App

[![Vercel Deploy](https://deploy-badge.vercel.app/vercel/plant-watering-htmx?style=for-the-badge)](https://plant-watering-htmx.vercel.app/) [![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](https://github.com/knapejar/plant-watering-htmx/blob/main/LICENSE.md)

V této aplikaci jsem se pokusil implementovat jednoduchou CRUD aplikaci za pomocí HTMX a Flasku. Aplikace slouží k evidenci rostlin a zaznamenávání jejich zalévání (později napojit na zalévací IoT zařízení).

Produkční prostředí aplikace je dostupné na adrese [plant-watering-htmx.vercel.app](https://plant-watering-htmx.vercel.app/).

## Funkce

- **Přidání nové rostliny**
- **Úprava rostliny**
- **Zalévání rostliny**
- **Smazání rostliny**

## Použité technologie

- **Flask**: Webový framework pro backendovou logiku a API.
- **SQLAlchemy**: ORM pro práci s databází.
- **SQLite**: Databáze pro ukládání dat o rostlinách.
- **HTMX**: Knihovna pro přidávání interaktivních funkcí pomocí HTML atributů.
- **Lordicon**: Animované ikony pro vizuální zpětnou vazbu.
- **Bootstrap 5**: Framework pro responsivní a moderní design.

## Instalace

1. Klonujte tento repozitář:
    ```bash
    git clone https://github.com/vase_jmeno/plant-watering-app.git
    cd plant-watering-app
    ```

2. Vytvořte a aktivujte virtuální prostředí:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
    Na Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Nainstalujte závislosti:
    ```bash
    pip install -r requirements.txt
    ```

4. Nastavte proměnné prostředí:
    ```bash
    export SQLALCHEMY_DATABASE_URI="sqlite:///plants.db"
    ```
    Na Windows:
    ```bash
    set SQLALCHEMY_DATABASE_URI="sqlite:///plants.db"
    ```

5. Spusťte aplikaci:
    ```bash
    python app.py
    ```

5. Otevřete webový prohlížeč a přejděte na `http://127.0.0.1:5000`.

## Použití

### Přidání nové rostliny
1. Vyplňte formulář v horní části stránky.
2. Klikněte na tlačítko "Add Plant".

### Úprava rostliny
1. Změňte hodnoty a klikněte na tlačítko "Update Plant".

### Zalévání rostliny
1. Klikněte na ikonu zalévání vedle rostliny.

### Smazání rostliny
1. Klikněte na ikonu koše vedle rostliny.

## Soubory

- **app.py**: Hlavní soubor aplikace Flask.
- **templates/**: Složka obsahující HTML šablony.
  - `base.html`: Základní šablona s importy pro Bootstrap, HTMX a Lordicon.
  - `index.html`: Hlavní stránka aplikace s formulářem a seznamem rostlin.
  - `_plant.html`: Částečná šablona pro jednotlivé rostliny.

## Licence

Tento projekt je licencován pod MIT licencí.

## Autor

- **Jaroslav Knápek** - [knapejar](https://github.com/knapejar)

