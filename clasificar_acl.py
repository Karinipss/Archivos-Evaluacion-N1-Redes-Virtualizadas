print("=" * 60)
print("CLASIFICADOR DE ACL IPv4 CISCO")
print("=" * 60)

try:
    numero_acl = int(input("Ingrese el número de ACL IPv4: "))

    if 1 <= numero_acl <= 99 or 1300 <= numero_acl <= 1999:
        print(f"\nLa ACL {numero_acl} corresponde a una ACL ESTÁNDAR.")
        print("Las ACL estándar filtran principalmente por IP de origen.")

    elif 100 <= numero_acl <= 199 or 2000 <= numero_acl <= 2699:
        print(f"\nLa ACL {numero_acl} corresponde a una ACL EXTENDIDA.")
        print(
            "Las ACL extendidas pueden filtrar por origen, destino, "
            "protocolo y puertos."
        )

    else:
        print(
            f"\nEl número {numero_acl} no corresponde al rango "
            "de una ACL IPv4 numerada."
        )

except ValueError:
    print("\nError: debe ingresar un número entero válido.")

print("=" * 60)
