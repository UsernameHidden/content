import requests
import json
from time import sleep
import urllib.request
from PIL import Image
import os

def thumbnail(prompt):
    improvement_string = f"{prompt}.The main character is at the bottom half of the image centered, symmetry, painted, intricate, volumetric lighting, beautiful, rich deep colors masterpiece, sharp focus, ultra detailed, in the style of dan mumford and marc simonetti, astrophotography"

    improvement_string = ""


    api_token = "v1.148e54eb83135f86fb32b79ac71883d2e5f025897b207dc975bd730e8abe13b0" #fca1a91e11525e52eb375e25fc9be68b4516207abb5364dfc7111d83503d2f47


    headers = {
    'Authorization': f'Bearer {api_token}',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    }

    json_data = {
        'style': 'anime',
        'layout': 'horizontal',
        'amount': 1,
        'isPublic': True,
        'isHd': False,
        'prompt': improvement_string,
        'negativePrompt': 'right arm small, asia eyes, man, black skin, ugly, mutilated hands limbs, poorly drawn face and hands and eyes, deformed, blurry, bad atrocious anatomy, bad proportions, disfigured, ugly sharp face, gross proportions, elongated body, cropped image, draft, deformed hands, signature, poor quality resolution, bad art, childish, incoherent, bad resolution, deformed, disfigured, disjointed, out of frame, duplicate, watermark, signature, text, ugly, morbid, mutated, deformed, blurry, watermark, twisted fingers, double image, oversaturated, grain, unattractive, separate limbs, disgusting, low-res, gross proportions, bad art, plastic, cropped image, double image, cut off, grainy, text, logo, wordmark, writing, heading',
        'steps': 25,
        'seed': 3749166748, #3198062813 3287557728 1852547501 2962700828
        'sampler': 'ddim',
    }

    response = requests.post('https://api.neural.love/v1/ai-art/generate', headers=headers, json=json_data)
    print(response.text)

    image_id = json.loads(response.text).get("orderId")


    is_ready = False
    sleep(7)


    while is_ready is False:
        headers = {
            'Authorization': f'Bearer {api_token}',
            'Accept': 'application/json',
        }

        check_image = requests.get('https://api.neural.love/v1/ai-art/orders/' + image_id, headers=headers)

        check_parsed_json = json.loads(check_image.text)

        is_ready = check_parsed_json["status"]["isReady"]

        sleep(3)

    print("\n\n")
    image_url = check_parsed_json["output"][0]["full"]

    urllib.request.urlretrieve(image_url, "temp.jpg")

    # open the image file
    image = Image.open("temp.jpg")

    # get the width and height of the image
    width, height = image.size

    # calculate the desired width and height for a 16:9 aspect ratio
    desired_height = int(width / (16 / 9))
    desired_width = width

    # calculate the y-coordinate of the top edge of the crop box
    y = (height - desired_height) // 2

    # define the crop box as (left, upper, right, lower)
    crop_box = (0, y, desired_width, y + desired_height)

    # crop the image
    cropped_image = image.crop(crop_box)

    # save the cropped image as "thumbnail.jpg"
    cropped_image.save("thumbnail.jpg")
    os.remove("temp.jpg")





prompt = '''A person standing at a crossroads, looking overwhelmed as they face a decision about their future. The figure is in the center of the image, with a dim, shadowy background behind them. The figure is holding a hammer, and there are small touches of light, like little nudges, on their shoulder. The person's face is contorted with emotion, and they appear to be in pain. In the background, there is a faint image of a rabbit hole, symbolizing the danger of falling into victimhood. The overall tone is one of struggle and uncertainty, but with a glimmer of hope for a better future.'''


thumbnail(prompt)