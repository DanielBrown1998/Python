from platform import platform, machine, processor, python_implementation, python_version_tuple
import numpy as np

print(platform(True, True),
      machine(),
      processor(),
      python_implementation(),
      python_version_tuple(), sep='\n')


vet = np.arange(10, dtype=np.uint8)
