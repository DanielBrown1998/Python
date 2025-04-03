from unittest import result
import requests
import asyncio

async def corroutine(num: int):
    print(f"Realizando a chamada {num}")
    await asyncio.sleep(2)
    print(f"Tarefa {num} concluida")


async def main():
    tarefa_1: asyncio.Task = asyncio.gather(corroutine(1), corroutine(2))
    #tarefa_2: asyncio.Task = asyncio.create_task(corroutine(2))
    await tarefa_1
    #await tarefa_2


#asyncio.run(main())


async def corroutine_one(future: asyncio.Future):
    print(f"iniciando tarefa 1")
    await asyncio.sleep(1)
    future.set_result("Resultado da Tarefa 1")
    print("tarefa 1 finalizada")


async def corroutine_two(future):
    print("Iniciando a tarefa 2")
    result = await future
    print(f"Tarefa 2 finalizada com o resultado {result}")


async def main_two():
    future = asyncio.Future()
    await asyncio.gather(
        corroutine_one(future),
        corroutine_two(future)
    )

asyncio.run(main_two())
