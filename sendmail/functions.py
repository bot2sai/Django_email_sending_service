

def handle_uploaded_file(to, f):
    with open(to+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
