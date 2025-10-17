"""
  _    _           _            _____               _ 
 | |  | |         | |          / ____|             | |
 | |  | |_ __   __| | ___ _ __| |  __ _ __ __ _  __| |
 | |  | | '_ \ / _` |/ _ \ '__| | |_ | '__/ _` |/ _` |
 | |__| | | | | (_| |  __/ |  | |__| | | | (_| | (_| |
  \____/|_| |_|\__,_|\___|_|   \_____|_|  \__,_|\__,_|
 """

__author__ = "Ákos Hadar"
__version__ = "0.5"

import customtkinter
import os
import mktemp
import subprocess as prog
import _config
import webbrowser as browser
from PIL import Image

configList = _config.get_config_list()

genType = configList["gen_type"]
genPath = configList["gen_path"]
homePath = configList["home_path"]
instOpen = configList["inst_open"]

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

rootWidth = 600
rootHeight = 400

yOffSet = -20

root = customtkinter.CTk()
root.geometry(f"{rootWidth}x{rootHeight}")
root.title("UnderGrad")
root.wm_resizable(width = False, height = False)
root.wm_iconbitmap(f'{homePath}\\UG_Cropped_Right.ico')

logoWidth = 260
logoHeight = 260

logoX = 20
logoY = 70

logoImage = customtkinter.CTkImage(light_image = Image.open('UG_Cropped_Right.png'), dark_image = Image.open('UG_Cropped_Right.png'), size=(logoWidth,logoHeight))

logoLabel = customtkinter.CTkLabel(root, text = "", image = logoImage)
logoLabel.place(x = logoX, y = logoY)

frame = customtkinter.CTkFrame(master = root)
frame.place(x = rootWidth / 2, y = 0)
frame._set_dimensions(width = rootWidth / 2, height = rootHeight)

titleLabel = customtkinter.CTkLabel(master = frame, text = "UnderGrad", font = ("Roboto", 40), text_color = "white")
titleLabel.place(x = 60, y = 30 + yOffSet)

authLabel = customtkinter.CTkLabel(master = frame, text = f"by {__author__}", font = ("Roboto", 10), text_color = "gray")
authLabel.place(x = 230, y = 380)

versionLabel = customtkinter.CTkLabel(master = frame, text = f"UnderGrad {__version__}", font = ("Roboto", 10), text_color = "white")
versionLabel.place(x = 166, y = 380)

#================================ New Template ================================
def NewDoc():
    dialog = customtkinter.CTkInputDialog(text = "Document Name:", title = "New Document")
    title = dialog.get_input()
    mktemp.CreateDocument(title)

newDocButton = customtkinter.CTkButton(master = root, text = "New File", command = NewDoc, fg_color = "#ce6c2a", hover_color = "#ff8433")
newDocButton.place(x = rootWidth * 0.75 - 75, y = 100 + yOffSet)
newDocButton._set_dimensions(width = 150, height = 30)

#================================ Open File ================================
def OpenFile():
    prog.Popen(f'explorer {genPath}')

openFileButton = customtkinter.CTkButton(master = root, text = "Open File", command = OpenFile, fg_color = "#ce6c2a", hover_color = "#ff8433")
openFileButton.place(x = rootWidth * 0.75 - 75, y = 150 + yOffSet)
openFileButton._set_dimensions(width = 150, height = 30)

#================================ Open Config ================================
def OpenConfig():
    os.chdir(homePath)
    os.system("config.json")

openConfigButton = customtkinter.CTkButton(master = root, text = "View Config File", command = OpenConfig, fg_color = "#ce6c2a", hover_color = "#ff8433")
openConfigButton.place(x = rootWidth * 0.75 - 75, y = 200 + yOffSet)
openConfigButton._set_dimensions(width = 150, height = 30)

#================================ Visit Github Page ================================
def EditTemplate():
    os.system('temp.tex')

editTemplateButton = customtkinter.CTkButton(master = root, text = "Edit Template", command = EditTemplate, fg_color = "#ce6c2a", hover_color = "#ff8433")
editTemplateButton.place(x = rootWidth * 0.75 - 75, y = 250 + yOffSet)
editTemplateButton._set_dimensions(width = 150, height = 30)

#================================ Terminal ================================
def Terminal():
    os.system('start')

visitGitHubButton = customtkinter.CTkButton(master = root, text = "Terminal", command = Terminal, fg_color = "#ce6c2a", hover_color = "#ff8433")
visitGitHubButton.place(x = rootWidth * 0.75 - 75, y = 300 + yOffSet)
visitGitHubButton._set_dimensions(width = 150, height = 30)

#================================ Visit Github Page ================================
def VisitGitHubPage():
    browser.open('https://github.com/Ak0sTib0r/UnderGrad')

visitGitHubButton = customtkinter.CTkButton(master = root, text = "GitHub Page", command = VisitGitHubPage, fg_color = "#651fc1", hover_color = "#7124d5")
visitGitHubButton.place(x = rootWidth * 0.75 - 75, y = 350 + yOffSet)
visitGitHubButton._set_dimensions(width = 150, height = 30)

#================================ Start GUI ================================
def init():
    root.mainloop()