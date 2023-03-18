import json, requests


async def react(bot, message):
    with open(r"./resources/reactions.json") as f:
        react_dict = json.loads(f.read())
        try:
            react_dict[str(message.guild.id)]
        except KeyError:
            return

    for element in react_dict[str(message.guild.id)]:
        if element in message.content.lower():
            await message.add_reaction(react_dict[str(message.guild.id)][element])


async def ai_chat(bot, message):
    res = requests.get(
        f'https://api.monkedev.com/fun/chat?msg=${"+".join(message.content)}&uid={message.author.id}&key=hPfSppLiteKFZYiBckOMXDYsT'
    )
    response = json.loads(res.text)
    fact = response.get("response")

    await message.reply(fact)
