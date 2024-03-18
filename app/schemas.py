from pydantic import BaseModel
from typing import List


class ImageBase(BaseModel):
    depth: float


class ImageResponse(ImageBase):
    image_data: str  # base64-encoded image data


class ImageListResponse(BaseModel):
    images: List[ImageResponse]
