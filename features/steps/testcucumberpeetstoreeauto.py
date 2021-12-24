
 
from behave import *
import restapicalls

endpoint = None
request = None
response_code = None
name= None
#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
baaseurl = 'https://petstore3.swagger.io/api/v3'
@given( 'I set GET pet/10 API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = 'pet/10'
@given('I have valid petid')
def set_endpoint(context):
  global name
  name = 'petid'
@when('I send GET HTTPS request pet/10')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= 'GET',url=baseurl+'/pet/10',load=None)
@then('I receive a valid HTTPS response code 200 from pet/10 using GET')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200


endpoint = None
request = None
response_code = None

#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
baseurl = 'https://petstore3.swagger.io/api/v3'
@given( 'I set GET store/order/2 API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = 'store/order/2'
@given('I have valid orderid')
def set_endpoint(context):
  global name
  name = 'orderid'
@when('I send GET HTTPS request store/order/2')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= 'GET',url=baseurl+'/store/order/2',load=None)
@then('I receive a valid HTTPS response code 200 from store/order/2 using GET')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200


endpoint = None
request = None
response_code = None

#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
baseurl = 'https://petstore3.swagger.io/api/v3'
@given( 'I set GET user/login API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = 'user/login'
@given('I have valid userid')
def set_endpoint(context):
  global name
  name = 'userid'
@when('I send GET HTTPS request user/login')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= 'GET',url=baseurl+'/user/login',load={'username': 'addy', 'password': 'paddy'})
@then('I receive a valid HTTPS response code 200 from user/login using GET')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200


endpoint = None
request = None
response_code = None

#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
baseurl = 'https://petstore3.swagger.io/api/v3'
@given( 'I set GET user/user1 API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = 'user/user1'
@given('I have valid username')
def set_endpoint(context):
  global name
  name = 'username'
@when('I send GET HTTPS request user/user1')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= 'GET',url=baseurl+'/user/user1',load=None)
@then('I receive a valid HTTPS response code 200 from user/user1 using GET')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200


endpoint = None
request = None
response_code = None

#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
baseurl = 'https://petstore3.swagger.io/api/v3'
@given( 'I set POST pet API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = 'pet'
@given('I have valid petnumber')
def set_endpoint(context):
  global name
  name = 'petnumber'
@when('I send POST HTTPS request pet')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= 'POST',url=baseurl+'/pet',load={'id': 0, 'category': {'id': 0, 'name': 'string'}, 'name': 'doggie', 'photoUrls': ['string'], 'tags': [{'id': 0, 'name': 'string'}], 'status': 'available'})
@then('I receive a valid HTTPS response code 200 from pet using POST')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200


endpoint = None
request = None
response_code = None

#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
baseurl = 'https://petstore3.swagger.io/api/v3'
@given( 'I set POST store/order API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = 'store/order'
@given('I have valid petorder')
def set_endpoint(context):
  global name
  name = 'petorder'
@when('I send POST HTTPS request store/order')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= 'POST',url=baseurl+'/store/order',load={'id': 10, 'petId': 198772, 'quantity': 7, 'shipDate': '2021-12-24T03:36:33.067Z', 'status': 'approved', 'complete': 'true'})
@then('I receive a valid HTTPS response code 200 from store/order using POST')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200


endpoint = None
request = None
response_code = None

#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
baseurl = 'https://petstore3.swagger.io/api/v3'
@given( 'I set PUT pet API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = 'pet'
@given('I have valid existingpetid')
def set_endpoint(context):
  global name
  name = 'existingpetid'
@when('I send PUT HTTPS request pet')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= 'PUT',url=baseurl+'/pet',load={'id': 10, 'name': 'doggie', 'category': {'id': 1, 'name': 'Dogs'}, 'photoUrls': ['string'], 'tags': [{'id': 0, 'name': 'string'}], 'status': 'available'})
@then('I receive a valid HTTPS response code 200 from pet using PUT')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200


endpoint = None
request = None
response_code = None

#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
baseurl = 'https://petstore3.swagger.io/api/v3'
@given( 'I set DELETE store/order/1 API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = 'store/order/1'
@given('I have valid deleteorderid')
def set_endpoint(context):
  global name
  name = 'deleteorderid'
@when('I send DELETE HTTPS request store/order/1')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= 'DELETE',url=baseurl+'/store/order/1',load=None)
@then('I receive a valid HTTPS response code 200 from store/order/1 using DELETE')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200
