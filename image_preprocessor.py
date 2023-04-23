import cv2

RESIZE_WIDTH = 1000
RESIZE_HEIGHT = None
THRESHOLD = 128
ALPHA = 1.2  # Contrast control (1.0-3.0)
BETA = 25   # Brightness control (0-100)

class ImagePreprocessor:
    # The class constructor initializes the input_path and sets an empty image attribute
    def __init__(self, input_path):
        self.input_path = input_path
        self.image = None

    # The load_image method reads the input image from the file path and stores it in the image attribute
    def load_image(self):
        self.image = cv2.imread(self.input_path, cv2.IMREAD_COLOR)
        return self.image

    # The resize_image method resizes the image based on the provided width or height while maintaining the aspect ratio
    def resize_image(self, width=None, height=None):
        if self.image is None:
            raise ValueError("Image not loaded. Call load_image() first.")

        # Determine the new dimensions based on the provided width and height
        if width is not None and height is not None:
            dimensions = (width, height)
        elif width is not None:
            aspect_ratio = float(self.image.shape[1]) / float(self.image.shape[0])
            dimensions = (width, int(width / aspect_ratio))
        elif height is not None:
            aspect_ratio = float(self.image.shape[0]) / float(self.image.shape[1])
            dimensions = (int(height / aspect_ratio), height)
        else:
            raise ValueError("Either width or height must be provided.")

        # Resize the image using the determined dimensions
        self.image = cv2.resize(self.image, dimensions, interpolation=cv2.INTER_AREA)
        return self.image
    


    # The enhance_image method converts the image to grayscale and applies histogram equalization to improve contrast
    def enhance_image(self, alpha, beta):
        if self.image is None:
            raise ValueError("Image not loaded. Call load_image() first.")

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Adjust the contrast and brightness using alpha and beta
        gray_image = cv2.convertScaleAbs(gray_image, alpha=alpha, beta=beta)

        # Apply histogram equalization to enhance contrast
        self.image = cv2.equalizeHist(gray_image)
        return self.image

    # The binarize_image method applies binary thresholding to create a black and white image
    def binarize_image(self, threshold=128):
        if self.image is None:
            raise ValueError("Image not loaded. Call load_image() first.")

        # Apply binary thresholding to create a black and white image
        _, self.image = cv2.threshold(self.image, threshold, 255, cv2.THRESH_BINARY)
        return self.image

# The following code is used to test the ImagePreprocessor class
if __name__ == "__main__":
    input_path = "photos/drawing1.jpg"
    preprocessor = ImagePreprocessor(input_path)
    image = preprocessor.load_image()
    resized_image = preprocessor.resize_image(width=RESIZE_WIDTH, height=RESIZE_HEIGHT)
    enhanced_image = preprocessor.enhance_image(ALPHA,BETA)
    binarized_image = preprocessor.binarize_image(THRESHOLD)

    # Save the pre-processed image for debugging purposes
    output_path = "photos/output/drawing1processed.jpg"
    cv2.imwrite(output_path, binarized_image)
