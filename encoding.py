import face_recognition
import numpy as np
import json
import os

ENCODING_FILE = "face_encoding.json"  # File to store multiple encodings

def faceRegisterEncoding(image_path, name):
    """
    Registers a face by encoding it and saving the encoding to a file with a name.
    """
    try:
        image = face_recognition.load_image_file("/Users/razer/Desktop/8 Sem/PythonFaceRec/face1.jpg")
        encodings = face_recognition.face_encodings(image)

        if encodings:
            encoding_list = encodings[0].tolist()  # Convert numpy array to list

            # Load existing encodings if the file exists and is not empty
            if os.path.exists(ENCODING_FILE) and os.path.getsize(ENCODING_FILE) > 0:
                try:
                    with open(ENCODING_FILE, "r") as file:
                        stored_encodings = json.load(file)
                except json.JSONDecodeError:
                    print("[ERROR] JSON file is corrupted. Resetting...")
                    stored_encodings = {}
            else:
                stored_encodings = {}

            # Store new encoding with a name
            stored_encodings[name] = encoding_list

            # Save updated encodings to file
            with open(ENCODING_FILE, "w") as file:
                json.dump(stored_encodings, file, indent=4)  # Pretty format for debugging

            print(f"✅ Face encoding for '{name}' saved.")
        else:
            print("❌ No face detected. Try a different image.")

    except Exception as e:
        print(f"[ERROR] faceRegisterEncoding failed: {e}")

def faceMatching(live_image_path):
    """
    Matches a live image with stored face encodings.
    """
    if not os.path.exists(ENCODING_FILE) or os.path.getsize(ENCODING_FILE) == 0:
        print("❌ No registered faces found. Please register first.")
        return

    try:
        # Load stored encodings
        with open(ENCODING_FILE, "r") as file:
            stored_encodings = json.load(file)

        # Load live image and encode it
        live_image = face_recognition.load_image_file(live_image_path)
        live_encodings = face_recognition.face_encodings(live_image)

        if live_encodings:
            live_encoding_np = np.array(live_encodings[0])

            for name, stored_encoding in stored_encodings.items():
                stored_encoding_np = np.array(stored_encoding)

                # Compare stored encoding with live image encoding
                matches = face_recognition.compare_faces([stored_encoding_np], live_encoding_np)

                if matches[0]:
                    print(f"✅ Face Matched! Name: {name}")
                    return

            print("❌ Face Not Matched.")
        else:
            print("❌ No face detected in the live image.")

    except json.JSONDecodeError:
        print("[ERROR] JSON decoding failed. The file might be empty or corrupted.")
    except Exception as e:
        print(f"[ERROR] faceMatching failed: {e}")

# ==== RUN THE FUNCTIONS ====
if __name__ == "__main__":
    # Step 1: Register two faces
    faceRegisterEncoding("face1.jpg", "Person1")  # Store first encoding
    faceRegisterEncoding("face2.jpg", "Person2")  # Store second encoding

    # Debugging: Check what got stored in JSON
    with open(ENCODING_FILE, "r") as file:
        print("\n🔍 Stored Encodings:", json.load(file))

    # Step 2: Match face with another image
    faceMatching("/Users/razer/Desktop/8 Sem/PythonFaceRec/face2.jpg")  # Test with a new image
