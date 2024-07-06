# sql_injection_script
***
The script below is intended for educational purposes only and should not be used for malicious purposes of any kind, the sharing of knowledge in the cyber field is first and foremost for the purpose of protecting our assets as individuals and as business companies.
***

validation of web input text strings with selenium

- pip install selenium
- download chromedriver

  define the desired web page element like:   input_field = driver.find_element(By.NAME, "username")
  you also need to make a login to see the user page for getting the result so define the "login button" by the name element like:
          login_button = driver.find_element(By.CSS_SELECTOR, "button") 
  define the text string ("Log out") that show in the user page for positive result like:  if "Log out" in html_content:
  and than set a file text in the same directory that contaings the strings and replace the "strings.txt" as the filename
  with open("strings.txt", 'r') as file:

![image](https://github.com/Shai-Simchon/sql_injection_script/assets/117099263/27244505-ff9a-4cbd-ac53-4b08132665b4)
