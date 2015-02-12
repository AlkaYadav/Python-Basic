"""
Circultous(tm)
Let's pretend we are building a company..

An advanced cicle analytics company.

We will use Lean Startup Method
Agile: waterfall:: Lean Startup:Business Plans

Just work a little and then evaluate what to do next.
"""
import math
from collections import namedtuple

Version=namedtuple('Version','major minor')
class Circle(object):
    """An advanced circle analytic toolkit"""
 #   version = '0.1.1'
    version = Version(0,5)
    def __init__(self,radius):
        """Not many ppl read docs"""
        self.radius = radius
        
    @classmethod
    def from_bbd(cls,diagonal):
        radius=diagonal/math.sqrt(2.0)/2.0
        return cls(radius)

    def get_radius(self):
        return self.diameter/2.0

    def set_radius(self,radius):
        self.diameter=radius*2.0
        
    radius=property(get_radius,set_radius)
    
    def perimeter(self):
        """Compute closed line integral for locus of points equidistant from a given point."""

        return math.pi*self.radius * 2
    __perimeter=perimeter
    def area(self):
        """Perform quadrature on a planar sahpe uniform revolution."""
        p=self.__perimeter()
        radius=p/2.0/math.pi
        return math.pi*radius ** 2
    
    
    def __repr__(self):
        return "%s(%r)"%(self.__class__.__name__,self.radius)

    @staticmethod
    def angle_to_grade(angle):
        """Returns a percent given an inclinometer reading in degrees"""
        return Percent(math.tan(math.radians(angle)))

class Percent(float):

    def __str__(self):
        return '%.2f%%'%(self*100)
        
