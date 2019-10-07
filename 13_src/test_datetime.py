import datetime
import locale

locale.setlocale(locale.LC_ALL, 'zh_CN')

dt = datetime.datetime.now()

print(dt.strftime('%A %d %B %Y %H:%M'))
