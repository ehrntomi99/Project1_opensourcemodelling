import asynchronous_motor


def test_torques():
    """ Check if torque calculation is correct for 200kW, 100kW """
    M_n, M_max = asynchronous_motor.torques(200000, 100000, 5000)
    assert round(M_max, 2) == 381.97
    assert round(M_n, 2) == 190.99

def test_torques_15000():
    """ Test torque at speed of 15000 rpm """
    M_n_15, M_max_15 = asynchronous_motor.torques_15000(300, 150, 5000, 15000)
    assert round(M_max_15, 0) == 100
