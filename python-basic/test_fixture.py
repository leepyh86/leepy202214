#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: test_fixture.py
# @time: 2022/1/4 12:10
# @author: leepy cham

import  pytest


@pytest.fixture()
def login():
    print("\n login start")
    yield
    print("\n quit end")

class TestFixture:
    def setup(self):
        print("start")
    def teardown(self):
        print("end")

    @pytest.mark.usefixtures("login")
    def test_fix(self):
        print("hello ")