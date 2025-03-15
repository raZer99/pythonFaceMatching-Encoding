# Python Face Matching & Encoding

A Python-based face recognition system using `face_recognition`, `dlib`, and `numpy` to register and match faces.

## 🚀 Features

- Encode faces from images and store them.
- Match live images with stored encodings.
- Uses `face_recognition` library for facial recognition.

## 📦 Requirements

Make sure you have the following installed:

- Python 3.x
- Required dependencies:
  ```sh
  pip install face_recognition dlib numpy Pillow
  ```

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/pythonFaceMatching-Encoding.git
cd pythonFaceMatching-Encoding
```

### 2️⃣ Install Dependencies

```sh
pip install -r requirements.txt  # If a requirements file is added
```

Or manually install:

```sh
pip install face_recognition dlib numpy Pillow
```

### 3️⃣ Run Face Encoding (`encoding.py`)

```sh
python encoding.py
```

This will:

- Load an image.
- Encode the face.
- Save the encoding in `face_encoding.json`.

### 4️⃣ Test Face Matching (`test_face.py`)

```sh
python test_face.py
```

This will:

- Load a test image.
- Compare it against stored encodings.
- Print the matching result.

## 📂 Project Structure

```
pythonFaceMatching-Encoding/
│── encoding.py  # Face registration
│── test_face.py  # Face matching
│── face_encoding.json  # Stored face encodings
│── README.md  # Project documentation
```

## 🛠️ Troubleshooting

- If `face_recognition` fails to install, ensure `dlib` is correctly installed.
- Make sure your image path is correct and contains faces.

## 📜 License

This project is licensed under the **MIT License**.

