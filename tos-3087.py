#!/usr/bin/python
# -*- coding:utf-8 -*-
from Tools import tools_v000 as tools
import os
from os.path import dirname
from MyHours import myhours as m


# -18 for the name of this project cafeAdministration
save_path = os.path.dirname(os.path.abspath("__file__"))
propertiesFolder_path = save_path + "/"+ "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'cafeAdministration', 'user_text=')

# Open Browser
tools.openBrowserChrome()

m.connectToMyHours()
m.enterCredentials()
m.startTrackWithDescription(u'TOS-3087', u'TOS-3087 - Work unforeseen CINS/IT4IT | ', u'RUN Life_CINS/IT4IT')

# Exit Chrome
tools.driver.quit()
