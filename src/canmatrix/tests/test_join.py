# -*- coding: utf-8 -*-
import pytest
import canmatrix.join
import decimal

def test_list_pgn():
    matrix1 = canmatrix.canmatrix.CanMatrix()
    frame1 = canmatrix.canmatrix.Frame("Frame1", arbitration_id=1)
    frame1.add_signal(canmatrix.canmatrix.Signal("SomeSignal"))
    matrix1.add_frame(frame1)

    pgn_x, id_x = canmatrix.join.list_pgn(matrix1)

    assert pgn_x == 0
    assert id_x == 1
