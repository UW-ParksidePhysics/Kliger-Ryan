def H(x):
    if x < 0:
        H = 0
    elif x >= 0:
        H = 1
        return H
def test_h():
    print(H(-10),H(-1e-15), H(0), H(1e-15), H(10))
    return
test_h()