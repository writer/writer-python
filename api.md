# Chat

Types:

```python
from writerai.types import Chat, ChatStreamingData
```

Methods:

- <code title="post /v1/chat">client.chat.<a href="./src/writerai/resources/chat.py">chat</a>(\*\*<a href="src/writerai/types/chat_chat_params.py">params</a>) -> <a href="./src/writerai/types/chat.py">Chat</a></code>

# Completions

Types:

```python
from writerai.types import Completion, StreamingData
```

Methods:

- <code title="post /v1/completions">client.completions.<a href="./src/writerai/resources/completions.py">create</a>(\*\*<a href="src/writerai/types/completion_create_params.py">params</a>) -> <a href="./src/writerai/types/completion.py">Completion</a></code>

# Models

Types:

```python
from writerai.types import ModelListResponse
```

Methods:

- <code title="get /v1/models">client.models.<a href="./src/writerai/resources/models.py">list</a>() -> <a href="./src/writerai/types/model_list_response.py">ModelListResponse</a></code>

# Graphs

Types:

```python
from writerai.types import (
    Graph,
    GraphCreateResponse,
    GraphUpdateResponse,
    GraphDeleteResponse,
    GraphRemoveFileFromGraphResponse,
)
```

Methods:

- <code title="post /v1/graphs">client.graphs.<a href="./src/writerai/resources/graphs.py">create</a>(\*\*<a href="src/writerai/types/graph_create_params.py">params</a>) -> <a href="./src/writerai/types/graph_create_response.py">GraphCreateResponse</a></code>
- <code title="get /v1/graphs/{graph_id}">client.graphs.<a href="./src/writerai/resources/graphs.py">retrieve</a>(graph_id) -> <a href="./src/writerai/types/graph.py">Graph</a></code>
- <code title="put /v1/graphs/{graph_id}">client.graphs.<a href="./src/writerai/resources/graphs.py">update</a>(graph_id, \*\*<a href="src/writerai/types/graph_update_params.py">params</a>) -> <a href="./src/writerai/types/graph_update_response.py">GraphUpdateResponse</a></code>
- <code title="get /v1/graphs">client.graphs.<a href="./src/writerai/resources/graphs.py">list</a>(\*\*<a href="src/writerai/types/graph_list_params.py">params</a>) -> <a href="./src/writerai/types/graph.py">SyncCursorPage[Graph]</a></code>
- <code title="delete /v1/graphs/{graph_id}">client.graphs.<a href="./src/writerai/resources/graphs.py">delete</a>(graph_id) -> <a href="./src/writerai/types/graph_delete_response.py">GraphDeleteResponse</a></code>
- <code title="post /v1/graphs/{graph_id}/file">client.graphs.<a href="./src/writerai/resources/graphs.py">add_file_to_graph</a>(graph_id, \*\*<a href="src/writerai/types/graph_add_file_to_graph_params.py">params</a>) -> <a href="./src/writerai/types/file.py">File</a></code>
- <code title="delete /v1/graphs/{graph_id}/file/{file_id}">client.graphs.<a href="./src/writerai/resources/graphs.py">remove_file_from_graph</a>(file_id, \*, graph_id) -> <a href="./src/writerai/types/graph_remove_file_from_graph_response.py">GraphRemoveFileFromGraphResponse</a></code>

# Files

Types:

```python
from writerai.types import File, FileDeleteResponse
```

Methods:

- <code title="get /v1/files/{fileId}">client.files.<a href="./src/writerai/resources/files.py">retrieve</a>(file_id) -> <a href="./src/writerai/types/file.py">File</a></code>
- <code title="get /v1/files">client.files.<a href="./src/writerai/resources/files.py">list</a>(\*\*<a href="src/writerai/types/file_list_params.py">params</a>) -> <a href="./src/writerai/types/file.py">SyncCursorPage[File]</a></code>
- <code title="delete /v1/files/{fileId}">client.files.<a href="./src/writerai/resources/files.py">delete</a>(file_id) -> <a href="./src/writerai/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /v1/files/{fileId}/download">client.files.<a href="./src/writerai/resources/files.py">download</a>(file_id) -> BinaryAPIResponse</code>
- <code title="post /v1/files">client.files.<a href="./src/writerai/resources/files.py">upload</a>(\*\*<a href="src/writerai/types/file_upload_params.py">params</a>) -> <a href="./src/writerai/types/file.py">File</a></code>
