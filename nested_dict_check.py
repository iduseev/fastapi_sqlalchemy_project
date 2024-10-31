import traceback
from pprint import pprint

period = 'year_1'
user = {
    'currency': 'RUB'
}

tariff = {
    'cost': {
        'year_1': {
            'RUB': 50000
        }
    }
}

if __name__ == '__main__':

    try:
        cost_1 = tariff['cost'][period][user['currency']]
        cost_1_1 = tariff.get('cost', {})
        cost_1_2 = cost_1_1.get(f'{period}', {})
        cost_1_3 = cost_1_2.get(f"{user['currency']}", None)
        pprint(f'cost_1: {cost_1}')
        pprint(f'cost_1_1: {cost_1_1}')
        pprint(f'cost_1_2: {cost_1_2}')
        pprint(f'cost_1_3: {cost_1_3}')
    except KeyError as e:
        tb = traceback.format_exc()
        pprint(f'Exception: {e}, traceback: {tb}')
