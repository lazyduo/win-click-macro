from win-click-macro.window import Window
import os
import yaml
import time


if __name__ == '__main__':
    cfg_file = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'config.yaml')
    with open(cfg_file, 'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
        name = cfg['window']['name']