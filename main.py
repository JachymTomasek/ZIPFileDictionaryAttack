import pyzipper

zip_path = input("ZIP file path: ")    # path of ZIP
dictionary_path = input("Dictionary TXT file path: ")    # path of dictionary

with open(dictionary_path, "r", encoding="utf-8") as f:

    correct_pwd = False
    for row in f.readlines():
        if correct_pwd == False:
            string_pwd = row.strip()
            print(string_pwd)

            my_password = bytes(string_pwd, encoding="utf8")
            print(my_password)

            with pyzipper.AESZipFile(zip_path) as my_zip:

                try:
                    my_zip.extractall(pwd=my_password)
                    print("spravne", string_pwd)
                    correct_pwd = True
                except Exception as e:
                    print("spatne")
                    correct_pwd = False
        else:
            break





