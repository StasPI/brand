import json
import logging
import sys
from multiprocessing import Pool, cpu_count

from aiohttp import web

from main_handler.handler import BrandScanner
from settings import config


'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    App
An asynchronous API implementation based on (aiohttp). With logging.
    Methods:
launch_processors(brand, data)
handle_get(request)
handle_post(request)
'''


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
    ip_info = 'Optional parameters.'
    response_obj = {'brand': brand_info,
                    'data': data_info,
                    'ip': ip_info}
    return web.Response(text=json.dumps(response_obj))
    # return web.Response(text=response_obj)


async def handle_post(request):
    '''
    Main Post request.
    Receives data, implements json.loads(obj).
    Call a function launch_processors().
    Returns json.dumps(obj).
    '''

    final_data = await request.post()
    data = json.loads(final_data['data'])
    brand = json.loads(final_data['brand'])
    final_data = await launch_processors(brand, data)
    return web.Response(text=json.dumps(final_data, ensure_ascii=False))


'''API logging.'''

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')

'''Routing.'''

app = web.Application(
    client_max_size=config['app']['client_max_size']**config['app']
    ['max_size_degree'])    # imposed a restriction on the post method
app.router.add_get('/', handle_get)
app.router.add_post('/find', handle_post)

'''Run.'''

if __name__ == '__main__':
    web.run_app(app, host=config['app']['host'], port=config['app']['port'])