import cv2

class ImagePreprocessor:
    def __init__(self, input_path):
        self.input_path = input_path
        self.image = None

    def load_image(self):
        self.image = cv2.imread(self.input_path, cv2.IMREAD_COLOR)
        return self.image

    def resize_image(self, width=None, height=None):
        if self.image is None:
            raise ValueError("Image not loaded. Call load_image() first.")

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

        self.image = cv2.resize(self.image, dimensions, interpolation=cv2.INTER_AREA)
        return self.image

    def enhance_image(self):
        if self.image is None:
            raise ValueError("Image not loaded. Call load_image() first.")

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Apply histogram equalization to enhance contrast
        self.image = cv2.equalizeHist(gray_image)
        return self.image

    def binarize_image(self, threshold=128):
        if self.image is None:
            raise ValueError("Image not loaded. Call load_image() first.")

        # Apply binary thresholding to create a black and white image
        _, self.image = cv2.threshold(self.image, threshold, 255, cv2.THRESH_BINARY)
        return self.image

if __name__ == "__main__":
    input_path = "path/to/your/input/image.jpg"
    preprocessor = ImagePreprocessor(input_path)
    image = preprocessor.load_image()
    resized_image = preprocessor.resize_image(width=800)  # Adjust the width or height as needed
    enhanced_image = preprocessor.enhance_image()
    binarized_image = preprocessor.binarize_image()

    # Save the pre-processed image for debugging purposes
    output_path = "path/to/your/output/image.jpg"
    cv2.imwrite(output_path, binarized_image)