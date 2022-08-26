from ast import While
import requests
#'MTAxMTgyNDkwODQwMzIxMjM3MA.Gv-_av.dXK96MY3H7Spn2p_V8ukvdpypUms8cFgnflZi8'
#"MTAxMTg5NTE4NTIyNTAzMTczMQ.G9ukEV.vdgp-2AFjjrfM05KTfPqVkJKALvyiXQRnhmP7o" mokoko
headers = {"authorization":  "MTAxMTg5NTE4NTIyNTAzMTczMQ.G9ukEV.vdgp-2AFjjrfM05KTfPqVkJKALvyiXQRnhmP7o"}

file = open("text.txt", "r")
lines = file.readlines()


while True:
    for line in lines:
        requests.post(f"https://discord.com/api/v9/channels/953513830691008533/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/953513830691008533/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/953519962973175900/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/995886225233805343/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/957891751979397160/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/981372945765118006/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/990129242102718485/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/953520313591820309/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/1002729990426742877/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/978443060327370782/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/958491972895637524/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/955324794180612146/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/964407197444489247/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/1011363979949506681/messages", headers = headers, json = {"content":line})
        # requests.post(f"https://discord.com/api/v9/channels/981805041604235285/messages", headers = headers, json = {"content":line})
        
        


