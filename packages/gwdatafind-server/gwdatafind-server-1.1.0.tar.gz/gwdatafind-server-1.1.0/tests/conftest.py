# -*- coding: utf-8 -*-
# Copyright (2019) Cardiff University
# Licensed under GPLv3+ - see LICENSE

"""Test configuration for gwdatafind_server
"""

import os
from pathlib import Path
from unittest import mock

import pytest

from gwdatafind_server import create_app


@mock.patch.dict("os.environ")
@pytest.fixture
def app():
    os.environ["LDR_LOCATION"] = str(Path(__file__).parent)
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()
