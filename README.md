
# MoveDuplicates Tool

## Video Tutorial

For a step-by-step guide on how to use the tool, watch the video tutorial:  

[<img src="https://img.youtube.com/vi/o6pMQoCuBs8/maxresdefault.jpg" width="100%">](https://youtu.be/o6pMQoCuBs8)


## Setting Up the Environment

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Creating the Executable

To generate the `.exe` file, run the following command:

```bash
pyinstaller --onefile --name=MoveDuplicates main.py
```

The executable will be available in the `dist` folder after the process completes.

## How to Use

1. Copy the `.exe` file from the `dist` folder (created in the previous step) or you can download from the [Releases](https://github.com/mrzaizai2k/deduplicate_images/releases/tag/v1.0.0) to the folder containing the images you want to check for duplicates.
2. Double-click the `.exe` file. This will:
    - Identify duplicate images.
    - Move all duplicates to a newly created folder named `MCB_duplicate` within your image folder.
3. Review the images in the `MCB_duplicate` folder and delete them if they are unnecessary.


