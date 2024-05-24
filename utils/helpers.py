import base64


async def image_to_base64(image_file):
    image_bytes = await image_file.download_as_bytearray()
    return base64.b64encode(image_bytes).decode('utf-8')