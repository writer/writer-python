# This example demonstrates writer.com chat streaming helper
#
# To run it locally you will need:
# - An API key from writer.com
# - Rye installed, see https://rye-up.com
#
# Run the following commands from the root of the repository:
# $ rye sync --all-features
# $ WRITERAI_API_KEY="<your api key>" rye run python examples/chat_streaming_helper.py

from writerai import Client, AsyncClient, BadRequestError


def sync_example() -> None:
    client = Client()

    print("Let's complete a prompt:")
    prompt = "Hi, today I want to write about"
    print(f"> {prompt}")
    try:
        with client.chat.stream(
            model="palmyra-x-004",
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for event in stream:
                if event.type == "content.delta":
                    print(event.delta, flush=True, end="")

    except BadRequestError as e:
        print(f"Error: {e.body}")


async def async_example() -> None:
    client = AsyncClient()

    print("Let's complete a prompt:")
    prompt = "Hi, today I want to write about"
    print(f"> {prompt}")
    try:
        async with client.chat.stream(
            model="palmyra-x-004",
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            async for event in stream:
                if event.type == "content.delta":
                    print(event.delta, flush=True, end="")

    except BadRequestError as e:
        print(f"Error: {e.body}")


if __name__ == "__main__":
    print("=== Synchronous example ===")
    sync_example()
    print()
    print()

    print("=== Asynchronous example ===")
    import asyncio

    asyncio.run(async_example())
