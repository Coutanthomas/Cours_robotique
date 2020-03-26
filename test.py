# import model as dk
# import model as ik 
# import model as update
import model

def test_dk():
    m = model.Model()
    assert m.dk(2, 2) == (2.0, 0.0)
    assert m.dk(0, 0) == (0.0, 0.0)
    assert m.dk(0, 0.120) == (0.06, -1.0)
    assert m.dk(0.120, 0) == (0.06, 1.0)
    assert m.dk(2, 4) == (3.0, -16.666666666666668)


def test_ik():
    m = model.Model()
    assert m.ik(1, 0) == (1.0, 1.0)
    assert m.ik(5, 0) == (5.0, 5.0)
    assert m.ik(-5, 0) == (-5.0, -5.0)
    assert m.ik(3.3, 0) == (3.3, 3.3)
    assert m.ik(0, 1) == (0.06, -0.06)
    assert m.ik(0, 5) == (0.3, -0.3)
    assert m.ik(0, -5) == (-0.3, 0.3)
    assert m.ik(0, 0) == (0.0, 0.0)


def test_update():
    m = model.Model()
    
    


    

