"""the script downloads images and uses the asyncio"""

import asyncio
import aiohttp
import aiofiles
from bs4 import BeautifulSoup


async def download_image(url: str, path_: str):
    """
    Download image
    :param url:
    :param path_:
    """

    image_url = None

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image_url = BeautifulSoup(await response.text(), 'html.parser').find(
                    name='img', attrs={'id': 'ii'})['src']

        async with session.get(image_url) as response:
            if response.status == 200:
                async with aiofiles.open(path_, 'wb') as file:
                    print('Start downloading', url)
                    await file.write(await response.read())
                    print(url, 'saved')


async def main(count: int = 5, path: str = 'images'):
    """
    Download images from https://archillect.com
    :param count: count of pictures
    :param path: path to download folder
    """

    site_url = 'https://archillect.com'

    await asyncio.gather(
        *[download_image(f'{site_url}/{i + 1}', f'{path}/{i + 1}.jpg') for i in range(count)]
    )


if __name__ == '__main__':
    asyncio.run(main(30))
