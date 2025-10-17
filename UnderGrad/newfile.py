import os
import shutil
import _config
import sys

configList = _config.get_config_list()

genType = configList["gen_type"]
genPath = configList["gen_path"]
homePath = configList["home_path"]
instOpen = configList["inst_open"]

docTitle = sys.argv[1]

def CreateDocument(title):
    if title != "":
        os.chdir(genPath)
        os.mkdir(f'{title}')

        source = f'{homePath}\\temp.tex'
        dest = f'{genPath}\\{title}\\{title}.tex'

        shutil.copyfile(source, dest)

        os.chdir(f'{genPath}\\{title}')
        os.system(f"{title}.tex")
    else:
        pass

CreateDocument(docTitle)