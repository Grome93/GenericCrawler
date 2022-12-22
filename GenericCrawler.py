from selenium import webdriver
import pandas as pd
import os
import sys

class GenericInterface:
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.target_path = "./data"
        self.target_path_windows = os.getcwd() + "\\data"
        self.base_url = "https://www.zwift.com/"
        self.driver = webdriver
        self.result_list = []
        self.login_expanse = "eu-de/sign-in?origin=shopify"
        self.workout_expanse = "eu-de/activity/1238531693430718480"
        self.username = "jerome.reich@hotmail.de"
        self.password = "783518Bb!!"
        self.wordout_id = "1238531693430718480"


    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %%%%%%%%%%%%%%% SET %%%%%%%%%%%%%%%%%
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #def set_keyword(self, keyword):
    #    self.keyword = keyword

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %%%%%%%%%%%%%%% GET %%%%%%%%%%%%%%%%%
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #def get_keyword(self):
    #    return self.keyword


    def get_list_from_id(self):
        getSellerUrl_id = "sellerProfileTriggerId"
            temp_seller_url = self.driver.find_element_by_id(getSellerUrl_id).get_property("href")
            self.driver.get(search_url)
            products = self.driver.find_elements_by_class_name(getHref_class)
            for temp_product in products:
                try:
                    temp_url = temp_product.get_property("href")
                    self.product_urls.append(temp_url)
                    self.append_entry2data(column="Product_URL", value=temp_url)
                except:
                    print("Error 1: TBD")
        else:
            for temp_page in range(int(self.first_page), int(self.last_page), 1):
                search_url = self.url + "s?k=" + self.keyword + "&page=" + str(temp_page)
                getHref_class = "a-link-normal.s-no-outline"
                # Process
                self.driver.get(search_url)
                products = self.driver.find_elements_by_class_name(getHref_class)
                for temp_product in products:
                    try:
                        temp_url = temp_product.get_property("href")
                        self.product_urls.append(temp_url)
                        self.append_entry2data(column="Product_URL", value=temp_url)
                    except:
                        print("Error 1: TBD")
        #self.save_list("product_urls", self.product_urls)
        self.save_data()

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %%%%%%%%%%% LOAD & SAVE %%%%%%%%%%%%%
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def load_data(self):
        textfile = open(self.target_path + "/data_" + self.keyword + ".csv", "w")
        for item in list:
            textfile.write(str(item)+ "\n")
        textfile.close()

    def save_data(self):
        self.data.to_csv(self.target_path + "/data_" + self.keyword + ".csv")

    def save_list(self, name, list):
        textfile = open(self.target_path + "/" + self.keyword + "_p" + str(self.current_page) + "_" + name + ".csv", "w")
        for item in list:
            textfile.write(str(item)+ "\n")
        textfile.close()

    def load_list(self, name):
        with open(self.target_path + "/" + self.keyword + "_p" + str(self.current_page) + "_" + name + ".csv") as f:
            lines = f.readlines()
        f.close()
        return lines

    def load_seller(self):
        with open(self.target_path + "/" + self.keyword + "_p" + str(self.current_page) + "_" + self.seller_urls_file_name + ".csv") as f:
            self.seller_urls = f.read().splitlines()
        f.close()

    def load_products(self):
        file_path = self.target_path + "/" + self.keyword + "_p" + str(self.current_page) + "_" + self.product_urls_file_name + ".csv"
        if os.path.exists(file_path):
            with open(file_path) as f:
                self.product_urls = f.read().splitlines()
            f.close()
        else:
            return "No such file or directory: " + file_path

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %%%%%%%%%%%%%%% HELPER %%%%%%%%%%%%%%
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def start_webdriver(self):
        #gecko_path =  "C:\\Users\\jerom\\Documents\\PycharmProjects\\AmazonAS\\install\\geckodriver.exe"
        fxProfile = webdriver.FirefoxProfile()
        fxProfile.set_preference('browser.download.manager.showWhenStarting', False)
        fxProfile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream')
        fxProfile.set_preference("browser.download.folderList", 2)
        fxProfile.set_preference("browser.download.dir", self.target_path_windows)
        driver = webdriver.Firefox(firefox_profile=fxProfile)
        driver.implicitly_wait(5)
        driver.maximize_window()
        #page.minimize_window()
        self.driver = driver


    def login(self):
        self.driver.get(self.base_url + self.login_expanse)
        # find username/email field and send the username itself to the input field
        driver.find_element("id", "email-input").send_keys(username)
        # find password input field and insert password as well
        driver.find_element("id", "password-input").send_keys(password)
        # click login button

    def list2table(self, list):
        table_entry = pd.DataFrame([["NaN"]*self.data_columns.__len__()], columns=self.data_columns)
        for item in list:
            if item[0] in table_entry:
                new_entry = pd.DataFrame({item[0]: [item[1]]})
            else:
                temp_extend = table_entry["Sonstiges"] + "\n" + item[0]
                new_entry = pd.DataFrame({"Sonstiges": [temp_extend]})
            table_entry.update(new_entry)
        table_entry.to_csv("tt.csv")
        return table_entry



if __name__ == "__main__":
    contact_interface = GenericInterface()
    contact_interface.start_webdriver()
    contact_interface.login()
