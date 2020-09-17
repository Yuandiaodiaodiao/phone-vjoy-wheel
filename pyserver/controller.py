from getDevice import device
import time
import pyvjoy
keyMap={
    "X":pyvjoy.HID_USAGE_X,
    "Y":pyvjoy.HID_USAGE_Y,
    "RX":pyvjoy.HID_USAGE_RX,
    "RY":pyvjoy.HID_USAGE_RY,
    "LT":pyvjoy.HID_USAGE_Z,
    "RT":pyvjoy.HID_USAGE_RZ,
    "Submit":1,
    "Cancel":2,
    "FireLeft":3,
    "Jump":4,
    "Spring":5,
    "Fire1":6,
    "Fire2":7,
    "Fire5":8,
}
device.reset()
def pressButton(id,t=1):
    device.set_button(id,1)
    time.sleep(t)
    device.set_button(id,0)

def changeAxisPercentage(side,per):
    side=keyMap[side]
    device.set_axis(side,int(0x8000*(per/100)))
def changeAxis(side,pos):
    side=keyMap[side]
    device.set_axis(
        side, 0x4000+pos*(0x4000))
def moveAroundAxis(side,t=1):
    side=keyMap[side]
    changeAxis(side,-1)
    time.sleep(t)
    changeAxis(side,1)
    time.sleep(t)


def moveAroundAndReset(side):
    moveAroundAxis(side)
    device.set_axis(
        side, 0x4000)
# time.sleep(1)
# print("start")
# pressButton(4)
# for i in range(1,20):
#     time.sleep(0.5)
#     pressButton(i)
# pressButton(i)
# moveAroundAndReset(keyMap["Y"])
# while True:
#     time.sleep(1)
#     moveAroundAxis(keyMap["X"])

# print("end")
