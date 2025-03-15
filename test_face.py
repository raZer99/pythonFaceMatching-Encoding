import face_recognition
import numpy as np

def encode_face(image_path):
    """
    Converts a face image (JPG) into a numerical encoding.
    This encoding is used for later face verification.

    :param image_path: Path to the image file (JPG)
    :return: A list of 128-dimensional face encoding if a face is found, else None
    """
    image = face_recognition.load_image_file("/Users/razer/Desktop/8 Sem/PythonFaceRec/face1.jpg")
    encodings = face_recognition.face_encodings(image)

    if encodings:
        return encodings[0].tolist()  # Convert numpy array to list
    else:
        return None  # No face found

def match_face(known_encoding, live_image_path):
    """
    Matches a stored face encoding from Firestore with a live image.

    :param known_encoding: The stored 128-dimensional encoding list
    :param live_image_path: Path to the live image taken from the app
    :return: Tuple (Boolean match result, live image encoding or None if no face detected)
    """
    live_image = face_recognition.load_image_file("/Users/razer/Desktop/8 Sem/PythonFaceRec/face2.jpg")
    live_encodings = face_recognition.face_encodings(live_image)

    if live_encodings:
        known_encoding_np = np.array(known_encoding)
        live_encoding_np = np.array(live_encodings[0])

        matches = face_recognition.compare_faces([known_encoding_np], live_encoding_np)

        return matches[0], live_encoding_np.tolist()  # Return match result and encoding
    else:
        return False, None  # No face found in live image

# ==== TESTING THE FUNCTIONS ====
if __name__ == "__main__":
    # Step 1: Encode a face and store encoding
    registered_encoding = encode_face("face1.jpg")

    if registered_encoding:
        print("Face encoded successfully. Encoding:")
        print(registered_encoding[:5])  # Print first 5 values to check

        # Step 2: Match with another image
        match_result, live_encoding = match_face(registered_encoding, "face2.jpg")

        if live_encoding:
            print("Live image encoded successfully. Matching result:", match_result)
        else:
            print("No face detected in live image.")
    else:
        print("No face detected in the registration image.")
