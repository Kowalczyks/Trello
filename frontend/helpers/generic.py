import datetime
from selenium.common.exceptions import WebDriverException


def find_element_extended(locator, driver_instance, supress_timeout_exception=False, timeout=10, parent_element=None):
    """finds element either on website or within parent
    additional try/except statement protects from stale element exception
    :param locator:
    :param parent_element:
    :param driver_instance:
    :param timeout:
    :param supress_timeout_exception: if true, then timeout exception won't be raised; empty list will be returned instead
    :return:
    """
    found_element = []
    start_time = datetime.datetime.now()
    while len(found_element) == 0:
        elapsed_seconds = (datetime.datetime.now() - start_time).total_seconds()
        if elapsed_seconds > timeout:
            if supress_timeout_exception:
                return found_element
            else:
                raise WebDriverException(
                    "Timeout : could not find any element with given locator in specified time. locator: " + locator)
        try:
            if parent_element is not None:
                found_element = parent_element.find_elements_by_css_selector(locator)
            else:
                found_element = driver_instance.find_elements_by_css_selector(locator)
        except:
            continue
    return found_element
