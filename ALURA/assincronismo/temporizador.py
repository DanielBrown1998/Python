import asyncio
import datetime
async def temporizador(hour: int = None, minute: int = None, seconds: int = None):
    time_limit: int = 0
    
    
    if hour:
        time_limit += hour*3600

    if minute:
        time_limit += minute*60

    if seconds:
        time_limit += seconds

    if time_limit != 0:
        print(f"iniciando o tempo em: {datetime.datetime.now().strftime(format="%H:%M:%S")}")
        await asyncio.sleep(time_limit)
        print(f"FIM DO TEMPORIZADOR: {datetime.datetime.now().strftime(format="%H:%M:%S")}")
    else:
        await asyncio.sleep(1)
        print(f"Nenhum dado passado")


asyncio.run(temporizador(seconds=60))
