from pycoingecko import CoinGeckoAPI

def precio_cripto(*args):
    c = CoinGeckoAPI()
    arg = ''
    for item in args:
        arg += item + ','
    res = c.get_price(arg, 'usd')
    return res

if __name__ == '__main__':
    def standard():
        print(precio_cripto('bitcoin', 'litecoin', 'ethereum'))

    def test():
        c = CoinGeckoAPI()
        res = c.get_coins_list()
        print(res)
        print(c.__class__)

    import sys
    print(sys.argv[0])
    if len(sys.argv) == 1:
        standard()
    elif sys.argv[1] == 'test':
        test()
    else:
        print('Comando desconocido')
