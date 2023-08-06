from pydaisi import Daisi
from pprint import pprint

p = Daisi("simple-pair")
pprint(p.hello('you'))
pprint(p.goodbye('them'))