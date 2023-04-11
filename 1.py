import os
import moviepy.editor as mp
import whisper
import requests
import json
import openai
import requests
import json
from time import sleep
import urllib.request
from PIL import Image
import os
openai.api_key = ("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")


def summarize_text(transcript):
    transcript = transcript.encode('utf-8')


    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IlliMnFrTEx6V1E3S0p4NnhFZUVlM0E9PSIsInZhbHVlIjoiUjdTVWQrcS9YYmRia3F6ckplbThtZzVqVWRmQWFyT3ZReFQxT0gxNDhoOXV4MXdGZEZGR0xwUFdOMWQxa0F2Z3ExNGVLQ3BFNEpxQmxQN1NaRFExRjFzT2F5ZEdEN0hKSXJPd1NmQm9QUHU4NlFuTHU0NjNQT2Fhd3pCUkwxVm4iLCJtYWMiOiJkYjhlNTUyMDNhNjllYzdkZWRkM2VjNmRhZDZjMjQ1M2ViOGQ4MjU1M2Y5ODNiN2I3YTNmZDMwMjg5ZmUxMjVjIiwidGFnIjoiIn0%3D',
        'laravel_session': 'eyJpdiI6ImhVdWNuZHZHN3RnZmptQlNpSExWUFE9PSIsInZhbHVlIjoiaElJR2pHbmtxaUwxQ3hzZDdkYWhnOVNsUEdzNlBML0FUTi8yMWtYK2pMZWVBeGc3bG5OT2FEM3MzV1prM2JBZGQ0T1VyNjIzWEhHa20vRmJvT1M4V0pJUTRWdkJGOEk1VVdsUTlqRWdQK0h4bkhZQWhRYnhObWQrSHVDWVRoRUciLCJtYWMiOiJkMjZlZThhNWRlZDJiOWM3YTU2MTdiZGI1NDFjY2U0YTk0OTViNjlkMzViMTM5NzdhMTg5MzM1NjdkY2JjMDJjIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-NewRelic-ID': 'VwEFVV9TCRABV1RSBAcAV1UH',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3MjQ5MDEiLCJhcCI6IjEzODYwMTg1MTciLCJpZCI6ImQ3ZGI5OTNhYjJjOTRmODYiLCJ0ciI6ImNkZTZjYmFjMmQzMDM2NWI5ZWMzMmQyODMwODgxZDgwIiwidGkiOjE2ODExNzUzODg0ODl9fQ==',
        'traceparent': '00-cde6cbac2d30365b9ec32d2830881d80-d7db993ab2c94f86-01',
        'tracestate': '3724901@nr=0-1-3724901-1386018517-d7db993ab2c94f86----1681175388489',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'multipart/form-data; boundary=---------------------------216887423924188855252613963746',
        'Origin': 'https://www.summarizer.org',
        'DNT': '1',
        'Alt-Used': 'www.summarizer.org',
        'Connection': 'keep-alive',
        'Referer': 'https://www.summarizer.org/',
        # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IlliMnFrTEx6V1E3S0p4NnhFZUVlM0E9PSIsInZhbHVlIjoiUjdTVWQrcS9YYmRia3F6ckplbThtZzVqVWRmQWFyT3ZReFQxT0gxNDhoOXV4MXdGZEZGR0xwUFdOMWQxa0F2Z3ExNGVLQ3BFNEpxQmxQN1NaRFExRjFzT2F5ZEdEN0hKSXJPd1NmQm9QUHU4NlFuTHU0NjNQT2Fhd3pCUkwxVm4iLCJtYWMiOiJkYjhlNTUyMDNhNjllYzdkZWRkM2VjNmRhZDZjMjQ1M2ViOGQ4MjU1M2Y5ODNiN2I3YTNmZDMwMjg5ZmUxMjVjIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImhVdWNuZHZHN3RnZmptQlNpSExWUFE9PSIsInZhbHVlIjoiaElJR2pHbmtxaUwxQ3hzZDdkYWhnOVNsUEdzNlBML0FUTi8yMWtYK2pMZWVBeGc3bG5OT2FEM3MzV1prM2JBZGQ0T1VyNjIzWEhHa20vRmJvT1M4V0pJUTRWdkJGOEk1VVdsUTlqRWdQK0h4bkhZQWhRYnhObWQrSHVDWVRoRUciLCJtYWMiOiJkMjZlZThhNWRlZDJiOWM3YTU2MTdiZGI1NDFjY2U0YTk0OTViNjlkMzViMTM5NzdhMTg5MzM1NjdkY2JjMDJjIiwidGFnIjoiIn0%3D',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    data = f'-----------------------------216887423924188855252613963746\r\nContent-Disposition: form-data; name="long_content"\r\n\r\n{transcript}\r\n\r\n-----------------------------216887423924188855252613963746\r\nContent-Disposition: form-data; name="summary_length"\r\n\r\n70\r\n-----------------------------216887423924188855252613963746\r\nContent-Disposition: form-data; name="_token"\r\n\r\nDlPmaNElPX10VSe2kdrCPjsbaIKTvGEEb2AAnXWA\r\n-----------------------------216887423924188855252613963746--\r\n'

    response = requests.post('https://www.summarizer.org/uploadFile', cookies = cookies, headers=headers, data=data)

    sumpara = json.loads(response.text)["sumpara"]
    return sumpara

