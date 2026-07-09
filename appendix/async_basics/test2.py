import asyncio, time
from dotenv import load_dotenv
from anthropic import AsyncAnthropic

load_dotenv()
sem = asyncio.Semaphore(1)


async def ask(client: AsyncAnthropic, prompt: str) -> str:
    async with sem:
        rsp = await client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )
        return rsp.content[0].text


async def main():  # 메소드 정의
    client = AsyncAnthropic()

    start_time = time.time()
    texts = ["파이선이란", "자바스크립트란", "고언어란"]
    result = await asyncio.gather(*[ask(client, value) for value in texts])
    elapsed_time = time.time() - start_time
    for text in result:
        print(text)
    print(f"총 소요시간{elapsed_time}")


if __name__ == "__main__":  # 메인 메소드 실행
    asyncio.run(main())
