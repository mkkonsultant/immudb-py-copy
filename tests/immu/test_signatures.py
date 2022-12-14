# Copyright 2021 CodeNotary, Inc. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from random import randint
import pytest


@pytest.fixture(scope="module")
def xkey():
    return "test_key_{:04d}".format(randint(0, 10000)).encode('ascii')


@pytest.fixture(scope="module")
def xval():
    return "test_value_{:04d}".format(randint(0, 10000)).encode('ascii')


def test_get_set(client, xkey, xval):
    setresp = client.verifiedSet(xkey, xval)
    assert setresp.verified
    getresp = client.verifiedGet(xkey)
    assert getresp.verified
    assert getresp.value == xval
    txresp = client.verifiedTxById(setresp.id)
    assert xkey in txresp


def test_ref(client, xkey, xval):
    refkey = "test_ref_{:04d}".format(randint(0, 10000)).encode('ascii')
    refresp = client.verifiedSetReference(xkey, refkey)
    assert refresp.verified
    getresp = client.verifiedGet(refkey)
    assert getresp.verified
    assert getresp.value == xval


def test_z(client, xkey):
    zsetname = "zset_{:04d}".format(randint(0, 10000)).encode('utf-8')
    zresp = client.verifiedZAdd(zsetname, 42.0, xkey)
    assert zresp.verified
