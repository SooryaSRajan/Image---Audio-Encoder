# Image to Audio Encoder & Decoder

This project allows you to **encode an image** into a `.wav` audio file and **decode** it back to the original image. This can be useful for research, data compression experiments, or just for fun!

---

## 🔧 **Setup Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\Scripts\activate    # On Windows
```

---

## **Install Requirements**

Run the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## **Usage**

### **Encoding an Image:**

To encode an image into a `.wav` file, run the following command:

```bash
python encode.py "path_to_image.png"
```

This will generate an audio file with the name format:

```
audio_encoded_image_<timestamp>.wav
```

---

### **Decoding the Audio File:**

To decode the `.wav` file back to an image, run:

```bash
python decode.py "path_to_audio.wav"
```

The original image will be reconstructed and saved with the name:

```
decoded_image_<timestamp>.png
```

---

## **Project Structure**

```
├── encode.py          # Script for encoding image to audio
├── decode.py          # Script for decoding audio back to image
├── requirements.txt   # List of dependencies
├── README.md          # Project documentation
└── venv/              # Virtual environment (not included in Git)
```
