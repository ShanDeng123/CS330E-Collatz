#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    # Makes sure that the basic read functionality works.
    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)

    def test_read_3(self):
        s = "30 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 30)
        self.assertEqual(j, 10)

    def test_read_4(self):
        s = "1 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 999999)

# Ensures that Alphabetical inputs raise an error
# def test_read_2(self):
##        self.assertRaises(ValueError, collatz_read, "30 abc\n")
##
# Ensures that Decimal inputs raise an error.
# def test_read_3(self):
##        self.assertRaises(ValueError, collatz_read, "42.22 36\n")

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_3(self):
        v = collatz_eval(90000, 70)
        self.assertEqual(v, 351)

    def test_eval_4(self):
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    def test_eval_5(self):
        v = collatz_eval(1, 6384)
        self.assertEqual(v, 262)

    def test_eval_6(self):
        self.assertRaises(ValueError, collatz_eval, 0, 999999)

    def test_eval_7(self):
        self.assertRaises(ValueError, collatz_eval, 999999, 1000000)

    def test_eval_8(self):
        self.assertRaises(TypeError, collatz_eval, "abc", 30)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
        self.assertIsInstance(w.getvalue(), str)

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")
        self.assertIsInstance(w.getvalue(), str)

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 200, 100, 125)
        self.assertEqual(w.getvalue(), "200 100 125\n")
        self.assertIsInstance(w.getvalue(), str)

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")
        self.assertIsInstance(w.getvalue(), str)

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        self.assertIsInstance(w.getvalue(), str)

    def test_solve_2(self):
        r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")
        self.assertIsInstance(w.getvalue(), str)

    def test_solve_3(self):
        r = StringIO("5 5 6 7\n2090 2100 9 12\n37 40 -1 23\n99 100 3\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "5 5 6\n2090 2100 126\n37 40 35\n99 100 26\n")
        self.assertIsInstance(w.getvalue(), str)

    def test_solve_4(self):
        r = StringIO("32 32 dog\n1 100\n2 200 cat elephant\n300 400\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "32 32 6\n1 100 119\n2 200 125\n300 400 144\n")
        self.assertIsInstance(w.getvalue(), str)

# ----
# main
# ----


if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
