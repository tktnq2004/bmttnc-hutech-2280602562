import base64

def main():
    try:
        with open("base64_encoded.txt", "r") as file:
            encoded_string = file.read().strip()
        
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        
        print("Decoded string:",decoded_string)
        
    except Exception as e:
        print("An error occurred during decoding:", str(e))

if __name__ == "__main__":
    main()