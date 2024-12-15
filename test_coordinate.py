from coordinate import Coordinate
import logging

# https://www.fcc.gov/media/radio/dms-decimal

my_logger = logging.getLogger('test_Coordinate')
my_logger.setLevel(logging.DEBUG)


def test_from_dms():
    # dms to dms
    dms = Coordinate.from_dms(49, 30, 45, 'N').to_dms()
    assert dms == '''49° 30' 45"'''
    dms = Coordinate.from_dms(49, 30, 45, 'S').to_dms()
    assert dms == '''-49° 30' 45"'''
    # dms to dm
    ddm = Coordinate.from_dms(49, 30, 56, 'N').to_ddm()
    assert ddm == "49° 30.93'"
    ddm = Coordinate.from_dms(49, 30, 56, 'S').to_ddm()
    assert ddm == "-49° 30.93'"
    ddm = Coordinate.from_dms(49, 30, 45, 'N').to_ddm()
    assert ddm == "49° 30.75'"
    #dms to dd
    dd = Coordinate.from_dms(49, 30, 56, 'N').to_dd() 
    assert dd == '49.515556°'
    dd = Coordinate.from_dms(49, 30, 45, 'S').to_dd() 
    assert dd == '-49.5125°'

def test_from_dms_as_str():
    # dms to dms
    dms = Coordinate.from_str('49°30\'45" N').to_dms()
    assert dms == '49° 30\' 45"'
    dms = Coordinate.from_str('49° 30\' 45\" S').to_dms()
    assert dms == '-49° 30\' 45"'
    # dms to dm
    ddm = Coordinate.from_str('49°30\'56\" N').to_ddm()
    assert ddm == '49° 30.93\''
    ddm = Coordinate.from_str('49° 30\' 45\" S').to_ddm()
    assert ddm == '-49° 30.75\''
    #dms to dd
    dd = Coordinate.from_str('49°30\'56\" N').to_dd() 
    assert dd == '49.515556°'
    dd = Coordinate.from_str('49° 30\' 45\" S').to_dd() 
    assert dd == '-49.5125°'

def test_from_ddm():
    #ddm to ddm
    ddm = Coordinate.from_ddm(49, 30.75, 'N').to_ddm()
    assert ddm == "49° 30.75'"
    ddm = Coordinate.from_ddm(49, 30.20, 'S').to_ddm()
    assert ddm == "-49° 30.2'"
    #dm to dms
    dms = Coordinate.from_ddm(49, 30.75, 'N').to_dms()
    assert dms == '49° 30\' 45"'
    dms = Coordinate.from_ddm(49, 30.75, 'S').to_dms()
    assert dms == '-49° 30\' 45"'
    #dm to dd
    dd = Coordinate.from_ddm(49, 30.75, 'N').to_dd()
    assert dd == '49.5125°'
    dd = Coordinate.from_ddm(49, 30.75, 'S').to_dd()
    assert dd == '-49.5125°'

def test_from_ddm_as_str():
    #ddm to ddm
    ddm = Coordinate.from_str("49°30.75 ' N").to_ddm()
    assert ddm == "49° 30.75'"
    ddm = Coordinate.from_str("49° 30.20 ' S").to_ddm()
    assert ddm == "-49° 30.2'"
    #dm to dms
    dms = Coordinate.from_str("49°30.75 ' N").to_dms()
    assert dms == '49° 30\' 45"'
    dms = Coordinate.from_str("49° 30.75' S").to_dms()
    assert dms == '-49° 30\' 45"'
    #dm to dd
    dd = Coordinate.from_str("49°30.75' N").to_dd()
    assert dd == '49.5125°'
    dd = Coordinate.from_str("49° 30.75' S").to_dd()
    assert dd == '-49.5125°'

def test_from_dd_as_str():
    #dd to dd
    dd = Coordinate.from_dd(49.174167).to_dd()
    assert dd == "49.174167°"
    #dd to dms
    dms = Coordinate.from_dd(-49.936700).to_dms()
    assert dms == "-49° 56' 12\""
    dms = Coordinate.from_dd(49.000698).to_dms()
    assert dms == "49° 00' 03\""
    dms = Coordinate.from_dd(-49.000691).to_dms()
    assert dms == "-49° 00' 02\""
    #dd to dm
    ddm = Coordinate.from_dd(49.0008123).to_ddm()
    assert ddm == "49° 00.05'"

def test_from_str_as_str():
    #dd to dd
    dd = Coordinate.from_str("49.1743° S").to_dd()
    assert dd == "-49.1743°"
    #dd to dms
    dms = Coordinate.from_str("49.9367° N").to_dms()
    assert dms == "49° 56' 12\""
    dms = Coordinate.from_str("49.0008° S").to_dms()
    assert dms == "-49° 00' 03\""
    dms = Coordinate.from_str("49.0008° N").to_dms()
    assert dms == "49° 00' 03\""
    #dd to dm
    ddm = Coordinate.from_str("49.0008° S").to_ddm()
    assert ddm == "-49° 00.05'"
    