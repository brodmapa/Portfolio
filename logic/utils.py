def imagerise(url_, resolution_=[]):
    from PIL import Image

    image_ = Image.open("./" + url_)
    image_ = image_.resize(resolution_)
    return image_