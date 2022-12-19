import vk_api
import time
from datetime import datetime

while True:
	vk = vk_api.VkApi(token="vk1.a.20xhwAYo7mX15E3MixEkspc9SwLD0WbFS9EbniiEr1jHrx7_oxjnF7NCewyUqgYmjkBb35_JTX647g-BhRW7QnnuPyP1kBkzjSWVbji-m7MihYL-O-aXBBFhPj7QykzelOTvG5CV_OZf6lGIEAKi52LO-TjLye7Trt_rhYM0dbFnu-uQuEnCsgsAeedpe55fcgi_MSmr-zqtS46TZUK8JQ")
	some_date = datetime(2022, 11, 30)
	now_date = datetime.now()
	a = some_date - now_date
	vk.method("status.set", {"text": "☆💖Бесконечно?🥺❣ Прошло " + str(a.days) + " дней" })
	time.sleep(60)
	vk.method("status.set", {"text": "★💖Бесконечно?🥺❣ Прошло " + str(a.days) + " дней" })
	time.sleep(60)
	vk.method("status.set", {"text": "✯💖Бесконечно?🥺❣ Прошло " + str(a.days) + " дней" })
	time.sleep(60)
	vk.method("status.set", {"text": "✡💖Бесконечно?🥺❣ Прошло " + str(a.days) + " дней" })
	time.sleep(60)