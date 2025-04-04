# Streaming Helpers

Writer supports streaming responses when interacting with the [Chat Completion API](#chat-completion-api).

## Chat Completion API

The SDK provides a `client.chat.stream()` method that wraps the `client.chat.chat(stream=True)` stream providing a more granular event API and automatic accumulation of each delta.

Unlike `client.chat.chat(stream=True)`, the `stream()` method requires usage within a context manager to prevent accidental leak of the response:

```py
from writerai import AsyncWriter

client = AsyncWriter()

async with client.chat.stream(
    model='palmyra-x-004',
    messages=[...],
) as stream:
    async for event in stream:
        if event.type == 'content.delta':
            print(event.content, flush=True, end='')
```

When the context manager is entered, a `ChatCompletionStream` / `AsyncChatCompletionStream` instance is returned which, like `.create(stream=True)` is an iterator in the sync client and an async iterator in the async client. The full list of events that are yielded by the iterator are outlined [below](#chat-completions-events).

When the context manager exits, the response will be closed, however the `stream` instance is still available outside
the context manager.

### Text Generation Events

These events allow you to track the progress of the chat completion generation, access partial results, and handle different aspects of the stream separately.

Below is a list of the different event types you may encounter:

#### ChunkEvent

Emitted for every chunk received from the API.

- `type`: `"chunk"`
- `chunk`: The raw `ChatCompletionChunk` object received from the API
- `snapshot`: The current accumulated state of the chat completion

#### ContentDeltaEvent

Emitted for every chunk containing new content.

- `type`: `"content.delta"`
- `delta`: The new content string received in this chunk
- `snapshot`: The accumulated content so far
- `parsed`: The partially parsed content (if applicable)

#### ContentDoneEvent

Emitted when the content generation is complete. May be fired multiple times if there are multiple choices.

- `type`: `"content.done"`
- `content`: The full generated content
- `parsed`: The fully parsed content (if applicable)

#### RefusalDeltaEvent

Emitted when a chunk contains part of a content refusal.

- `type`: `"refusal.delta"`
- `delta`: The new refusal content string received in this chunk
- `snapshot`: The accumulated refusal content string so far

#### RefusalDoneEvent

Emitted when the refusal content is complete.

- `type`: `"refusal.done"`
- `refusal`: The full refusal content

#### LogprobsContentDeltaEvent

Emitted when a chunk contains new content log probabilities.

- `type`: `"logprobs.content.delta"`
- `content`: A list of the new log probabilities received in this chunk
- `snapshot`: A list of the accumulated log probabilities so far

#### LogprobsContentDoneEvent

Emitted when all content log probabilities have been received.

- `type`: `"logprobs.content.done"`
- `content`: The full list of token log probabilities for the content

#### LogprobsRefusalDeltaEvent

Emitted when a chunk contains new refusal log probabilities.

- `type`: `"logprobs.refusal.delta"`
- `refusal`: A list of the new log probabilities received in this chunk
- `snapshot`: A list of the accumulated log probabilities so far

#### LogprobsRefusalDoneEvent

Emitted when all refusal log probabilities have been received.

- `type`: `"logprobs.refusal.done"`
- `refusal`: The full list of token log probabilities for the refusal

### Helper methods

A handful of helper methods are provided on the stream class for additional convenience,

**`.get_final_completion()`**

Returns the accumulated `ParsedChatCompletion` object

```py
async with client.chat.stream(...) as stream:
    ...

completion = await stream.get_final_completion()
print(completion.choices[0].message)
```

**`.until_done()`**

If you want to wait for the stream to complete, you can use the `.until_done()` method.

```py
async with client.chat.stream(...) as stream:
    await stream.until_done()
    # stream is now finished
```
