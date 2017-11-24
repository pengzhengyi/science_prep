###################################BACKGROUND###################################

#  Salmon Run:

# From wikipedia: https://en.wikipedia.org/wiki/Salmon_run
# The salmon run is the time when salmon, which have migrated from the ocean, swim to the upper reaches of rivers where they spawn on gravel beds. After spawning, all Pacific salmon and most Atlantic salmon die, and the salmon life cycle starts over again. The annual run can be a major event for grizzly bears, bald eagles and sport fishermen. Most salmon species migrate during the fall (September through November).[1]

# Salmon spend their early life in rivers, and then swim out to sea where they live their adult lives and gain most of their body mass. When they have matured, they return to the rivers to spawn. Usually they return with uncanny precision to the natal river where they were born, and even to the very spawning ground of their birth. It is thought that, when they are in the ocean, they use magnetoception to locate the general position of their natal river, and once close to the river, that they use their sense of smell to home in on the river entrance and even their natal spawning ground.

# In northwest America, salmon is a keystone species, which means the impact they have on other life is greater than would be expected in relation to their biomass. The death of the salmon has important consequences, since it means significant nutrients in their carcasses, rich in nitrogen, sulfur, carbon and phosphorus, are transferred from the ocean to terrestrial wildlife such as bears and riparian woodlands adjacent to the rivers. This has knock-on effects not only for the next generation of salmon, but to every species living in the riparian zones the salmon reach.[2] The nutrients can also be washed downstream into estuaries where they accumulate and provide much support for estuarine breeding birds.


###################################CODE###################################
# Let's simulate this marvelous and dangerous migration.

from math import sqrt
from random import random
from random import randint
import random

###################################PLOTTING###################################
###################################DO NOT EDIT###################################
import webbrowser
from numbers import Number

import tempfile
import os
import atexit

_browser = None

def plot(L, scale=4, dot_size = 3, browser=None):
    """ plot takes a list of points, optionally a scale (relative to a 200x200 frame),
        optionally a dot size (diameter) in pixels, and optionally a browser name.
        It produces an html file with SVG representing the given plot,
        and opens the file in a web browser. It returns nothing.
        """
    scalar = 200./scale
    origin = (0, 210)
    hpath = create_temp('.html')
    with open(hpath, 'w') as h:
        h.writelines(
            ['<!DOCTYPE html>\n'
            ,'<head>\n'
            ,'<title>plot</title>\n'
            ,'</head>\n'
            ,'<body>\n'
            ,'<svg height="420" width=420 xmlns="http://www.w3.org/2000/svg">\n'
            ,'<line x1="0" y1="210" x2="420" y2="210"'
            ,'style="stroke:rgb(0,0,0);stroke-width:2"/>\n'
            ,'<line x1="210" y1="0" x2="210" y2="420"'
            ,'style="stroke:rgb(0,0,0);stroke-width:2"/>\n'
            ,'<line x1="0" y1="0" x2="0" y2="420"'
            ,'style="stroke:rgb(0,0,0);stroke-width:2"/>\n'])
        for pt in L:
            if isinstance(pt, Number):
                x,y = pt.real, pt.imag
            else:
                if isinstance(pt, tuple) or isinstance(pt, list):
                    x,y = pt
                else:
                    raise ValueError
            h.writelines(['<circle cx="%d" cy="%d" r="%d" fill="salmon"/>\n'
                        % (origin[0]+scalar*x,origin[1]-scalar*y,dot_size)])
        h.writelines(['</svg>\n</body>\n</html>'])
    if browser is None:
        browser = _browser
    webbrowser.get(browser).open('file://%s' % hpath)

def setbrowser(browser=None):
    """ Registers the given browser and saves it as the module default.
        This is used to control which browser is used to display the plot.
        The argument should be a value that can be passed to webbrowser.get()
        to obtain a browser.  If no argument is given, the default is reset
        to the system default.
        
        webbrowser provides some predefined browser names, including:
        'firefox'
        'opera'
        
        If the browser string contains '%s', it is interpreted as a literal
        browser command line.  The URL will be substituted for '%s' in the command.
        For example:
        'google-chrome %s'
        'cmd "start iexplore.exe %s"'
        
        See the webbrowser documentation for more detailed information.
        
        Note: Safari does not reliably work with the webbrowser module,
        so we recommend using a different browser.
        """
    global _browser
    if browser is None:
        _browser = None  # Use system default
    else:
        webbrowser.register(browser, None, webbrowser.get(browser))
        _browser = browser

