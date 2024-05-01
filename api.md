# Chat

Types:

```python
from writer_ai.types import ChatChatResponse
```

Methods:

- <code title="post /v1/chat">client.chat.<a href="./src/writer_ai/resources/chat.py">chat</a>(\*\*<a href="src/writer_ai/types/chat_chat_params.py">params</a>) -> <a href="./src/writer_ai/types/chat_chat_response.py">ChatChatResponse</a></code>

# Completions

Types:

```python
from writer_ai.types import Completion, StreamingData
```

Methods:

- <code title="post /v1/completions">client.completions.<a href="./src/writer_ai/resources/completions.py">create</a>(\*\*<a href="src/writer_ai/types/completion_create_params.py">params</a>) -> <a href="./src/writer_ai/types/completion.py">Completion</a></code>

# Models

Types:

```python
from writer_ai.types import ModelListResponse
```

Methods:

- <code title="get /v1/models">client.models.<a href="./src/writer_ai/resources/models.py">list</a>() -> <a href="./src/writer_ai/types/model_list_response.py">ModelListResponse</a></code>
