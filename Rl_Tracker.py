import tkinter
from tkinter import *
import tkinter.messagebox
from RlApi import*
from PIL import Image, ImageTk 


def leave():
    window.destroy()

def normal():
    pseudo = pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    check=0

    try:
        player_id=rltracker.player_id( pseudo )
        check=1

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    if check==1:
        try:
            saison=rltracker.saison( pseudo )
            solo=rltracker.solo( pseudo )
            solo_div=rltracker.solo_div( pseudo )
            solo_ws=rltracker.solo_ws( pseudo )
            solo_mmr=rltracker.solo_mmr( pseudo )
            solo_nb=rltracker.solo_nb( pseudo )
            solo_pourcent=rltracker.solo_pourcent( pseudo )

            solo="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn 1v1 , il est : " + solo + " " + solo_div+"\nIl a un mmr de : "+str(solo_mmr)+"\nEn : "+str(solo_nb)+ " game\nIl a une win streak de : "+str(solo_ws)+"\nIl est top :" +str(100-solo_pourcent) + "%"
            
            duo=rltracker.duo( pseudo )
            duo_div=rltracker.duo_div( pseudo )
            duo_ws=rltracker.duo_ws( pseudo )
            duo_mmr=rltracker.duo_mmr( pseudo )
            duo_nb=rltracker.duo_nb( pseudo )
            duo_pourcent=rltracker.duo_pourcent( pseudo )

            duo="\n\nEn 2v2 , il est : " + duo + " " + duo_div+"\nIl a un mmr de : "+str(duo_mmr)+"\nEn : "+str(duo_nb)+ " game\nIl a une win streak de : "+str(duo_ws)+"\nIl est top :" +str(100-duo_pourcent) + "%"
            
            trio=rltracker.trio( pseudo )
            trio_div=rltracker.trio_div( pseudo )
            trio_ws=rltracker.trio_ws( pseudo )
            trio_mmr=rltracker.trio_mmr( pseudo )
            trio_nb=rltracker.trio_nb( pseudo )
            trio_pourcent=rltracker.trio_pourcent( pseudo )

            trio="\n\nEn 3v3 , il est : " + trio + " " + trio_div+"\nIl a un mmr de : "+str(trio_mmr)+"\nEn : "+str(trio_nb)+ " game\nIl a une win streak de : "+str(trio_ws)+"\nIl est top :" +str(100-trio_pourcent) + "%"
            
            texte=solo+duo+trio
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)
        except:
            IndexError
            texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())
   
def solo():
    pseudo=pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    
    try:
        player_id=rltracker.player_id( pseudo )

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    try:
        saison=rltracker.saison( pseudo )
        solo=rltracker.solo( pseudo )
        solo_div=rltracker.solo_div( pseudo )
        solo_ws=rltracker.solo_ws( pseudo )
        solo_mmr=rltracker.solo_mmr( pseudo )
        solo_nb=rltracker.solo_nb( pseudo )
        solo_pourcent=rltracker.solo_pourcent( pseudo )

        solo="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn 1v1 , il est : " + solo + " " + solo_div+"\nIl a un mmr de : "+str(solo_mmr)+"\nEn : "+str(solo_nb)+ " game\nIl a une win streak de : "+str(solo_ws)+"\nIl est top :" +str(100-solo_pourcent) + "%"
        
        texte=solo
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

def duo():
    pseudo=pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    
    try:
        player_id=rltracker.player_id( pseudo )

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    try:
        saison=rltracker.saison( pseudo )
        duo=rltracker.duo( pseudo )
        duo_div=rltracker.duo_div( pseudo )
        duo_ws=rltracker.duo_ws( pseudo )
        duo_mmr=rltracker.duo_mmr( pseudo )
        duo_nb=rltracker.duo_nb( pseudo )
        duo_pourcent=rltracker.duo_pourcent( pseudo )

        duo="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn 2v2 , il est : " + duo + " " + duo_div+"\nIl a un mmr de : "+str(duo_mmr)+"\nEn : "+str(duo_nb)+ " game\nIl a une win streak de : "+str(duo_ws)+"\nIl est top :" +str(100-duo_pourcent) + "%"
        
        texte=duo
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

