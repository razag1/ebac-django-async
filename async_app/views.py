
import asyncio
import time
import httpx

from django.http import HttpResponse


async def http_call_async(request):
    inicio = time.perf_counter()

    # Contador assincrono de 1 ate 5
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    # Requisicao HTTP assincrona
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                "https://httpbin.org/get"
            )

            response.raise_for_status()
            print(response)

    except httpx.HTTPError as erro:
        return HttpResponse(
            f"Erro na requisicao HTTP: {erro}",
            status=502
        )

    tempo_total = time.perf_counter() - inicio

    return HttpResponse(
        f"Contagem concluida: 1, 2, 3, 4, 5\n"
        f"Status HTTP: {response.status_code}\n"
        f"Tempo total: {tempo_total:.2f} segundos",
        content_type="text/plain; charset=utf-8"
    )