def thumbnail(prompt):
    improvement_string = f"Anime {prompt}.The main character is at the bottom half of the image centered, symmetry, painted, intricate, volumetric lighting, beautiful, rich deep colors masterpiece, sharp focus, ultra detailed, in the style of dan mumford and marc simonetti, astrophotography"

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
        'prompt': prompt,
        'negativePrompt': 'right arm small, asia eyes, man, black skin, ugly, mutilated hands limbs, poorly drawn face and hands and eyes, deformed, blurry, bad atrocious anatomy, bad proportions, disfigured, ugly sharp face, gross proportions, elongated body, cropped image, draft, deformed hands, signature, poor quality resolution, bad art, childish, incoherent, bad resolution, deformed, disfigured, disjointed, out of frame, duplicate, watermark, signature, text, ugly, morbid, mutated, deformed, blurry, watermark, twisted fingers, double image, oversaturated, grain, unattractive, separate limbs, disgusting, low-res, gross proportions, bad art, plastic, cropped image, double image, cut off, grainy, text, logo, wordmark, writing, heading',
        'steps': 25,
        'seed': 2962700828, #3198062813 3287557728 best 1852547501
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

def title(transcript):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Create an SEO optimized title for Youtube. This is the transcript: "+ transcript,
    temperature=0.9,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    answer = response['choices'][0]['text'].strip()
    return answer

def description(transcript):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Create an SEO optimized description for Youtube. At the end of the description add 30 hashtags  This is the transcript: "+ transcript,
    temperature=0.9,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    answer = response['choices'][0]['text'].strip()
    return answer

