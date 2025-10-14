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

    # list of some theater articles: [19370, 19374,19376,19398,19399,19403,19415,19447,19448,19453,19456,19457,19509,19523,19533,19594,19770,19830,19869,19893,19922,20015,20016,20073,20075,20100,20153,20156,20158,20266,20267,20353,20378,20409,20472,20489,20491,20496,20506,20525,20537,20538,20545,20560,20575,20576,20588,20599,20612,20639,20661,20669,20671,20691,20702,20709,20711,20718,20723,20732,20733]

    for i in np.arange(start=20732, stop=29350, step = 1):
        page = await browser.get(f'https://www.varsity.co.uk/theatre/{i}')
        
        is_fourofour = await page.select_all('div[class="grid_8 error404"]', timeout=0.1, include_frames=False) # naive check for 404 error

        if len(is_fourofour) == 0:
            #print(len(is_fourofour))
            url = await page.select_all('meta[name="twitter:url"]', timeout=0.1, include_frames=False) # naive returns base url to see if it's a theatre article
            try:    
                if 'theatre' in str(url[0]): # simple check to see if theatre is in the url. hoping i miss nothing lol
                    print(f'theatre article found: {i}')

                    index.append(i) 

                    stars = await page.select_all('i[class="fa fa-star star"]', timeout=1, include_frames=False)
                    half_stars = await page.select_all('i[class="fa fa-star-half-o star"]', timeout=1, include_frames=False)
                    empty_stars = await page.select_all('i[class="fa fa-star-o star"]', timeout=1, include_frames=False)

                    star_flt = len(stars)+0.5*len(half_stars)
                    sum_stars = len(stars)+len(half_stars)+len(empty_stars)

                    pos_stars.append(star_flt)
                    check.append(sum_stars)
            except:
                print(f'error in theatre article {i}')
        else:
            #print(f'404 error at article {i}')
            pass

    for i in range(len(index)):
        print(f"{index[i]} : ({pos_stars[i]} / {check[i]})")

    np.asarray(pos_stars).tofile('stars.csv', sep = ',')
    np.asarray(index).tofile('index.csv', sep = ',')
    np.asarray(check).tofile('check.csv', sep = ',')


    

    print(url)
    if 'theatre' in str(url[0]):
        print('theatre')
    print(star_flt)
    print(sum_stars)

    

    # hm. i'm pretty astounded at this framework's ability to do what it does, which... scares me. Because I don't know 
    # literally anything about websec, and I just couldn't even begin to imagine what sort of things I might be overlooking.
    # I definitely will be careful with this in terms of accounts that matter to more people than me.
    # also, i'm fucking around with coroutines. How do I always end up doing this?






#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




if __name__ == "__main__":
    print('go')
    asyncio.run(main())


