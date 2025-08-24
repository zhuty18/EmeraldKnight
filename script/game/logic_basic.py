# coding = utf-8

"""基类逻辑"""

from abc import ABC


class BasicLogic(ABC):
    """基类固有逻辑"""

    @classmethod
    def get_functions(cls):
        """获取生成函数"""
        if not hasattr(cls, "_existence_functions"):
            cls._existence_functions = []
        return cls._existence_functions

    @classmethod
    def add_get_functions(cls, func, end=True):
        """增加基于id生成的函数"""
        if func not in cls.get_functions():
            cls.get_functions().insert(-1 if end else 0, func)

    @classmethod
    def get_existence(cls, para_1=None, para_2=None):
        """通过id获取实例"""
        for func in cls.get_functions():
            item = func(para_1, para_2)
            if item:
                return item
        return None

    def get_id(self):
        """获取实例ID"""
        return getattr(self, "_id", self.__class__.__name__ + " ID")
