import time
import xbmc

class lazy_logger(object):
	''' adds addon specific logging to xbmc.log '''


	def __init__(self, addon, addonid, logging_enabled):
		self.addon       = addon
		self.addonid     = addonid
		self.keep_logs   = logging_enabled
		self.base_time   = time.time()
		self.start_time  = time.time()


	def post_log(self, message, label = '', reset = False):

		if self.keep_logs:

			new_time    	= time.time()
			gap_time 		= "%5f" % (new_time - self.start_time)
			total_gap  		= "%5f" % (new_time - self.base_time)
			self.base_time  = start_time if reset else self.base_time
			self.start_time = new_time

			xbmc.log(msg = '{} service : {} :: {} ::: {} - {} '.format(self.addonid, total_gap, gap_time, label, message) )

	def logging_switch(self, switch):

		self.keep_logs = switch

	def lang(self, id):

		return self.addon.getLocalizedString(id).encode( 'utf-8', 'ignore' )


class setting_cleaner(object):

	def __init__(self, setting_function):
		self.setting_function = setting_function
		self.id_dict = {
		'playlist_notifications': 'notify',
		}

	def clean(self, setting_id):
		if setting_id in self.id_dict.keys():
			setting_id = self.id_dict.get(setting_id,setting_id)

		value = self.setting_function(setting_id)

		if value == 'true':
			value = True 
		elif value == 'false':
			value = False
		else:
			try:
				value = int(float(value))
			except:
				pass

		return value


