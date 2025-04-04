import asyncio

def fatorial(num: int):
    resp = 1
    for i in range(1, num+1):
        resp *= i 
    return resp

async def exc_fatorial(num: int):

    resp = fatorial(num)
    await asyncio.sleep(3)
    print(f"O fatorial de {num} e {resp}")


async def main():
    numeros = [5, 3, 7, 4, 6]
    list_tasks = []
    for item in numeros:
        print(f"iniciando o fatorial de {item}")
        task = exc_fatorial(item)
        #asyncio.create_task(task)
        list_tasks.append(task)

    await asyncio.gather(
        *list_tasks
    )


asyncio.run(main())
