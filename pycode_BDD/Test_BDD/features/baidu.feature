Feature: Gome Internet FlagsShip Store Fitting
	Scenario: The first behavior is user arrive in Login Page,after Check Page Element ,in the end Submit User private infomation Successful
		Given I go to "http://10.115.3.177:3860/toLogin.do"
		When I fill username in field with tag "input" and attribute "[@id='userCode']" and "ghj"
		And I fill password in field with tag "input" and attribute "[@id='password']" and "Ghj123456"
		And I fill auth in field with tag "input" and attribute "[@id='password']" and "{AUTO}"
		And I click tag "a" and attribute "[@class='login_btn']" with Gome Login once way
		#You maybe find a login error,because the auth was change every time,so I change another way -- cookies
		When I chose to use cookies "9CD3CFC689B820658027FBD551258831" for  login in "http://10.115.3.177:3860/index.do"
		And I want to enlarge this browser window
		Then I stand here for "2" seconds
		#HomePage model step Test
		When I arrive in system page,The first I click HomePage button tag "li" and attribute "[@id='nav_index']/a"
		And I click tag "a" and attribute "[@id='create_btn']" with Create HomePage immediately button
		And In the Page attribute windows,For PageType I want to chose tag "input" and attribute "[@name='page'and @value='index']"
		And In the Page attribute windows,For PageName I want to fill tag "dd" and attribute "[@id='pagePropertyName']/label[1]/input[1]" and written "cs009"
		And In the Page attribute windows,For PageKeyWord I want to fill tag "input" and attribute"[@id='pagePropertyKeyword']" and written "cs009"
		And In the Page attribute windows,For PageDescription I want to fill tag "textarea" and attribute "[@id='pagePropertyDesc']" and written "cs009"
		And In the Page attribute windows,Must input was over,So we have save this message,I will click tag "a" and attribute "[@id='pagePropertyType-ok']" to save this HomePage
		Then I stand here for "3" seconds
		#if this session submit successful,page will be arrive to PC Client Fitting
		When I arrive in PC-Client-Fitting page,The first I click Public_Model button tag "ul" and attribute "[@id='shopDecorate-side']/li[2]"
		And I will drag Dianzhao_tool_bar tag "ul" and attribute "[@id='shopDecorateModulesList']/li[1]/span[2]/img" to tag "ul" and attribute "[@id='shopDecorate-content-dianzhao']"
		And I will drag HengDaohang_tool_bar tag "ul" and attribute "[@id='shopDecorateModulesList']/li[2]/span[2]/img" to tag "ul" and attribute "[@id='shopDecorate-content-daohang']"
		Then Public Model was fit over, so we are begin to ZH_Model,I click Public_Model button tag "ul" and attribute "[@id='shopDecorate-side']/li[3]"
		And I stand here for "3" seconds
		And I will drag DANTU_tool_bar tag "ul" and attribute "[@id='shopDecorateModulesList']/li[2]/span[2]/img" to tag "ul" and attribute "[@id='shopDecorate-content']"
		Then I stand here for "2" seconds
		Then This Template tag "li" and attribute "[@id='pageSave']" will be saved "True"
		Then I stand here for "1" seconds
		#this template was complate(We do not upload Img,because we will do it in the Picture library Model
		#Let's go to Picture Library to auto test
		When I want to go to click tag "li" and attribute "[@id='nav_image']/a" button
		And I want to upload to local picture tag "p" and attribute "[@id='upload']/input",and send file "G:\pycode_BDD\Test_BDD\Atuo.jpg"
		And I will be click one_click_upload button tag "div" and attribute "[@id='zwb_upload_status']/div/div[3]/span[1]" to uploading
		And If upload successful,I will click close button tag "div" and attribute "[@id='zwb_upload_status']/div/div[3]/span[2]" to over uploading
		# this picture was conplate,I will go to Product Manage
		When I will go to Product Manage with tag "li" and attribute "[@id='nav_product']/a"
		And I stand here for "1" seconds
		And I am arriving Product Manage Page,The first,I will fill classify name tag "input" and attribute "[@id='addCategoryText']" to written "cs009"
		And I am click add classify button tag "a" and attribute "[@onclick='addCategory()']"
		Then I stand here for "1" seconds
		And Now I was build a first classify,So I will build a second classify tag "div" and attribute "[contains(@class,'clickOne')]"
		Then I stand here for "1" seconds
		And I will click add "div" and attribute "[contains(@class,'clickOne')]/i[3]"
		Then I stand here for "1" seconds
		And I will fill in second classify tag "dd" and attribute "[@class='changT chT']/form/input" and written "cs009"
		And I click submit to save the second classify tag "a" and attribute "[@class='pSure']"
		And I will click Import Button tag "p" and attribute "[@id='import']"
		And alert a Input window,I will click chose classify tag "select" and attribute "[@id='oneC']"
		And I stand here for "1" seconds
		And In the ImportFrame I will chose the newest classify tag "select" and attribute "[@id='oneC']/option"
		And I stand here for "1" seconds
		And In the ImportFrame I will click the second classify tag "select" and attribute "[@id='twoC']"
		And So I will be chose second classify tag "select" and attribute "[@id='twoC']/option"
		And In the end,I will be upload a tag "input" and attribute "[@id='excel']" Excel file ,this path is "G:\pycode_BDD\Test_BDD\temp.xlsx"
		Then I click make sure Import Button to save this Import Product tag "a" and attribute "[@id='submint']"
		And I stand here for "2" seconds
		And If upload was succesful,This system was alert Import Successful "True"
		Then I click close Button to close this window tag "span" and attribute "[@id='close']"
		# This Product Manage was test over,in the future This model will be fix so much better
		# In the next Step ,we will go to test Page manage
		When I will be go to Page Manage,I will click tag "li" and attribute "[@id='nav_page']/a"
		And I arrive in the Page Manage,The first I fill in page name tag "input" and attribute "[@id='title']" and written "cs009"
		And I want to search this Page,I click button tag "div" and attribute "[@id='pageCon-btn']/input[1]"
		And I will click fitting Button tag "a" and attribute "[@class='btn-link']"
		Then I stand here for "2" seconds
		And I want to replace dzqy picture,so I click button tag "img" and attribute "[@usemap='#Map1' and @ref='imageMaps']"
		Then I stand here for "2" seconds
		And In the forward step,system alert a Frame,I want to replace Picture tag "span" and attribute "[@class='change']"
		Then I stand here for "2" seconds
		And If I click change place,system will be alert upload picture,I chose the first IMG "ul" and attribute "[@id='picModifyBox-imagelist']/li[1]"
		And The picture was chosed,I click OK to save tag "a" and attribute "[@id='picModifyBox-ok']"
		And I am click OK too,because This Picture was enable tag "a" and attribute "[@id='btn-ok-image']"
		#double chose picture, zong he mu ban place replace IMG
		Then I stand here for "3" seconds
		And I want to replace dzqy picture,so I click button tag "*" and attribute "[@id='shopDecorate-content']/li/div/div/div/ul/li[1]/a/img"
		Then I stand here for "2" seconds
		And In the forward step,system alert a Frame,I want to replace Picture tag "span" and attribute "[@class='change']"
		Then I stand here for "2" seconds
		And If I click change place,system will be alert upload picture,I chose the first IMG "ul" and attribute "[@id='picModifyBox-imagelist']/li[1]"
		Then I stand here for "1" seconds
		And The picture was chosed,I click OK to save tag "a" and attribute "[@id='picModifyBox-ok']"
		And I am click OK too,because This Picture was enable tag "a" and attribute "[@id='btn-ok-image']"
		#Pictur was replaced,I am starting to save this model
		Then I stand here for "1" seconds
		And I am click save this model to save tag "*" and attribute "[@id='pageSave']"
		Then I stand here for "3" seconds
		And If saving is successful,system alert "True",I was accept it
		Then I stand here for "1" seconds
		When all model was complate,I will be starting commit audit tag "*" and attribute "[@id='pageExamine']"
		Then I stand here for "3" seconds
		And If saving is successful,system alert "True",I was accept it
		And I am closing current window
		# I closing PC fitting window , and I will open preview window
		# I will check this page in the  url   http://10.115.3.177:3860/bfsPage/list.do
		Then I stand here for "1" seconds
		When I will goto url "http://10.115.3.177:3860/bfsPage/check.do" and This written "cs009" tag "div" and attribute "[@class='content_tab']/table[1]/tbody[1]/tr[1]/td[1]", return Check suceessful
		Then I stand here for "1" seconds
		When I will be click preview button,system will be alert new window tag "a" and attribute "[@class='btn-link']"


