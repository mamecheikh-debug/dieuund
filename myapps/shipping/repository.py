from oscar.apps.shipping import repository
from . import methods

# class Repository(repository.Repository):
#     methods = (methods.FixedPrice(charge_excl_tax=None, charge_incl_tax=None))

class Repository(repository.Repository):
    methods = (methods.Standard(), methods.Express())