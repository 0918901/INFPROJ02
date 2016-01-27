print("---------------------------------------------------------------")
#Naam opdracht
print("Assignment 4 Exercise 2 RPS Deel A")
print("---------------------------------------------------------------")

#declaratie RPS
def RPS():
    #Speluitleg
    print("Player VS Player [Rock,Paper,Scisscors]")
    print("---------------------------------------------------------------")
    print("Game Choices")
    print("1 = Rock")
    print("2 = Scissors")
    print("3 = Paper")
    print("---------------------------------------------------------------")

    #Player 1
    #Zolang bovenstaande klopt wordt het onderstaande wordt uitgevoerd
    while True:
        #Tekst die aangeeft wie er aan de beurt is
        print("Player 1")
        #Invoer keuze Speler 1
        print("choose a number:")
        choice = input('=')
        print("---------------------------------------------------------------")
        #Detect Invoer keuze Rock Speler 1
        if choice == 'r' or choice == 'R' or choice == 'Rock' or choice == 'rock' or choice == '1':
            player1_choice = 1
            break
        #Detect Invoer keuze Scissors Speler 1
        elif choice == 'S' or choice == 's' or choice == 'Scissors' or choice == 'sciccors' or choice == '2':
            player1_choice = 2
            break
        #Detect Invoer keuze Paper Speler 1
        elif choice == 'P' or choice == 'p' or choice == 'Paper' or choice == 'paper' or choice == '3':
            player1_choice = 3
            break
        else:
            #Foutmelding bij ongeldige invoer
            print("---------------------------------------------------------------")
            print('That\'s not possible!!')
            #Tekst die aangeeft wat er moet gebeuren
            print('Please try again')
            print("---------------------------------------------------------------")
            #Probeer nog eens
            continue

    #Player 2
    #Zolang bovengenomde klopt het onderstaande wordt uitgevoerd
    while True:
        #uitleg keuzemenu
        print("Game Choices")
        print("1 = Rock")
        print("2 = Scissors")
        print("3 = Paper")
        print("---------------------------------------------------------------")
        #Tekst die aangeeft wie er aan de beurt is
        print("Player 2")
        #Invoer keuze Speler 2
        print("choose a number:")
        choice = input('=')
        print("---------------------------------------------------------------")
        #Detect Invoer keuze Rock Speler 2
        if choice == 'r' or choice == 'R' or choice == 'Rock' or choice == 'rock' or choice == '1':
            player2_choice = 1
            break
        #Detect Invoer keuze Scissors Speler 2
        elif choice == 'S' or choice == 's' or choice == 'Scissors' or choice == 'sciccors' or choice == '2':
            player2_choice = 2
            break
        #Detect Invoer keuze Paper Speler 2
        elif choice == 'P' or choice == 'p' or choice == 'Paper' or choice == 'paper' or choice == '3':
            player2_choice = 3
            break
        #als bovenstaande niet wordt gebruikt wordt onderstaande van toepassing
        else:
            #Foutmelding bij ongeldige invoer
            print("---------------------------------------------------------------")
            print('That\'s not possible!!')
            #Tekst die aangeeft wat er moet gebeuren
            print('Please try again')
            print("---------------------------------------------------------------")
            #Probeer nog eens
            continue

    #Zolang bovengenomde klopt het onderstaande wordt uitgevoerd
    while True:
        #Bij gelijk spel
        if player1_choice ==  player2_choice:
            print('It\'s a draw!')
            print("---------------------------------------------------------------")

        #Speler 1 Rock - Speler 2 Scissors
        elif (player1_choice == 1 and  player2_choice == 2 and print("Player 1 Wins! Because Rock smashes Scissors")):
            print("")

        #Speler 1 Rock - Speler 2 Paper
        elif (player1_choice == 1 and  player2_choice == 3 and print("Player 2 Wins! Because Paper covers Rock")):
            print("")

        #Speler 1 Scissors - Speler 2 Rock
        elif (player1_choice == 2 and  player2_choice == 1 and print("Player 2 Wins! Because Rock smashes Scissors")):
            print("")

        #Speler 1 Scissors - Speler 2 Paper
        elif (player1_choice == 2 and  player2_choice == 3 and print("Player 1 Wins! Because Scissors cuts Paper")):
            print("")

        #Speler 1 Paper - Speler 2 Rock
        elif (player1_choice == 3 and  player2_choice == 1 and print("Player 1 Wins! Because Paper covers Rock")):
            print("")

        #Speler 1 Paper - Speler 2 Scissors
        elif (player1_choice == 3 and  player2_choice == 2 and print("Player 2 Wins! Because Scissors cuts Paper")):
            print("")

        #Zolang bovengenomde klopt het onderstaande wordt uitgevoerd
        while True:
            #Tekst met bedankt voor het spelen
            print("---------------------------------------------------------------")
            print("Thanks for playing!")
            #Wachten op enter om opnieuw te beginnen
            answer = input("Play again? Press enter")
            print("---------------------------------------------------------------")
            #Terug naar het begin
            return RPS()
#einde declaratie RPS
RPS()