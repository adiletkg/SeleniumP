from selenium import webdriver
a=webdriver.Firefox()
a.get("http://www.craigslist.org/about/sites")
link=a.find_element_by_link_text("manhattan")
link.click()
ass=a.find_element_by_link_text("my account")
ass.click()
inputusrs=a.find_element_by_name("inputEmailHandle")
inputusrs.send_keys("adilet_kg@outlook.com")
inpasscode=a.find_element_by_name("inputPassword")
inpasscode.send_keys("bishkek312")
button=a.find_element_by_xpath(".//*[@id='loginBox']/p[3]/button")
button.click()
selectcity=a.find_element_by_xpath(".//*[@id='pagecontainer']/section/form[2]/select")
selectcity.send_keys("madrid,es")
buttongo=a.find_element_by_xpath(".//*[@id='pagecontainer']/section/form[2]/input")
buttongo.click()
radiobyowner=a.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/blockquote/label[8]")
radiobyowner.click()
selectbyphone=a.find_element_by_name("contact_phone_ok")
selectbyphone.click()
inputphone=a.find_element_by_name("contact_phone")
inputphone.send_keys("3476663435")
inputname=a.find_element_by_name("contact_name")
inputname.send_keys("Manas")
inputpostitle=a.find_element_by_xpath(".//*[@id='PostingTitle']")
inputpostitle.send_keys("Toyota Prius")
inprice=a.find_element_by_xpath(".//*[@id='Ask']")
inprice.send_keys("5000")
postbody=a.find_element_by_id("PostingBody")
postbody.send_keys("I need Toyota Prius 2008")
buttonsubmit=a.find_element_by_xpath(".//*[@id='postingForm']/button")
buttonsubmit.click()
bigbut=a.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/button")
bigbut.click()
publish=a.find_element_by_xpath(".//*[@id='previewButtons']/form[1]/button")
publish.click()
a.get("http://www.outlook.com")
usname=a.find_element_by_xpath(".//*[@id='i0116']")
usname.send_keys("adilet_kg@outlook.com")
psword=a.find_element_by_xpath(".//*[@id='i0118']")
psword.send_keys("Bishkek312")
butsign=a.find_element_by_xpath(".//*[@id='idSIButton9']")
butsign.click()
linkcrack=a.find_element_by_xpath(".//*[@id='807934f9-8863-11e3-92ed-00215ad7b3ca']")
linkcrack.click()
linktopage=a.find_element_by_xpath(".//*[@id='mpf0_MsgContainer']/a[1]")
linktopage.click()












