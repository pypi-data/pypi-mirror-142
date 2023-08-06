# -*- coding: utf-8 -*-
# Copyright (2019) Cardiff University
# Licensed under GPLv3+ - see LICENSE

import os
from pathlib import Path
from unittest import mock

import pytest

from gwdatafind_server import config
from gwdatafind_server.api import utils as api_utils

header = {'SSL_CLIENT_S_DN':
          '/DC=org/DC=cilogon/C=US/O=LIGO/CN=Albert Einstein '
          'albert.einstein@ligo.org',
          'SSL_CLIENT_I_DN': '/DC=org/DC=cilogon/C=US/O=LIGO/CN='}

# -- app ------------------------------


def test_shutdown(app):
    """Test that `app.shutdown()` kills the cache thread
    """
    assert app.cache_manager.is_alive()
    app.shutdown()
    assert not app.cache_manager.is_alive()


# -- config ---------------------------

@mock.patch.dict(
    os.environ,
    {"LDR_LOCATION": str(Path(__file__).parent)},
)
def test_get_config_path():
    """Test that get_config_path() can resolve a file
    """
    assert config.get_config_path() == str(
        Path(os.environ["LDR_LOCATION"]) / "gwdatafind-server.ini"
    )


@mock.patch("os.path.isfile", return_value=False)
def test_get_config_path_error(_):
    """Test that get_config_path() errors when it can't resolve a file
    """
    with pytest.raises(ValueError):
        config.get_config_path()


# -- views ----------------------------

def test_find_observatories(client):
    """Test the `find_observatories` view
    """
    resp = client.get("/services/data/v1/gwf.json", headers=header)
    assert resp.status_code == 200
    assert sorted(resp.json) == ["H", "L"]


@pytest.mark.parametrize('type_, types', [
    ('L', ["L1_TEST_1", "L1_TEST_2"]),
    ('all', ["H1_TEST_1", "L1_TEST_1", "L1_TEST_2"]),
])
def test_find_types(client, type_, types):
    """Test the `find_types` view
    """
    resp = client.get("/services/data/v1/gwf/{}.json".format(type_),
                      headers=header)
    assert resp.status_code == 200
    assert sorted(resp.json) == sorted(types)


@pytest.mark.parametrize('ext, segs', [
    ('gwf', [[1000000000, 1000000008], [1000000012, 1000000020]]),
    ('h5', [[1000000000, 1000000008]]),
])
def test_find_times_all(client, ext, segs):
    """Test the `find_times` view without specifying limits
    """
    resp = client.get(
        "/services/data/v1/{}/L/L1_TEST_1/segments.json".format(ext),
        headers=header)
    assert resp.status_code == 200
    assert resp.json == segs


def test_find_times(client):
    """Test the `find_times` view with limits
    """
    resp = client.get(
        "/services/data/v1/gwf/L/L1_TEST_1/segments/"
        "1000000007,1000000013.json",
        headers=header)
    assert resp.status_code == 200
    assert resp.json == [
        [1000000007, 1000000008],
        [1000000012, 1000000013],
    ]


@mock.patch.object(api_utils, "_DEFAULT_GSIFTP_HOST", new="testhost")
def test_find_url(client):
    """Test the `find_url` view
    """
    resp = client.get(
        "/services/data/v1"
        "/h5/L/L1_TEST_1/L-L1_TEST_1-1000000004-4.h5.json",
        headers=header)
    assert resp.status_code == 200
    assert resp.json == [
        "file://localhost/test/path/L-L1_TEST_1-1000000004-4.h5",
        "gsiftp://testhost:15000/test/path/L-L1_TEST_1-1000000004-4.h5",
    ]


@mock.patch.object(api_utils, "_DEFAULT_GSIFTP_HOST", new="testhost")
def test_find_urls(client):
    """Test the `find_urls` view with no special options
    """
    resp = client.get(
        "/services/data/v1/gwf/L/L1_TEST_1/1000000004,1000000016.json",
        headers=header)
    assert resp.status_code == 200
    assert sorted(resp.json) == [
        "file://localhost/test/path/L-L1_TEST_1-1000000004-4.gwf",
        "file://localhost/test/path2/L-L1_TEST_1-1000000012-4.gwf",
        "gsiftp://testhost:15000/test/path/L-L1_TEST_1-1000000004-4.gwf",
        "gsiftp://testhost:15000/test/path2/L-L1_TEST_1-1000000012-4.gwf",
    ]


def test_find_urls_fancy(client):
    """Test the `find_urls` view with extra options
    """
    resp = client.get(
        "/services/data/v1"
        "/gwf/L/L1_TEST_1/1000000000,1000000008/file.json?match=04",
        headers=header)
    assert resp.status_code == 200
    assert sorted(resp.json) == [
        "file://localhost/test/path/L-L1_TEST_1-1000000004-4.gwf",
    ]


def test_find_urls_filter_preference(client):
    """Test the `find_urls` view with `filter_preference`
    """
    resp = client.get(
        "/services/data/v1"
        "/h5/H/H1_TEST_1/1000000000,1000000004/file.json",
        headers=header)
    assert resp.status_code == 200
    assert sorted(resp.json) == [
        "file://localhost/test/preferred/path/H-H1_TEST_1-1000000000-8.h5",
    ]


@mock.patch.object(api_utils, "_DEFAULT_GSIFTP_HOST", new="testhost")
def test_find_latest(client):
    """Test the `find_latest` view
    """
    resp = client.get(
        "/services/data/v1/gwf/L/L1_TEST_1/latest.json",
        headers=header)
    assert resp.status_code == 200
    assert resp.json == [
        "file://localhost/test/path2/L-L1_TEST_1-1000000016-4.gwf",
        "gsiftp://testhost:15000/test/path2/L-L1_TEST_1-1000000016-4.gwf",
    ]


def test_find_latest_urltype(client):
    """Test the `find_latest` view with urltype
    """
    resp = client.get(
        "/services/data/v1/gwf/L/L1_TEST_1/latest/file.json",
        headers=header)
    assert resp.status_code == 200
    assert resp.json == [
        "file://localhost/test/path2/L-L1_TEST_1-1000000016-4.gwf",
    ]
