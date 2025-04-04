import asyncio


pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

estoque = True

async def verificar_pagamento(future, pedido):

    global estoque

    if estoque:
        print(f"Verificando pagamento do pedido {pedido['id']}...")
        await asyncio.sleep(3)
        resultado = pedido["pagamento_aprovado"]
        if not resultado:
            print(f"Pagamento não aprovado")
            future.set_result("Não Aprovado")
        else:
            print(f"Pagamento aprovado")
            future.set_result("Aprovado")
    else:
        future.set_result("Indisponível")

async def verificar_estoque(future, pedido):
    
    global estoque
    
    print(f"Verificando estoque do pedido {pedido['id']}...")
    if pedido["estoque_disponivel"]:
        print(f"Estoque disponível")
        estoque = True
        resultado = await future      
    else:
        print(f"Estoque indisponível")
        estoque = False

async def processar_pedido(future, pedido):
    print(f"Processando pedido {pedido['id']}...")
    resultado = await future
    if resultado == "Aprovado":
        print(f"Pedido {pedido['id']} processado com sucesso!")


async def main():
    list_task = []
    for pedido in pedidos:
        print("-" * 20)
        future = asyncio.Future()
        
        tarefa1 = asyncio.create_task(processar_pedido(future, pedido))
        tarefa2 = asyncio.create_task(verificar_estoque(future, pedido))
        tarefa3 = asyncio.create_task(verificar_pagamento(future, pedido))

        await tarefa1
        await tarefa2
        await tarefa3   


if __name__ == "__main__":
    asyncio.run(main())