import vk_api
import time
from datetime import datetime

while True:
	vk = vk_api.VkApi(token="vk1.a.dY1Xe-1oShvWHIQyf-x_joD2wvQVrVEEBmktf6z1FzQL2OfN-JspI646Xib8j6Vk5dXH_AcCySyTQItJauZ5XpEKI03Y4YMBwAdf3XIGZjFtMujwr-3HWlco8nTRWaTri2bkF5pacXqDtocoP0wGCxluxTqxFrBhM4BGWRZaXxbeeLLX9j5QN82QrLzTWHiVJnG0sF8aqZGGmFKPcVOTAw")
	some_date = datetime(2022, 11, 30)
	now_date = datetime.now()
	a = some_date - now_date
	vk.method("status.set", {"text": "☆💘Навсегда!😍❣ Прошло " + str(a.days) + " дней" })
	time.sleep(60)
	vk.method("status.set", {"text": "★💘Навсегда!😍❣ Прошло " + str(a.days) + " дней" })
	time.sleep(60)
	vk.method("status.set", {"text": "✯💘Навсегда!😍❣ Прошло " + str(a.days) + " дней" })
	time.sleep(60)
	vk.method("status.set", {"text": "✡💘Навсегда!😍❣ Прошло " + str(a.days) + " дней" })
	time.sleep(60)