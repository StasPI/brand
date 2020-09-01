import json
from multiprocessing import Pool, cpu_count

from aiohttp import web

from main_handler.handler import BrandScanner
from settings import config

''' функции исполнения ''' 
def launch_processors(brand, data):
    hend = BrandScanner(brand, data)
    data, brand = hend.retrieving_objects()
    ''' processing '''
    if __name__ == '__main__':
        with Pool(cpu_count()) as p:
            final_data = p.map(hend.handler, data)
        return final_data


''' обработчики запросов '''
async def handle_get(request):
    response_obj = { 
                    'brand' : 'brand',
                     'data' : 'data',
                     'ip' : 'primer'
                    }
    return web.Response(text=json.dumps(response_obj))


async def handle_post(request):
    final_data = await request.post()
    data = json.loads(final_data['data'])
    brand = json.loads(final_data['brand'])
    final_data = launch_processors(brand, data)
    return web.Response(text=json.dumps(final_data, ensure_ascii=False))


''' маршрутизация '''
app = web.Application(client_max_size=1024**8, server_port=8888) # наложено ограничение на метод post
app.router.add_post('/', handle_get)
app.router.add_post('/find', handle_post)
''' запуск '''
if __name__ == '__main__':
    web.run_app(app)
