from classi import Classi
import asyncio

async def main():
    async with Classi('YourID','Password') as s:
        await s.post_today_report("今日はなんの変哲もない1日だった。")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())