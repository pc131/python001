import time
odpowiedz1 = input("\nCzy chcesz robić karierę w korporacji - tak/nie? ")
while odpowiedz1 not in ('tak'):
    odpowiedz2 = input("\nJak to? Co ci tu nie pasuje?\n\nA) Brak rozwoju\nB) Sztywna atmosfera \nC) Lider banany mo zabiera\n\n")
    while odpowiedz1 not in ('B'):
        odpowiedz2 = input("\nDobrze. Wybierz profil dla siebie.\n\nA) Microsoft Azure\nB) Żur na zakwasie \nC) Rozwój pochmurny\n\n")
        while odpowiedz1 not in ('C'):
            odpowiedz3 = input("\nMicrosoft Azure jest niedostępny. Czy chcesz zamienić na Excela - tak/nie?\n\n")
            while odpowiedz1 not in ('tak'):
                for i in range(40):
                    print('\nAle tego chce dla ciebie Ela.')
                    time.sleep(0.5)
                    print('ERROR_INVALID_KARIERA at 0x0f6765AB001FF')
                    time.sleep(0.5)