def trio():
    pseudo=pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    
    try:
        player_id=rltracker.player_id( pseudo )

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    try:
        saison=rltracker.saison( pseudo )
        trio=rltracker.trio( pseudo )
        trio_div=rltracker.trio_div( pseudo )
        trio_ws=rltracker.trio_ws( pseudo )
        trio_mmr=rltracker.trio_mmr( pseudo )
        trio_nb=rltracker.trio_nb( pseudo )
        trio_pourcent=rltracker.trio_pourcent( pseudo )

        trio="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn 3v3 , il est : " + trio + " " + trio_div+"\nIl a un mmr de : "+str(trio_mmr)+"\nEn : "+str(trio_nb)+ " game\nIl a une win streak de : "+str(trio_ws)+"\nIl est top :" +str(100-trio_pourcent) + "%"
        
        texte=trio
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())


def extra():
    pseudo = pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    check=0

    try:
        player_id=rltracker.player_id( pseudo )
        check=1

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    if check==1:
        try:
            saison=rltracker.saison( pseudo )
            panier=rltracker.panier( pseudo )
            panier_div=rltracker.panier_div( pseudo )
            panier_ws=rltracker.panier_ws( pseudo )
            panier_mmr=rltracker.panier_mmr( pseudo )
            panier_nb=rltracker.panier_nb( pseudo )
            panier_pourcent=rltracker.panier_pourcent( pseudo )

            panier="Voila les stats de "+str(pseudo)+" en mode extra lors de la saison "+str(saison)+"\n\nEn panier , il est : " + panier + " " + panier_div+"\nIl a un mmr de : "+str(panier_mmr)+"\nEn : "+str(panier_nb)+ " game\nIl a une win streak de : "+str(panier_ws)+"\nIl est top :" +str(100-panier_pourcent) + "%"
            
            rumble=rltracker.rumble( pseudo )
            rumble_div=rltracker.rumble_div( pseudo )
            rumble_ws=rltracker.rumble_ws( pseudo )
            rumble_mmr=rltracker.rumble_mmr( pseudo )
            rumble_nb=rltracker.rumble_nb( pseudo )
            rumble_pourcent=rltracker.rumble_pourcent( pseudo )

            rumble="\n\nEn rumble , il est : " + rumble + " " + rumble_div+"\nIl a un mmr de : "+str(rumble_mmr)+"\nEn : "+str(rumble_nb)+ " game\nIl a une win streak de : "+str(rumble_ws)+"\nIl est top :" +str(100-rumble_pourcent) + "%"
            
            dropshot=rltracker.dropshot( pseudo )
            dropshot_div=rltracker.dropshot_div( pseudo )
            dropshot_ws=rltracker.dropshot_ws( pseudo )
            dropshot_mmr=rltracker.dropshot_mmr( pseudo )
            dropshot_nb=rltracker.dropshot_nb( pseudo )
            dropshot_pourcent=rltracker.dropshot_pourcent( pseudo )

            dropshot="\n\nEn dropshot , il est : " + dropshot + " " + dropshot_div+"\nIl a un mmr de : "+str(dropshot_mmr)+"\nEn : "+str(dropshot_nb)+ " game\nIl a une win streak de : "+str(dropshot_ws)+"\nIl est top :" +str(100-dropshot_pourcent) + "%"
            
            palet=rltracker.palet( pseudo )
            palet_div=rltracker.palet_div( pseudo )
            palet_ws=rltracker.palet_ws( pseudo )
            palet_mmr=rltracker.palet_mmr( pseudo )
            palet_nb=rltracker.palet_nb( pseudo )
            palet_pourcent=rltracker.palet_pourcent( pseudo )

            palet="\n\nEn palet , il est : " + palet + " " + palet_div+"\nIl a un mmr de : "+str(palet_mmr)+"\nEn : "+str(palet_nb)+ " game\nIl a une win streak de : "+str(palet_ws)+"\nIl est top :" +str(100-palet_pourcent) + "%"
            
            tournoi=rltracker.tournoi( pseudo )
            tournoi_div=rltracker.tournoi_div( pseudo )
            tournoi_ws=rltracker.tournoi_ws( pseudo )
            tournoi_mmr=rltracker.tournoi_mmr( pseudo )
            tournoi_nb=rltracker.tournoi_nb( pseudo )
            tournoi_pourcent=rltracker.tournoi_pourcent( pseudo )

            tournoi="\n\nEn tournoi , il est : " + tournoi + " " + tournoi_div+"\nIl a un mmr de : "+str(tournoi_mmr)+"\nEn : "+str(tournoi_nb)+ " game\nIl a une win streak de : "+str(tournoi_ws)+"\nIl est top :" +str(100-tournoi_pourcent) + "%"


            texte=panier+rumble+dropshot+palet+tournoi
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)

        except:
            IndexError
            texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())


