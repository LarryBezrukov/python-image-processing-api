# python-image-processing-api

The Image Processing API provides a powerful, easy-to-use interface for uploading, processing, and retrieving images based on depth information. It allows clients to upload images or CSV files containing image data, which are then processed, resized, and stored with custom color mapping. Clients can retrieve these processed images by specifying a depth range, making it ideal for applications requiring depth-based image analysis and visualization.

## Features

* CSV Upload: Process and store images from a CSV file, with each row representing an image's pixel data and depth information.
* Image Retrieval: Fetch images within a specified depth range, with support for dynamic resizing and custom color mapping.
* Base64 Encoding: Images are encoded in base64 format for easy transmission over the web.

## Endpoints

### Upload CSV File

* **URL**: `/upload_csv/`
* **Method**: `POST`
* **Body**: `multipart/form-data` with a key of `file` associated with the CSV file.
* **Description**: Processes a CSV file containing images represented as pixel values along with their depth. Each processed image is stored in the database.

### Get Images

* **URL**: `/`
* **Method**: `GET`
* **Query Parameters**:
`depth_min`: The minimum depth value for the images to retrieve.
`depth_max`: The maximum depth value for the images to retrieve.
* **Description**: Retrieves images within the specified depth range. Images are returned as a list of base64-encoded strings.

## How to Run the Project

### Prerequisites

* Python 3.8+
* pip
* A virtual environment (recommended)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/LarryBezrukov/python-image-processing-api.git
cd python-image-processing-api
```

2. **Create and activate a virtual environment**
  * For Unix or MacOS:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
  * For Windows:
  ```bash
  python -m venv env
  .\env\Scripts\activate
  ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the FastAPI server
   ```bash
   uvicorn app.main:app --reload
   ```
   The --reload flag enables hot reloading during development.
2. Access the API
   The API will be available at `http://localhost:8000`. You can visit `http://localhost:8000/docs` for the interactive API documentation provided by FastAPI, where you can test the API endpoints directly from your browser.

### Docker (Optional)

If you prefer running the application in a Docker container:

1. Build the Docker image
   ```bash
   docker build -t image-processing-api .
   ```
2. Run the container
   ```bash
   docker run -p 8000:8000 image-processing-api
   ```
   Adjust the port mapping if necessary. The application will be accessible at `http://localhost:8000`.
