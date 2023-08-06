from .interval import Interval, str_to_iv
from dataclasses import dataclass
from itertools import product
from math import prod

@dataclass(frozen=True)
class Cuboid:
    points: list[Interval]
    value: any = None

    def volume(self) -> int:
        return prod((x.get_length() for x in self.points))
    
    def dims(self) -> int:
        """Number of dimensions of the cuboid"""
        return len(self.points)

    def __eq__(self,other:"Cuboid") -> bool:
        if not isinstance(other,Cuboid): return False
        if other.dims() != self.dims(): return False
        return all(x==y for (x,y) in zip(self.points,other.points))

    def __and__(self,other:"Cuboid") -> "Cuboid":
        """Return intersection of two cuboids of the same dimensionality"""
        if not isinstance(other,Cuboid): return None
        if other.dims() != self.dims(): return None
        intersection = [a&b for (a,b) in zip(self.points,other.points)]
        if None in intersection: return None
        return Cuboid(intersection)

    def __sub__(self,other:"Cuboid") -> list["Cuboid"]:
        """Return list of cuboids that add together to (self-other)"""
        if not isinstance(other,Cuboid): return []
        if not self.dims() == other.dims(): return []
        intersection = self & other
        if not intersection: return []
        # List of list of segments of intervals in respective dimentions
        sections = [[x&y] + (x-y)  for x,y in zip(self.points,other.points)]
        result = [Cuboid(p,self.value) for p in product(*sections) if Cuboid(p)!=intersection]
        return result

def str_to_cb(s:str, val:any=None) -> Cuboid:
    """Converts a string of the type a..b c..e [...] into a Cuboid"""
    _s = s.strip()
    l = [str_to_iv(x) for x in _s.split()]
    return Cuboid(l,val)
