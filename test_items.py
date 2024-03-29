from selenium.webdriver.common.by import By

def test_tes(browser):        

    url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(url=url)
    
    element = browser.find_element(By.CSS_SELECTOR,"#add_to_basket_form > button").text
    
    assert (element) == "Добавить в корзину", "Сравнение текста" 
    if __name__ == "__main__":
       print("Кнопка есть и текст совпадает")
 