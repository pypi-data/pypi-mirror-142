# PyOkofen

Python interface for Okofen (oekofen) JSON API

```python
import pyokofen

boiler = pyokofen.Okofen()
# Set here you ip:port/password/ - eg. 1.1.1.1:4321/XXXX/
boiler.credentials("1.1.1.1", "4321", "XXXX")
try boiler.update():
    print("It works!")
    print("Current temperature: " + boiler.get("hk0", "L_roomtemp_act"))
    print("Target temperature: " + boiler.get("hk0", "L_roomtemp_set"))
except:
    print('Oh no!')
```

**Notice! Beside the class init, every other function are async functions.**  
**Notice! Okofen have a soft limitation of 1 request per 10 seconds, regardless of the origin nor if it's to get or set something.**

## Todo

- Document actual okofen API
- Implement value modification (eg. GET /ww1.heat_once=1 to enable domestic hot water force heating)\ beware 1x request per 10 seconds regardless of the source. Maybe implement a queue?
- Missing Power, Stirling, Thirdparty, Pu (accu), Se (Solar), Circ (circulation pump), St5k (5kw stirling) datas, as I do not own them, I don't know their format. Lack of documentation on Okofen side.
