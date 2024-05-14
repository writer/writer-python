# Chat

Types:

```python
from writer.types import Chat, ChatStreamingData
```

Methods:

- <code title="post /v1/chat">client.chat.<a href="./src/writer/resources/chat.py">chat</a>(\*\*<a href="src/writer/types/chat_chat_params.py">params</a>) -> <a href="./src/writer/types/chat.py">Chat</a></code>

# Completions

Types:

```python
from writer.types import Completion, StreamingData
```

Methods:

- <code title="post /v1/completions">client.completions.<a href="./src/writer/resources/completions.py">create</a>(\*\*<a href="src/writer/types/completion_create_params.py">params</a>) -> <a href="./src/writer/types/completion.py">Completion</a></code>

# Models

Types:

```python
from writer.types import ModelListResponse
```

Methods:

- <code title="get /v1/models">client.models.<a href="./src/writer/resources/models.py">list</a>() -> <a href="./src/writer/types/model_list_response.py">ModelListResponse</a></code>
