def test_result_count(self):
        #load the page you want to test
        self.driver.get("https://atg.world/")

        # get the search textbox
        search_field = self.driver.find_element_by_name("")
        search_field.clear()

        #enter search text and submit
        search_field.send_keys("Automated Testing")
        search_field.submit()

        #xpath for search result titles
        search_output_title_xpath = "//h3[@class='LC20lb']"

        #Wait 10 seconds for the results
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, search_output_title_xpath)))

        page1_result_titles = self.driver.find_elements(By.XPATH, search_output_title_xpath)

        #printing the search result headers
        #this is NOT part of automated testing
        #this is for our reference only - we don't use print inside tests
        for item in page1_result_titles:
            print(item.text)

        #this is the actual test we do
        #assert (check) if the number of results returned is greater than 5
        self.assertGreater(len(page1_result_titles), 5)