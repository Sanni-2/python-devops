

data = []
class Game:
    
    def __init__(self,player):
        self.player = player


    def setName(self,new_player):
        self.player = new_player

  




    def Intro(self):
        print("                                                                                                       ")
        print("-------------------------------------------------------------------------------------------------------")
        print("-----                         WELCOME TO THIS CHOSE YOUR ADVENTURE GAME!                          -----")
        print("-----                  YOU ARE EATING AND STARTED CHOKING, CHOSE YOUR NEXT MOVE                   -----")
        print("-------------------------------------------------------------------------------------------------------")
        print("                                                                                                       ")

        a_b=["water","dechoker"]
        water_dechocker = ''
        while water_dechocker not in a_b:
            water_dechocker = input("    Careful now, do you want to drink some waater or grab the dechocker? Water/Dechocker : ")
            if water_dechocker.lower() == "water":
                data.append("Player choosed water")
                self.water()
            elif water_dechocker.lower() == "dechocker":
                data.append("Player choosed Dechocker")
                self.dechocker()
            else:
                data.append("Player did not select any yet")
                print("You dont't have much time, quickly enter a choice. Water/Dechocker")


    def water(self):
        print("                                                                                                       ")
        print("-------------------------------------------------------------------------------------------------------")
        print("-----                        coughs!!!! coughs!!!!  ....................                          -----")
        print("-----                  you grab your cup of water, tried to drink!!! cough some more and fell     -----")
        print("-----                                      OH NO!! YOU DIED!!!                                    -----")
        print("-------------------------------------------------------------------------------------------------------")
        print("                                                                                                       ")
        with open("game-log.log", mode="w", encoding="utf-8") as my_log:
            for i in data:
                my_log.write(f" {str(i)} |\n")

        quit()
    


    def dechocker(self):
        print("                                                                                                                          ")
        print("--------------------------------------------------------------------------------------------------------------------------")
        print("-----                                           Oh!!!! I guess this will work                                        -----")
        print("-----                  you grabbed the dechocker in the firstaid box, set it up and ready to go,                     -----")
        print("-----      you placed the mask over your mouth, but dont know what to do next, now its a guessing game to survive,   -----")
        print("-----                                    you thought to yourself, uhm one final guess                                -----")
        print("--------------------------------------------------------------------------------------------------------------------------")
        print("                                                                                                                          ")

        pul_pus=["pull","push"]
        pull_push = ''
        while pull_push not in pul_pus:
            pull_push = input("Do you want to push or pull the valve? Pull/Push: ")
            if pull_push.lower() == "pull":
                data.append("Player choosed Pull")
                self.pull()
            elif pull_push.lower() == "push":
                data.append("Player choosed push")
                self.push()
            else:
                data.append("Player did not select yet")
                print("Buddy, remember you are chocking, make a decission!  Pull/Push")



    def pull(self):
        print("                                                                                                                     ")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("-----                                           just with an attempt of pulling,                                -----")
        print("-----                                tadaaaa!!!   you were relieved and live to see another day                 -----")
        print("-----                         Thanks for completing, dont forget to buy a DECHOCKER for your household          -----")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("                                                                                                                     ")
        with open("game-log.log", mode="w", encoding="utf-8") as my_log:
            for i in data:
                my_log.write(f" {str(i)} |\n")
        quit()



    def push(pull):
        print("                                                                                            ")
        print("--------------------------------------------------------------------------------------------")
        print("-----                                coughs!!! coughs!!!                               -----")
        print("-----                                falls to the ground                               -----")
        print("-----                                OH NO!! YOU DIED!!!                               -----")
        print("--------------------------------------------------------------------------------------------")
        print("                                                                                            ")
        with open("game-log.log", mode="w", encoding="utf-8") as my_log:
            for i in data:
                my_log.write(f" {str(i)} |\n")
        quit()












def main():
    player = input("Enter name: ")
    chocking = Game(player)
    chocking.Intro()

main()





