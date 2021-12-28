# -*- coding: utf-8 -*-
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import time
import xbmc, sys
xbmc.log(repr(sys.argv))

path = xbmc.translatePath(os.path.join('special://profile/addon_data/plugin.video.iptv/'))


if __name__ == '__main__':
    ADDON = xbmcaddon.Addon('plugin.video.iptv')

    version = ADDON.getAddonInfo('version')
    if ADDON.getSetting('version') != version:
	    ADDON.setSetting('version', version)

	    time.sleep(2)
	    xbmcvfs.copy('special://home/addons/plugin.video.iptv/resources/customTVGroups.xml','special://home/userdata/addon_data/pvr.iptvsimple/channelGroups/customTVGroups.xml')