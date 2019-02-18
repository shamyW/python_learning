# -*- coding:utf-8 -*-

#import standard
#import standard
#import standard

#import others
#import others
#import others

#import myself
#import myself
#import myself


class Test(object):

    def __init__(self):
        pass

    def output(self):
        print('i am a tester')
        print('i am a tester')
        print('i am a tester')
        return 1


def function(num=1):
    '''
    this is a function for testing
    :return: num
    '''

    return num


def addxy(x=1, y=2):
    '''
    this function used for addxy
    :param x: the first input
    :param y: the second input
    :return: the result of addxying x and y
    '''

    return x + y

def gitaddtest():
    '''
    this is for git update test
    :return: 1
    '''

    print('this is for git update test')
    return 1

print(function(1))

print(function.__doc__)

dic = {'key': 'value'}

print(dic['key'])

print(addxy())

print(addxy.__doc__)


a = Test()
print(a.output())

print(gitaddtest())
