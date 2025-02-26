def validate_email(line, outfile):
    # Convert the entire address to lowercase
    line = line.lower()

    if '@' in line:
        if line.count('@') == 1:
            components = line.split('@')
            prefix, domain = components[0], components[1]
            index=line.index('@')
            for i in range(0,len(line)):
                index=line.index('@')
                index=len(line)-index
                index=-index

            if prefix and domain and prefix[0] != '@' and prefix[-1] != '@' and index < -6:
                if prefix.replace('_', '').isalpha() or prefix.replace('_', '').isalnum() and not prefix[0].isdigit() and len(prefix) < 64 and len(domain) < 255 and domain.count('.') >= 1:
                    if '..' not in prefix and '..' not in domain and ',' not in line and not domain.replace('.', '').isdigit() and (domain.replace('.', '').isalnum() or domain.replace('.', '').isalpha() or '-' in domain):
                        # Validate TLD (e.g., ".com", ".org")
                        valid_tlds = {".com", ".org", ".net", ".edu",".in"}  # Add more as needed
                        if domain.lower().endswith(tuple(valid_tlds)):
                            outfile.write(f"***VALID*** {line}\n")
                        else:
                            outfile.write(f"***INVALID (Invalid TLD)*** {line}\n")
                    else:
                        outfile.write(f"***INVALID*** {line}\n")
                else:
                    outfile.write(f"***INVALID*** {line}\n")
            else:
                outfile.write(f"***INVALID*** {line}\n")
        else:
            outfile.write(f"***INVALID*** {line}\n")
    else:
        outfile.write(f"***INVALID*** {line}\n")


file_path = R"C:\Users\Vinay Kumar\Documents\PYTHON internship\Sample_input.txt"
output_path = R"C:\Users\Vinay Kumar\Documents\PYTHON internship\outputfile.txt"

with open(file_path) as file, open(output_path, 'w') as outfile:
    lines = file.read().splitlines()

    for line in lines:
        validate_email(line, outfile)

email = input("Enter an email address: ")
with open(output_path, 'a') as outfile:
    validate_email(email, outfile)
    
file.close()
outfile.close()
