import hashlib


# Based on https://stackoverflow.com/a/55542529

def get_digest(file_path) -> int:
    h = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return int(h.hexdigest(), 16)
