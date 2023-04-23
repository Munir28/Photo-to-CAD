import cv2

# Edge detection parameters
DILATION_KERNEL_SIZE = 2
EROSION_KERNEL_SIZE = 3
METHOD = "canny"
# Only for canny
LOW_THRESHOLD = 10
HIGH_THRESHOLD = 100
# Only for sobel must be odd 1-31
KSIZE = 5



class EdgeDetector:
    def __init__(self, image):
        self.image = image

    def dilate_image(self, kernel_size=DILATION_KERNEL_SIZE):
        if self.image is None:
            raise ValueError("Image not provided.")

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        self.image = cv2.dilate(self.image, kernel, iterations=1)

    def erode_image(self, kernel_size=EROSION_KERNEL_SIZE):
        if self.image is None:
            raise ValueError("Image not provided.")

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        self.image = cv2.erode(self.image, kernel, iterations=1)

    def detect_edges(self, method=METHOD, low_threshold=LOW_THRESHOLD, high_threshold=HIGH_THRESHOLD, ksize=KSIZE):
        if self.image is None:
            raise ValueError("Image not provided.")

        if method.lower() == "canny":
            # Apply Canny edge detection to the pre-processed image
            edges = cv2.Canny(self.image, low_threshold, high_threshold)
        elif method.lower() == "sobel":
            # Apply Sobel edge detection to the pre-processed image
            sobelx = cv2.Sobel(self.image, cv2.CV_64F, 1, 0, ksize=ksize)
            sobely = cv2.Sobel(self.image, cv2.CV_64F, 0, 1, ksize=ksize)

            # Combine Sobel X and Sobel Y gradients
            edges = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
            edges = cv2.convertScaleAbs(edges)
        else:
            raise ValueError("Invalid method specified. Use 'canny' or 'sobel'.")

        return edges

# The following code is used to test the EdgeDetector class
if __name__ == "__main__":
    # Load the pre-processed image
    input_path = "photos/output/drawing1processed.jpg"
    preprocessed_image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Create an instance of the EdgeDetector class and detect edges
    edge_detector = EdgeDetector(preprocessed_image)
    edge_detector.dilate_image()
    edge_detector.erode_image()
    detected_edges = edge_detector.detect_edges()

    # Save the detected edges for debugging purposes
    output_path = "photos/output/drawing1edges.jpg"
    cv2.imwrite(output_path, detected_edges)