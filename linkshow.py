#@title Paste Link Address from Above and Insert Search Terms
#@markdown ### 1st Category -->
Copied_Link_url1 = "https://media.sciencephoto.com/image/c0389506/800wm/C0389506-Low_grade_invasive_ductal_breast_cancer,_light_micrograph.jpg" #@param {type:"string"}
search_Keywords1= "breast ductal carcinoma" #@param {type:"string"}
Site_to_Search1 = ""  #@param ["http://atlas.gechem.org/", "https://askhematologist.com/","https://www.pathpedia.com/","https://histologylab.ctl.columbia.edu/lab07/hematopoiesis/","https://allaboutblood.com/",""]
#@markdown ### 2nd Category -->

Copied_Link_url2 = "https://www.webpathology.com/slides-13/slides/Breast_LobularCA38.jpg" #@param {type:"string"}
search_Keywords2 = "invasive lobular carcinoma" #@param {type:"string"}
Site_to_Search2 = ""  #@param ["http://atlas.gechem.org/", "https://askhematologist.com/","https://www.pathpedia.com/","https://histologylab.ctl.columbia.edu/lab07/hematopoiesis/","https://allaboutblood.com/",""]
#@markdown ### Run The Code Cell To Get the Visually Similar Image Links





from IPython.display import HTML
import copy
def get_similar_image_link_w_driver(Copied_Link_url,search_Keywords,Site_to_Search,cat):
  driver = webdriver.Chrome('chromedriver',options=options)
  driver.get("https://www.google.com/") 

  driver.set_window_size(1000, 775)    # Test name: test

  element = driver.find_element(By.LINK_TEXT, "Images")

  actions = ActionChains(driver)

  actions.move_to_element(element).perform()

  driver.find_element(By.LINK_TEXT, "Images").click()

  driver.find_element(By.CSS_SELECTOR, ".BwoPOe").click()
  driver.find_element(By.ID, "Ycyxxc").send_keys("")
  driver.find_element(By.ID, "Ycyxxc").send_keys(Copied_Link_url)

  driver.find_element(By.ID, "Ycyxxc").send_keys(Keys.ENTER)
  driver.find_element(By.NAME, "q").click()

  driver.find_element(By.NAME, "q").clear()
  if Site_to_Search == "":
    driver.find_element(By.NAME, "q").send_keys(search_Keywords)
  else:
    driver.find_element(By.NAME, "q").send_keys(search_Keywords+" site:"+Site_to_Search)
  driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
  driver.find_element(By.NAME, "q").click()

  #driver.find_element(By.CSS_SELECTOR, ".gbqfb").click()
  driver.find_element(By.LINK_TEXT, "Visually similar images").click()
  url1 = driver.current_url


  print(search_Keywords)
  link1 = '<i><b><h2><font size=18> <a href="{0}" target="_blank">{1}</a></font></b></i>'.format(url1, "Similar Images For Category "+cat)
  print(link1)
  return link1, driver

link1, driver1 = get_similar_image_link_w_driver(Copied_Link_url1,search_Keywords1,Site_to_Search1,"1")
link2, driver2 = get_similar_image_link_w_driver(Copied_Link_url2,search_Keywords2,Site_to_Search2,"2")

HTML(link1+link2)