def panier():
    pseudo=pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    
    try:
        player_id=rltracker.player_id( pseudo )

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    try:
        saison=rltracker.saison( pseudo )
        panier=rltracker.panier( pseudo )
        panier_div=rltracker.panier_div( pseudo )
        panier_ws=rltracker.panier_ws( pseudo )
        panier_mmr=rltracker.panier_mmr( pseudo )
        panier_nb=rltracker.panier_nb( pseudo )
        panier_pourcent=rltracker.panier_pourcent( pseudo )

        panier="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn panier , il est : " + panier + " " + panier_div+"\nIl a un mmr de : "+str(panier_mmr)+"\nEn : "+str(panier_nb)+ " game\nIl a une win streak de : "+str(panier_ws)+"\nIl est top :" +str(100-panier_pourcent) + "%"
        
        texte=panier
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

def rumble():
    pseudo=pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    
    try:
        player_id=rltracker.player_id( pseudo )

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    try:
        saison=rltracker.saison( pseudo )
        rumble=rltracker.rumble( pseudo )
        rumble_div=rltracker.rumble_div( pseudo )
        rumble_ws=rltracker.rumble_ws( pseudo )
        rumble_mmr=rltracker.rumble_mmr( pseudo )
        rumble_nb=rltracker.rumble_nb( pseudo )
        rumble_pourcent=rltracker.rumble_pourcent( pseudo )

        rumble="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn rumble , il est : " + rumble + " " + rumble_div+"\nIl a un mmr de : "+str(rumble_mmr)+"\nEn : "+str(rumble_nb)+ " game\nIl a une win streak de : "+str(rumble_ws)+"\nIl est top :" +str(100-rumble_pourcent) + "%"
        
        texte=rumble
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

def dropshot():
    pseudo=pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    
    try:
        player_id=rltracker.player_id( pseudo )

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    try:
        saison=rltracker.saison( pseudo )
        dropshot=rltracker.dropshot( pseudo )
        dropshot_div=rltracker.dropshot_div( pseudo )
        dropshot_ws=rltracker.dropshot_ws( pseudo )
        dropshot_mmr=rltracker.dropshot_mmr( pseudo )
        dropshot_nb=rltracker.dropshot_nb( pseudo )
        dropshot_pourcent=rltracker.dropshot_pourcent( pseudo )

        dropshot="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn dropshot , il est : " + dropshot + " " + dropshot_div+"\nIl a un mmr de : "+str(dropshot_mmr)+"\nEn : "+str(dropshot_nb)+ " game\nIl a une win streak de : "+str(dropshot_ws)+"\nIl est top :" +str(100-dropshot_pourcent) + "%"
        
        texte=dropshot
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

def palet():
    pseudo=pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    
    try:
        player_id=rltracker.player_id( pseudo )

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    try:
        saison=rltracker.saison( pseudo )
        palet=rltracker.palet( pseudo )
        palet_div=rltracker.palet_div( pseudo )
        palet_ws=rltracker.palet_ws( pseudo )
        palet_mmr=rltracker.palet_mmr( pseudo )
        palet_nb=rltracker.palet_nb( pseudo )
        palet_pourcent=rltracker.palet_pourcent( pseudo )

        palet="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn palet , il est : " + palet + " " + palet_div+"\nIl a un mmr de : "+str(palet_mmr)+"\nEn : "+str(palet_nb)+ " game\nIl a une win streak de : "+str(palet_ws)+"\nIl est top :" +str(100-palet_pourcent) + "%"
        
        texte=palet
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

def tournoi():
    pseudo=pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    
    try:
        player_id=rltracker.player_id( pseudo )

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

    try:
        saison=rltracker.saison( pseudo )
        tournoi=rltracker.tournoi( pseudo )
        tournoi_div=rltracker.tournoi_div( pseudo )
        tournoi_ws=rltracker.tournoi_ws( pseudo )
        tournoi_mmr=rltracker.tournoi_mmr( pseudo )
        tournoi_nb=rltracker.tournoi_nb( pseudo )
        tournoi_pourcent=rltracker.tournoi_pourcent( pseudo )

        tournoi="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn tournoi , il est : " + tournoi + " " + tournoi_div+"\nIl a un mmr de : "+str(tournoi_mmr)+"\nEn : "+str(tournoi_nb)+ " game\nIl a une win streak de : "+str(tournoi_ws)+"\nIl est top :" +str(100-tournoi_pourcent) + "%"
        
        texte=tournoi
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

