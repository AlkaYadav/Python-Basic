'''
abstract.py
Demonstrating abstract base classes in python
'''
from abc import abstractmethod,ABCMeta
from collections import Sequence
class Capper:
    def capper(self):
        return [str((self.seq[index])).upper() for index in range(len(self.seq))]
    
class SkipSequence(object):
    __metaclass__=ABCMeta
    def __init__(self,seq):
        self.seq=seq
    @abstractmethod
    def __getitem__(self,index):
        return 0
    
    @abstractmethod
    def __len__():
        return 0
    
class SkipSequenceTwo(SkipSequence,Sequence,Capper):
    def __init__(self,seq):
        self.seq=seq
    def get_sequence_skiptwo(self):
        for c in self.seq:
            l=[]
            for index in range(len(self.seq)/2):
                l.append(self.seq[index*2])
        return l
    def __getitem__(self,index):
        try:
            return self.seq[index*2]
        except IndexError:
            pass
    def __len__():
        return len(self.seq)//2

class SkipSequenceThree(SkipSequence,Sequence,Capper):
    def __init__(self,seq):
        self.seq=seq
    def get_sequence_skipthree(self):
        for c in self.seq:
            l=[]
            for index in range(len(self.seq)/3):
                l.append(self.seq[index*3])
        return l
    def __getitem__(self,index):
        try:
            return self.seq[index*3]
        except IndexError:
            pass
    def __len__():
        return len(self.seq)//3    
