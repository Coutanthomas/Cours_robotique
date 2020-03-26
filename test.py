# import model as dk
# import model as ik 
# import model as update
import model
import math

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
    assert m.ik(5, 3) == (5.18, 4.82)


def test_update_same_opposite_speed():
    m = model.Model()
    m.m1.speed = 2
    m.m2.speed = -2
    m.update(1/60)
    assert (m.x, m.y) == (0.0, 0.0)
    

def test_update_same_speed():
    m = model.Model()
    m.m1.speed = 60
    m.m2.speed = 60
    m.update(1/60)
    assert (m.x, m.y) == (1.0, 0.0)


def test_update_change_pos_Y():
    m = model.Model()
    m.m1.speed = 0
    m.m2.speed = 0
    m.theta = math.pi/2
    m.update(1/60)
    m.m1.speed = 60
    m.m2.speed = 60
    m.update(1/60)
    assert (round(m.x,2), round(m.y,2)) == (0.00, 1.00)       


 
    

