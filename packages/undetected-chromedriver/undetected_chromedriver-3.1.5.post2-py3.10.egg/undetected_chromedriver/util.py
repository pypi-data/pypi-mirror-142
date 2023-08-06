#!/usr/bin/env python3
# this module is part of undetected_chromedriver

import math
import traceback
import random
import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder


class UtilMixin:  # mixin
    """
    This can be used as mixin together with uc.Chrome()
    """

    @staticmethod
    def offset_circular(r, n=100):
        for x in range(n, 0, -1):
            yield math.cos(2 * math.pi / n * x) * r, math.sin(2 * math.pi / n * x) * r

    def perform_natural(self, element, click=True, callback=None, hold=False):
        """
        Performs a click ( or move, or hold ), on a more natural way
        than hitting straight up center of the element.

        :param self: self
        :param element: the element to move/click
        :param click: should perform click
        :param hold: should perform hold (to test, use on canvas draw)
        :return:
        """

        action = ActionChains(self)
        try:
            h, w, x, y = element.rect.values()
            h, w, x, y = int(h), int(w), int(x), int(y)
        except:  # noqa
            traceback.print_exc()
        h, w, x, y = 100, 100, 10, 10
        if hold:
            action.click_and_hold()
        action.move_to_element(element)
        for offset in self.offset_circular(5, 5):
            action.move_by_offset(*offset)
        if hold:
            action.release()
        if click:
            action.click()
        action.perform()
        if callback:
            try:
                callback(element)
            except:
                traceback.print_exc()

    def human_click(self, element):
        return self.perform_natural(element, True, None, False)

    def human_keys(self, element, text):
        def interval(key):
            time.sleep(random.uniform(0.19, 0.89))
            element.send_keys(key)

        list(map(lambda key: interval(key), text))

    def find_element_by_any_match(self, text, selector="*", multiple=True):

        elements = self.find_elements(by="css selector", value=selector)
        retval = []
        for element in elements:
            element_html = self.execute_script(
                """return arguments[0].outerHTML""", element
            )
            if text.lower() in element_html.lower():
                if multiple:
                    retval.append(element)
                else:
                    return element
        return retval

    def element_html(self, element):
        return self.execute_script("""return arguments[0].outerHTML""", element)

    def iter_all_elements(self):
        """generator"""
        for element in self.find_elements(by="tag name", value="*"):
            yield element

    def get_closest(self, tagname, to_element):
        """
        gets closest element of `tagname` relative to `to_element`.
        :param tagname: element you're looking for
        :param to_element: starting point
        :return:
        """
        return self.execute_script(
            """return arguments[0].closest('%s')""" % tagname, to_element
        )

    def scroll_into_view(self, element):
        return self.execute_script("""return arguments[0].scrollIntoView()""", element)

    def scroll(self, amount=None, relative=True):
        if relative:
            base = "window.scrollY"
        else:
            base = ""
        if not amount:
            amount = "window.innerHeight/2"
        else:
            amount = amount
        script = "window.scrollTo(0, (%s + %s))" % (base, amount)
        return self.execute_script(script)

    def get_parent_element(self, element):
        return self.execute_script("""return arguments[0].parentElement""", element)


class Markers:
    all_markers = {}

    def has_marker(self, element):
        if f"marker-{element._id}" in self.all_markers:
            return True
        else:
            return self.execute_script(
                """
                return document.querySelector('#marker-{}') 
                """.format(
                    element._id
                )
            )

    def remove_marker(self, element):
        if f"marker-{element._id}" in self.all_markers:
            self.execute_script(
                """
                document.querySelector('%s').remove()
                """
                % element._id,
                element,
            )
            self.all_markers.pop(f"marker-{element._id}")

    def set_marker(self, element):
        self.execute_script(
            """
            var marker_id = 'marker-{}';
            var marker = document.createElement('div');
            marker.id = marker_id;
            marker.style.borderRadius="50%";
            marker.style.position="absolute";
            marker.style.padding="2em";
            marker.style.zIndex="99999";
            marker.style.background="rgba(255,0,0,.5)";
            marker.style.visibility="visible";
            marker.style.opacity="1";
            marker.style.display="block";
            arguments[0].appendChild(marker);
        """.format(
                str(element._id)
            ),
            element,
        )
        self.all_markers[f"marker-{element._id}"] = element


from . import Chrome


class ChromeWithUtils(Chrome, UtilMixin):
    pass


class ChromeWithMoreUtils(Chrome, UtilMixin, Markers):
    pass


# def find_instagram_articles(driver):
#     return driver.find_elements(by="css selector", value="article")
#
# def find_like_button_in_article(driver, article):
#     for button in article.find_elements(by="css selector", value="button"):
#         if len(button.find_elements(by="css selector", value="span")):
#             return button
#
# def instatimelinescrolllikeall(driver):
#
#     liked = set()
#
#     while True:
#         driver.scroll(2500)
#         articles = find_instagram_articles(driver)
#         articleids = set(a._id for a in articles)
#         liked |= articleids
#         articles = [a for a in articles if a._id in articleids]
#
#         try:
#             for article in articles:
#                 driver.scroll(article.location["y"], relative=False)
#                 btn = find_like_button_in_article(driver, article)
#                 if btn:
#                     driver.human_click(btn)
#         except:
#             traceback.print_exc()
#             continue
#
# def insta_auto_scroll_and_like(driver):
#     import time
#
#     done = set()
#     while True:
#         scroll(driver)
#         try:
#             arias = driver.find_elements_by_css_selector("*[aria-label=Like]")
#             btns = [get_closest(driver, "button", aria) for aria in arias]
#
#             print("found ", len(btns), btns)
#             btns = set(btns)
#             for btn in btns:
#                 try:
#                     if not btn:
#                         continue
#                     if btn.is_displayed():
#                         if not has_marker(driver, btn):
#                             done.add(btn)
#                             mark_element(driver, btn)
#                             perform_natural(driver, btn)
#                     time.sleep(1)
#                 except Exception as e:
#                     print(e)
#                     break
#         except Exception as e:
#             print(e)
#         time.sleep(1)
