# request
import httpx

# response = httpx.get("https://directline.digital/media/page_photos/0000/photo_14.normal.png")
# d = response.content
# with open("img.png" , "wb") as f:
#     f.write(d)

response = httpx.get("https://jsonplaceholder.typicode.com/posts")
d = response.json()
for i in d:
    print(i)



