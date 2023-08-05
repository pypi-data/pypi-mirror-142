from math import fabs
import uuid
from functools import wraps
import inspect
from configparser import ConfigParser
import time

from enum import Enum


class GattinoEvent(Enum):
    EVENT_START = "EVENT_START"
    EVENT_TICK = "EVENT_TICK"
    EVENT_EXIT = "EVENT_EXIT"


class Gattino:
    # 应用id
    appid = None
    # 配置文件
    conf_file = None
    # 配置文件节点
    conf_key = "gattino"
    # 应用id文件
    pid_file = "app.pid"
    # 调试模式
    is_debug = False
    # 命令行参数
    argv = None
    # 配置文件
    conf = {}
    # 扩展文件包
    ext = []
    # 配置工具
    cfg = None
    # 事件列表
    events = {}
    # 运行方法列表
    runner_Dict = {}

    timer_delta = 0.1
    is_running = True

    def debug_print(self, content):
        if self.is_debug:
            print(content)

    def __init__(self, appid=None, conf=None, argv=None, is_debug=False):
        self.appid = appid if appid else str(uuid.uuid1())
        self.conf_file = conf if conf else "app.conf"
        self.argv = argv if argv else None
        self.is_debug = is_debug
        for item in GattinoEvent:
            self.events[item.value] = []

    def load_conf(self):
        """
        从配置文件加载配置
        """
        self.cfg = ConfigParser()
        self.cfg.read(self.conf_file)
        self.conf = dict(self.cfg.items(self.conf_key))

    """
    从配置函数读取配置信息
    """

    def load_conf_read_args(self, func, args):
        return dict(zip(inspect.signature(func).parameters.keys(), args))

    """
    初始化装饰器
    """

    def init(self, *args2, **option):
        # 初始化appid
        with open(self.pid_file, 'w') as f:
            f.write(self.appid)
        # 从配置文件加载
        self.load_conf()
        self.debug_print(
            f"配置文件:[{self.conf_file}]加载[{len(self.conf.items())}]项配置信息")
        # 加载扩展配置
        for item in self.ext:
            item_conf = item.load_conf()
            self.debug_print(
                f"扩展配置文件:[{item.conf_key}]|[{self.conf_file}]加载[{len(item_conf.items())}]项配置信息")
            self.conf.update(item_conf)
        # 从参数中读取配置
        args_conf = {}
        [args_conf.update(arg) for arg in args2]
        self.debug_print(
            f"配置函数:[{self.init.__name__}]加载[{len(args_conf.items())}]项配置信息")
        self.conf.update(args_conf)
        self.debug_print(
            f"配置函数:[{self.init.__name__}-KV]加载[{len(option.items())}]项配置信息")
        self.conf.update(option)

        def wrapped_function(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # 执行配置函数
                return func(*args, **kwargs)
            return wrapper
        return wrapped_function

    def run(self, delta_time: int = 0, at_once: bool = False):
        """[启动装饰器]

        Args:
            delta_time (int, optional): [执行间隔]. Defaults to 0.
            at_once (bool, optional): [是否立刻执行]. Defaults to False.
        """
        def wrapped_function(func):
            self.debug_print(
                f"添加运行器:[{func.__name__}]加载[执行间隔]:{delta_time},是否立刻执行:{at_once}]")
            # 添加运行器
            self.runner_Dict[func.__name__] = {"func":
                                               func, "delta_time": delta_time, "at_once": at_once, "timer": 0 if at_once else delta_time}

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return wrapped_function

    """
    启动
    """

    def start(self):
        self.is_running = True
        print("==================================================")
        print(f"应用[{self.appid}]启动")
        print("=============== Powered by Gattino ===============")
        [item(None)
         for item in self.events[GattinoEvent.EVENT_START.value]]
        ts = time.time()
        for _, v in self.runner_Dict.items():
            v["timer"] = ts+(0 if v["at_once"] else v["delta_time"])
        while self.is_running:
            for _, v in self.runner_Dict.items():
                if v["timer"] - ts < 0:
                    v["timer"] = ts + v["delta_time"]
                    v["func"]()
            [item(ts)
             for item in self.events[GattinoEvent.EVENT_TICK.value]]
            ts = time.time()
            time.sleep(self.timer_delta)
        [item(None)
         for item in self.events[GattinoEvent.EVENT_EXIT.value]]
        print(f"应用[{self.appid}]退出")

    """
    中止
    """

    def stop(self):
        self.is_running = False
