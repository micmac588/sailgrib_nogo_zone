from degree_converter import DegreeConverter
import logging

my_logger = logging.getLogger()

def test_from_dms():
    # dms to dms
    dms = DegreeConverter(my_logger).from_dms(49, 30, 45).to_dms()
    assert dms == '49° 30\' 45"'
    dms = DegreeConverter(my_logger).from_dms(49, 30, 45).to_dms()
    assert dms == '49° 30\' 45"'
    # dms to dm
    ddm = DegreeConverter(my_logger).from_dms(49, 30, 56).to_ddm()
    assert ddm == '49° 30,93\''
    ddm = DegreeConverter(my_logger).from_dms(49, 30, 45).to_ddm()
    assert ddm == '49° 30,75\''
    #dms to dd
    dd = DegreeConverter(my_logger).from_dms(49, 30, 56).to_dd() 
    assert dd == '49,5156°'
    dd = DegreeConverter(my_logger).from_dms(49, 30, 45).to_dd() 
    assert dd == '49,5125°'

def test_from_dms_as_str():
    # dms to dms
    dms = DegreeConverter(my_logger).from_str('49°30\'45"').to_dms()
    assert dms == '49° 30\' 45"'
    dms = DegreeConverter(my_logger).from_str('49° 30\' 45\"').to_dms()
    assert dms == '49° 30\' 45"'
    # dms to dm
    ddm = DegreeConverter(my_logger).from_str('49°30\'56\"').to_ddm()
    assert ddm == '49° 30,93\''
    ddm = DegreeConverter(my_logger).from_str('49° 30\' 45\"').to_ddm()
    assert ddm == '49° 30,75\''
    #dms to dd
    dd = DegreeConverter(my_logger).from_str('49°30\'56\"').to_dd() 
    assert dd == '49,5156°'
    dd = DegreeConverter(my_logger).from_str('49° 30\' 45\"').to_dd() 
    assert dd == '49,5125°'

def test_from_ddm():
    #ddm to ddm
    ddm = DegreeConverter(my_logger).from_ddm(49, 30.75).to_ddm()
    assert ddm == "49° 30,75'"
    ddm = DegreeConverter(my_logger).from_ddm(49, 30.20).to_ddm()
    assert ddm == "49° 30,20'"
    #dm to dms
    dms = DegreeConverter(my_logger).from_ddm(49, 30.75).to_dms()
    assert dms == '49° 30\' 45"'
    dms = DegreeConverter(my_logger).from_ddm(49, 30.75).to_dms()
    assert dms == '49° 30\' 45"'
    #dm to dd
    dd = DegreeConverter(my_logger).from_ddm(49, 30.75).to_dd()
    assert dd == '49,5125°'
    dd = DegreeConverter(my_logger).from_ddm(49, 30.75).to_dd()
    assert dd == '49,5125°'

def test_from_ddm_as_str():
    #ddm to ddm
    ddm = DegreeConverter(my_logger).from_str("49°30,75'").to_ddm()
    assert ddm == "49° 30,75'"
    ddm = DegreeConverter(my_logger).from_str("49° 30,20'").to_ddm()
    assert ddm == "49° 30,20'"
    #dm to dms
    dms = DegreeConverter(my_logger).from_str("49°30,75'").to_dms()
    assert dms == '49° 30\' 45"'
    dms = DegreeConverter(my_logger).from_str("49° 30,75'").to_dms()
    assert dms == '49° 30\' 45"'
    #dm to dd
    dd = DegreeConverter(my_logger).from_str("49°30,75'").to_dd()
    assert dd == '49,5125°'
    dd = DegreeConverter(my_logger).from_str("49° 30,75'").to_dd()
    assert dd == '49,5125°'

def test_from_dd_as_str():
    #dd to dd
    dd = DegreeConverter(my_logger).from_dd(49.1743).to_dd()
    assert dd == "49,1742°"
    #dd to dms
    dms = DegreeConverter(my_logger).from_dd(49.9367).to_dms()
    assert dms == "49° 56' 12\""
    dms = DegreeConverter(my_logger).from_dd(49.0008).to_dms()
    assert dms == "49° 0' 03\""
    dms = DegreeConverter(my_logger).from_dd(49.0008).to_dms()
    assert dms == "49° 0' 03\""
    #dd to dm
    ddm = DegreeConverter(my_logger).from_dd(49.0008).to_ddm()
    assert ddm == "49° 0,05'"

def test_from_dd_as_str():
    #dd to dd
    dd = DegreeConverter(my_logger).from_str("49,1743°").to_dd()
    assert dd == "49,1742°"
    #dd to dms
    dms = DegreeConverter(my_logger).from_str("49,9367°").to_dms()
    assert dms == "49° 56' 12\""
    dms = DegreeConverter(my_logger).from_str("49,0008°").to_dms()
    assert dms == "49° 0' 03\""
    dms = DegreeConverter(my_logger).from_str("49,0008°").to_dms()
    assert dms == "49° 0' 03\""
    #dd to dm
    ddm = DegreeConverter(my_logger).from_str("49,0008°").to_ddm()
    assert ddm == "49° 0,05'"
    
