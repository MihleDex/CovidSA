KV = '''
BoxLayout:
    orientation:'vertical'
    md_bg_color: app.theme_cls.bg_darkest

    MDToolbar:
        title: 'Covid-SA'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Cases'
            icon: 'virus-outline'

            FloatLayout:
                MDCard:
                    padding: "8dp"
                    size_hint:.9,.9
                    pos_hint: {"x": .05, "y": .05}

                    BoxLayout:
                        orientation:'vertical'
                        BoxLayout:
                            orientation:"horizontal"
                            Image:
                                source:"img/tube.png"
                            MDLabel:
                                text:"Tests Conducted"
                                font_style:"Button"

                            MDLabel:
                                text:app.tests
                                font_style:"H6"

                        BoxLayout:
                            orientation:"horizontal"
                            Image:
                                source:"img/covid.png"
                            MDLabel:
                                text:"Positive Cases"
                                font_style:"Button"

                            MDLabel:
                                text:app.cases
                                font_style:"H6"

                        BoxLayout:
                            orientation:"horizontal"
                            Image:
                                source:"img/death.png"
                            MDLabel:
                                text:"Deaths"
                                font_style:"Button"

                            MDLabel:
                                text:app.deaths
                                font_style:"H6"

                        BoxLayout:
                            orientation:"horizontal"
                            Image:
                                source:"img/health.png"
                            MDLabel:
                                text:"Recoveries"
                                font_style:"Button"

                            MDLabel:
                                text:app.recoveries
                                font_style:"H6"

                        


                
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'vaccinations'
            icon: 'needle'

            FloatLayout:
                MDCard:
                    padding: "8dp"
                    size_hint:.9,.9
                    pos_hint: {"x": .05, "y": .05}

                    BoxLayout:
                        orientation:"vertical"
                        BoxLayout:
                            orientation:"horizontal"
                            Image:
                                source:"img/vaccine.png"
                            MDLabel:
                                text:"Doses Administered"
                                font_style:"Button"

                            MDLabel:
                                text:app.vaccinated
                                font_style:"H6"


        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'about'
            icon: 'information-outline'

            
            MDLabel:
                text:"The information from this app is collected from https://sacoronavirus.co.za/ "
                pos_hint: {"x": .07, "y": .4}

        
'''

from kivy.lang import Builder
from kivymd.app import MDApp
import bs4
import requests as Req
from bs4 import BeautifulSoup as soup 


class SiteParser():
    list_values = []

    def __init__(self):
        self.myurl = "https://sacoronavirus.co.za/"
        self.uclient = Req.get(self.myurl)
        self.p_soup = soup(self.uclient.content,"html.parser")
        self.values = self.p_soup.find_all('span',class_='display-counter')
        for value in self.values:
            self.list_values.append(value['data-value'])

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        return Builder.load_string(KV)

    parser = SiteParser()
    tests = "{:,d}".format(int(parser.list_values[0]))
    cases = "{:,d}".format(int(parser.list_values[1]))
    recoveries = "{:,d}".format(int(parser.list_values[2]))
    deaths = "{:,d}".format(int(parser.list_values[3]))
    vaccinated = "{:,d}".format(int(parser.list_values[4]))


MainApp().run()