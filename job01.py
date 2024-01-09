import hashlib

def is_valid_password(password):
    # Vérifie les exigences de sécurité du mot de passe
    return (
        len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "!@#$%^&*" for c in password)
    )

def get_valid_password():
    while True:
        password = input("Choisissez un mot de passe : ")
        if is_valid_password(password):
            return password
        else:
            print("Le mot de passe ne respecte pas les exigences de sécurité. Veuillez réessayer.")

def hash_password(password):
    # Crypte le mot de passe avec l'algorithme de hachage SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def main():
    password = get_valid_password()
    hashed_password = hash_password(password)
    print("Mot de passe valide !")
    # Ne pas afficher le mot de passe crypté
    # Vous pouvez le stocker en toute sécurité dans une base de données ou autre moyen sécurisé

if __name__ == "__main__":
    main()
