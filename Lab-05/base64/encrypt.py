import base64

def main():
    input_string = input("Enter a string to encode in Base64: ")
    
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    
    with open("base64_encoded.txt", "w") as file:
        file.write(encoded_string)
        
    print("Base64 encoded string saved to base64_encoded.txt")
    
if __name__ == "__main__":
    main()