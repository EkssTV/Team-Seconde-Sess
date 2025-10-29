class Banner:
    def __init__(self):
        pass
    def shw_banner(self):
        with open("data/assets/fonts/banner/banner.txt",'r',encoding='utf-8') as t :
            txt = t.read()
        return txt
banner = Banner()
