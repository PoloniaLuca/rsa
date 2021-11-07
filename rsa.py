from RSAfunction import (
    is_prime,
    create_h,
    phi_func,
    modinv,
    msg_to_number,
    number_to_msg,
)

DIMENSION = 26


def main():

    while True:
        choose = input("Vuoi criptare o decriptare? ")
        if choose == "criptare":
            cripting()
        elif choose == "decriptare":
            decripting()
        else:
            print("Puoi scrivere soltanto 'criptare' o 'decriptare'.")
        to_continue = input("Vuoi ripetere il programma?('si' o 'no') ")
        if to_continue == "si":
            pass
        elif to_continue == "no":
            break


def cripting():
    # inizializzazione variabili
    text = ""
    p, q = 4, 4

    # input p, q (con controllo) e messaggio
    while is_prime(p) is False and is_prime(q) is False:
        p, q = int(input("Inserire il primo numero primo: ")), int(
            input("Inserire il secondo numero primo: ")
        )

    text = input("Inserisca il messaggio prego: ").lower()

    n = p * q
    phi_n = phi_func(n)
    ## phi_phi_n = phi_func(phi_n)

    # creazione chiave pubblica h
    h = create_h(p, q, phi_n)
    h = 1093531

    # calcolo della chiave privata k
    k = modinv(h, phi_n)
    print(
        "Chiave pubblica h: "
        + str(h)
        + "\nChiave privata k: "
        + str(k)
        + "\nN: "
        + str(n)
    )

    # trasformazione del messaggio in numero
    number = msg_to_number(text, DIMENSION)

    # numero criptato da dare
    cripted_number = pow(number, h) % n

    # trasformazione numero criptato in testo
    cripted_text = number_to_msg(cripted_number, DIMENSION)
    print("Messaggio decriptato: " + cripted_text)


def decripting():

    cripted_text = input("Inserisci il testo criptato: ")
    k = int(input("Inserisci la chiave privata k: "))
    n = int(input("Inserisci n: "))

    # trasformazione testo criptato in numero criptato
    cripted_number = msg_to_number(cripted_text, DIMENSION)

    # calcolo del numero iniziale tramite numero criptato, chiave privata e n
    initial_number = pow(int(cripted_number), k) % n

    # trasformazione del numero nel messaggio iniziale
    initial_text = number_to_msg(initial_number, DIMENSION)

    print("Messaggio decriptato: " + initial_text)


if __name__ == "__main__":
    main()
