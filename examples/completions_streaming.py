# This example demonstrates writer.com completion streaming
#
# To run it locally you will need:
# - An API key from writer.com
# - Rye installed, see https://rye-up.com
#
# Run the following commands:
# $ rye sync --all-features
# $ WRITERAI_API_KEY="<your api key>" rye run python examples/completions_streaming.py

import random

from writerai import AsyncClient, BadRequestError


async def main():
    client = AsyncClient()

    print("Supported models:")
    res = await client.models.list()
    for model in res.models:
        print(model.id)

    print()
    print("Let's complete a prompt:")
    prompt = "Hi, today I want to write about"
    print(f"> {prompt}")
    try:
        stream_res = await client.completions.create(
            model=random.choice(res.models).id,
            prompt=prompt,
            stream=True,
            max_tokens=64,
        )
        async with stream_res:
            async for response in stream_res:
                print(f"< {response.value}")

    except BadRequestError as e:
        print(f"Error: {e.body}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
