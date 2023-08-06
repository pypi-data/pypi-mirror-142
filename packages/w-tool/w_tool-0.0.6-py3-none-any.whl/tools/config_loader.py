# coding=utf-8
#!/usr/bin/env python3
import copy
import json
import os
import sys
import threading
import time
import uuid

from logzero import logger
platform = 1 if sys.platform.startswith('win') else 0

CONFIG_PATH = 'C:/configs' if platform else '/home/configs'
if not os.path.exists(CONFIG_PATH):
    os.mkdir(CONFIG_PATH)
else:
    if not os.path.isdir(CONFIG_PATH):
        os.remove(CONFIG_PATH)
        os.mkdir(CONFIG_PATH)

class ConfigLoader:

    def __init__(self, web_name):
        self.web_name = web_name
        self.__config = {}
        self.__reload()
        self.m_time = None
        self.save_no_reload = False
        self.save_lock = threading.Lock()
        t = threading.Thread(target=self.monitor_change, daemon=True)
        t.start()

    @property
    def config(self):
        return self.__config

    def monitor_change(self):
        path = os.path.join(CONFIG_PATH, self.web_name + '.json')
        if self.m_time is None:
            self.m_time = os.path.getmtime(path)
        while True:
            m_time = os.path.getmtime(path)
            if not m_time == self.m_time:
                self.__reload()
                logger.info('配置文件已修改， 重载配置')
                self.m_time = m_time
            time.sleep(5)

    def __reload(self):
        web_name = self.web_name
        path = os.path.join(CONFIG_PATH, web_name + '.json')
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                f.write('{}')
        cp_conf = copy.deepcopy(self.__config)
        with open(path, 'r', encoding='utf-8') as f:
            config_str = f.read()
        try:
            config = json.loads(config_str)
            self.__config.clear()
            for k, v in config.items():
                self.__config[k] = copy.deepcopy(v)
        except Exception as e:
            logger.error('配置加载出错: ' + str(e))
            self.__config.update(cp_conf)

    def set(self, name, value, is_save=False):
        if self.__config.get(name, 'w_undefined') != value:
            self.__config[name] = value
            if is_save:
                with self.save_lock:
                    self.save()
                    self.save_no_reload = True

    def get(self, *args):
        res = self.__config.get(*args)
        if len(args) > 1:
            if args[0] not in self.__config:
                self.__config[args[0]] = res
                with self.save_lock:
                    self.save_no_reload = True
                    self.save()
        return res

    def save(self):
        path = os.path.join(CONFIG_PATH, self.web_name + '.json')
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                f.write('{}')
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(json.dumps(self.__config, ensure_ascii=False, indent=4))
        except Exception as e:
            logger.error('覆盖配置文件失败')

    def get_uuid_with_key(self, key):
        uuid_ref = self.get('uuid_ref', {})
        if not uuid_ref:
            self.set('uuid_ref', {})
            self.save()
        if not key in uuid_ref:
            uuid_ref[key] = str(uuid.uuid1()).upper()
            self.set('uuid_ref', uuid_ref)
            self.save()
        return uuid_ref.get(key)