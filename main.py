import argparse
import os
import requests
from dotenv import load_dotenv, set_key

load_dotenv()

def get_conversion(api_key, base, target, amount):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base}/{target}/{amount}"
    
    response = requests.get(url)
    data = response.json()
    
    if data.get("result") == "success":
        return data["conversion_result"]
    else:
        return "Fejl i opslag"

def main():
    parser = argparse.ArgumentParser(description="Valutaomregner CLI")
    
    parser.add_argument("--key", help="Gem din API nøgle i .env")
    
    parser.add_argument("beløb", type=float, nargs="?", help="Beløb")
    parser.add_argument("fra", nargs="?", help="Fra valuta")
    parser.add_argument("til", nargs="?", help="Til valuta")

    args = parser.parse_args()

    if args.key:
        set_key(".env", "API_KEY", args.key)
        print(f"API nøgle er gemt i .env!")
        return

    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Fejl: Ingen nøgle fundet. Brug --key [nøgle] først.")
        return

    if args.beløb and args.fra and args.til:
        resultat = get_conversion(api_key, args.fra.upper(), args.til.upper(), args.beløb)
        print(f"Resultat: {resultat} {args.til.upper()}")
    else:
        print("Prøv: python main.py 100 USD DKK")

if __name__ == "__main__":
    main()