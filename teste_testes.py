from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class auto_tests(unittest.TestCase):

    def precondition(self):
        return webdriver.Firefox()

    def access(self, driver):
        driver.get("https://testlink.org/")

    def tests(self, driver):
        # Title
        title = driver.title
        self.assertEqual(title, "TestLink", "Title incorrect!")

        # First text frame
        text = driver.find_element(By.XPATH, '/html/body/div/div[2]/h1').text
        self.assertEqual(text, "TestLink Open Source Test Management", "Text incorrect!")

        # Footer text
        footerText = driver.find_element(By.CLASS_NAME, 'footer').text
        self.assertNotEqual(footerText, "Other text", "Diferent text!")

    def goToGitHub(self, driver):
        # Going to the repository
        link_github = driver.find_element(By.LINK_TEXT, 'Access Git Repository (GitHub)').get_attribute("href")
        driver.get(link_github)

    def testsGitHub(self,driver):
        # Title
        title = driver.title
        self.assertEqual(title, "GitHub - TestLinkOpenSourceTRMS/testlink-code at testlink_1_9_20_fixed", "Title incorrect!")
       
        #Reposittory Title
        repoTitle = driver.find_element(By.CLASS_NAME, "author").text
        self.assertEqual(repoTitle, "TestLinkOpenSourceTRMS", "Incorrect repo title!")

    def searchGitHub(self, driver):
        # Search by Lemont037 on Github
        searchBox = driver.find_element(By.NAME, 'q')
        searchBox.send_keys("Lemont037")
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "jump-to-suggestion-search-global"))).click()
        # Clicking in Users
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Users')]"))).click()
        # Click on Leonardo Monteiro
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Leonardo Monteiro'))).click()

        # Testing page
        # Repository's username
        userRepoName = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'p-name'))).text
        self.assertEqual(userRepoName, "Leonardo Monteiro", "Repository's username incorrect!")

    def poscondition(self, driver):
        driver.close()
        driver.quit()

if __name__ == '__main__':
    t = auto_tests()
    driver = t.precondition()
    t.access(driver)
    try:
        # TestLink
        t.tests(driver)
        # GitHub
        t.goToGitHub(driver)
        t.testsGitHub(driver)
        t.searchGitHub(driver)
    except ValueError:
        print(ValueError)
    finally:
        t.poscondition(driver)
