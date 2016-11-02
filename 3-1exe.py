# coding=utf-8
# 如何实现可迭代对象和迭代器对象
'''for x in l :中，in 后面l是可迭代对象，由内置函数iter得到迭代器对象 x
列表中调用__iter__获得迭代器对象，字符串调用__getitem__获得迭代器对象
迭代器对象调用next()获得下一项，最终抛出异常
'''
# 实现一个迭代器对象WeatherIterator,next方法每次返回一个城市气温
# 实现一个可迭代对象WeatherIterable，__iter__方法返回一个迭代器对象
import requests
from collections import Iterable, Iterator

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s ' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable([u'南京', u'连云港', u'北京', u'上海']):
    print x

