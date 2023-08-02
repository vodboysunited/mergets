# mergets

This Python script allows for efficient merging of streaming video files (`.ts` files) from a given directory, and generates a single output file. 

## Features

- Selective merging: The script can select a range of `.ts` files for merging, based on their indices.

- Temporal file handling: The script allows for specification of a temporary directory to store the intermediate files during the merging process. This can help in managing disk space effectively, especially for large streams.

- Error Handling: The script includes checks to ensure that only valid `.ts` files (those that start with "stream" and end with ".ts") are considered for merging.

## How to Use

To use the script, provide the arguments as follows:

`python <script_name.py> -i <input_dir> -o <output_file> -r <range> -t <temp_dir>`

Where: 

- `<input_dir>`: Directory to look for `.ts` files. Default is the current directory.

- `<output_file>`: Output file path. Default is `output.ts`.

- `<range>`: Range of `.ts` files to consider for merging, given as "start-end". This parameter is optional.

- `<temp_dir>`: Temporary directory for storing intermediate files. This parameter is optional.

Example:

`python <script_name.py> -i ./streams -o ./merged/output.ts -r 1-10 -t ./temp`

In this example, the script will merge the stream files indexed from 1 to 10 in the `./streams` directory and generate an output file `output.ts` in the `./merged` directory. Intermediate files during the process will be stored in `./temp` directory.

## Dependencies

This script depends on `ffmpeg` for the actual merging of the video files. Please ensure you have `ffmpeg` installed in your system and added to your PATH.
