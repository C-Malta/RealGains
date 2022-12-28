from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)
from selenium.webdriver.common.by import By

fedreserv = 'https://www.federalreserve.gov/releases/h6/current/default.htm'
browser.get(fedreserv)




def convert_raw_date(input):



     date_array = input.split('-')

     unconverted_day = date_array[2]

     def remove_zero(input):
      conversion = ""
      for number in input:
        if number == "0":
             conversion = conversion
        else:
             conversion = conversion + number
        return conversion

     converted_first_digit_day = remove_zero(unconverted_day[0])

     day = converted_first_digit_day + unconverted_day[1]


     unconverted_month = date_array[1]

     def remove_zero(input):
         conversion = ""
         for number in input:
             if number == "0":
                 conversion = conversion
             else:
                 conversion = conversion + number
             return conversion

     converted_first_digit_month = remove_zero(unconverted_month[0])

     month = converted_first_digit_month + unconverted_month[1]

     results = month + "/" + day + "/" + date_array[0]
     return results



from fredapi import Fred

FRED_API_KEY = '944b898e6ddc56dfbba1c666470e3511'
fred = Fred(api_key=FRED_API_KEY)

def remove_comma(input):
    result = ""
    for thing in input:
        if thing ==",":
            result = result
        else:
            result = result + thing
    return result


def calculate_real_gains(past_unit_price_input, past_unit_price_input_date, unit_price_input):
    pastm2 = fred.get_series('M2', past_unit_price_input_date)[0] * (10 ** 9)
    latest_m2_data = (float((remove_comma((browser.find_element(By.XPATH, "/html/body/div[3]/div[4]/table/tbody/tr[last()]/td[2]").text))))) * (10 ** 9)

    past_unit_price_to_pastm2 = float(past_unit_price_input) / pastm2
    present_unit_price_to_m2 = float(unit_price_input) / latest_m2_data
    return int((present_unit_price_to_m2/past_unit_price_to_pastm2)*100)-100

def calculate_nominal_gains(past_unit_price_input, unit_price_input):
    result = int((unit_price_input/past_unit_price_input)*100)-100
    return result


     unconverted_month = date_array[1]

     def remove_zero(input):
         conversion = ""
         for number in input:
             if number == "0":
                 conversion = conversion
             else:
                 conversion = conversion + number
             return conversion

     converted_first_digit_month = remove_zero(unconverted_month[0])

     month = converted_first_digit_month + unconverted_month[1]

     results = month + "/" + day + "/" + date_array[0]
     return results



from fredapi import Fred

FRED_API_KEY = '944b898e6ddc56dfbba1c666470e3511'
fred = Fred(api_key=FRED_API_KEY)

def remove_comma(input):
    result = ""
    for thing in input:
        if thing ==",":
            result = result
        else:
            result = result + thing
    return result


def calculate_real_gains(past_unit_price_input, past_unit_price_input_date, unit_price_input):
    pastm2 = fred.get_series('M2', past_unit_price_input_date)[0] * (10 ** 9)
    latest_m2_data = (float((remove_comma((browser.find_element(By.XPATH, "/html/body/div[3]/div[4]/table/tbody/tr[last()]/td[2]").text))))) * (10 ** 9)

    past_unit_price_to_pastm2 = float(past_unit_price_input) / pastm2
    present_unit_price_to_m2 = float(unit_price_input) / latest_m2_data
    return int((present_unit_price_to_m2/past_unit_price_to_pastm2)*100)-100

def calculate_nominal_gains(past_unit_price_input, unit_price_input):
    result = int((unit_price_input/past_unit_price_input)*100)-100
    return result
