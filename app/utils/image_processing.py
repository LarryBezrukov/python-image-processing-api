import pandas as pd
from PIL import Image, ImageOps
import numpy as np
import io
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from typing import IO

from app.crud import save_image_to_database


async def process_csv_row(db: AsyncSession, depth: float, pixel_values: np.ndarray):
    image = Image.fromarray(pixel_values.reshape((10, 20)), 'L')

    new_width = 150
    new_height = int((new_width / image.width) * image.height)
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    image = ImageOps.colorize(image.convert("L"), black="blue", white="red")

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    save_image_to_database(db, depth, img_byte_arr)


async def process_and_store_csv_image_data(db: AsyncSession, csv_file: IO):
    df = pd.read_csv(csv_file)

    tasks = []
    for index, row in df.iterrows():
        depth = row['depth']
        pixel_values = row.drop('depth').to_numpy(dtype=np.uint8)
        task = asyncio.create_task(process_csv_row(db, depth, pixel_values))
        tasks.append(task)

    await asyncio.gather(*tasks)