def info():
    pseudo = pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    check=0

    try:
        player_id=rltracker.player_id( pseudo )
        check=1

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)

    if check==1:
        try:
            
            compte=rltracker.compte( pseudo )
            if compte!=[]:
                compte="Son compte est lié "+str(compte)
            else:    
                compte=""

            user_id=rltracker.user_id( pseudo )
            player_id=rltracker.player_id( pseudo )
            pays=rltracker.pays( pseudo )
            profil=rltracker.profil( pseudo )

            user_id="\nSon user id est : "+str(user_id)+"\n"
            player_id="Son player id est : "+str(player_id)+"\n"
            pays="Son pays est : "+str(pays)+"\n"
            profil="Son tracker a été vu "+str(profil)+" fois\n"

            louche=rltracker.louche( pseudo )

            if louche==True:
                louche="Il est louche"
            else:
                louche="Il n'est pas louche"

            

            texte=compte+user_id+player_id+pays+profil+louche
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)
        except:
            IndexError
            texte="Le joueur : "+pseudo+"n'a pas fait assez de game"
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)

    

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

def stats():
    pseudo = pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    check=0

    try:
        player_id=rltracker.player_id( pseudo )
        check=1

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())


    if check==1:

        try:

            wins=rltracker.wins( pseudo )
            wins_pourcent=rltracker.wins_pourcent( pseudo )

            wins="Il a fait : "+str(wins)+" wins \nIl est top : "+str(100-wins_pourcent)+"%\n\n"

            goals=rltracker.goals( pseudo )
            goals_pourcent=rltracker.goals_pourcent( pseudo )

            goals="Il a marqué : "+str(goals)+" buts \nIl est top : "+str(100-goals_pourcent)+"%\n\n"

            MVPs=rltracker.MVPs( pseudo )
            MVPs_pourcent=rltracker.MVPs_pourcent( pseudo )

            MVPs="Il a été MVP : "+str(MVPs)+" fois \nIl est top : "+str(100-MVPs_pourcent)+"%\n\n"

            saves=rltracker.saves( pseudo )
            saves_pourcent=rltracker.saves_pourcent( pseudo )

            saves="Il a fait : "+str(saves)+" saves \nIl est top : "+str(100-saves_pourcent)+"%\n\n"

            assists=rltracker.assists( pseudo )
            assists_pourcent=rltracker.assists_pourcent( pseudo )

            assists="Il a fait : "+str(assists)+" assists \nIl est top : "+str(100-assists_pourcent)+"%\n\n"

            shots=rltracker.shots( pseudo )
            shots_pourcent=rltracker.shots_pourcent( pseudo )

            shots="Il a fait : "+str(shots)+" tires \nIl est top : "+str(100-shots_pourcent)+"%\n\n"

            goalShotRatio=rltracker.goalShotRatio( pseudo )
            goalShotRatio_pourcent=rltracker.goalShotRatio_pourcent( pseudo )

            goalShotRatio="Il a un goal ratio de : "+str(goalShotRatio)+" \nIl est top : "+str(100-goalShotRatio_pourcent)+"%\n\n"

            seasonReward=rltracker.seasonReward( pseudo )
            seasonReward_pourcent=rltracker.seasonReward_pourcent( pseudo )
            seasonReward_wins=rltracker.seasonReward_wins( pseudo )

            seasonReward="Il a les récompenses : "+str(seasonReward)+"\nIl a fait : "+str(seasonReward_wins)+" wins\nIl est top : "+str(100-seasonReward_pourcent)+"%\n\n"


            texte=wins+goals+MVPs+saves+assists+shots+goalShotRatio+seasonReward
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)
        except:
            IndexError
            texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)

    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

