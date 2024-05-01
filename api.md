# Chat

Types:

```python
from writerai.types import ChatChatResponse
```

Methods:

- <code title="post /v1/chat">client.chat.<a href="./src/writerai/resources/chat.py">chat</a>(\*\*<a href="src/writerai/types/chat_chat_params.py">params</a>) -> <a href="./src/writerai/types/chat_chat_response.py">ChatChatResponse</a></code>

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
