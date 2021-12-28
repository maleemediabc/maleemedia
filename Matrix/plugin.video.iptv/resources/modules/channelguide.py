import xbmc 
import time



#xbmc.executebuiltin("ActivateWindow(Home)")
time.sleep(1)

xbmc.executebuiltin("RunAddon(plugin.video.3satmediathek)")
xbmc.executebuiltin("ActivateWindow(TVGuide)")
#xbmc.executebuiltin("StopScript(special://home/addons/plugin.video.iptv/resources/modules/channelguide.py)")


