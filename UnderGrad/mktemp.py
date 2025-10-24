import os
import shutil
import _config

configList = _config.get_config_list()

genType = configList["gen_type"]
genPath = configList["gen_path"]
homePath = configList["home_path"]
instOpen = configList["inst_open"]

def CreateDocument(title):
    if genType == "boxed":
        if title != "":
            os.chdir(genPath)
            os.mkdir(f'{title}')

            source = f'{homePath}\\temp.tex'
            dest = f'{genPath}\\{title}\\{title}.tex'

            shutil.copyfile(source, dest)

            os.chdir(f'{genPath}\\{title}')

            if instOpen == "true":
                os.system(f"{title}.tex")
        else:
            pass
    elif genType == "free":
        os.chdir(genPath)

        source = f'{homePath}\\temp.tex'
        dest = f'{genPath}\\{title}.tex'

        shutil.copyfile(source, dest)

        os.chdir(f'{genPath}')
        
        if instOpen == "true":
            os.system(f"{title}.tex")