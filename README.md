# Valutaomregner CLI 

Dette er et simpelt Command Line Interface (CLI) værktøj skrevet i Python, der gør det muligt at omregne valutaer direkte fra terminalen. Programmet benytter [ExchangeRate-API](https://www.exchangerate-api.com/) til at hente de nyeste valutakurser.

## Installation og Setup

Følg disse trin for at få programmet til at køre lokalt på din maskine.


### 1. Klon projektet:
   git clone [https://github.com/MartinMD-Git/valuta.git](https://github.com/MartinMD-Git/valuta.git)  
   cd valuta

### 2. Opret og aktiver Virtual Environment (Venv)
Det anbefales altid at bruge et virtuelt miljø for at isolere projektets afhængigheder.

**I din terminal:**
* **Windows:**
    python -m venv venv
    .\venv\Scripts\activate
* **Mac/Linux:**
    python3 -m venv venv
    source venv/bin/activate

### 3. Installer nødvendige pakker
Når dit virtuelle miljø er aktivt, skal du installere de nødvendige biblioteker:  
pip install -r requirements.txt

## Anvendelse

### 1. Tilføj API-nøgle
Første gang du bruger programmet, skal du gemme din API-nøgle. Dette gøres med --key argumentet, som gemmer nøglen i en lokal .env fil:  
python main.py --key DIN_API_NØGLE_HER

### 2. Omregn valuta
Når nøglen er gemt, kan du foretage omregninger ved at angive beløb, fra-valuta og til-valuta:  
Eksempelvis: python main.py 100 USD DKK  
Her bliver der omregnet fra 100 USD til Danske Kroner