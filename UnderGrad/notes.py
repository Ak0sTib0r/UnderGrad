import _config
import subprocess as prog

configList = _config.get_config_list()
genPath = configList["gen_path"]

prog.Popen(f'explorer {genPath}')