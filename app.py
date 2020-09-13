import asyncio
import logging
from multiprocessing import Pool, cpu_count
from sys import getsizeof

from aiohttp import web

import ujson
from config.settings import config
from main_handler.handler import BrandScanner


'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    App
An asynchronous API implementation based on (aiohttp). With logging.
    Methods:
launch_processors(brand, data)
handle_get(request)
handle_post(request)
'''


async def adding_headers(final_data):
    '''
    Adds headers to the response, as the first element in the array. 
    
    It makes sense to track on the client. Also, when changing the main_handler 
    module (handler), it is necessary to change this function.
    '''

    headers_row = [
        'seller', 'name_of_product', 'id', 'exact_match_brand',
        'probable_match_brand', 'status'
    ]
    final_data.insert(0, headers_row)
    return final_data


async def launch_processors(brand, data):
    '''Launch of the main brand search module'''

    hend = BrandScanner(brand, data)
    data, brand = hend.retrieving_objects()
    # multiprocessing
    if __name__ == '__main__':
        with Pool(cpu_count()) as p:
            final_data = p.map(hend.handler, data)
        return final_data


async def handle_get(request):
    '''
    Welcome Get Request. In response, it provides brief information 
    on the required data.
    '''

    brand_info = 'An array of the form [["brand name", "id"], [...]] is passed. Order is important!'
    data_info = 'An array of the form [["name of the organization", "name of product", "id"], [...]] is passed. Order is important!'
    token = 'Login token.'
    response_obj = {'brand': brand_info, 'data': data_info, 'token': token}
    return web.Response(text=ujson.dumps(response_obj))


async def handle_post(request):
    '''
    Main Post request.
    Receives data, implements json.loads(obj).
    Call a function launch_processors().
    Returns json.dumps(obj).
    '''

    final_data = await request.post()
    data = ujson.loads(final_data['data'])
    brand = ujson.loads(final_data['brand'])
    final_data = await launch_processors(brand, data)
    final_data = await adding_headers(final_data)
    return web.Response(text=ujson.dumps(final_data, ensure_ascii=False))


'''API logging.'''

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')


def run_server():
    '''Run server and Routing'''
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = web.Application(client_max_size=config['app']['client_max_size']**
                          config['app']['max_size_degree'])

    # start routing ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    app.router.add_get('/', handle_get)
    app.router.add_post('/find', handle_post)
    # finish routing +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner,
                       host=config['app']['host'],
                       port=config['app']['port'],
                       shutdown_timeout=config['app']['shutdown_timeout'])
    loop.run_until_complete(site.start())
    loop.run_forever()


if __name__ == '__main__':
    run_server()
