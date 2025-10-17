import json

configFile = open("config.json")
configs = json.load(configFile)["configs"]

#'gen_type' refers to the way the program generates the latex files. 
#'boxed' (creates a folder for each tex triplet) or 'free' (puts each latex triplet straight in the main path folder)
genType = configs["gen_type"]

#'gen_path' refers to the path the program saves all latex triplets.
genPath = configs["gen_path"]

#'home_path' the path of the program and the temp.tex file.
homePath = configs["home_path"]

#'instant_open' refers to the whether the program opens a file on generation
#boolean
instantOpen = configs["instant_open"]

configList = {"gen_type": genType, "gen_path": genPath, "home_path": homePath, "inst_open": instantOpen}

def get_config_list():
    return configList

def __config__():

    if genType == "boxed":
        pass
    elif genType == "free":
        pass

    if instantOpen == "true":
        pass
    elif instantOpen == "false":
        pass
        