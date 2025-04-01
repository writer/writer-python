# Shared Types

```python
from writerai.types import (
    ErrorMessage,
    ErrorObject,
    FunctionDefinition,
    FunctionParams,
    GraphData,
    Logprobs,
    LogprobsToken,
    Source,
    ToolCall,
    ToolCallStreaming,
    ToolChoiceJsonObject,
    ToolChoiceString,
    ToolParam,
)
```

# Applications

Types:

```python
from writerai.types import (
    ApplicationGenerateContentChunk,
    ApplicationGenerateContentResponse,
    ApplicationRetrieveResponse,
    ApplicationListResponse,
)
```

Methods:

- <code title="get /v1/applications/{application_id}">client.applications.<a href="./src/writerai/resources/applications/applications.py">retrieve</a>(application_id) -> <a href="./src/writerai/types/application_retrieve_response.py">ApplicationRetrieveResponse</a></code>
- <code title="get /v1/applications">client.applications.<a href="./src/writerai/resources/applications/applications.py">list</a>(\*\*<a href="src/writerai/types/application_list_params.py">params</a>) -> <a href="./src/writerai/types/application_list_response.py">SyncCursorPage[ApplicationListResponse]</a></code>
- <code title="post /v1/applications/{application_id}">client.applications.<a href="./src/writerai/resources/applications/applications.py">generate_content</a>(application_id, \*\*<a href="src/writerai/types/application_generate_content_params.py">params</a>) -> <a href="./src/writerai/types/application_generate_content_response.py">ApplicationGenerateContentResponse</a></code>

## Jobs

Types:

```python
from writerai.types.applications import (
    ApplicationGenerateAsyncResponse,
    ApplicationJobsListResponse,
    JobCreateResponse,
    JobRetryResponse,
)
```

Methods:

- <code title="post /v1/applications/{application_id}/jobs">client.applications.jobs.<a href="./src/writerai/resources/applications/jobs.py">create</a>(application_id, \*\*<a href="src/writerai/types/applications/job_create_params.py">params</a>) -> <a href="./src/writerai/types/applications/job_create_response.py">JobCreateResponse</a></code>
- <code title="get /v1/applications/jobs/{job_id}">client.applications.jobs.<a href="./src/writerai/resources/applications/jobs.py">retrieve</a>(job_id) -> <a href="./src/writerai/types/applications/application_generate_async_response.py">ApplicationGenerateAsyncResponse</a></code>
- <code title="get /v1/applications/{application_id}/jobs">client.applications.jobs.<a href="./src/writerai/resources/applications/jobs.py">list</a>(application_id, \*\*<a href="src/writerai/types/applications/job_list_params.py">params</a>) -> <a href="./src/writerai/types/applications/application_generate_async_response.py">SyncApplicationJobsOffset[ApplicationGenerateAsyncResponse]</a></code>
- <code title="post /v1/applications/jobs/{job_id}/retry">client.applications.jobs.<a href="./src/writerai/resources/applications/jobs.py">retry</a>(job_id) -> <a href="./src/writerai/types/applications/job_retry_response.py">JobRetryResponse</a></code>

## Graphs

Types:

```python
from writerai.types.applications import ApplicationGraphsResponse
```

Methods:

- <code title="put /v1/applications/{application_id}/graphs">client.applications.graphs.<a href="./src/writerai/resources/applications/graphs.py">update</a>(application_id, \*\*<a href="src/writerai/types/applications/graph_update_params.py">params</a>) -> <a href="./src/writerai/types/applications/application_graphs_response.py">ApplicationGraphsResponse</a></code>
- <code title="get /v1/applications/{application_id}/graphs">client.applications.graphs.<a href="./src/writerai/resources/applications/graphs.py">list</a>(application_id) -> <a href="./src/writerai/types/applications/application_graphs_response.py">ApplicationGraphsResponse</a></code>

# Chat

Types:

```python
from writerai.types import (
    ChatCompletion,
    ChatCompletionChoice,
    ChatCompletionChunk,
    ChatCompletionMessage,
    ChatCompletionParams,
    ChatCompletionUsage,
)
```

