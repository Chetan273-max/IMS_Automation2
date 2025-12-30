def parse_sip_file(file_path):
    headers = {}

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()

    return headers
