from lxml import etree
from urllib.parse import urlencode
import requests,json,csv

def get_index(num):
	data={
		'limit':'20',
		'offset':num
	}
	header = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	}
	url = 'https://zhuanlan.zhihu.com/api/columns/hemingke/posts?' + urlencode(data)
	html = requests.get(url,headers = header)
	if html.status_code == 200:
		return html.text
	return None
	

def main():
	for i in range(20):
		print('正在处理第'+ str(i) +'页数据')
		html = get_index(i*20)
		projson = json.loads(html)
		write_csv(projson)
		print('第'+ str(i) +'页数据处理完成')


def write_csv(pro):
	for item in pro:
		with open('data.csv','a', newline='') as csvfile:
			csv_write = csv.writer(csvfile)
			csv_write.writerow([item['title'],item['url'],item['titleImage'],item['commentsCount'],item['likesCount'],item['publishedTime']])
			csvfile.close()


if __name__ == '__main__':
 	main()
