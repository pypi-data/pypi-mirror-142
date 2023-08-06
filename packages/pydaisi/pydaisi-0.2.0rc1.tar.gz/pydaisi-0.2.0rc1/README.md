# Simples Steps for PyDaisi SDK

## Preliminary Steps

### Install with PIP:

- `pip install pydaisi`

### (Optional) Set your personal access token:

Create your personal access token

- https://app.daisi.io/settings/personal-access-tokens

Set it in the environment or in a `.env` file:
```
DAISI_ACCESS_TOKEN=a1b2c3d4e5f67890abcdef124567890
```

## Using PyDaisi
=======
```
import time
from pydaisi import Daisi

###
### Titanic: Part One
###

# Connect to Titantic Statistics, a multi-endpoint Daisi service
d = Daisi("Titanic Statistics", base_url="https://dev3.daisi.io")

# Calling the functions of the Daisi
d.mean(field="Age")
d.percentile(field="Age", percentile=.1)
d.raw(rows=10)

# Getting the DaisiExecution object back and storing it
de = d.raw(rows=10)

# Error tracebacks are now MUCH more user friendly.
d.mean(field="Potato")
d.mean(fake_field="Age")


###
### Live Logging: Part Two
###

# Connect to the live logging Daisi and run a 30 second computation
d2 = Daisi("Live Logging", base_url="https://dev3.daisi.io")
d2e = d2.live_log_test(firstNumber=5, secondNumber=10, delay=30)

###
### Daisi Object Serialization: Part Three
###

# Connect to the Serialization Daisi
d3 = Daisi("Daisi Serialize", base_url="https://dev3.daisi.io")

# Import numpy and define the MapStack class that we will use as an example of custom serialization
import numpy as np

class MapStack:
    def __init__(self, nx, ny):
        self.nx = nx
        self.ny = ny
        self.nb_layers = None
        self.maps = []

    def add_layer(self, map):
        if len(map.shape) == 2 and map.shape[0] == self.ny and map.shape[1] == self.nx:
            self.maps.append(map)
            self.nb_layers = len(self.maps)
            return "Map sucessfully added."
        else:
            return "Could not add map. Incompatible dimensions."

# Initialize a new MapStack object with 10 layers
nx = 200
ny = 200
ms = MapStack(nx, ny)
for i in range(10):
    ms.add_layer(np.random.rand(nx, ny))

# Compute the daisi, adding a new layer
d3_execution = d3.compute(map_stack=ms, map=np.random.rand(nx, ny))

# The `result` attribute is the raw data, no unpickling / data loading performed
d3_execution.result

# When we GET the result, the data is downloaded and unpickled automatically
status, ms = d3_execution.get_result()

# Note we have added a new layer to it
print(status, ms.nb_layers)

# Now, we are going to pass our EXECUTION object as the input to a parameter
d3_execution2 = d3.compute(map_stack=d3_execution, map=np.random.rand(nx, ny))
status, ms = d3_execution2.get_result()

# You can see, the PyDaisi client automatically found the lookup id and added a 12th layer!
print(status, ms.nb_layers)

# One more update - we don't need to automatically fetch the result!
d3_execution3 = d3.compute(map_stack=d3_execution2, map=np.random.rand(nx, ny), defer_result=True)
d3_execution3.get_result(keep_pickle=True)

d3_execution4 = d3.compute(map_stack=d3_execution3, map=np.random.rand(nx, ny), defer_result=True)

time.sleep(2)

# Let's prove it still worked with no local data transfer
status, ms = d3_execution4.get_result()
print(status, ms.nb_layers)
```
