import requests

def get_api(url, load,headers=None,auth=None):
    response_code = -1
    output = ''
    try:
        response_get = requests.get(url, params = load, timeout = 10, verify = True,headers=headers,auth=auth)
        response_code = response_get.status_code
        output = response_get.json()
    except Exception as error:
        print(error)
        return [response_code]
    print(response_code)
    return [response_code,output]

def post_api(url, pload,headers=None,auth=None):
    response_code = -1
    output = ''
    try:
        response_post = requests.post(url, data = pload, timeout = 10, verify = True,headers=headers,auth=auth)
        response_code = response_post.status_code
        output = response_post.json()
    except Exception as error:
        print(error)
        return [response_code]
    print(response_code)
    return [response_code,output]

def delete_api(url, pload,headers=None,auth=None):
    response_code = -1
    output = ''
    try:
        response_delete = requests.delete(url, data = pload, timeout = 10, verify = True,headers=headers,auth=auth)
        response_code = response_delete.status_code
        output = response_delete.text
    except Exception as error:
        print(error)
        return [response_code]
    print(response_code)
    return [response_code,output]

def put_api(url, params,headers=None,auth=None):
    response_code = -1
    output = ''
    try:
        response_put = requests.put(url, data = params, timeout = 10, verify = True,headers=headers,auth=auth)
        response_code = response_put.status_code
        output = response_put.text
    except Exception as error:
        print(error)
        return [response_code]
    print(response_code)
    return [response_code,output]
    
def api_call(method,url,load,headers=None,auth=None):
    method = method.lower()
    if method == 'get':
        return(get_api(url,load,headers,auth))
    
    if method == 'post':
        return(post_api(url,load,headers,auth))
    
    if method == 'put':
        return(put_api(url,load,headers,auth))
    
    if method == 'delete':
        return(delete_api(url,pload=load,headers=headers,auth=auth))


        
        
    
    