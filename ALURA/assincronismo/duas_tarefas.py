import asyncio

async def corroutine(num: int):
    print(f"iniciando tarefa {num}")
    await asyncio.sleep(1)
    print(f"finalizando tarefa {num}")

async def main():
    await asyncio.gather(
        corroutine(1),
        corroutine(2)
    )

asyncio.run(main())
