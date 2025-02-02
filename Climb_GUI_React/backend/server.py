from io import BytesIO

import cv2 as cv
import numpy as np
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from path_calc import shortestPath
from PIL import Image

app = Flask(__name__)
CORS(app)

# Define color ranges for detection
color_ranges = {
    "red": [(100, 0, 0), (255, 50, 50)],
    "green": [(0, 100, 0), (90, 255, 100)],
    "blue": [(0, 0, 100), (80, 80, 255)],
    "orange": [(255, 100, 0), (255, 200, 100)],
    "purple": [(200, 100, 200), (250, 165, 250)],
    "yellow": [(200, 200, 0), (255, 255, 100)],
    "black": [(0, 0, 0), (50, 50, 20)],
}


# Map colors to RGB tuples
def strToColor(color):
    mapping = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "orange": (255, 128, 0),
        "yellow": (255, 255, 0),
        "purple": (255, 0, 255),
        "black": (0, 0, 0),
    }
    return mapping.get(color.lower(), (255, 255, 255))


# Process a single color mask and extract bounding boxes
def process_color(img_rgb, chosenColor):
    lower, upper = color_ranges[chosenColor]
    mask = cv.inRange(img_rgb, np.array(lower), np.array(upper))
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    boxes = []
    for contour in contours:
        x, y, z, a = cv.boundingRect(contour)
        boxes.append(((x, y), (x + z, y + a)))
    return boxes


# Detect and mark paths for selected colors
def get_colors(image, colors):
    bounding_boxes = {color: [] for color in color_ranges.keys()}

    # Normalize the colors list
    if colors == ["all"]:
        colors = list(color_ranges.keys())
    else:
        colors = [color.lower() for color in colors]

    # Convert image to OpenCV format
    img = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_marked = img.copy()

    paths = []

    # Process each selected color
    for chosenColor in colors:
        if chosenColor in color_ranges:
            bounding_boxes[chosenColor] = process_color(img_rgb, chosenColor)

            if bounding_boxes[chosenColor]:
                dist = 150
                path = shortestPath(
                    bounding_boxes[chosenColor][0],
                    bounding_boxes[chosenColor][-1],
                    bounding_boxes[chosenColor],
                    dist,
                )
                retries = 0
                while path is None and retries < 5:
                    dist += 50
                    path = shortestPath(
                        bounding_boxes[chosenColor][0],
                        bounding_boxes[chosenColor][-1],
                        bounding_boxes[chosenColor],
                        dist,
                    )
                    retries += 1

                if path:
                    paths.append((chosenColor, path))

    # Draw bounding boxes and paths
    for color, path in paths:
        for box in bounding_boxes[color]:
            (x1, y1), (x2, y2) = box
            cv.rectangle(img_marked, (x1, y1), (x2, y2), strToColor(color), 2)

        for i in range(len(path) - 1):
            start = path[i][1]  # Start point
            end = path[i + 1][0]  # End point
            cv.line(img_marked, start, end, strToColor(color), 2)

    # Convert back to PIL format
    result_image = Image.fromarray(cv.cvtColor(img_marked, cv.COLOR_BGR2RGB))
    return result_image

@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({"success": True}), 200

@app.route("/api/getPath/<colors>", methods=["POST"])
def alter_image(colors):
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    try:
        # Read the uploaded file into a Pillow Image
        image = Image.open(file).convert("RGB")  # Ensure RGB mode

        # Process the image to find the best paths
        result_image = get_colors(image, colors.split(","))

        # Save the processed image to an in-memory bytes buffer
        img_io = BytesIO()
        result_image.save(img_io, format="PNG")
        img_io.seek(0)

        # Return the image as a response
        return send_file(img_io, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=8080, debug=True)
