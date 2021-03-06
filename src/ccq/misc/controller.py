#
#  Copyright (c) 2017 Helmut Merz helmutm@cy55.de
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

"""
View controllers for the CCQ_... skins.
"""

from zope.browserpage.viewpagetemplatefile import \
        ViewPageTemplateFile, BoundPageTemplate

from cco.skin.r2.controller import Controller as BaseController


mainTemplate = ViewPageTemplateFile('main.pt')
mainTemplateFB = ViewPageTemplateFile('free-brass/main-fb.pt')


class Controller(BaseController):

    def setMainPage(self):
        self.view.index = BoundPageTemplate(mainTemplate, self.view)


class ControllerFB(BaseController):

    def setMainPage(self):
        self.view.index = BoundPageTemplate(mainTemplateFB, self.view)

