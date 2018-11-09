from Rational_Number import RationalNumber
from Polynomial import Polynomial


# Elliptic Curve
class EC(Polynomial):
    def __init__(self, a, b=0, c=0):
        if 'internal_access' in dir(EC):
            if EC.internal_access:
                EC.internal_access = False
            else:
                raise TypeError('you are wrong')
        else:
            raise TypeError('you are wrong')

        super().__init__(
            {
                'y^2': -1, 'x^3': 1, 'x^2': RationalNumber(a),
                'x^1': RationalNumber(b), '1': RationalNumber(c)
             }
        )

    # we can check whether this function includes point(x, y).
    def includes(self, x, y):
        if isinstance(x, (RationalNumber, int)) and isinstance(y, (RationalNumber, int)):
            return (super().input(x, 'x')).input(y, 'y')['1'] == 0
        else:
            return False

    # method about check multiple root of x.
    def has_multiple_root_of_x(self):
        return 0 == self.get_discriminant_value_of_x()

    # We can get Discriminant of self equation.(f(x)=0,y=0)
    def get_discriminant_value_of_x(self):
        a = self[2]
        b = self[1]
        c = self[0]

        return -4*(a**3)*(c**3) + (a**2)*(b**2)\
            + 18*a*b*c - 4*(b**3) - 27*(c**2)

    # The following functions are special methods.
    def __add__(self, other):
        if isinstance(other, EC):
            return EC(
                (self[2]+other[2])/2, (self[1]+other[1])/2, (self[0]+other[0])/2
            )
        else:
            return NotImplemented

    # We can get a coefficient of x, which has key index.
    def __getitem__(self, item):
        if isinstance(item, int):
            if 0 == item:
                item = '1'
            elif 0 < item < 4:
                item = 'x^' + str(item)

        if isinstance(item, str):
            try:
                return super().__getitem__(item)
            except AttributeError:
                return 0
        else:
            return super().__getitem__(item)

    # The following functions are singleton methods.
    # We can get instance.
    # We cannot use default constructor.
    @staticmethod
    def get_instance(a=0, b=0, c=0):
        if EC.has_instance():
            return EC.instance
        else:
            EC.internal_access = True
            EC.instance = EC(a, b, c)
            return EC.instance

    # Whether Ec is created.
    @staticmethod
    def has_instance():
        return 'instance' in dir(EC)

    # We can remove EC.
    @staticmethod
    def remove_instance():
        if EC.has_instance():
            del EC.instance
