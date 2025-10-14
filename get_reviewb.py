'''
Agenda 2025. A fun little experiment with nodriver, in an attempt to get around a few anti-bot things. 
'''

import nodriver as uc
import numpy as np
import asyncio
from time import sleep


class Agenda2025:
    
    def __init__(self):

        pass

    #page = await browser.get(f'https://www.varsity.co.uk/theatre/28701') # test movember article

async def main():
    pos_stars = []
    check = []
    index = []


    browser = await uc.start()#headless=True)
    
    #for i in np.arange(start=28501, stop=29350, step = 1):
    # get all non-404 pages
    non_404 = []
    theatre_pages = []

    for i in np.arange(start = 4, stop=29350, step = 1):

        page = await browser.get(f'https://www.varsity.co.uk/theatre/{i}')

        is_fourofour = await page.select_all('div[class="grid_8 error404"]', timeout=0.1, include_frames=False)

        if len(is_fourofour) == 0:
            url = await page.select_all('meta[name="twitter:url"]', timeout=0.1, include_frames=False)
            if 'theatre' in str(url[0]):
                theatre_pages.append(i)
                print(i)
        

    
    np.asarray(non_404).tofile('non_404.csv', sep = ',')
    np.asarray(theatre_pages).tofile('theatre_pages.csv', sep = ',')




    







#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




if __name__ == "__main__":
    print('go')
    asyncio.run(main())


