DSP utility packages  
===
Common utilities developed by DSP inc.

# packages  
1. log  
2. dbintf  

## log
A loggin decorator keeps logging functions' error messeages  

* features  
    1. Crete logger using different log file  
    2. Identical log file shared by multiple `log` instances (in same module scope) won't create multiple file handler for multiple write  
* import package
```python
from dsputility import log
instance = log()
```
```python
from dsputility.log import log
instance = log()
```
```python
import dsputility as du
instance = du.log()
```
* usseage  

```python
from dsputility import log

logName = os.path.basename(__file__)
myLog = log(logPath=logName) 
myLog2 = log(logPath=logName)

@myLog.errlog(logName)
def func1(x):
    return x/0

@myLog.errlog(logName)
async def afunc1():
    open('not exist', 'r')
		
@myLog2.errlog(logName)
def func2(x):
    "won't cause multiple handler problem"
    return x/0
```

## dbintf
A simple interface to setup user, password, host and establish an DB engine
* features
    1. Setup an attribute `engine` contain an DB engine established by `sqlalchemy`
* import package
```python
from dsputility import dbintf
instance = dbintf()
```
```python
from dsputility.dbintf import dbintf
instance = dbintf()
```
```python
import dsputility as du
instance = du.dbintf()
```
* usseage  

```python
from dsputility import dbintf
intf = dbintf(db_name='data', user='postgres', password='password', host='localhost', port='5432', vendor:str='postgresql')
# this will setup intf.engine as an instance of
# sqlalchemy.create_engine(f"postgresql://postgres:password@localhost:5432/data")

# after setup intf, you can do database operations through intf.engine, such as
intf.engine.connect()
```
