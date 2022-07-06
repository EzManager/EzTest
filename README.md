# EzTest
<p align="center">
  <img src="https://github.com/EzManager/EzTest/blob/main/Document/EzTest.png?raw=true" height="200px" /> <br/>
  <img src="https://img.shields.io/badge/Python-1.0.0rc1-brightgreen?style=flat-square&logo=python" /></a>
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
You should install integrated `Ez` package by pip.
```
pip install ezmanager
```
Now you can import `Eztest`
```python
from ez.eztest import EzTest
```


## Basic useage

### Dataset
Simple example
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
- `# i type` and `# o type` command fix the type of input/output value to that type, cast values to that type.\
When EzTest cannot cast the value, it prints the error message and passes that test line.\
You can use `int`, `float`, `double (except some languages)`, `str`, `bool`, and finally `auto` (Auto mode)\
In auto mode, `Struct` file will analyze the string and make it to real variable(s).

- When you use `# i str` or `# o str`, you don't have to write quotations for string value.\
**But you cannot convert over two strings at once.** See the example below.
```
// not allowed
# i str
str1, str2 >>> (output)

// use like this
# i auto
"str1", "str2" >>> (output)
```

- Output does not support comma separating.\
Instead, write it as an array, list, etc.\
(In case of Python, it returns multiple values in list.)

- `# tag msg` command add a tag into the log like this:
```
<<<<<<<<<<<<<<< msg >>>>>>>>>>>>>>>
```
Of course, you can use whitespace in the tag message.

- `// msg` is just a comment, but **you must write `//` in front of the line**
Comments in the middle are not available.

- When you handle string values, you can use escape characters such as `\n` and `\t`.\
Also, if you want to write >, you should write it like `\>`

### Python
``` python
ezt = EzTest('testset.txt', add).start().print_log().clear_log()
ezt.change_method(sub).start().save_log()
```

## Methods

### Python
| Method                | Description                                                            |
|-----------------------|------------------------------------------------------------------------|
| change_method(method) | Change target method                                                   |
| start()               | Start testing                                                          |
| add_tag(msg)          | Add tag line (in testset, use "# tag" command)                         |
| clear_log()           | Clear saved log                                                        |
| save_log(path)        | Save log as .txt in path                                               |
| print_log(colored)    | Print saved log<br/>If colored=True, some keywords will be highlighted |



## Version
| Version    | Changes                                                                                                                                          |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0.0rc1   | - Most of builtin types(int, float, str, list, tuple, dict) are supported<br/>(set, complex are not supported)<br/>- Auto type structing support |