Methods:

- <code title="post /v1/chat">client.chat.<a href="./src/writerai/resources/chat.py">chat</a>(\*\*<a href="src/writerai/types/chat_chat_params.py">params</a>) -> <a href="./src/writerai/types/chat_completion.py">ChatCompletion</a></code>

# Completions

Types:

```python
from writerai.types import Completion, CompletionChunk, CompletionParams
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
    Question,
    QuestionResponseChunk,
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
- <code title="post /v1/graphs/question">client.graphs.<a href="./src/writerai/resources/graphs.py">question</a>(\*\*<a href="src/writerai/types/graph_question_params.py">params</a>) -> <a href="./src/writerai/types/question.py">Question</a></code>
- <code title="delete /v1/graphs/{graph_id}/file/{file_id}">client.graphs.<a href="./src/writerai/resources/graphs.py">remove_file_from_graph</a>(file_id, \*, graph_id) -> <a href="./src/writerai/types/graph_remove_file_from_graph_response.py">GraphRemoveFileFromGraphResponse</a></code>

# Files

Types:

```python
from writerai.types import File, FileDeleteResponse, FileRetryResponse
```

Methods:

- <code title="get /v1/files/{file_id}">client.files.<a href="./src/writerai/resources/files.py">retrieve</a>(file_id) -> <a href="./src/writerai/types/file.py">File</a></code>
- <code title="get /v1/files">client.files.<a href="./src/writerai/resources/files.py">list</a>(\*\*<a href="src/writerai/types/file_list_params.py">params</a>) -> <a href="./src/writerai/types/file.py">SyncCursorPage[File]</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/writerai/resources/files.py">delete</a>(file_id) -> <a href="./src/writerai/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /v1/files/{file_id}/download">client.files.<a href="./src/writerai/resources/files.py">download</a>(file_id) -> BinaryAPIResponse</code>
- <code title="post /v1/files/retry">client.files.<a href="./src/writerai/resources/files.py">retry</a>(\*\*<a href="src/writerai/types/file_retry_params.py">params</a>) -> <a href="./src/writerai/types/file_retry_response.py">FileRetryResponse</a></code>
- <code title="post /v1/files">client.files.<a href="./src/writerai/resources/files.py">upload</a>(\*\*<a href="src/writerai/types/file_upload_params.py">params</a>) -> <a href="./src/writerai/types/file.py">File</a></code>

# Tools

Types:

```python
from writerai.types import ToolContextAwareSplittingResponse, ToolParsePdfResponse
```

Methods:

- <code title="post /v1/tools/context-aware-splitting">client.tools.<a href="./src/writerai/resources/tools/tools.py">context_aware_splitting</a>(\*\*<a href="src/writerai/types/tool_context_aware_splitting_params.py">params</a>) -> <a href="./src/writerai/types/tool_context_aware_splitting_response.py">ToolContextAwareSplittingResponse</a></code>
- <code title="post /v1/tools/pdf-parser/{file_id}">client.tools.<a href="./src/writerai/resources/tools/tools.py">parse_pdf</a>(file_id, \*\*<a href="src/writerai/types/tool_parse_pdf_params.py">params</a>) -> <a href="./src/writerai/types/tool_parse_pdf_response.py">ToolParsePdfResponse</a></code>

## Comprehend

Types:

```python
from writerai.types.tools import ComprehendMedicalResponse
```

Methods:

- <code title="post /v1/tools/comprehend/medical">client.tools.comprehend.<a href="./src/writerai/resources/tools/comprehend.py">medical</a>(\*\*<a href="src/writerai/types/tools/comprehend_medical_params.py">params</a>) -> <a href="./src/writerai/types/tools/comprehend_medical_response.py">ComprehendMedicalResponse</a></code>

# Vision

Types:

```python
from writerai.types import VisionRequest, VisionResponse
```

Methods:

- <code title="post /v1/vision">client.vision.<a href="./src/writerai/resources/vision.py">analyze</a>(\*\*<a href="src/writerai/types/vision_analyze_params.py">params</a>) -> <a href="./src/writerai/types/vision_response.py">VisionResponse</a></code>
