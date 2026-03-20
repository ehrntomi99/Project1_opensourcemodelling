import asynchronous_motor

def test_torques():
    M_n, M_max = asynchronous_motor.torques(200000, 100000, 5000)
    assert round(M_max, 2) == 381.97
    assert round(M_n, 2) == 190.99