def all():
    pseudo = pseudo_entry.get()
    toplevel = tkinter.Toplevel()
    toplevel.attributes ('-fullscreen', True)
    check=0

    try:
        player_id=rltracker.player_id( pseudo )
        check=1

    except:
        IndexError
        texte="Le joueur : "+pseudo+" n'existe pas"
        text = Text(toplevel, height=200, width=1000)
        text.insert(INSERT, texte)
        text.pack(pady=20)
        toplevel.bind("<Escape>", lambda evt: toplevel.destroy())


    if check==1:

        try:

            wins=rltracker.wins( pseudo )
            wins_pourcent=rltracker.wins_pourcent( pseudo )

            wins="Il a fait : "+str(wins)+" wins \nIl est top : "+str(100-wins_pourcent)+"%\n\n"

            goals=rltracker.goals( pseudo )
            goals_pourcent=rltracker.goals_pourcent( pseudo )

            goals="Il a marqué : "+str(goals)+" buts \nIl est top : "+str(100-goals_pourcent)+"%\n\n"

            MVPs=rltracker.MVPs( pseudo )
            MVPs_pourcent=rltracker.MVPs_pourcent( pseudo )

            MVPs="Il a été MVP : "+str(MVPs)+" fois \nIl est top : "+str(100-MVPs_pourcent)+"%\n\n"

            saves=rltracker.saves( pseudo )
            saves_pourcent=rltracker.saves_pourcent( pseudo )

            saves="Il a fait : "+str(saves)+" saves \nIl est top : "+str(100-saves_pourcent)+"%\n\n"

            assists=rltracker.assists( pseudo )
            assists_pourcent=rltracker.assists_pourcent( pseudo )

            assists="Il a fait : "+str(assists)+" assists \nIl est top : "+str(100-assists_pourcent)+"%\n\n"

            shots=rltracker.shots( pseudo )
            shots_pourcent=rltracker.shots_pourcent( pseudo )

            shots="Il a fait : "+str(shots)+" tires \nIl est top : "+str(100-shots_pourcent)+"%\n\n"

            goalShotRatio=rltracker.goalShotRatio( pseudo )
            goalShotRatio_pourcent=rltracker.goalShotRatio_pourcent( pseudo )

            goalShotRatio="Il a un goal ratio de : "+str(goalShotRatio)+" \nIl est top : "+str(100-goalShotRatio_pourcent)+"%\n\n"

            seasonReward=rltracker.seasonReward( pseudo )
            seasonReward_pourcent=rltracker.seasonReward_pourcent( pseudo )
            seasonReward_wins=rltracker.seasonReward_wins( pseudo )

            seasonReward="Il a les récompenses : "+str(seasonReward)+"\nIl a fait : "+str(seasonReward_wins)+" wins\nIl est top : "+str(100-seasonReward_pourcent)+"%\n\n"

            
            compte=rltracker.compte( pseudo )
            if compte!=[]:
                compte="Son compte est lié "+str(compte)
            else:    
                compte=""

            user_id=rltracker.user_id( pseudo )
            player_id=rltracker.player_id( pseudo )
            pays=rltracker.pays( pseudo )
            profil=rltracker.profil( pseudo )

            user_id="\nSon user id est : "+str(user_id)+"\n"
            player_id="Son player id est : "+str(player_id)+"\n"
            pays="Son pays est : "+str(pays)+"\n"
            profil="Son tracker a été vu "+str(profil)+" fois\n"

            louche=rltracker.louche( pseudo )

            if louche==True:
                louche="Il est louche"
            else:
                louche="Il n'est pas louche"

            saison=rltracker.saison( pseudo )
            panier=rltracker.panier( pseudo )
            panier_div=rltracker.panier_div( pseudo )
            panier_ws=rltracker.panier_ws( pseudo )
            panier_mmr=rltracker.panier_mmr( pseudo )
            panier_nb=rltracker.panier_nb( pseudo )
            panier_pourcent=rltracker.panier_pourcent( pseudo )

            panier="Voila les stats de "+str(pseudo)+" en mode extra lors de la saison "+str(saison)+"\n\nEn panier , il est : " + panier + " " + panier_div+"\nIl a un mmr de : "+str(panier_mmr)+"\nEn : "+str(panier_nb)+ " game\nIl a une win streak de : "+str(panier_ws)+"\nIl est top :" +str(100-panier_pourcent) + "%"
            
            rumble=rltracker.rumble( pseudo )
            rumble_div=rltracker.rumble_div( pseudo )
            rumble_ws=rltracker.rumble_ws( pseudo )
            rumble_mmr=rltracker.rumble_mmr( pseudo )
            rumble_nb=rltracker.rumble_nb( pseudo )
            rumble_pourcent=rltracker.rumble_pourcent( pseudo )

            rumble="\n\nEn rumble , il est : " + rumble + " " + rumble_div+"\nIl a un mmr de : "+str(rumble_mmr)+"\nEn : "+str(rumble_nb)+ " game\nIl a une win streak de : "+str(rumble_ws)+"\nIl est top :" +str(100-rumble_pourcent) + "%"
            
            dropshot=rltracker.dropshot( pseudo )
            dropshot_div=rltracker.dropshot_div( pseudo )
            dropshot_ws=rltracker.dropshot_ws( pseudo )
            dropshot_mmr=rltracker.dropshot_mmr( pseudo )
            dropshot_nb=rltracker.dropshot_nb( pseudo )
            dropshot_pourcent=rltracker.dropshot_pourcent( pseudo )

            dropshot="\n\nEn dropshot , il est : " + dropshot + " " + dropshot_div+"\nIl a un mmr de : "+str(dropshot_mmr)+"\nEn : "+str(dropshot_nb)+ " game\nIl a une win streak de : "+str(dropshot_ws)+"\nIl est top :" +str(100-dropshot_pourcent) + "%"
            
            palet=rltracker.palet( pseudo )
            palet_div=rltracker.palet_div( pseudo )
            palet_ws=rltracker.palet_ws( pseudo )
            palet_mmr=rltracker.palet_mmr( pseudo )
            palet_nb=rltracker.palet_nb( pseudo )
            palet_pourcent=rltracker.palet_pourcent( pseudo )

            palet="\n\nEn palet , il est : " + palet + " " + palet_div+"\nIl a un mmr de : "+str(palet_mmr)+"\nEn : "+str(palet_nb)+ " game\nIl a une win streak de : "+str(palet_ws)+"\nIl est top :" +str(100-palet_pourcent) + "%"
            
            tournoi=rltracker.tournoi( pseudo )
            tournoi_div=rltracker.tournoi_div( pseudo )
            tournoi_ws=rltracker.tournoi_ws( pseudo )
            tournoi_mmr=rltracker.tournoi_mmr( pseudo )
            tournoi_nb=rltracker.tournoi_nb( pseudo )
            tournoi_pourcent=rltracker.tournoi_pourcent( pseudo )

            tournoi="\n\nEn tournoi , il est : " + tournoi + " " + tournoi_div+"\nIl a un mmr de : "+str(tournoi_mmr)+"\nEn : "+str(tournoi_nb)+ " game\nIl a une win streak de : "+str(tournoi_ws)+"\nIl est top :" +str(100-tournoi_pourcent) + "%"

            saison=rltracker.saison( pseudo )
            solo=rltracker.solo( pseudo )
            solo_div=rltracker.solo_div( pseudo )
            solo_ws=rltracker.solo_ws( pseudo )
            solo_mmr=rltracker.solo_mmr( pseudo )
            solo_nb=rltracker.solo_nb( pseudo )
            solo_pourcent=rltracker.solo_pourcent( pseudo )

            solo="Voila les stats de "+str(pseudo)+" lors de la saison "+str(saison)+"\n\nEn 1v1 , il est : " + solo + " " + solo_div+"\nIl a un mmr de : "+str(solo_mmr)+"\nEn : "+str(solo_nb)+ " game\nIl a une win streak de : "+str(solo_ws)+"\nIl est top :" +str(100-solo_pourcent) + "%"
            
            duo=rltracker.duo( pseudo )
            duo_div=rltracker.duo_div( pseudo )
            duo_ws=rltracker.duo_ws( pseudo )
            duo_mmr=rltracker.duo_mmr( pseudo )
            duo_nb=rltracker.duo_nb( pseudo )
            duo_pourcent=rltracker.duo_pourcent( pseudo )

            duo="\n\nEn 2v2 , il est : " + duo + " " + duo_div+"\nIl a un mmr de : "+str(duo_mmr)+"\nEn : "+str(duo_nb)+ " game\nIl a une win streak de : "+str(duo_ws)+"\nIl est top :" +str(100-duo_pourcent) + "%"
            
            trio=rltracker.trio( pseudo )
            trio_div=rltracker.trio_div( pseudo )
            trio_ws=rltracker.trio_ws( pseudo )
            trio_mmr=rltracker.trio_mmr( pseudo )
            trio_nb=rltracker.trio_nb( pseudo )
            trio_pourcent=rltracker.trio_pourcent( pseudo )

            trio="\n\nEn 3v3 , il est : " + trio + " " + trio_div+"\nIl a un mmr de : "+str(trio_mmr)+"\nEn : "+str(trio_nb)+ " game\nIl a une win streak de : "+str(trio_ws)+"\nIl est top :" +str(100-trio_pourcent) + "%"
            

            texte=solo+duo+trio+panier+rumble+dropshot+palet+tournoi+compte+user_id+player_id+pays+profil+louche+wins+goals+MVPs+saves+assists+shots+goalShotRatio+seasonReward
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)
        except:
            IndexError
            texte="Le joueur : "+pseudo+" n'a pas fait assez de game"
            text = Text(toplevel, height=200, width=1000)
            text.insert(INSERT, texte)
            text.pack(pady=20)
        
    toplevel.bind("<Escape>", lambda evt: toplevel.destroy())

