TC_PIM_01: 

Pages: 
	fp_page.py -- clicking forget password link
	rp_page.py -- Entering username and click reset
	
Tests: 
	Forget.py -- Opening chrome through webdriver and creating object and calling methods in fp_page.py and rp_page.py and generating html report using pytest.

Use this command to generate pytest report: pytest Forget.py  --html=report.html	
	
	
	
TC_PIM_02:

Pages: 
	loginpage.py-- Entering username, password and clicking login button
	adminpage.py -- Validating "OrangeHRM" title validation and validate the options displaying in admin page
	
Tests: 
	adminheader-test.py -- Opening chrome through webdriver and creating object and calling methods in loginpage.py and adminpage.py and generating html report using pytest.


Use this command to generate pytest report: pytest adminheader-test.py  --html=admin_test.html


	
TC_PIM_03:

Pages: 
	homepage.py-- Entering username, password and clicking login button
	adminsidepanel_page.py -- validate the below MENU options (on side panel) displaying in admin page
	
Tests: 
	admin_sidepanel_test.py -- Opening chrome through webdriver and creating object and calling methods in homepage.py and adminsidepanel_page.py and generating html report using pytest.


Use this command to generate pytest report: pytest admin_sidepanel_test.py  --html=admin_sidepanel.html
