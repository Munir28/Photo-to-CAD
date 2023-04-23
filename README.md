# Photo to CAD
This project aims to automate the process of converting photos of technical drawings into CAD files. The main focus is on image processing, computer vision, and machine learning techniques to extract valuable information from the input images and create accurate CAD representations.

## Features
Image preprocessing: Enhance and prepare input images for further processing.
Edge detection: Identify and extract the essential lines and shapes from the input images.
Vectorization: Convert the detected edges into vector format.
Dimension recognition: Extract dimension annotations (measurements) from the input images using OCR and geometric heuristics.
Line separation: Separate the model lines from the measurement lines based on their attributes and geometric relationships.
DXF export: Export the vectorized drawing and extracted dimensions into a DXF file format.
## Getting Started
### Prerequisites
Python 3.x
OpenCV
NumPy
Other libraries (TBD)
## Installation
Clone the repository or download the source files.
Create and activate a Python virtual environment (recommended).
Install the required packages using pip or conda.
## Usage
Run the main.py script to execute the entire pipeline, from loading the input image to exporting the final DXF file.
Contributing
Please feel free to submit pull requests or report issues to improve the project. Any feedback and suggestions are appreciated.

## License
This project is open source and available under the MIT License.

## Acknowledgments
OpenAI for the ChatGPT API and assistance during the development process.
The open-source community for providing valuable resources and inspiration.