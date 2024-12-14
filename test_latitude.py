from latitude import Latitude
import logging

# https://www.fcc.gov/media/radio/dms-decimal

my_logger = logging.getLogger('test_latitude')
my_logger.setLevel(logging.DEBUG)


def test_from_dms():
    # dms to dms
    dms = Latitude.from_dms(49, 30, 45, 'N').to_dms()
    assert dms == '49° 30\' 45"'
    dms = Latitude.from_dms(49, 30, 45, 'S').to_dms()
    assert dms == '-49° 30\' 45"'
    # dms to dm
    ddm = Latitude.from_dms(49, 30, 56, 'N').to_ddm()
    assert ddm == '49° 30.93\''
    ddm = Latitude.from_dms(49, 30, 56, 'S').to_ddm()
    assert ddm == '-49° 30.93\''
    ddm = Latitude.from_dms(49, 30, 45, 'N').to_ddm()
    assert ddm == '49° 30.75\''
    #dms to dd
    dd = Latitude.from_dms(49, 30, 56, 'N').to_dd() 
    assert dd == '49.515556°'
    dd = Latitude.from_dms(49, 30, 45, 'S').to_dd() 
    assert dd == '-49.512500°'

def test_from_dms_as_str():
    # dms to dms
    dms = Latitude.from_str('49°30\'45"', 'N').to_dms()
    assert dms == '49° 30\' 45"'
    dms = Latitude.from_str('49° 30\' 45\"', 'S').to_dms()
    assert dms == '-49° 30\' 45"'
    # dms to dm
    ddm = Latitude.from_str('49°30\'56\"', 'N').to_ddm()
    assert ddm == '49° 30.93\''
    ddm = Latitude.from_str('49° 30\' 45\"', 'S').to_ddm()
    assert ddm == '-49° 30.75\''
    #dms to dd
    dd = Latitude.from_str('49°30\'56\"', 'N').to_dd() 
    assert dd == '49.515556°'
    dd = Latitude.from_str('49° 30\' 45\"', 'S').to_dd() 
    assert dd == '-49.512500°'

def test_from_ddm():
    #ddm to ddm
    ddm = Latitude.from_ddm(49, 30.75, 'N').to_ddm()
    assert ddm == "49° 30.75'"
    ddm = Latitude.from_ddm(49, 30.20, 'S').to_ddm()
    assert ddm == "-49° 30.20'"
    #dm to dms
    dms = Latitude.from_ddm(49, 30.75, 'N').to_dms()
    assert dms == '49° 30\' 45"'
    dms = Latitude.from_ddm(49, 30.75, 'S').to_dms()
    assert dms == '-49° 30\' 45"'
    #dm to dd
    dd = Latitude.from_ddm(49, 30.75, 'N').to_dd()
    assert dd == '49.512500°'
    dd = Latitude.from_ddm(49, 30.75, 'S').to_dd()
    assert dd == '-49.512500°'

def test_from_ddm_as_str():
    #ddm to ddm
    ddm = Latitude.from_str("49°30,75'", 'N').to_ddm()
    assert ddm == "49° 30.75'"
    ddm = Latitude.from_str("49° 30,20'", 'S').to_ddm()
    assert ddm == "-49° 30.20'"
    #dm to dms
    dms = Latitude.from_str("49°30,75'", 'N').to_dms()
    assert dms == '49° 30\' 45"'
    dms = Latitude.from_str("49° 30,75'", 'S').to_dms()
    assert dms == '-49° 30\' 45"'
    #dm to dd
    dd = Latitude.from_str("49°30,75'", 'N').to_dd()
    assert dd == '49.512500°'
    dd = Latitude.from_str("49° 30,75'", 'S').to_dd()
    assert dd == '-49.512500°'

def test_from_dd_as_str():
    #dd to dd
    dd = Latitude.from_dd(49.174167, 'N').to_dd()
    assert dd == "49.174167°"
    #dd to dms
    dms = Latitude.from_dd(49.936700, 'S').to_dms()
    assert dms == "-49° 56' 12\""
    dms = Latitude.from_dd(49.000698, 'N').to_dms()
    assert dms == "49° 0' 03\""
    dms = Latitude.from_dd(49.000691, 'S').to_dms()
    assert dms == "-49° 0' 02\""
    #dd to dm
    ddm = Latitude.from_dd(49.0008123, 'N').to_ddm()
    assert ddm == "49° 0.05'"

def test_from_str_as_str():
    #dd to dd
    dd = Latitude.from_str("49,1743°", 'S').to_dd()
    assert dd == "-49.174167°"
    #dd to dms
    dms = Latitude.from_str("49,9367°", 'N').to_dms()
    assert dms == "49° 56' 12\""
    dms = Latitude.from_str("49,0008°", 'S').to_dms()
    assert dms == "-49° 0' 03\""
    dms = Latitude.from_str("49,0008°", 'N').to_dms()
    assert dms == "49° 0' 03\""
    #dd to dm
    ddm = Latitude.from_str("49,0008°", 'S').to_ddm()
    assert ddm == "-49° 0.05'"
    