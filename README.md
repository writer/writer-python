# Writer Python API library

[![PyPI version](https://img.shields.io/pypi/v/writer-sdk.svg)](https://pypi.org/project/writer-sdk/)

The Writer Python library provides access to the Writer REST API from any Python 3.8+
application. It includes a set of tools and utilities that make it easy to integrate the capabilities
of Writer into your projects.

It is generated with [Stainless](https://www.stainless.com/).

## Documentation

The REST API documentation can be found on [dev.writer.com](https://dev.writer.com/api-guides/introduction). The full API of this library can be found in [api.md](api.md).

## Installation

To install the package from PyPI, use `pip`:

```sh
# install from PyPI
pip install writer-sdk
```

## Prequisites

Before you begin, ensure you have:

- Python 3.8 or higher
- A [Writer API key](https://dev.writer.com/api-guides/quickstart#generate-a-new-api-key)

## Authentication

To authenticate with the Writer API, set the `WRITER_API_KEY` environment variable.

```shell
$ export WRITER_API_KEY="my-api-key"
```

The `Writer` class automatically infers your API key from the `WRITER_API_KEY` environment variable.

```python
from writerai import Writer

client = Writer()  # The API key will be inferred from the `WRITER_API_KEY` environment variable
```

You can also explicitly set the API key with the `api_key` parameter:

```python
from writerai import Writer

client = Writer(api_key="my-api-key")
```

> Never hard-code your API keys in source code or commit them to version control systems like GitHub.
> We recommend adding `WRITER_API_KEY="My API Key"` to your `.env` file so that your API Key is not stored in source control.

## Usage

You can find the full API for this library in [api.md](api.md).

### Synchronous versus asynchronous usage

The Writer Python library supports both synchronous and asynchronous usage. With synchronous usage, you call the API methods directly:

```python
from writerai import Writer

client = Writer()

chat_completion = client.chat.chat(
    messages=[
        {
            "content": "Write a haiku about programming",
            "role": "user",
        }
    ],
    model="palmyra-x-004",
)
print(chat_completion.choices[0].message.content)
```

With asynchronous usage, you import `AsyncWriter` instead of `Writer` and use `await` with each API call:

```python
import asyncio
from writerai import AsyncWriter

client = AsyncWriter()


async def main() -> None:
    chat_completion = await client.chat.chat(
        messages=[
            {
                "content": "Write a haiku about programming",
                "role": "user",
            }
        ],
        model="palmyra-x-004",
    )
    print(chat_completion.choices[0].message.content)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Streaming versus non-streaming responses

The Writer Python library provides support for streaming responses using Server Side Events (SSE).

To use streaming, set the `stream` parameter to `True` when calling an API method. You can then iterate over the stream to get the response data:

```python
from writerai import Writer

client = Writer()

stream = client.chat.chat(
    messages=[
        {
            "content": "Write a haiku about programming",
            "role": "user",
        }
    ],
    model="palmyra-x-004",
    stream=True,
)

output_text = ""
for chunk in stream:
    if chunk.choices[0].delta.content:
        output_text += chunk.choices[0].delta.content
    else:
        continue
print(output_text)
```

The async client uses the same interface.

```python
import asyncio
from writerai import AsyncWriter

client = AsyncWriter()

stream = await client.chat.chat(
    messages=[
        {
            "content": "Write a haiku about programming",
            "role": "user",
        }
    ],
    model="palmyra-x-004",
    stream=True,
)

output_text = ""
async for chunk in stream:
    if chunk.choices[0].delta.content:
        output_text += chunk.choices[0].delta.content
    else:
        continue
print(output_text)
```

For non-streaming responses, the library returns a single response object.

### Streaming Helpers

The SDK also includes helpers to process streams and handle incoming events.

```python
with client.chat.stream(
    model="palmyra-x-004",
    messages=[{"role": "user", "content": prompt}],
) as stream:
    for event in stream:
        if event.type == "content.delta":
            print(event.delta, flush=True, end="")
```

More information on streaming helpers can be found in the dedicated documentation: [helpers.md](helpers.md)

## Pagination

List methods in the Writer API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
from writerai import Writer

client = Writer()

all_graphs = []
# Automatically fetches more pages as needed.
for graph in client.graphs.list():
    # Do something with graph here
    all_graphs.append(graph)
print(all_graphs)
```

Or, asynchronously:

```python
import asyncio
from writerai import AsyncWriter

client = AsyncWriter()


async def main() -> None:
    all_graphs = []
    # Iterate through items across all pages, issuing requests as needed.
    async for graph in client.graphs.list():
        all_graphs.append(graph)
    print(all_graphs)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await client.graphs.list()  # Remove `await` for non-async usage.
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")
```

You can also work directly with the returned data:

```python
first_page = await client.graphs.list()  # Remove `await` for non-async usage.

print(f"next page cursor: {first_page.after}")  # => "next page cursor: ..."
for graph in first_page.data:
    print(graph.id)
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from writerai import Writer

client = Writer()

chat_completion = client.chat.chat(
    messages=[{"role": "user"}],
    model="model",
    stream_options={"include_usage": True},
)
print(chat_completion.stream_options)
```

## File uploads

You can pass file upload parameters as `bytes`, a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance or a tuple of `(filename, contents, media type)`.

The `content_type` parameter is the [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types) of the file being uploaded. The file upload supports `txt`, `doc`, `docx`, `ppt`, `pptx`, `jpg`, `png`, `eml`, `html`, `pdf`, `srt`, `csv`, `xls`, and `xlsx` file extensions.

```python
from pathlib import Path
from writerai import Writer

client = Writer()

client.files.upload(
    content=Path("/path/to/file/example.pdf"),
    content_disposition="attachment; filename='example.pdf'",
    content_type="application/pdf",
)
```

The async client uses the exact same interface. If you pass a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, the file contents will be read asynchronously automatically.

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems, a timeout, or a firewall that doesn't allow the connection), a subclass of `writerai.APIConnectionError` is raised.

> If you are behind a firewall, you may need to configure it to allow connections to the Writer API at `https://api.writer.com/v1`.

When the API returns a non-success status code - 4xx or 5xx - a subclass of `writerai.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `writerai.APIError`.

```python
import writerai
from writerai import Writer

client = Writer()

try:
    client.chat.chat(
        messages=[
            {
                "content": "Write a haiku about programming",
                "role": "user",
            }
        ],
        model="palmyra-x-004",
    )
except writerai.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except writerai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except writerai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

The library automatically retries certain errors two times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), `408 Request Timeout`, `409 Conflict`,
`429 Rate Limit`, and `>=500 Internal errors` are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from writerai import Writer

# Configure the default for all requests:
client = Writer(
    # default is 2
    max_retries=0,
)

# Or, configure per request:
client.with_options(max_retries=5).chat.chat(
    messages=[
        {
            "content": "Write a haiku about programming",
            "role": "user",
        }
    ],
    model="palmyra-x-004",
)
```

### Timeouts

By default, requests time out after three minutes. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
import httpx
from writerai import Writer

# Configure the default for all requests:
client = Writer(
    # 20 seconds (default is 3 minutes)
    timeout=20.0,
)

# More granular control:
client = Writer(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per request:
client.with_options(timeout=5.0).chat.chat(
    messages=[
        {
            "content": "Write a haiku about programming",
            "role": "user",
        }
    ],
    model="palmyra-x-004",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Logging

We use the standard [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `WRITER_LOG` to `info`.

```shell
$ export WRITER_LOG=info
```

Or to `debug` for more verbose logging.

## Advanced

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Result was {}.')
  else:
    print('Result was{"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

You can access the raw Response object by prefixing `.with_raw_response.` to any HTTP method call.

#### Non-streaming responses

```py
from writerai import Writer

client = Writer()
response = client.chat.with_raw_response.chat(
    messages=[{
        "content": "Write a haiku about programming",
        "role": "user",
    }],
    model="palmyra-x-004",
)
print(response.headers.get('X-My-Header'))

chat = response.parse()  # get the object that `chat.chat()` would have returned
print(chat.id)
```

Calling a method with `.with_raw_response` returns an [`APIResponse`](https://github.com/writer/writer-python/tree/main/src/writerai/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/writer/writer-python/tree/main/src/writerai/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### Streaming responses

To stream the raw response body, use `.with_streaming_response`, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.chat.with_streaming_response.chat(
    messages=[
        {
            "content": "Write a haiku about programming",
            "role": "user",
        }
    ],
    model="palmyra-x-004",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, parameters, or response properties, you can still use the library.

#### Undocumented endpoints

To make requests to undocumented endpoints, use `client.get`, `client.post`, and other
http verbs. Options on the client (such as retries) are respected when making these requests.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request parameters

If you want to explicitly send an extra parameter, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from writerai import Writer, DefaultHttpxClient

client = Writer(
    # Or use the `WRITER_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default, the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from writerai import Writer

with Writer() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/writer/writer-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import writerai
print(writerai.__version__)
```

## Feedback

We welcome feedback! Please open an [issue](https://www.github.com/writer/writer-python/issues) with questions, bugs, or suggestions.
