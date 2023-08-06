import asyncio
from email import message
from nio import AsyncClient

async def SendMessage(message, roomid):
    try:
        userid = 'gsanas'
        password = 'Woyce@123'
        client = AsyncClient("https://stockly.ems.host", userid)
        await client.login(password)
        await client.room_send(
            room_id=roomid,
            message_type="m.room.message",
            content={
                "msgtype": "m.text",
                "body": "{}".format(message)
            }
        )
        await client.close()
    except Exception as e:
        print(e)

# roomId = "!cAMpKSOoWRZmBPetkc:stockly.ems.host"
# asyncio.run(SendMessage('Hello', roomId))
