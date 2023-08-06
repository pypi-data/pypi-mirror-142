from dataclasses import dataclass

@dataclass(frozen=True)
class Interval:
    start:int
    end:int
    
    def __post_init__(self):
        """Assures correct ordering of start and end"""
        a,b = self.start,self.end
        object.__setattr__(self,"start",min(a,b))
        object.__setattr__(self,"end",max(a,b))

    def clone(self) -> "Interval":
        return Interval(self.start,self.end)

    def get_length(self) -> int:
        """
        [DEPRECATED]
        Length of the interval, ends included
        """
        return len(self)

    def __len__(self) -> int:
        return self.end - self.start + 1
    
    def __lt__(self,other:"Interval") -> bool:
        """
        Is this interval completely contained within other? (no ovelapping border)
        """
        if not isinstance(other,Interval): return False
        a,b,c,d = self.tup() + other.tup()
        return a>c and b<d

    def __le__(self,other:"Interval") -> bool:
        """
        Is this interval completely contained within other? (allows ovelapping border)
        """
        if not isinstance(other,Interval): return False
        a,b,c,d = self.tup() + other.tup()
        return a>=c and b<=d

    def tup(self) -> tuple[int,int]:
        """Get tuple of extremes"""
        return (self.start,self.end)

    def __and__(self,other:"Interval") -> "Interval":
        """
        Get the intersection of the two intervals, as an Interval
        Returns None if the two intervals don't intersect
        """
        if not isinstance(other,Interval): return None
        a,b,c,d = self.tup() + other.tup()
        if b<c or d<a: return None
        new_min, new_max = max(a,c),min(b,d)
        return Interval(new_min,new_max)

    def __sub__(self,other:"Interval") -> list["Interval"]:
        """
        List of 0-2 intervals that belong to this Interval, but not to the other
        """
        if not isinstance(other,Interval): return [] # Exclude non-intervals
        if self <= other: return [] # Exclude cases when self is completely in other
        a,b,c,d = self.tup() + other.tup() # Get quick refs for interval limits
        if b<c or d<a: return [self.clone()] # Cover cases where intvs don't overlap
        if other < self: # Cover cases where there's exactly two sub-intervals
            return [Interval(a,c-1),Interval(d+1,b)]
        else:
            if d < b: return [Interval(d+1,b)]
            else: return [Interval(a,c-1)]

    def segment(self,other:"Interval") -> tuple["Interval","Interval","Interval"]:
        """
        Get 3-tuple of (Interval|None) representing (leftmost,a&b,rightmost)
        """
        if not isinstance(other,Interval): return (None, self.clone(), None)
        a,b,c,d = self.tup() + other.tup()
        # TODO

    def __str__(self) -> str:
        """Common interval representation (e.g. '1..5')"""
        return f"{self.start}..{self.end}"

def str_to_iv(s:str) -> Interval:
    """Turn strings of the type "1..5" into an interval"""
    _s = s.strip()
    a,b,*l = _s.split("..")
    a,b = map(int,[a,b])
    return Interval(a,b)
