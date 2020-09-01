import json
import logging
import sys
from multiprocessing import Pool, cpu_count

from aiohttp import web

from main_handler.handler import BrandScanner
from settings import config


'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Main implementation modules. 
'''


def launch_processors(brand, data):
    # Launch of the main brand search module
    hend = BrandScanner(brand, data)
    data, brand = hend.retrieving_objects()
    ''' processing '''
    if __name__ == '__main__':
        with Pool(cpu_count()) as p:
            final_data = p.map(hend.handler, data)
        return final_data


'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Request handlers. 
'''


async def handle_get(request):
    response_obj = {'brand': 'brand', 'data': 'data', 'ip': 'primer'}
    return web.Response(text=json.dumps(response_obj))


async def handle_post(request):
    final_data = await request.post()
    data = json.loads(final_data['data'])
    brand = json.loads(final_data['brand'])
    final_data = launch_processors(brand, data)
    return web.Response(text=json.dumps(final_data, ensure_ascii=False))


'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
Server logging.
'''
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')
'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
Routing.
'''
app = web.Application(
    client_max_size=config['app']['client_max_size']**config['app']
    ['max_size_degree'])    # imposed a restriction on the post method
app.router.add_post('/', handle_get)
app.router.add_post('/find', handle_post)
'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
Run.
'''
if __name__ == '__main__':
    web.run_app(app, host=config['app']['host'], port=config['app']['port'])
