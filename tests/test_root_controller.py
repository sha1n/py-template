import pytest
from google.protobuf.json_format import Parse

from generated.proto.webapp.api.message_pb2 import Message  # type: ignore
from tests.conftest import ITContext


@pytest.mark.it
def test_http_get_root_resource(context: ITContext):
    response = context.client.get(url="/", auth=context.basic_auth)
    actual_message = Parse(text=response.json(), message=Message())

    assert response.status_code == 200
    assert actual_message == Message(content="Hello World")
