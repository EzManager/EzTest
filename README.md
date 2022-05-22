# EzTest
<p align="center">
  <img src="https://github.com/EzManager/EzTest/blob/main/Document/EzTest.png?raw=true" height="200px" /> <br/>
  <img src="https://img.shields.io/badge/Python-1.0.0alpha-brightgreen?style=flat-square&logo=python" /></a>
  <img src="https://img.shields.io/badge/Java-unsupported-red?style=flat-square&logo=java" /></a>
  <img src="https://img.shields.io/badge/C++-unsupported-red?style=flat-square&logo=cplusplus" /></a>
  <img src="https://img.shields.io/badge/JavaScript-unsupported-red?style=flat-square&logo=javascript" /></a>
<p/>


## Introduction
EzTest is just a unit tester.\
There is no awesome, complex functions.\
But "Ez" to use.

## Import
This library is the part of EzManager package.\
EzManager repository will be created ASAP.

### Python
```python
from EzManager.EzTest import EzTest
from EzTest import EzTest
```
Will be integrated into the EzManager package.


## Basic useage

### Dataset Syntax
``` bash
// Comment line (A line should starts with "//")

// You can fix I/O types
# i int
# o int
1, 2 >>> 3
// '1', '2' will cast to integer
'1', '2', >>> 12
100, 10, 1 >>> '111'

// This will cause error
'A', '1' >>> 1

# tag You can add some tag lines in your log
// Fix input type as string
# i str
'1', '2' >>> 12
1, 2 >>> 12
// error
'A', 'B', 'C' >>> 'ABC'
```

### Python
``` python
ezt = EzTest('testset.txt', add).start().print_log().clear_log()
ezt.change_method(sub).start().save_log()
```
