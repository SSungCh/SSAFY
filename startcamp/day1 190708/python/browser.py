import webbrowser

idols= ['bts','iu','itzy','obama']

for idol in idols:
    # String interpolation
    # 문자열 보간법 : f-string / 3.6+
    webbrowser.open(f'https://search.naver.com/search.naver?query={idol}')
