import asynchronous_motor

def test_torques():
    # Prüft die Grundberechnung der Momente
    M_max, M_n = asynchronous_motor.torques(200000, 100000, 5000)
    assert M_max == 381.97
    assert M_n == 190.99
