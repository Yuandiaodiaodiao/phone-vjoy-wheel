import pyvjoy

#Pythonic API, item-at-a-time
device=None
for i in range(10):
    try:
        device = pyvjoy.VJoyDevice(i)
        print(f"get vjoy device{i}")
        break
    except:
        pass
