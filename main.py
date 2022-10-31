import asyncio

from quiz import Quiz


async def main():
    Quiz().run()
    await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
