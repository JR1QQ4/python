#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 29 条: 用纯属性取代 get 和 set 方法

# 编写新类时，应该用简单的 public 属性来定义其接口，而不要手工实现 set 和 get 方法
# 如果访问对象的某个属性时，需要表现出特殊的行为，那就用 @property 来定义这种行为
# @property 方法应该遵循最小惊讶原则，而不应产生奇怪的副作用
# @property 需要执行得迅速一些，缓慢或复杂得工作，应该放在普通得方法里面


class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


r0 = OldResistor(50e3)
print('Before: %5r' % r0.get_ohms())  # Before: 50000.0
r0.set_ohms(10e3)
print('After: %5r' % r0.get_ohms())  # After: 10000.0


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
print(r1.ohms)  # 50000.0
r1.ohms = 10e3
print(r1.ohms)  # 10000.0
r1.ohms += 5e3
print(r1.ohms)  # 15000.0


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print('Before: %5r amps' % r2.current)  # Before:     0 amps
r2.voltage = 10
print('After: %5r amps' % r2.current)  # After:  0.01 amps


class BoundeResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


# r3 = BoundeResistance(1e3)
# r3.ohms = 0  # ValueError

# BoundeResistance(-5)  # ValueError


class FixedResistance(Resistor):
    # ...
    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


# r4 = FixedResistance(1e3)
# r4.ohms = 2e3  # AttributeError: Can't set attribute


class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms


# r7 = MysteriousResistor(10)
# r7.current = 0.01
# print('Before: %5r' % r7.voltage)
# r7.ohms
# print('After: %5r' % r7.voltage)































