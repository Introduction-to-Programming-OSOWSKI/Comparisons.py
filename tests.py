#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 10
day = 8

def test_code():
    assert main.greaterThan(5,6) == False, "function greaterThan(5, 6) failed"
    assert main.greaterThan(100,44) == True, "function greaterThan(100, 44) failed"

    assert main.equalTo(10, 15) == False, "function equalTo(10, 15) failed"
    assert main.equalTo(130,130) == True, "function equalTo(130, 130) failed"

    assert main.lessOrEqual(99,98) == False, "function lessOrEqual(99, 98) failed"
    assert main.lessOrEqual(98,98) == True, "function lessorEqual(98, 98) failed"
    assert main.lessOrEqual(98,99) == True, "function lessorEqual(98, 99) failed"

    assert main.lessThan(50,49) == False, "function lessThan(50, 49) failed"
    assert main.lessThan(50,51) == True, "function lessThan(50, 51) failed"
    
    assert main.greaterOrEqual(99,98) == True, "function greaterOrEqual(99, 98) failed"
    assert main.greaterOrEqual(99,100) == False, "function greaterOrEqual(99, 100) failed"
    assert main.greaterOrEqual(99,99) == True, "function greaterOrEqual(99, 99) failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