def getbrowser():
    """ Returns the module's default browser """
    return _browser

# Create a temporary file that will be removed at exit
# Returns a path to the file
def create_temp(suffix='', prefix='tmp', dir=None):
    _f, path = tempfile.mkstemp(suffix, prefix, dir)
    os.close(_f)
    remove_at_exit(path)
    return path

# Register a file to be removed at exit
def remove_at_exit(path):
    atexit.register(os.remove, path)

###################################DO NOT EDIT###################################
###################################PLOTTING###################################


###################################Salmon Class###################################
class Salmon:
    """
        A salmon has these attributes(fields):
        pos - a two elements list, [H, V] representing the current location of this salmon
        speed - a int around 10, representing the units a salmon travels during an interval
        direction - a two elements list, [H, V] representing the direction that salmon swims
        (the direction vector has norm 1: H^2+V^2 == 1^2)
        sex - a string indicating this salmon is "Male" or "Female"
        """
    def __init__(self, pos, speed, direction, sex):
        "Constructor - Usage Salmon(pos, speed, direction, sex)"
        assert isinstance(pos, list)
        assert len(pos) == 2
        assert speed >= 0
        assert isinstance(direction, list)
        assert len(direction) == 2
        assert isinstance(sex, str)
        assert sex == "Male" or sex == "Female"
        self.pos = pos
        self.speed = speed
        self.direction = direction
        self.sex = sex
    
    def is_male(self):
        return self.sex == "Male"
    
    ### Task one: Try write a is_female method
    ### replace the pass with a return statement
    def is_female(self):
        pass
    
    def move(self):
        """
        move the salmon by some unit distance, calculated from the following formula:
        current_position = current_position + speed * direction
        """
        self.pos = [self.pos[i] + self.speed*self.direction[i]  for i in range(2)]
    
    def migrate(self, n):
        """
        migrate the salmon, calling salmon.migrate(n) is equivalent to calling salmon.move() n times
        """
        self.pos = [self.pos[i] + n*self.speed*self.direction[i]  for i in range(2)]
    
    def __str__(self):
        "print the speicific statistics of a salmon"
        s = "Sex: " + self.sex + "\t pos: " + str(self.pos) + "\t speed: " + str(self.speed)
        s += "\t direction: " + str(self.direction) + "\n"
        return s
    
    def report_pos(self):
        "returns the current location of this salmon, represented as a string"
        return str(self.pos) + "\n"

###################################Salmon Class###################################


## Tests for the is_female() method you just written
    """
    >>> male_salmon = Salmon([0, 0], 0, [1, 0], "Male")
    >>> male_salmon.is_female()
    False
    >>> female_salmon = Salmon([0, 0], 0, [1, 0], "Female")
    >>> female_salmon.is_female()
    True
    """




###################################Generate Salmon Group###################################

def rand_sex():
    """
    randomly generates a string represents the sex of a salmon
    >>> s = rand_sex()
    >>> s == "Male" or s == "Female"
    True
    >>> s_ls = [rand_sex() for i in range(10)]
    >>> False not in [s == "Male" or s == "Female" for s in s_ls]
    True
    """
    sex = randint(0, 1)
    return "Male" if sex else "Female"


def rand_dir():
    """
    randomly generates a two elements list representing a direction
    V is a float point number between -1 and 1
        
    >>> dir = rand_dir()
    >>> len(dir) == 2
    True
    >>> 1- (dir[0]**2 + dir[1]**2) < 1e-10
    True
    >>> dirs = [rand_dir() for i in range(10)]
    >>> False not in [1- (dir[0]**2 + dir[1]**2) < 1e-10 for dir in dirs]
    True
    """
    V = random.uniform(-1, 1)
    return [sqrt(1 - V**2), V]


