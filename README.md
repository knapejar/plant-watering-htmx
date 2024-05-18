# Plant Watering App

Tato aplikace umožňuje správu rostlin včetně přidávání, úpravy, zalévání a mazání rostlin. Backend je postaven na Flasku a frontend využívá HTMX, Lordicon a Bootstrap 5 pro dynamickou a interaktivní user experience.

## Funkce

- **Přidání nové rostliny**: Přidejte nové rostliny pomocí jednoduchého formuláře.
- **Úprava rostliny**: Aktualizujte jméno nebo popis rostliny přímo z přehledu rostlin.
- **Zalévání rostliny**: Zaznamenejte poslední zalévání rostliny kliknutím na ikonu.
- **Smazání rostliny**: Odstraňte rostliny ze seznamu jednoduchým kliknutím.

## Použité technologie

- **Flask**: Webový framework pro backendovou logiku a API.
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
    source venv/bin/activate  # Na Windows použijte `venv\Scripts\activate`
    ```

3. Nainstalujte závislosti:
    ```bash
    pip install -r requirements.txt
    ```

4. Spusťte aplikaci:
    ```bash
    python app.py
    ```

5. Otevřete webový prohlížeč a přejděte na `http://127.0.0.1:5000`.

## Použití

### Přidání nové rostliny
1. Vyplňte formulář v horní části stránky.
2. Klikněte na tlačítko "Add Plant".

### Úprava rostliny
1. Klikněte na jméno nebo popis rostliny, kterou chcete upravit.
2. Změňte hodnoty a klikněte na tlačítko "Update Plant".

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

## Autor

Tento projekt vytvořil Jaroslav Knápek. Pokud máte jakékoliv dotazy nebo připomínky, neváhejte mě kontaktovat.
