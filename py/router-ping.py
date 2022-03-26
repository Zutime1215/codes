import requests

ip = '172.16.12.66'

base_url = "http://" + ip
url2 = base_url + "/cgi?2"
url1 = base_url + "/cgi?1"
url7 = base_url + "/cgi?7"


link = 'techshopbd.com'

cgi2 = f'[IPPING_DIAG#0,0,0,0,0,0#0,0,0,0,0,0]0,6\r\ndataBlockSize=64\r\ntimeout=1\r\nnumberOfRepetitions=4\r\nhost={link}\r\nX_TP_ConnName=ewan_pppoe\r\ndiagnosticsState=Requested\r\n'
cgi1 = '[IPPING_DIAG#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n'
cgi7 = '[ACT_OP_IPPING#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n'


def get_header(data):
    return {
        'Host': ip,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'text/plain',
        'Content-Length': f'{len(data)}',
        'Origin': 'http://'+ip,
        'Referer': 'http://'+ip+'/mainFrame.htm'
    }


cookie = { 'Authorization' : 'Basic YWRtaW46YWRtaW4='}

s = requests.session()
response = s.post(url2, headers=get_header(cgi2), cookies=cookie, data=cgi2)
response = s.post(url1, headers=get_header(cgi1), cookies=cookie, data=cgi1); print(response.text)
response = s.post(url7, headers=get_header(cgi7), cookies=cookie, data=cgi7); print(response.text)
response = s.post(url1, headers=get_header(cgi1), cookies=cookie, data=cgi1); print(response.text)