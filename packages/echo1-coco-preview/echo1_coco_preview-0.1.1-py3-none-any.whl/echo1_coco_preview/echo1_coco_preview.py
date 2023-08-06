import argparse, json
from email.policy import strict
import os
import cv2
from pydash import py_
import bbox_visualizer as bbv
from loguru import logger
from os.path import exists

# The main function for execution
def main(args):

    # If the annotations file does not exist
    if not exists(args.annotations_file):
        logger.warning("There annotations file {} does not exist.".format(image_path))
        exit(1)

    with open(args.annotations_file, "r") as f:
        data = json.load(f)

    # Get all of the matching images
    matching_image = py_(data).get("images").find({"id": args.image_id}).value()

    # If there are no matching images in the data
    if matching_image == None:
        logger.error(
            "There are no images that match the id {}. Please verify your data.".format(
                args.image_id
            )
        )
        exit(1)

    # Get the image path
    image_path = os.path.join(args.data_base_path, matching_image["file_name"])

    # If the file does not exist
    if not exists(image_path):
        logger.warning("The image {} does not exist.".format(image_path))
        exit(1)

    # Get all of the matching annotations
    matching_annotations = (
        py_(data).get("annotations").filter_({"image_id": args.image_id}).value()
    )

    # If there are no matching annotations in the data
    if len(matching_annotations) == 0:
        logger.warning(
            "There are no annotations for the image id {}. Please verify your data.".format(
                args.image_id
            )
        )

    # Get all of the categories in the data
    categories = py_(data).get("categories").value()

    # Read in the image frame data
    frame = cv2.imread(image_path)

    # Append the bounding boxes and labels to the frame
    for a in matching_annotations:
        x, y, w, h = a["bbox"]
        xmin, yMin, xMax, yMax = [x, y, (x + w), (y + h)]
        bbox = [xmin, yMin, xMax, yMax]
        frame = bbv.draw_rectangle(frame, bbox, thickness=1)
        category = py_(categories).find({"id": a["category_id"]}).value()
        frame = bbv.add_label(frame, "{}".format(category["name"]), bbox, top=True)

    # If the scale percent is greater than 100 then rescale
    if args.scale_percent > 100:
        width = int(frame.shape[1] * args.scale_percent / 100)
        height = int(frame.shape[0] * args.scale_percent / 100)
        frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
        logger.debug("Resized the image to {}".format(frame.shape))

    # Setup the preview window with the image
    cv2.namedWindow(matching_image["file_name"], cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(matching_image["file_name"], cv2.WND_PROP_TOPMOST, 1)
    cv2.imshow(matching_image["file_name"], frame)

    # Waits for the user to press any key
    cv2.waitKey(0)

    # Close all open windows
    cv2.destroyAllWindows()


def app():
    parser = argparse.ArgumentParser(
        description="Previews an image and its annotations via a coco json file."
    )
    parser.add_argument(
        "--annotations_file",
        type=str,
        dest="annotations_file",
        default="./labels.json",
        help="Path to COCO annotations file. (e.g. labels.json)",
    )
    parser.add_argument(
        "--data_base_path",
        type=str,
        dest="data_base_path",
        default="./data",
        help="Path to the images referenced in the COCO annotations file.",
    )
    parser.add_argument(
        "--scale_percent",
        type=int,
        dest="scale_percent",
        default=100,
        help="The amount that we should scale the image size.",
        required=False,
    )
    parser.add_argument(
        "--image_id",
        type=int,
        dest="image_id",
        help="The id of the image to preview annotations for.",
        required=True,
    )

    args = parser.parse_args()

    main(args)
