

import json

try:
    # Apertura del archivo JSON.
    with open("myfile.json", "r", encoding="utf-8") as json_file:

        # Carga de la información mediante json.load.
        ourjson = json.load(json_file)

    # Lectura del token y del tiempo de vigencia.
    token = ourjson.get("access_token", ourjson.get("token"))
    expires_in = ourjson.get(
        "expires_in",
        ourjson.get("expires", ourjson.get("expires_in_seconds"))
    )

    print("=" * 60)
    print("ANÁLISIS DEL ARCHIVO JSON")
    print("=" * 60)

    if token is not None:
        print(f"Token: {token}")
    else:
        print("No se encontró el campo 'access_token' o 'token'.")

    if expires_in is not None:
        try:
            segundos = int(expires_in)
            minutos = segundos // 60
            segundos_restantes = segundos % 60

            print(f"Tiempo restante: {segundos} segundos")
            print(
                f"Equivalente: {minutos} minutos y "
                f"{segundos_restantes} segundos"
            )
        except (ValueError, TypeError):
            print(f"Tiempo de caducidad informado: {expires_in}")
    else:
        print("No se encontró el campo que indica la caducidad.")

    print("=" * 60)

except FileNotFoundError:
    print("Error: no se encontró el archivo myfile.json.")

except json.JSONDecodeError:
    print("Error: el archivo myfile.json no contiene un JSON válido.")

except PermissionError:
    print("Error: no existen permisos para leer myfile.json.")

except Exception as error:
    print(f"Se produjo un error inesperado: {error}")
