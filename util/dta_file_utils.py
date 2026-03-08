def find_dta_file(files):
    for file in files:
        if file.endswith(".dta"):
            yield file