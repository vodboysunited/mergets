import os
import shutil
import argparse
import subprocess
import tempfile

def is_valid_file(file_name):
    return file_name.startswith("stream") and file_name.endswith(".ts")

def get_file_index(file_name):
    if is_valid_file(file_name):
        return int(file_name[6:].split(".")[0])
    return float('inf')  # Any invalid files are sorted to the end

def merge_files(input_dir, output_file, temp_dir=None, range_start=None, range_end=None):
    with tempfile.NamedTemporaryFile(suffix='.ts', dir=temp_dir, delete=False) as tmpfile:
        for i in sorted(os.listdir(input_dir), key=get_file_index):
            if not is_valid_file(i):
                continue
            index = get_file_index(i)
            if range_start is not None and index < range_start:
                continue
            if range_end is not None and index > range_end:
                continue
            with open(os.path.join(input_dir, i), 'rb') as f:
                shutil.copyfileobj(f, tmpfile)

        tmpfile.close()

        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

        cmd = ['ffmpeg', '-i', tmpfile.name, '-c', 'copy', output_file]
        subprocess.run(cmd)

        os.unlink(tmpfile.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', type=str, default='.', 
                        help='Directory to look for .ts files')
    parser.add_argument('-o', '--output_file', type=str, default='output.ts',
                        help='Output file path')
    parser.add_argument('-r', '--range', type=str, default=None,
                        help='Range of .ts files to consider, given as "start-end"')
    parser.add_argument('-t', '--temp_dir', type=str, default=None,
                    help='Temporary directory for intermediate files')

    args = parser.parse_args()

    range_start, range_end = None, None
    if args.range is not None:
        range_start, range_end = map(int, args.range.split("-"))

    merge_files(args.input_dir, args.output_file, args.temp_dir, range_start, range_end)