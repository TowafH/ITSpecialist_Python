import io

binary_stream = io.BytesIO() # In-Memory Binary Stream
binary_stream.write(b"Hello I'm binary data!")

binary_stream.seek(0)
data = binary_stream.read()

print(data)