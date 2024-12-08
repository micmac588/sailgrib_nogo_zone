from angle import Angle
import logging

# https://www.fcc.gov/media/radio/dms-decimal

my_logger = logging.getLogger('test_degree_converter')
my_logger.setLevel(logging.DEBUG)


def test_from_dms():
    # dms to dms
    dms = Angle.from_dms(49, 30, 45).to_dms()
    assert dms == '49° 30\' 45"'
    dms = Angle.from_dms(49, 30, 45).to_dms()
    assert dms == '49° 30\' 45"'
    # dms to dm
    ddm = Angle.from_dms(49, 30, 56).to_ddm()
    assert ddm == '49° 30.93\''
    ddm = Angle.from_dms(49, 30, 45).to_ddm()
    assert ddm == '49° 30.75\''
    #dms to dd
    dd = Angle.from_dms(49, 30, 56).to_dd() 
    assert dd == '49.515556°'
    dd = Angle.from_dms(49, 30, 45).to_dd() 
    assert dd == '49.512500°'

def test_from_dms_as_str():
    # dms to dms
    dms = Angle.from_str('49°30\'45"').to_dms()
    assert dms == '49° 30\' 45"'
    dms = Angle.from_str('49° 30\' 45\"').to_dms()
    assert dms == '49° 30\' 45"'
    # dms to dm
    ddm = Angle.from_str('49°30\'56\"').to_ddm()
    assert ddm == '49° 30.93\''
    ddm = Angle.from_str('49° 30\' 45\"').to_ddm()
    assert ddm == '49° 30.75\''
    #dms to dd
    dd = Angle.from_str('49°30\'56\"').to_dd() 
    assert dd == '49.515556°'
    dd = Angle.from_str('49° 30\' 45\"').to_dd() 
    assert dd == '49.512500°'

def test_from_ddm():
    #ddm to ddm
    ddm = Angle.from_ddm(49, 30.75).to_ddm()
    assert ddm == "49° 30.75'"
    ddm = Angle.from_ddm(49, 30.20).to_ddm()
    assert ddm == "49° 30.20'"
    #dm to dms
    dms = Angle.from_ddm(49, 30.75).to_dms()
    assert dms == '49° 30\' 45"'
    dms = Angle.from_ddm(49, 30.75).to_dms()
    assert dms == '49° 30\' 45"'
    #dm to dd
    dd = Angle.from_ddm(49, 30.75).to_dd()
    assert dd == '49.512500°'
    dd = Angle.from_ddm(49, 30.75).to_dd()
    assert dd == '49.512500°'

def test_from_ddm_as_str():
    #ddm to ddm
    ddm = Angle.from_str("49°30,75'").to_ddm()
    assert ddm == "49° 30.75'"
    ddm = Angle.from_str("49° 30,20'").to_ddm()
    assert ddm == "49° 30.20'"
    #dm to dms
    dms = Angle.from_str("49°30,75'").to_dms()
    assert dms == '49° 30\' 45"'
    dms = Angle.from_str("49° 30,75'").to_dms()
    assert dms == '49° 30\' 45"'
    #dm to dd
    dd = Angle.from_str("49°30,75'").to_dd()
    assert dd == '49.512500°'
    dd = Angle.from_str("49° 30,75'").to_dd()
    assert dd == '49.512500°'

def test_from_dd_as_str():
    #dd to dd
    dd = Angle.from_dd(49.174167).to_dd()
    assert dd == "49.174167°"
    #dd to dms
    dms = Angle.from_dd(49.936700).to_dms()
    assert dms == "49° 56' 12\""
    dms = Angle.from_dd(49.000698).to_dms()
    assert dms == "49° 0' 03\""
    dms = Angle.from_dd(49.000691).to_dms()
    assert dms == "49° 0' 02\""
    #dd to dm
    ddm = Angle.from_dd(49.0008123).to_ddm()
    assert ddm == "49° 0.05'"

def test_from_str_as_str():
    #dd to dd
    dd = Angle.from_str("49,1743°").to_dd()
    assert dd == "49.174167°"
    #dd to dms
    dms = Angle.from_str("49,9367°").to_dms()
    assert dms == "49° 56' 12\""
    dms = Angle.from_str("49,0008°").to_dms()
    assert dms == "49° 0' 03\""
    dms = Angle.from_str("49,0008°").to_dms()
    assert dms == "49° 0' 03\""
    #dd to dm
    ddm = Angle.from_str("49,0008°").to_ddm()
    assert ddm == "49° 0.05'"
    