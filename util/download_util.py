import os
import ssl

import aiohttp
import asyncio
from tqdm.asyncio import tqdm
import certifi

_NO_OF_CHUNKS = int(os.getenv("NO_OF_CHUNKS", 10))
_CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1024))


async def _download_file(session, url, filename):
    chunk_size = _NO_OF_CHUNKS * _CHUNK_SIZE
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    async with session.get(url, ssl_context=ssl_context) as response:
        total_size = int(response.headers.get("content-length", 0))

        with open(filename, "wb") as f, tqdm(
                total=total_size,
                unit="B",
                unit_scale=True,
                desc=filename,
                position=0,
        ) as pbar:
            async for chunk in response.content.iter_chunked(chunk_size):
                f.write(chunk)
                pbar.update(len(chunk))


async def download_files(urls, filenames):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url, filename in zip(urls, filenames):
            task = asyncio.create_task(_download_file(session, url, filename))
            tasks.append(task)

        await asyncio.gather(*tasks)


__all__ = ["download_files"]

if __name__ == "__main__":
    urls = ["https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHAMCS/stata/ed2021-stata.zip"]
    filenames = ["ed2021-stata.zip"]
    asyncio.run(download_files(urls, filenames))
