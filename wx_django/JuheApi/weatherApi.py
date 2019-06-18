import json
import requests


def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    print("in")
    key = '862a3a40af245f7e21c196474c4c3532'
    api = 'http://apis.juhe.cn/simpleWeather/query'
    params = 'city=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    # print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    # print(json_data)

    result = json_data.get('result')
    realtime = result.get('realtime')
    response = dict()

    response['temperature'] = realtime.get('temperature')
    # print(response['temperature'])
    response['humidity'] = realtime.get('humidity')
    # print(response['humidity'])

    response['info'] = realtime.get('info')
    response['wid'] = realtime.get('wid')
    response['direct'] = realtime.get('direct')
    response['power'] = realtime.get('power')
    response['aqi'] = realtime.get('aqi')

    # future = result.get('future')
    # print(future)
    # print(future[0].get('date'))

    return response


if __name__ == '__main__':
    data = weather('合肥')