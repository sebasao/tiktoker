import os
import sys
import tiktoken

def compare_encodings(example_string: str) -> int:
    """Prints a comparison of 3 different encodings."""
    encodings = ["r50k_base", "p50k_base", "cl100k_base"]

    for encoding_name in encodings:
        encoding = tiktoken.get_encoding(encoding_name)
        token_integers = encoding.encode(example_string)
        num_tokens = len(token_integers)
        num_chars = len(example_string)
        token_bytes = [encoding.decode_single_token_bytes(token) for token in token_integers]
        # print()
        # print(f"{encoding_name} > {num_chars} chars >  {num_tokens} tokens")
        # print(f"  Token integers: {token_integers}")
        # print(f"  Token bytes: {token_bytes}")
        return num_tokens
    
# Use the first argument as the data directory, or default to "data"
data_dir = sys.argv[1] if len(sys.argv) > 1 else "data"
# Use the second argument as the the optional file extensions to exclude
exclude_extensions = sys.argv[2] if len(sys.argv) > 2 else []

def process_file(file_path):
    print(f"Processing {file_path}...")
    try:
        with open(file_path, "r") as f:
            example_string = f.read()
        return compare_encodings(example_string)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return 0

def process_directory(directory):
    total_files = 0
    total_tokens = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Skip files with the specified extensions
            if any(file.endswith(ext) for ext in exclude_extensions):
                continue
            total_files += 1
            total_tokens += process_file(file_path)
    return total_files, total_tokens

total_files, total_tokens = process_directory(data_dir)
print(f"Total number of files: {total_files}")
print(f"Total tokens across all processed files: {total_tokens}")