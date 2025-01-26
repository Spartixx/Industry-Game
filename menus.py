import tkinter as tk
import pygame
from utils.fonctions.files import loadConfig
from utils.fonctions.solde import strSolde

# Je ferais un fichier de configuration pour obtenir les textures avec des constantes plus tard, j'ai pas eus le courage
# J'optimiserais la création de menu plus tard, tKinter n'est pas un domaine où je suis très bon
    
priceConfig = loadConfig("configs/price.json")
config = loadConfig("configs/config.json")
blocConfig = loadConfig("configs/blocs.json")

finalSelection = []



# Exécuter le menu en paramètres
def execMenu(menu, level = None, playerConfig = None):
    # Il n'y a que le menu des convoyeurs pour le moment, celui pour l'achat de terrain est le prochain
    if menu == "convoyeur":
        return convoyeurMenu()
    elif menu == "buyField":
        return BuyMenu(playerConfig)
    elif menu == "upgrade":
        return upgradeMenu(level)
    elif menu == "bloc":
        return BlocMenu()
    elif menu == "machine":
        return MachineMenu()
    

def setMenuInfos(dimensions, titre, bg = "black", xAdd=0, yAdd=0):
    coords = pygame.mouse.get_pos() # coordonnées souris
    gui = tk.Tk() # fenêtre Tkinter
    gui.geometry(f"{dimensions[0]}x{dimensions[1]}+{coords[0]+xAdd}+{coords[1]+yAdd}") # Taille de la fenêtre
    gui.title(titre) # Titre ( même si on ne le voit pas )
    gui["bg"] = bg # Fond d'écran 
    gui.resizable(width=False, height=False) # On ne peut pas la redimensionner
    gui.wm_attributes("-topmost", 1) # La fenêtre doit être affichée en premier plan quoi qu'il arrive
    gui.overrideredirect(True) # La fenêtre ne peut pas être fermée
    selection = [None] # Variable qui associe le convoyeur choisit
    return {"coords": coords, "gui": gui, "selection": selection}


def setButtonsV(gui, tkImages, selections):
    for i, j in enumerate(selections):
        tk.Button(gui, image=tkImages[i], command=lambda j=j: selectionnedButon(j, gui), bg=gui["bg"]).grid(column=1, row=i)

def setButtonsH(gui, tkImages, selections):
    for i, j in enumerate(selections):
        tk.Button(gui, image=tkImages[i], command=lambda j=j: selectionnedButon(j, gui), bg=gui["bg"]).grid(column=i, row=1)


def selectionnedButon(selection, gui):
    finalSelection.append(selection)
    gui.destroy()
    

def getImages(images):
    return [tk.PhotoImage(file = image) for image in images]


# Menu des convoyeurs
def convoyeurMenu():
    
    menuInfos = setMenuInfos(["134", "535"], "Convoyeur", xAdd=-64)
    gui = menuInfos["gui"]
    
    tkImages = getImages([config["CONVOYEUR_LEFT_BUTTON"], config["CONVOYEUR_RIGHT_BUTTON"], config["CONVOYEUR_UP_BUTTON"], config["CONVOYEUR_DOWN_BUTTON"]])
    selections = [config["CONVOYEUR_LEFT"], config["CONVOYEUR_RIGHT"], config["CONVOYEUR_UP"], config["CONVOYEUR_DOWN"]]
    setButtonsV(gui, tkImages, selections)


    gui.mainloop()

    return (finalSelection[-1], "convoyeur") # Je retourne le convoyeur choisit


def upgradeMenu(level):

    coords = pygame.mouse.get_pos() # coordonnées souris

    if coords[1] < 178:
        menuInfos = setMenuInfos(["402", "185"], "Upgrades", "#367ea0", 0, 178)
    elif coords[1] > pygame.display.get_window_size()[1]-178:
        menuInfos = setMenuInfos(["402", "185"], "Upgrades", "#367ea0", 0, -178)
    else:
        menuInfos = setMenuInfos(["402", "185"], "Upgrades", "#367ea0")
    gui = menuInfos["gui"]
    
    tkImages = getImages([config["UPGRADE_RESSOURCE"], config["UPGRADE_SPEED"], config["UPGRADE_STOCK"]])
    selections = ["ressource", "speed", "stock"]
    
    setButtonsH(gui, tkImages, selections)
    for i, j in enumerate(("ressource", "speed", "stock")):
        tk.Label(gui, text=strSolde(priceConfig["machines"][j][str(level[j]+1)]), font=("", 30), bg="#367ea0").grid(column=i, row=2)

    gui.mainloop()

    return finalSelection[-1] # Je retourne le convoyeur choisit


def BlocMenu():


    menuInfos = setMenuInfos(["138", "125"], "Blocs", bg="#524f4f")
    gui = menuInfos["gui"]
    
    tkImages = getImages([config["GRASS"], config["DIRT"]])
    selections = [(config["GRASS"], "grass"), (config["DIRT"], "dirt")]
    
    setButtonsH(gui, tkImages, selections)
    for i, j in enumerate(("grass", "dirt")):
        tk.Label(gui, text=strSolde(blocConfig[j]["price"]), font=("", 30), bg="#524f4f", fg="white").grid(column=i, row=2)

    gui.mainloop()

    return finalSelection[-1] # Je retourne le convoyeur choisit


def MachineMenu():


    menuInfos = setMenuInfos(["255", "125"], "Machines", bg="#524f4f", xAdd=-192)
    gui = menuInfos["gui"]
    
    tkImages = getImages([config["FOREUSE_BUTTON"], config["FONDERIE_BUTTON"], config["CONVOYEUR_BUTTON"]])
    selections = [(config["FOREUSE_BUTTON"], "foreuse"), (config["FONDERIE_BUTTON"], "fonderie"), (config["CONVOYEUR_BUTTON"], "convoyeur")]
    
    setButtonsH(gui, tkImages, selections)
    for i, j in enumerate(("foreuse", "fonderie", "convoyeur")):
        tk.Label(gui, text=strSolde(blocConfig[j]["price"]), font=("", 30), bg="#524f4f", fg="white").grid(column=i, row=2)

    gui.mainloop()

    return finalSelection[-1] # Je retourne le convoyeur choisit


def BuyMenu(playerConfig):


    menuInfos = setMenuInfos(["270", "135"], "Blocs", bg="#524f4f")
    gui = menuInfos["gui"]
    
    tkImages = getImages([config["GREEN"], config["NO"]])
    selections = ["yes", "no"]
    
    setButtonsH(gui, tkImages, selections)
    tk.Label(gui, text=strSolde(int(playerConfig["field"])), font=("", 20), bg="#18b123", fg="white").grid(column=0, row=1)

    gui.mainloop()

    return finalSelection[-1] # Je retourne le convoyeur choisit