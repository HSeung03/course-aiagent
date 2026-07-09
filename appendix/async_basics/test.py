import asyncio
import time
from dotenv import load_dotenv
from anthropic import AsyncAnthropic

load_dotenv()

MODEL = "claude-haiku-4-5-20251001"


async def ask(client: AsyncAnthropic, question: str) -> str:
    response = await client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text


async def main():
    start_time = time.time()
    client = AsyncAnthropic()
    text = ["파이썬이 뭐야", "자바스크립트가 뭐야", "Go언어가 뭐야"]
    result = await asyncio.gather(*[ask(client, value) for value in text])

    elapsed_time = time.time() - start_time
    for text in result:
        print(text)
        print("*" * 50)
    print(f"총 소요시간{elapsed_time}")


if __name__ == "__main__":
    asyncio.run(main())
