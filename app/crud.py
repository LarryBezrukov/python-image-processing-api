from sqlalchemy.orm import Session
from . import models


def save_image_to_database(db: Session, depth: float, image_data: bytes):
    existing_image = db.query(models.Image).filter(
        models.Image.depth == depth).first()
    if existing_image is None:
        db_image = models.Image(depth=depth, data=image_data)
        db.add(db_image)
        db.commit()
        db.refresh(db_image)
        return db_image
    # Optionally, update existing_image data or simply return it
    return existing_image


def get_images_by_depth_range_from_database(db: Session, depth_min: float, depth_max: float):
    images = db.query(models.Image).filter(
        models.Image.depth >= depth_min, models.Image.depth <= depth_max).all()
    return images
