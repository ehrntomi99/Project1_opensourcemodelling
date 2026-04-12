import asynchronous_motor


def test_torques_values():
    """ Test if function returns M_max and M_n """
    result = asynchronous_motor.torques(200000, 100000, 5000)
    assert len(result) == 2


def test_torques():
    """ Check if torque calculation is correct for 200kW, 100kW """
    M_n, M_max = asynchronous_motor.torques(200000, 100000, 5000)
    assert round(M_max, 2) == 999
    assert round(M_n, 2) == 99


def test_torques_15000_values():
    """ Test if function returns two values """
    result = asynchronous_motor.torques_15000(150, 300)
    assert len(result) == 2


def test_torques_15000():
    """ Test torque at speed of 15000 rpm """
    M_n_15, M_max_15 = asynchronous_motor.torques_15000(150, 300)
    assert round(M_max_15, 0) == 100


def test_torque_curve():
    """ Check if logic determines 2500 constant torque, 10000 field weakening """
    results = asynchronous_motor.torque_curve([2500, 10000], 200, 5000)
    
    assert results[0] == 200
    assert results[1] == 100