def imagine(transcript):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt='''bRaky and dear. The illusion of control is God, you know Yes. Yeah. Yeah. Thats, you know, one of the things you want to talk about tonight was like the Mel Robbins. Yes. Video. Very interesting video. Yeah. And like this illusion of control. Right. Yeah. So I just rewatched it before we got on this call. Its just so so interesting. Its its you know, I think weve talked before about this idea like everybody has their own distinct journey through all this stuff. Yeah. Yeah. But there are some there theres so many things that are similar to each other. You know, like its like cascading failure across lights is one of them. It looks different for everybody. But it seems to happen for most people, not everybody, but theres Id say thats good way of putting it though the cascading failure of stuff. Yeah. Yeah. And and its like I think that it happens for everybody. It just looks differently. So some people its like no, its like a complete cascading failure where theyre like out on the streets kind of thing. Yes. And theyre, you know, or theyre like going through like the full bankruptcy or almost for bankruptcy or whatever it is. And then some people are just having like an emotional breakdown. But its still like this. Like its like the old has to degrade. I guess is probably the easiest general term to be able to put it in is that the degradation of the old version of you has to start to move in some way. Like you have to have that essentially like some type of a pain point to push through into whats next. And its more like getting the brain to not be comfortable with the old narrative of you. And start to search for something else like even through like a why is this happening to me And I think one of my questions at this point as well is because what I was thinking about was I was going to say do you think how hard it hits you is related to how much you are aware and choose the process and dont choose it. But then Im kind of like I thought that was a good question to ask and Im kind of realizing now that actually were all kind of like whether its a conscious or unconscious thing. Its kind of like you choose to go that way because whatever the other stuff was is dying like Im kind of like youre dying inside of it so that cant operate anymore. But because I was going to say like because I remember parts during my process that it was brutal. And I would say to an extent I did choose some of it, which I think helped give the illusion of helping to speed things up, which probably made things rougher in the short term. But as I was watching Mals video, what I was present to is its either youre kind of willing to go there now, like to be like I dont know what this is but like lets go. Or why do you kind of keep kicking and screaming, which just pushes this further, which then kind of just gives you more of an impact to move like you talked about this comfort, like the pain point, you know, and for me thats thats life. Im not about like pleasure driven. Im like all about avoidance of pain. But its like when the pain gets bad enough, its like then Ill go, then Ill move. Yeah, I think I think its a good question. Not easy to answer really because I think its mostly, you know, theres so many different way its so many different levels to answer it on, right Like you could say, you know, its its going to go the way that youve chosen it to go before you came into this life. You know, you can down that road and stuff like that. I, you know, I think that thats a valid answer to it. But theres no power in that answer for you. Right. You know, sort of being like a bit of a thing to the whole thing and like I dont have any control and all this kind of stuff, which without having the proper support around that. You could fall into victim with that. Thats a dark place. Yeah, it can be. So you cant you can be like, oh, Im just a victim to this. And I have to say and all thats kind of stuff. And you go down, you know, a bad rabbit hole that way. Or it could be, you know, the where you surrender. And you understand that this is the process that you go through. And this is your journey. And Im going to allow it to happen. So that. Yeah. But I think you need coaching around the set, the second one more than anything else to help you because its not easy. Not easy to do by yourself. And the way that I like to look at it is, you know, that the, you get the, you get the touch on the shoulder. And if you dont listen, the touch gets harder and harder and say you got to hit and the head with a hammer. Yeah. And I feel like in Mels video, shes already had like the little bit of a nudge at some point. Its getting to be a little bit more of a push. Now, as I was looking at the video that her, her next video after that. And not 100 sure because in the right up, it said that it was her first anxiety attack in six years, but she made it sound like it happened six months ago. Or something like that, not now, but she posted the video now. And it was her saying that she had an anxiety attack and its been like six years since shes had an anxiety attack. And Im watching this and Im like, yeah, not surprising after your last video. Right, because this is another one of those, those pieces like this old stuff is is kind of coming up and the more that you try and sort of push it down and go, yeah, yeah, yeah. Im not actually looking at this. Im not looking at this. This is the life that Ive created. This is the life Im going for and everything else. And I saw something weird with Jordan Peterson recently that I think will tie into this. At another point, like a standard, but its what I call, or there were pieces there in people who are normally very good and appear to be critical thinkers, like they able to think on their own feet. And but its like when when those things start to go. Or they dont they dont apply it in all areas. Then you have these other bits, which are like the tops on the shoulder or the no just that. Get worse. Yeah, yeah, yeah, and you know, the fight with the ego, you know, the ego does not want to leave. I find that that causes a lot of anxiety problems. Yeah. And a lot of this is so much around the ego, starting to take a backseat than anything else, right. True self, true self coming up to run the show. And you get the same anxiety. And its another one of those kind of. And to me, it was like a like a nod like yeah, this is this is this process thats actually going on because these are some of the things that Ive seen over and over and over again with people. Yeah. And I noticed in both of her videos, theres like wow, you know what this is going on for me and this really sucks. And its like shes sharing something thats very heartfelt. And then she flips and she said so these are the the five things that I do. Yeah, yeah, yeah, yeah, deal with this, which you know, I mean, its its what she does for a living, right. Like shes doing it because she genuinely wants to help people and everything else is absolutely nothing wrong with that. But its like this. Its almost like like Im watching like Im watching a football game, right. Its like yeah, yeah, yeah, yeah, yeah, no, yeah, I think of the post. Oh. Yeah. Yeah, its so its such a fascinating thing watching other people go through this. Cause you one, you know, its on the other side to, you know, its going to suck. I almost say its like a myriad of emotions that that I kind of go through, right. Its like I, my heart goes out to them. Im dying to like I watched that video. The first thing I wanted to do is like reach out to her and say, look, I would love to help you. This is the thing that youre going through. And you know, I would just want to help whatever I can do to help. Yeah. More than anything else. But everybody has to go through their, their process. And it was really beautiful that she actually chose to share how shes feeling. And I hope that she continues to document this, this process as she goes through it. And, you know, yeah. Also hope that its easy. Because it sounds like her whole like everything was falling apart. Like in a lot of ways her, you know, she had a TV show that got that got canceled her book deal got rescinded. here is the transcript: '''+ transcript,
    temperature=0.9,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    answer = response['choices'][0]['text'].strip()
    return answer


final_transcript = ""
model = whisper.load_model("base")

folder_path = 'videos/'

for video_file_path in os.listdir(folder_path):
    if video_file_path.endswith('.mp4'):

        # Extract audio from video and save it as a WAV file
        audio_file_path = os.path.splitext(folder_path + video_file_path)[0] + ".wav"
        clip = mp.VideoFileClip(folder_path + video_file_path)
        clip.audio.write_audiofile(audio_file_path)
        os.remove(folder_path + video_file_path)

        result = model.transcribe(audio_file_path)
        final_transcript = result["text"]
        os.remove(audio_file_path)


        if len(final_transcript) > 15000:
            final_transcript = summarize_text(final_transcript)
