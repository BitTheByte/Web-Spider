import re
import urllib2
import sys

Host = sys.argv[1]
html_triggers = [
'href=',
'src='
]



def Check_html(html):
	triggered_line = []
	for html_line in html.splitlines():
		for trigger in html_triggers:
				if trigger in html_line:
					triggered_line.append(html_line)
	return triggered_line
def Extract_links(html_filtered):
	return_data = []
	for line in html_filtered:
		line = line.strip("\n")
		for trigger in html_triggers:
			if trigger in line:
				full_trigger = trigger + "\"(.*?)\""									
				try:
					match = re.search(full_trigger,line).group()
					return_data.append(match)
				except Exception as e:
					continue
	return return_data
def Get_html(url):

	 return urllib2.urlopen(url).read()
def Check_response(url):
	print "Check url "+ str(url)
	try:
		c = urllib2.urlopen(url, timeout=30).getcode()
	except Exception as e:
		c = "timeout"
	return c
def Run_scan(Host):
	fetched_urls1 = Extract_links(Check_html(Get_html(Host)))
	complete_urls1 = []
	vaild_urls1 = {}
	temp1 = []
	for x in fetched_urls1:
		for regex_line in html_triggers:
			if regex_line in x:
				url_filterd = x.replace(regex_line,"")
				if url_filterd[:1] == '/':
					temp1.append(Host + url_filterd)
				else:
					temp1.append(url_filterd)
	for x in temp1:
		x = x.replace('"','')
		if(re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', x) is not None):
			complete_urls1.append(x)
		else:
			if x[:1] == '/' and x[1:2] != "/":
				complete_urls1.append(Host + x)
			else:
				complete_urls1.append(Host + '/' + x)
			if x[:2] == '//':
				complete_urls1.append("https:"+ x)
			else:
				complete_urls1.append(Host + '/' + x)
	for x in complete_urls1:
		response = Check_response(x)
		vaild_urls1[x] = response
	for x in vaild_urls1:
		print str(x) + " : " + str(vaild_urls1[str(x)])
Run_scan(Host)

""" Junck
fetched_urls = Extract_links(Check_html(Get_html(Host)))
complete_urls = []
vaild_urls = {}
temp = []
for x in fetched_urls:
		for regex_line in html_triggers:
			if regex_line in x:
				url_filterd = x.replace(regex_line,"")
				if url_filterd[:1] == '/':
					temp.append(Host + url_filterd)
				else:
					temp.append(url_filterd)
for x in temp:
		x = x.replace('"','')
		if(re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', x) is not None):
			complete_urls.append(x)
		else:
			if x[:1] == '/':
				complete_urls.append(Host + x)
			else:
				complete_urls.append(Host + '/' + x)
for x in complete_urls:
		response = Check_response(x)
		vaild_urls[x] = response
for x in vaild_urls:
	print str(x) + " : " + str(vaild_urls[str(x)])
	if vaild_urls[x] == 200:
		Run_scan(x)
"""
