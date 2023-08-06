
import logging
from xml import etree as et

log = logging.getLogger(__name__)

class Vmix():
    def __init__(self,connection=None):
        '''Give me an open handle to the port'''
        self.con = connection
        # self.state = et.getroot()
        self.state=''
        # SUBSCRIBE ACTS
        # SUBSCRIBE TALLY
        # XML
        # FUNCTION thing value
        # FUNCTION setText Input=1&SelectedName=Team%20Lineups.Text&Value=Hello
        # FUNCTION SetText Input=3&SelectedName=Headline&Value=Hello world\r\n
        # FUNCTION SetImageVisible Input=22&SelectedValue=Image1.Source
        # FUNCTION SetImageVisibleOff Input=22&SelectedValue=Image1.Source
        # http://127.0.0.1:8088/API/?Function=SetText&Input=6&SelectedName=P1%20Set%201&Value=GGGGGG

    def newXML(xml):
        '''Process and incoming XML'''
    def setField(field, value):
        '''Sets all instances of this field name to value '''
    def consume_pcs(data):
        ''' Callback to consume new PCS data '''
        