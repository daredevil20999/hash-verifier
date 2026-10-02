#!/usr/bin/env python3
import argparse
import hashlib
import sys


def verify_hash(file_path: str, expected_hash: str, algorithm: str = "sha256"):
    expected_hash = expected_hash.strip().lower()
    try:
        with open(file_path, "rb") as f:
            file_hash = hashlib.file_digest(f, algorithm).hexdigest()
        print(f"Calculated Hash: {file_hash}")
        print(f"Expected Hash: {expected_hash}")
        return file_hash.lower() == expected_hash
    except FileNotFoundError: 
        print(f"Error: The file at {file_path} was not found.")
        return False 
    except ValueError:
        print(f"Error: The algorithm '{algorithm}' is not supported.")
        return False 
    except PermissionError:
        print(f"Error: You do not have permission to access the file at {file_path}.")
        return False 
    except IsADirectoryError:
        print(f"Error: The path at {file_path} is a directory, not a file.")
        return False 

    
def main():
    parser = argparse.ArgumentParser(
        description="Verify the integrity of a file using hash functions."
    )
    parser.add_argument("file", help="Path to the file you want to check")
    parser.add_argument("hash", help="The expected hash value of the file")
    args = parser.parse_args()
    if verify_hash(args.file, args.hash):
        print("Hash verification successful")
        sys.exit(0)
    else: 
        print("Hash verification failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
            
