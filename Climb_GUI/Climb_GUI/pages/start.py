"""The Start page."""
from Climb_GUI.templates import template

from fastapi import UploadFile
from ..state import State
import reflex as rx
import numpy as np
import cv2 as cv
import asyncio
from datetime import datetime
from Climb_GUI.lib.path_calc import shortestPath

def strToColor(color):
    color = color.lower()
    if(color == 'red'):
        return (255, 0, 0)
    elif(color == 'green'):
        return (0,255,0)
    elif(color == 'blue'):
        return (0,0,255)
    elif(color == 'orange'):
        return (255,128,0)
    elif(color == 'yellow'):
        return (255,255,0)
    elif(color == 'purple'):
        return (255,0,255)
    elif(color == 'black'):
        return (0,0,0)

# 54: black (medium, medium)
# 13: blue (good)
# 14: red (good)
# 41: green (decent, few detected)
# 46: yellow (alright, most)
# 18: purple (bad, nothing detected)
# experiment with grayscale
color_ranges = {
    "red": [(100, 0, 0), (255, 50, 50)],  # Define the red color range
    "green": [(0, 100, 0), (90, 255, 100)],
    "blue": [(0, 0, 100), (80, 80, 255)],  # Define the blue color range
    "orange": [(255, 100, 0), (255, 200, 100)],
    "purple": [(200, 100, 200), (250, 165, 250)],
    "yellow": [(200, 200, 0), (255, 255, 100)],
    "black": [(0, 0, 0), (50, 50, 20)]
}

async def colors(img_path, chosenColor, name):  
    # array of tuples containing coordinates of each box
    bounding_boxes = []  
    img = cv.imread(img_path) #load image
    if img is None:
        raise Exception(f"Failed to load the image: {img_path}")
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) #convert image to RGB
    img_marked = img.copy() #create new blank image to populate
    for color, (lower, upper) in color_ranges.items():
        if(color.lower() == chosenColor.lower()):
            #for specified range of colors, create a mask
            mask = cv.inRange(img_rgb, np.array(lower), np.array(upper))
            #within mask, identify contours
            contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            #draw boxes around color holds
            for contour in contours:
                x, y, z, a = cv.boundingRect(contour)
                cv.rectangle(img_marked, (x, y), (x+z,y+a), strToColor(chosenColor), 2) #Green bound box
                bounding_boxes.append(((x, y), (x + z, y + a)))  # Store bounding box coordinates

    # for i in range(len(bounding_boxes) - 1):
    #     if(i % 2 == 0):
    #         cv.line(img_marked, bounding_boxes[i][1], bounding_boxes[i + 1][0], strToColor(chosenColor), 2)
    #     elif(i % 2 != 0 and chosenColor != "blue"):
    #         cv.line(img_marked, bounding_boxes[i][1], bounding_boxes[i + 1][0], strToColor("blue"), 2)
    #     elif(i % 2 != 0 and chosenColor == "blue"):
    #         cv.line(img_marked, bounding_boxes[i][1], bounding_boxes[i + 1][0], strToColor("red"), 2)
    
    path = shortestPath(bounding_boxes[0], bounding_boxes[len(bounding_boxes)-1], bounding_boxes, 300)
    path1 = shortestPath(bounding_boxes[1], bounding_boxes[len(bounding_boxes)-1], bounding_boxes, 250)
    path2 = shortestPath(bounding_boxes[2], bounding_boxes[len(bounding_boxes)-1], bounding_boxes, 200)
    path3 = shortestPath(bounding_boxes[3], bounding_boxes[len(bounding_boxes)-1], bounding_boxes, 150)
    
    for i in range(len(path)-1):
        cv.line(img_marked, path[i][1], path[i+1][0], strToColor("blue"), 2)
    for i in range(len(path1)-1):
        cv.line(img_marked, path1[i][1], path1[i+1][0], strToColor("red"), 2)
    for i in range(len(path2)-1):
        cv.line(img_marked, path2[i][1], path2[i+1][0], strToColor("green"), 2)
    for i in range(len(path3)-1):
        cv.line(img_marked, path3[i][1], path3[i+1][0], strToColor("yellow"), 2)

    cv.imwrite(f"assets/output_{str(datetime.now().minute)+'_'+name}", img_marked)
    # cv.imwrite(f"assets/output{Global_State.file_num}.png", img_marked)
    await asyncio.sleep(3)

class Global_State(State):
    uploaded_image: str= ''
    """The app state."""

    names: list = []
    color: str
    text: str = ""
    
    def set_color(self, color: str):
        self.text = "Please wait, processing file..."
        self.color = color
    
    async def handle_upload(
        self, files: list[UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = f".web/public/{file.filename}"

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)
            self.names.append(f"/output_{str(datetime.now().minute)+'_'+file.filename}")
            # self.names.append(f"/output{Global_State.file_num}.png")
        
            await colors(outfile, self.color, file.filename)
        self.text = ""
            
color = "rgb(107,99,246)"
bg = "rgb(0,0,0)"


@template(route="/start", title="Start")
def start():
    """The main view."""
    return rx.box(
        rx.upload(
            rx.box(
                rx.button(
                    "Select File",
                    color="black",
                    bg="white",
                    border=f"1px solid {color}",
                    background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                ),
                rx.text(
                    "Drag and drop files here or click to select files"
                ),
            ),
            multiple=False,
            accept={
                # "application/pdf": [".pdf"],
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
                # "image/gif": [".gif"],
                # "image/webp": [".webp"],
                # "text/html": [".html", ".htm"],
            },
            max_files=1,
            disabled=False,
            on_keyboard=True,
            border=f"1px dotted {color}",
            padding="5em",
        ),
        # rx.input(placeholder="Enter the color of the holds you wish to climb", on_blur=Global_State.set_color, background_color="rgb(200,200,200)", border=f"1px dotted rgb(255,255,255)"),
        rx.input(placeholder="Enter the color of the holds you wish to climb", on_blur=Global_State.set_color, background_image="linear-gradient(216deg, rgb(0, 0, 255), rgb(128, 0, 128), rgb(160, 32, 240))", border=f"1px dotted rgb(255,255,255)", color="rgb(255,255,255)"),
        rx.button(
            "Run",
            on_click=lambda: Global_State.handle_upload(
                rx.upload_files(),
            ),
            margin_y = "1em",
            color="black",
            background_image="linear-gradient(144deg,#00DDEB,#5B42F3 50%,#AF40FF)",
        ),
        rx.text(Global_State.text),
        # rx.foreach(
        #     Global_State.names,
        #     lambda names, index: rx.vstack(
        #         rx.flex(
        #             rx.image(src=f"{Global_State.names[index]}", width=600, height=600),
        #             align="center",
        #             justify="center",
        #             height="100%",
        #             width="100%"
        #         ),
        #         # rx.text(names),
        #         width = "100%"
        #     ),
        # ),
        rx.cond(
            Global_State.names.length() > 0,
            rx.flex(
                rx.image(src=f"{Global_State.names[Global_State.names.length()-1]}", width=600, height=600),
                align="center",
                justify="center",
                height="100%",
                width="100%"
            ),
        ),
        # rx.text("Every single hold our program detects is connected to by a line, the left side of the line indicates a left hand or foot, and the right side indicates a right hand or foot.", width="100%"),
    )
