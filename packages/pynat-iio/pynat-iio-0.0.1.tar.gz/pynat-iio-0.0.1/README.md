<!-- PYADI-NAT README -->

### pynat-iio: N.A.T. GmbH python interfaces for SDR hardware

pynat-iio is a python abstraction module for N.A.T. hardware with IIO drivers to make them easier to use. The libIIO interface although extremely flexible can be cumbersome to use due to the amount of boilerplate code required for even simple examples, especially when interfacing with buffers. This module has custom interfaces classes for specific parts and development systems which can generally make them easier to understand and use. To get up and running with a device can be as simple as a few lines of code:
```python
import nat

# Create device from specific uri address
sdr = nat.nat_amc_zynqup_sdr8(uri="ip:192.168.1.160")
# Get data from transceiver
data = sdr.rx()
```

### Dependencies
- [pyadi-iio with optional dependency for JESD debugging](https://github.com/analogdevicesinc/pyadi-iio)

### Installing from source
```
~$ git clone https://github.com/NAT-GmbH/pynat-iio
~$ cd pynat-iio
~$ (sudo) python setup.py install
```
### Installing from pip
```
~$ (sudo) pip install pynat-iio
```
