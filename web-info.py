

import requests
import argparse

def obtener_headers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Failed to reach goal: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="web detector")
    parser.add_argument('-t', '--target', help="prey")
    args = parser.parse_args()

    if args.target:
        headers = obtener_headers(args.target)
        if headers:
            for key, value in headers.items():
                print(f"{key} : {value}")
    else:
        print("the prey was not found")

if __name__ == '__main__':
    main()
