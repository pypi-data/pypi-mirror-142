import re
from urllib.parse import urlparse, unquote

clash_ss_template = '   - {{name: "{}", server: {}, port: {}, type: ss, cipher: {}, password: {}}}'
surge_ss_template = '{} = ss, {}, {}, encrypt-method={}, password={}'
class Ss(object):
    def __init__(self, parse_result):
        self.parse_result = parse_result

    def do(self, type):
        [credential, host, port] = re.split('@|:', self.parse_result.netloc)
        [encryption, password] = base64_decode(credential).decode().split(':')
        if type == 'clash':
            print(clash_ss_template.format(unquote(self.parse_result.fragment), host, port, encryption, password))
        elif type == 'surge':
            print(surge_ss_template.format(unquote(self.parse_result.fragment), host, port, encryption, password))
        else:
            return None



clash_vmess_template = '   - {{name: {}, server: {}, port: {}, type: vmess, uuid: {}, alterId: {}, cipher: auto, tls: false, network: {}, ws-path: {}, ws-headers: {{Host: {}}}}}'
surge_vmess_template = '# {} = vmess, {}, {}, username={}, tls=false, ws=true, ws-path={}, sni={}, ws-headers=Host:{}'

class Vmess(object):
    def __init__(self, parse_result):
        self.parse_result = parse_result

    def do(self, type):
        import json
        import base64
        data = json.loads(base64_decode(self.parse_result.netloc))
        if type == 'clash':
            print(clash_vmess_template.format(data['ps'], data['add'], data['port'], data['id'], data['aid'], data['net'], data['path'], data['add']))
        elif type == 'surge':
            print(surge_vmess_template.format(data['ps'], data['add'], data['port'], data['id'], data['path'], data['add'], data['add']))
        else:
            return None


def base64_decode(s):
    import base64
    import binascii
    """Add missing padding to string and return the decoded base64 string."""
    s = str(s).strip()
    try:
        return base64.b64decode(s)
    except binascii.Error:
        padding = len(s) % 4
        if padding == 1:
            print("Invalid base64 string: {}".format(s))
            return ''
        elif padding == 2:
            s += '=='
        elif padding == 3:
            s += '='
        return base64.b64decode(s)

def dispatch(stdin, type):
    for line in stdin:
        result = urlparse(line)
        if result.scheme == 'ss':
            Ss(result).do(type)
        elif result.scheme == 'vmess':
            Vmess(result).do(type)
        else:
            pass


def do(args):
    import sys
    # match args.type:
    #     case 'clash':
    #         dispatch(sys.stdin, 'clash')
    #     case 'surge':
    #         dispatch(sys.stdin, 'surge')
    if args.type == 'clash':
        dispatch(sys.stdin, 'clash')
    elif args.type == 'surge':
        dispatch(sys.stdin, 'surge')
    else:
        print('Unknown type: {}'.format(args.type))


def run():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, default='clash')

    args = parser.parse_args()
    do(args)
