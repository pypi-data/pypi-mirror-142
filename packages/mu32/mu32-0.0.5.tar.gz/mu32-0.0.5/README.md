# Mu32

Python MegaMicro Mu32 driver.

*Megamicro 32 (Mu32)* is an antenna with 8 to 32 microphones used to locate, characterize and classify sound sources. For more information, visit the website [DistalSense.com](https://distalsense.com).

This repository gathers the drivers allowing to use the *Mu32* system, an API to write your application programs as well as many illustrative examples.

Consult the documentation on the site [DistalSense.io](https://DistalSense.io).

## Changelog

### 0.0.5 (2022-03-15)

* Fix some bugs due to logging update done in previous release
* Add mu32doa realtime example 
* Update documentation

### 0.0.4 (2022-03-13)

* Add beamformer and synthesis modules
* Add jupyter examples files for beamforming
* Remove Mu32Exception and Logging tools from core: create new corresponding separate files

### 0.0.3 (2022-03-06)

* Add examples/mu32save.py example program for saving data in HDF5 format

### 0.0.2 (2022-02-20)

* Fixes the data unflushing warning (adds a function to empty Mu32 internal buffers)

### 0.0.1 (2022-02-18)

* Initial release
