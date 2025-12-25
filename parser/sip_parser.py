def parse_sip_file(file_path):
    headers = {}

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            if ":" in line:
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()

    return headers


if __name__ == "__main__":
    sip_file = "../data/sip_register.txt"
    parsed_headers = parse_sip_file(sip_file)

    print("Parsed SIP Headers:\n")
    for k, v in parsed_headers.items():
        print(f"{k}: {v}")