def create_adgos(groupsize=1000, LOWER_SPEED=0, UPPER_SPEED=20):
    """
    create a group of salmon of default size, this group has, by default, 1000
    salmons. Each salmon will be generated in the following way:
    pos: set to be the origin [0, 0]
    speed:speed is a random number chosen from LOWER_SPEED - UPPER_SPEED, inclusive
    direction: generated by rand_dir()
    sex: generated by rand_sex()
    
    >>> agos = create_adgos()
    >>> len(agos) == 1000
    True
    >>> len(create_adgos(500)) == 500
    True
    """
    return [Salmon([0, 0], random.uniform(LOWER_SPEED, UPPER_SPEED), rand_dir() , rand_sex()) for i in range(groupsize)]

###################################Generate Salmon Group###################################




###################################Reproduction###################################

def offspring_speed(f_speed, m_speed, LOWER_SPEED=0, UPPER_SPEED=20,
                    MUTATION_FACTOR=0.6, FINHERITANCE_FACTOR=0.2, MINHERITANCE_FACTOR=0.2):
    """
        generates the direction for the child salmon based on the directions of its father and mother
        formula:
        offspring_speed = mutation_factor*(randint(LOWER_SPEED, UPPER_SPEED)
        + father_inheritance_factor*father_speed
        + mother_inheritance_factor*mother_speed
        
        >>> os = offspring_speed(10, 10, 5, 15)
        >>> MIN = 5*0.6 + 10*0.2 + 10*0.2
        >>> MAX = 15*0.6 + 10*0.2 + 10*0.2
        >>> MIN <= os and os <= MAX
        True
        >>> f_sps = [randint(5, 15) for i in range(10)]
        >>> m_sps = [randint(5, 15) for i in range(10)]
        >>> oss = [offspring_speed(f_sps[i], m_sps[i], 5, 15) for i in range(10)]
        >>> False not in [(5*0.6+f_sps[i]*0.2+m_sps[i]*0.2)<=oss[i] and oss[i]<=(15*0.6+f_sps[i]*0.2+m_sps[i]*0.2)  for i in range(10)]
        True
        """
    return MUTATION_FACTOR*random.uniform(LOWER_SPEED, UPPER_SPEED) + FINHERITANCE_FACTOR*f_speed + MINHERITANCE_FACTOR*m_speed


def offspring_dir(f_dir, m_dir, MUTATION_FACTOR=0.6, FINHERITANCE_FACTOR=0.2, MINHERITANCE_FACTOR=0.2):
    """
    generates the direction for the child salmon based on the directions of its father and mother
    formula: 
    V = mutation_factor*random.uniform(-1, 1)
        + father_inheritance_factor*father_salmon.direction[1]
        + mother_inheritance_factor*mother_salmon.direction[1]
    H = sqrt(1 - V**2)
    
    >>> f_dir = rand_dir()
    >>> m_dir = rand_dir()
    >>> c_dir = offspring_dir(f_dir, m_dir)
    >>> len(c_dir) == 2
    True
    >>> 1- (c_dir[0]**2 + c_dir[1]**2) < 1e-10
    True
    >>> f_dirs = [rand_dir() for i in range(10)]
    >>> m_dirs = [rand_dir() for i in range(10)]
    >>> False not in [1- (dir[0]**2 + dir[1]**2) < 1e-10 for dir in [offspring_dir(f_dirs[i], m_dirs[i]) for i in range(10)]]
    True
    """
    V = MUTATION_FACTOR*(random.uniform(-1, 1))+FINHERITANCE_FACTOR*f_dir[1]+MINHERITANCE_FACTOR*m_dir[1]
    return [sqrt(1 - V**2), V]

NORM_DEFAULT_SQUARE_LIMIT = 625

def in_spawn_area(salmon_pos, center_H=100, center_V=0):
    """
    check whether a salmon has reached the optimal spawn area, returns a boolean
    by default, the center of optimal spawn location is set to [100, 0]
    any location whose distance from the center is within NORM_SQUARE_LIMIT is considered in the spawn area
    (a circle at [100, 0])
    
    >>> in_spawn_area([100, 0])
    True
    >>> in_spawn_area([0, 0])
    False
    >>> in_spawn_area([100, 25])
    True
    >>> in_spawn_area([75, -25])
    False
    """
    Hstar = center_H - salmon_pos[0]
    Vstar = center_V - salmon_pos[1]
    return Hstar**2 + Vstar**2 <= NORM_DEFAULT_SQUARE_LIMIT


