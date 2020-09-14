#!/usr/bin/env python3

import obspython as obs
import urllib.request
import urllib.error
import lxml

url         = ""
interval    = 30
source_name_text = ""
source_name_browser = ""

# ------------------------------------------------------------

def update_text():
	global url
	global interval
	global source_name_text
	global source_name_browser

	source = obs.obs_get_source_by_name(source_name_text)
	if source is not None:
		try:
			with urllib.request.urlopen(url) as response:
				data = response.read()
				txt = str(data)
				x = txt.find("\"videoId\"")
				y = x + 23
				y = txt[x:y]
				z = y.find(":") + 1
				extractvid = y[z:]
				newvid = extractvid.replace("\"","")
				newUrl = "https://www.youtube.com/watch?v="+newvid
				newchatUrl = "https://www.youtube.com/live_chat?dark_theme=1&is_popout=1&v="+newvid
				with urllib.request.urlopen(newUrl) as response2:
					data2 = response2.read()
					from lxml import etree
					youtube = etree.HTML(data2) 
					video_url = youtube.xpath("//title")
					video_text = video_url[0].text
					findu2b = video_text.find(" - YouTube")
					if findu2b >= 0:
						video_text = video_text[:findu2b]
					string_length=len(video_text)+2    # will be adding 2 extra spaces
					text=video_text.center(string_length)

				settings = obs.obs_data_create()
				obs.obs_data_set_string(settings, "text", text.encode('latin_1').decode('utf8'))
				obs.obs_source_update(source, settings)
				obs.obs_data_release(settings)

		except urllib.error.URLError as err:
			obs.script_log(obs.LOG_WARNING, "Error opening URL '" + url + "': " + err.reason)
			obs.remove_current_callback()

		obs.obs_source_release(source)

	sourceb = obs.obs_get_source_by_name(source_name_browser)
	if source is not None:
		try:
			#test
			settingsb = obs.obs_data_create()
			obs.obs_data_set_string(settingsb, "url", newchatUrl)
			obs.obs_source_update(sourceb, settingsb)
			obs.obs_data_release(settingsb)

		except urllib.error.URLError as err:
			obs.script_log(obs.LOG_WARNING, "Error opening URL '" + url + "': " + err.reason)
			obs.remove_current_callback()

		obs.obs_source_release(sourceb)		

def refresh_pressed(props, prop):
	update_text()

# ------------------------------------------------------------

def script_description():
	return "Updates a text source to the youtube title retrieved from a URL at every specified interval.\n\nBy HM"

def script_update(settings):
	global url
	global interval
	global source_name_text
	global source_name_browser

	url         = obs.obs_data_get_string(settings, "url")
	interval    = obs.obs_data_get_int(settings, "interval")
	source_name_text = obs.obs_data_get_string(settings, "source")
	source_name_browser = obs.obs_data_get_string(settings, "sourceb")

	obs.timer_remove(update_text)

	if url != "" and source_name_text != "" and source_name_browser != "":
		obs.timer_add(update_text, interval * 1000)

def script_defaults(settings):
	obs.obs_data_set_default_int(settings, "interval", 30)

def script_properties():
	props = obs.obs_properties_create()

	obs.obs_properties_add_text(props, "url", "Channel URL", obs.OBS_TEXT_DEFAULT)
	obs.obs_properties_add_int(props, "interval", "Update Interval (seconds)", 5, 3600, 1)

	p = obs.obs_properties_add_list(props, "source", "Text Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
	sources = obs.obs_enum_sources()
	if sources is not None:
		for source in sources:
			source_id = obs.obs_source_get_id(source)
			if source_id == "text_gdiplus" or source_id == "text_ft2_source":
				name = obs.obs_source_get_name(source)
				obs.obs_property_list_add_string(p, name, name)

		obs.source_list_release(sources)

	q = obs.obs_properties_add_list(props, "sourceb", "Browser Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
	sourcesb = obs.obs_enum_sources()
	if sourcesb is not None:
		for sourceb in sourcesb:
			source_id = obs.obs_source_get_id(sourceb)
			if source_id == "browser_source":
				nameb = obs.obs_source_get_name(sourceb)
				obs.obs_property_list_add_string(q, nameb, nameb)

		obs.source_list_release(sourcesb)

	obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)
	return props