from aiohttp import web
import json

with open('test_file.json', 'r') as read_file:
    json_data = json.load(read_file)

print(len(json_data['data']))
print(json_data['ip'])


''' запросы '''


async def handle(request):
    return web.Response(text=json.dumps(json_data, ensure_ascii=False))


# async def new_data(request):
#     try:
#         data = request.query['data']
#         print("Creating data: " , data)

#         response_obj = { 'status' : 'success' }
#         return web.Response(text=json.dumps(response_obj), status=200)

#     except Exception as e:
#         ## Bad path where data is not set
#         response_obj = { 'status' : 'failed', 'reason': str(e) }
#         ## return failed with a status code of 500 i.e. 'Server Error'
#         return web.Response(text=json.dumps(response_obj), status=500)


''' маршрутизация '''
app = web.Application()
app.router.add_get('/', handle)
# app.router.add_post('/data', new_data) #http://localhost:8080/data?data=test
''' запуск '''
if __name__ == '__main__':
    web.run_app(app)