def reached_salmons(alos):
    """
    Given a list of salmons, return salmons who reached the optimal spawn area
    as a tuple (male_salmons, female_salmons)
    male_salmons and female_salmons are lists representing the group of (fe)male salmons
    reached the optimal spawn area
    """
    male_salmons = []
    female_salmons = []
    num_salmons = len(alos)
    for s in alos:
        if (in_spawn_area(s.pos)):
            if (s.is_male()):
                male_salmons.append(s)
            else: female_salmons.append(s)
    return (male_salmons, female_salmons)


def group_paring(agos):
    """
    Given a group of salmons, return a list of parings (tuples) 
    (father, mother)
    The number of pairing is decided by the minimum number between the number
    of male salmons and female salmons
    """
    male_salmons, female_salmons = reached_salmons(agos)
    num_of_pairing = min(len(male_salmons), len(female_salmons))
    return [(male_salmons[i], female_salmons[i]) for i in range(num_of_pairing)]



def reproduce(father_salmon, mother_salmon, MIN_NUM_OFFSPRINGS=10, MAX_NUM_OFFSPRINGS=35):
    """
        spawn a bunch of salmon babies
        
        >>> f_salmon = Salmon([0, 0], 10, [1, 0], "Male")
        >>> m_salmon = Salmon([0, 0], 10, [1, 0], "Female")
        >>> offsprings = reproduce(f_salmon, m_salmon, 10, 35)
        >>> len(offsprings) >= 10 and len(offsprings) <= 35
        True
        
        """
    assert isinstance(father_salmon, Salmon)
    assert isinstance(mother_salmon, Salmon)
    num_of_offsprings = randint(MIN_NUM_OFFSPRINGS, MAX_NUM_OFFSPRINGS)
    return [Salmon([0, 0],
                   offspring_speed(father_salmon.speed, mother_salmon.speed),
                   offspring_dir(father_salmon.direction, mother_salmon.direction),
                   rand_sex())
            for i in range(num_of_offsprings)]



def next_generation(agos):
    """
    produce the next generation of salmons from the given group of salmons
    It first determines the salmons which reached the optimal spawn position, then
    pair between male salmon and mother salmons to let them reproduce.
    """
    return sum([reproduce(father_salmon, mother_salmon) for father_salmon, mother_salmon in group_paring(agos)], [])

###################################Reproduction###################################


###################################SIMULATION###################################

def cycle(agos, NUM_OF_MOVES=10):
    """
    perform one cycle (produce the next generation of salmons)
    """
    for s in agos: s.migrate(NUM_OF_MOVES)
    plot([s.pos for s in agos], 150, 1)
    return next_generation(agos)



def demo_migrations_cycles(CYCLES=7):
    """
    simulate CYCLES number of cycles, printing the number of salmons of each generation
    """
    adgos = create_adgos()
    for i in range(CYCLES):
        print("Current Group Size: " + str(len(adgos)))
        adgos = cycle(adgos)


## Resources limited
def demo_migrations_cycles_LR(CYCLES=15):
    """
    The area suitable for spawn will decreases when there are t0o many salmons (> 1500)
    and will restore if the number of salmons are below 1000
    """
    global NORM_DEFAULT_SQUARE_LIMIT
    adgos = create_adgos()
    for i in range(CYCLES):
        cur_group_size = len(adgos)
        print("Current Group Size: " + str(cur_group_size))
        print("Current Area: " + str(NORM_DEFAULT_SQUARE_LIMIT))
        adgos = cycle(adgos)
        if cur_group_size < 1000: NORM_DEFAULT_SQUARE_LIMIT = 625
        elif cur_group_size > 1700:
            NORM_DEFAULT_SQUARE_LIMIT = max(200, (NORM_DEFAULT_SQUARE_LIMIT-cur_group_size//10))
    NORM_DEFAULT_SQUARE_LIMIT = 625


###################################SIMULATION###################################
