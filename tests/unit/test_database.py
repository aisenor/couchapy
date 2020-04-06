import  couchapy
from    couchapy.decorators import AllowedKeys
import  pytest
import  pytest_httpserver as test_server


@pytest.fixture
def httpserver_listen_address():
    return ("127.0.0.1", 8000)


@pytest.fixture(autouse=True)
def setup():
    """ setup any state specific to the execution of the given module."""
    global couch
    couch = couchapy.CouchDB(name="test", password="test", host="http://127.0.0.1", port=8000, database_kwargs={"db": '_local'})
    yield


def test_database_exists(httpserver: test_server.HTTPServer):
    httpserver.expect_request("/_local", method="HEAD").respond_with_json({}, headers={'ETag': 'revidhere'}, status=200)

    # simulate a 404
    httpserver.expect_request("/doesnotexist", method="HEAD").respond_with_json({}, headers={'ETag': 'revidhere'}, status=404)
    response = couch.db.exists(uri_segments={'db': '_local'})
    assert response is True

    response = couch.db.exists(uri_segments={'db': 'doesnotexist'})
    assert response is False

    response = couch.db.exists(uri_segments={'db': 'generateinternalservererror'})
    assert response is False

def test_get_doc_info(httpserver: test_server.HTTPServer):
    expected = 'revidhere'

    httpserver.expect_request("/_local/testdoc", method="HEAD").respond_with_json({}, headers={'ETag': 'revidhere'})
    response = couch.db.get_doc_info(uri_segments={'docid': 'testdoc'})

    assert response == expected
