# INF250: Mandatory Exercise 1

Task: _In this exercise you will write a python-program that reads an image and makes a threshold using the [Otsu algorithm](https://en.wikipedia.org/wiki/Otsu%27s_method)._

_You will use [this skeleton program](https://nmbu.instructure.com/courses/5600/files/1019649/download) in Python. It consists of one function making a histogram, one that carries out the Outsu thresholding and one function that uses this to make a binary image._

_You will hand in the python code on Canvas._

## Features:

- Histogram
- Otsu thresholding
- Visualization of Otsu's thresholding method

The main script performs the vizualization with both OpenCV's implementation and this assignments manual implementation.

## Comments:

- File based on code template from Yngve Mardal Moe
- Removed redundant threshold function, as it is only needed if we don't want to use Otsu thresholding
- Auto-formatted by black with a custom line length  
  To enable in VSCode, add this to your settings.json:

  ```JSON
  "editor.formatOnSave": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["-l", "79"],
  ```

  ...and say yes to any prompts the next time you save a Python file
