from django.http import HttpResponse
import json
from subprocess import call


def dict_fetch_all(cursor):
    desc = cursor.description
    return [[zip([col[0] for col in desc], row)] for row in cursor.fetchall()]

def flush_redis():
    call(["redis-cli", 'FLUSHDB'])

def json_response(f):
    def wrapped(request, *args, **kwargs):
        response = f(request, *args, **kwargs)
        try:
            if issubclass(response, HttpResponse):
                return response(mimetype="application/json")
        except TypeError:
            pass
        jr = json.dumps(response)
        return HttpResponse(jr, mimetype="application/json")
    return wrapped

def is_mobile_browser(user_agent):
    '''Device detection, returns True for mobile devices'''

    mobile_user_agent_list = [
        'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
        'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
        'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
        'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
        'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
        'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
        'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
        'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
        'wapr','webc','winw','winw','xda','xda-'
        ]

    mobile_user_agent_hist_list = ['SymbianOS', 'Opera Mini', 'iPhone']

    if user_agent.lower()[0:4] in mobile_user_agent_list:
        return True

    for hint in mobile_user_agent_hist_list:
        if user_agent.find(hint) > 0:
            return True

    return False