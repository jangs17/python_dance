#!/usr/bin/env python
import hashlib
import sys

def multi_hash(filename):
    """
    Calculates the md5 and sha256 hashes
    of the specified file and returns a list
    containing the hash sums as hex strings.
    """
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    try:
        with open(filename, 'rb') as f:
            while True:
                buf = f.read(2**20)
                if not buf:
                    break
                md5.update(buf)
                sha256.update(buf)
        return [md5.hexdigest(), sha256.hexdigest()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: checksum.py <file1> <file2> ...")
        sys.exit(1)
    
    hashes = []
    print('---------- MD5 sums ----------')
    for filename in sys.argv[1:]:
        h = multi_hash(filename)
        if h:
            hashes.append(h)
            print(f'{h[0]} {filename}')
    
    print('---------- SHA256 sums ----------')
    for i in range(len(hashes)):
        print(f'{hashes[i][1]} {sys.argv[i+1]}')

