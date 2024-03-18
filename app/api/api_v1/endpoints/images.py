import base64
from fastapi import Depends, APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO
from ....utils import image_processing
from ....database import get_db
from .... import crud
from ....schemas import ImageListResponse, ImageResponse

router = APIRouter()


@router.post("/upload_csv")
async def upload_csv_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        file_content = await file.read()
        file_like = BytesIO(file_content)

        await image_processing.process_and_store_csv_image_data(db, file_like)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "CSV processing initiated"}


@router.get("/", response_model=ImageListResponse)
async def get_images(depth_min: float, depth_max: float, db: Session = Depends(get_db)):
    db_images = crud.get_images_by_depth_range_from_database(
        db, depth_min, depth_max)
    if not db_images:
        raise HTTPException(status_code=404, detail="Images not found")

    images_response = []
    for img in db_images:
        base64_encoded_data = base64.b64encode(img.data).decode('utf-8')
        images_response.append(ImageResponse(
            depth=img.depth, image_data=base64_encoded_data))

    return ImageListResponse(images=images_response)
