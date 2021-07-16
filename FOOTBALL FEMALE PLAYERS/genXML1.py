# Import all the necessary modules
import string
from hashlib import sha1
from datetime import datetime

# Change below siteinfo if a different website is picked
# The following siteinfo can be obtained from the XML file downloaded from the mediawiki
tewiki = ''' <mediawiki xml:lang="te" version="0.10" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.mediawiki.org/xml/export-0.10/">
    <siteinfo>
        <sitename>tewiki</sitename>
        <dbname>indicwiki</dbname>
        <base>https://tewiki.iiit.ac.in/index.php?title=%E0%B0%AE%E0%B1%8A%E0%B0%A6%E0%B0%9F%E0%B0%BF_%E0%B0%AA%E0%B1%87%E0%B0%9C%E0%B1%80</base>
        <generator>MediaWiki 1.34.0</generator>
        <case>first-letter</case>
        <namespaces>
            <namespace case="first-letter" key="-2">మీడియా</namespace>
            <namespace case="first-letter" key="-1">ప్రత్యేక</namespace>
            <namespace case="first-letter" key="0"/>
            <namespace case="first-letter" key="1">చర్చ</namespace>
            <namespace case="first-letter" key="2">వాడుకరి</namespace>
            <namespace case="first-letter" key="3">వాడుకరి చర్చ</namespace>
            <namespace case="first-letter" key="4">Project</namespace>
            <namespace case="first-letter" key="5">Project చర్చ</namespace>
            <namespace case="first-letter" key="6">దస్త్రం</namespace>
            <namespace case="first-letter" key="7">దస్త్రంపై చర్చ</namespace>
            <namespace case="first-letter" key="8">మీడియావికీ</namespace>
            <namespace case="first-letter" key="9">మీడియావికీ చర్చ</namespace>
            <namespace case="first-letter" key="10">మూస</namespace>
            <namespace case="first-letter" key="11">మూస చర్చ</namespace>
            <namespace case="first-letter" key="12">సహాయం</namespace>
            <namespace case="first-letter" key="13">సహాయం చర్చ</namespace>
            <namespace case="first-letter" key="14">వర్గం</namespace>
            <namespace case="first-letter" key="15">వర్గం చర్చ</namespace>
            <namespace case="first-letter" key="120">Item</namespace>
            <namespace case="first-letter" key="121">Item talk</namespace>
            <namespace case="first-letter" key="122">Property</namespace>
            <namespace case="first-letter" key="123">Property talk</namespace>
            <namespace case="first-letter" key="482">Config</namespace>
            <namespace case="first-letter" key="483">Config talk</namespace>
            <namespace case="first-letter" key="710">TimedText</namespace>
            <namespace case="first-letter" key="711">TimedText talk</namespace>
            <namespace case="first-letter" key="828">మాడ్యూల్</namespace>
            <namespace case="first-letter" key="829">మాడ్యూల్ చర్చ</namespace>
            <namespace case="first-letter" key="2300">Gadget</namespace>
            <namespace case="first-letter" key="2301">Gadget talk</namespace>
            <namespace case="case-sensitive" key="2302">Gadget definition</namespace>
            <namespace case="case-sensitive" key="2303">Gadget definition talk</namespace>
            <namespace case="first-letter" key="2600">Topic</namespace>
            <namespace case="first-letter" key="3022">Tewiki</namespace>
            <namespace case="first-letter" key="3023">Tewiki talk</namespace>
        </namespaces>
    </siteinfo>\n'''
# Initialize the global variables
# Intialize the page_id such that it does not conflict with other wikipages

page_id = 530000

user_id='18114'
username='V.Abhinaya'

# Functions to write page to file object

def sha36(page_id):
    page_id = str(page_id).encode('utf-8')
    sha16 = sha1(page_id).hexdigest()
    sha10=int(sha16,16)

    chars=[]
    alphabets=string.digits+string.ascii_lowercase
    while sha10>0:
        sha10,r=divmod(sha10,36)
        chars.append(alphabets[r])

    return ''.join(reversed(chars))

# Function to replace the entity references

def modify(text):
    text = text.replace('&',"&amp;")
    text = text.replace('<',"&lt;")
    text = text.replace('>',"&gt;")
    text = text.replace('"',"&quot;")
    text = text.replace("'","&apos;")
    return text

def writepage(title,wikitext,fobj):
    global user_id,username
    
    pglen=len(wikitext)
    text = modify(wikitext)
    time=datetime.now().strftime('%Y-%m-%dT%H-%M-%SZ')
    
    curPage ='''\n\n
	<page>
	    <title>''' +title +'''</title>
            <ns>0</ns>
	    <id>''' +str(page_id) +'''</id>
	    <revision>
		<id>''' +str(page_id) +'''</id>
		<timestamp>'''+time+'''</timestamp>
		<contributor>
		<username>''' +username +'''</username>
		    <id>''' +str(user_id) +'''</id>
		</contributor>
		<comment>xmlpage created</comment>
		<model>wikitext</model>
		<format>text/x-wiki</format>
		<text xml:space="preserve" bytes="''' +str(pglen) +'''">
                    \n''' +text +'''
		</text>
		<sha1>''' +sha36(page_id) +'''</sha1>
	    </revision>
	</page>
	\n\n'''

    fobj.write(curPage)
    return

    