window = tkinter.Tk()
window.attributes ('-fullscreen', True)
window.title("RlTracker by Garrug")
window.iconbitmap("icon.ico")

C = Canvas( bg="blue", height=250, width=300)
filename = PhotoImage(file = "fond.png")
background_label = Label(image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()


# Création du cadre-conteneur pour les menus
zoneMenu = Frame(window, borderwidth=3, bg='#557788')
zoneMenu.pack()

# Création de l'onglet Fichier
menuNormal = Menubutton(zoneMenu, text='normal', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menuNormal.grid(row=0,column=0)

# Création d'un menu défilant
menuDeroulant1 = Menu(menuNormal)
menuDeroulant1.add_command(label='Solo', command = solo)
menuDeroulant1.add_command(label="Duo", command = duo)
menuDeroulant1.add_command(label="Trio", command = trio)
menuDeroulant1.add_command(label="Tout en normal", command = normal)


# Attribution du menu déroulant au menu Affichage
menuNormal.configure(menu=menuDeroulant1)


# Création de l'onglet Edition
menuExtra = Menubutton(zoneMenu, text='extra', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menuExtra.grid(row=0,column=1)

# Création d'un menu défilant
menuDeroulant2 = Menu(menuExtra)
menuDeroulant2.add_command(label='Panier', command = panier)
menuDeroulant2.add_command(label="Rumble", command = rumble)
menuDeroulant2.add_command(label="Dropshot", command = dropshot)
menuDeroulant2.add_command(label="Palet", command = palet)
menuDeroulant2.add_command(label="Tournoi", command = tournoi)
menuDeroulant2.add_command(label="Tout en extra", command = extra)


# Attribution du menu déroulant au menu Affichage
menuExtra.configure(menu=menuDeroulant2)

# Création de l'onglet Format
menuInfo = Menubutton(zoneMenu, text='info', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menuInfo.grid(row=0,column=2)

# Création d'un menu défilant
menuDeroulant3 = Menu(menuInfo)
menuDeroulant3.add_command(label="Toutes les infos", command = info)


# Attribution du menu déroulant au menu Affichage
menuInfo.configure(menu=menuDeroulant3)


menuStats = Menubutton(zoneMenu, text='stats', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menuStats.grid(row=0,column=3)

# Création d'un menu défilant
menuDeroulant4 = Menu(menuStats)
menuDeroulant4.add_command(label="Toutes les stats", command = stats)


# Attribution du menu déroulant au menu Affichage
menuStats.configure(menu=menuDeroulant4)




tkinter.Label(window, text="Entrez le pseudo épic", width=20, height=2).pack()


pseudo_entry = tkinter.Entry()
pseudo_entry.pack(pady=50)

button_normal=tkinter.Button(text="Traquer en normal !", command=normal)
button_normal.pack(pady=5)

button_extra=tkinter.Button(text="Traquer en extra !", command=extra)
button_extra.pack(pady=5)

button_info=tkinter.Button(text="Traquer les infos !", command=info)
button_info.pack(pady=5)

button_stats=tkinter.Button(text="Traquer les stats !", command=stats)
button_stats.pack(pady=5)

button_all=tkinter.Button(text="Traquer tout !", command=all)
button_all.pack(pady=5)

photo = PhotoImage(file ="bouton.png")

button_leave=tkinter.Button(command=leave,image=photo,height=30, width=80)
button_leave.pack(pady=20)

window.mainloop()