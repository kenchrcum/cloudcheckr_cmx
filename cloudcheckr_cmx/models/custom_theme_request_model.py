# coding: utf-8

"""
    CloudCheckr API

    CloudCheckr API  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@cloudcheckr.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CustomThemeRequestModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'logo': 'str',
        'browser_tab_title': 'str',
        'browser_tab_icon': 'str',
        'colors_nav': 'str',
        'colors_accent': 'str',
        'colors_dark_nav_icons': 'bool',
        'support_info_support_link': 'str',
        'support_info_support_link_text': 'str'
    }

    attribute_map = {
        'logo': 'logo',
        'browser_tab_title': 'browserTabTitle',
        'browser_tab_icon': 'browserTabIcon',
        'colors_nav': 'colorsNav',
        'colors_accent': 'colorsAccent',
        'colors_dark_nav_icons': 'colorsDarkNavIcons',
        'support_info_support_link': 'supportInfoSupportLink',
        'support_info_support_link_text': 'supportInfoSupportLinkText'
    }

    def __init__(self, logo=None, browser_tab_title=None, browser_tab_icon=None, colors_nav=None, colors_accent=None, colors_dark_nav_icons=None, support_info_support_link=None, support_info_support_link_text=None):  # noqa: E501
        """CustomThemeRequestModel - a model defined in Swagger"""  # noqa: E501
        self._logo = None
        self._browser_tab_title = None
        self._browser_tab_icon = None
        self._colors_nav = None
        self._colors_accent = None
        self._colors_dark_nav_icons = None
        self._support_info_support_link = None
        self._support_info_support_link_text = None
        self.discriminator = None
        if logo is not None:
            self.logo = logo
        if browser_tab_title is not None:
            self.browser_tab_title = browser_tab_title
        if browser_tab_icon is not None:
            self.browser_tab_icon = browser_tab_icon
        if colors_nav is not None:
            self.colors_nav = colors_nav
        if colors_accent is not None:
            self.colors_accent = colors_accent
        if colors_dark_nav_icons is not None:
            self.colors_dark_nav_icons = colors_dark_nav_icons
        if support_info_support_link is not None:
            self.support_info_support_link = support_info_support_link
        if support_info_support_link_text is not None:
            self.support_info_support_link_text = support_info_support_link_text

    @property
    def logo(self):
        """Gets the logo of this CustomThemeRequestModel.  # noqa: E501

        Logo to display as the header in the user interface and exports. This property supports: resetting.  # noqa: E501

        :return: The logo of this CustomThemeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this CustomThemeRequestModel.

        Logo to display as the header in the user interface and exports. This property supports: resetting.  # noqa: E501

        :param logo: The logo of this CustomThemeRequestModel.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def browser_tab_title(self):
        """Gets the browser_tab_title of this CustomThemeRequestModel.  # noqa: E501

        Text to display on the browser tab. This property supports: resetting.  # noqa: E501

        :return: The browser_tab_title of this CustomThemeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._browser_tab_title

    @browser_tab_title.setter
    def browser_tab_title(self, browser_tab_title):
        """Sets the browser_tab_title of this CustomThemeRequestModel.

        Text to display on the browser tab. This property supports: resetting.  # noqa: E501

        :param browser_tab_title: The browser_tab_title of this CustomThemeRequestModel.  # noqa: E501
        :type: str
        """

        self._browser_tab_title = browser_tab_title

    @property
    def browser_tab_icon(self):
        """Gets the browser_tab_icon of this CustomThemeRequestModel.  # noqa: E501

        Icon to show on the browser tab.  Base-64 encoded image. This property supports: resetting.  # noqa: E501

        :return: The browser_tab_icon of this CustomThemeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._browser_tab_icon

    @browser_tab_icon.setter
    def browser_tab_icon(self, browser_tab_icon):
        """Sets the browser_tab_icon of this CustomThemeRequestModel.

        Icon to show on the browser tab.  Base-64 encoded image. This property supports: resetting.  # noqa: E501

        :param browser_tab_icon: The browser_tab_icon of this CustomThemeRequestModel.  # noqa: E501
        :type: str
        """

        self._browser_tab_icon = browser_tab_icon

    @property
    def colors_nav(self):
        """Gets the colors_nav of this CustomThemeRequestModel.  # noqa: E501

        Color to use for navigation menu.  Specify as a hexadecimal color value. This property supports: resetting.  # noqa: E501

        :return: The colors_nav of this CustomThemeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._colors_nav

    @colors_nav.setter
    def colors_nav(self, colors_nav):
        """Sets the colors_nav of this CustomThemeRequestModel.

        Color to use for navigation menu.  Specify as a hexadecimal color value. This property supports: resetting.  # noqa: E501

        :param colors_nav: The colors_nav of this CustomThemeRequestModel.  # noqa: E501
        :type: str
        """

        self._colors_nav = colors_nav

    @property
    def colors_accent(self):
        """Gets the colors_accent of this CustomThemeRequestModel.  # noqa: E501

        Color to use for accent elements.  Specify as a hexadecimal color value. This property supports: resetting.  # noqa: E501

        :return: The colors_accent of this CustomThemeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._colors_accent

    @colors_accent.setter
    def colors_accent(self, colors_accent):
        """Sets the colors_accent of this CustomThemeRequestModel.

        Color to use for accent elements.  Specify as a hexadecimal color value. This property supports: resetting.  # noqa: E501

        :param colors_accent: The colors_accent of this CustomThemeRequestModel.  # noqa: E501
        :type: str
        """

        self._colors_accent = colors_accent

    @property
    def colors_dark_nav_icons(self):
        """Gets the colors_dark_nav_icons of this CustomThemeRequestModel.  # noqa: E501

        Determines if the navigation icons should be light or dark. This property supports: resetting.  # noqa: E501

        :return: The colors_dark_nav_icons of this CustomThemeRequestModel.  # noqa: E501
        :rtype: bool
        """
        return self._colors_dark_nav_icons

    @colors_dark_nav_icons.setter
    def colors_dark_nav_icons(self, colors_dark_nav_icons):
        """Sets the colors_dark_nav_icons of this CustomThemeRequestModel.

        Determines if the navigation icons should be light or dark. This property supports: resetting.  # noqa: E501

        :param colors_dark_nav_icons: The colors_dark_nav_icons of this CustomThemeRequestModel.  # noqa: E501
        :type: bool
        """

        self._colors_dark_nav_icons = colors_dark_nav_icons

    @property
    def support_info_support_link(self):
        """Gets the support_info_support_link of this CustomThemeRequestModel.  # noqa: E501

        The URL that the support link leads to. This property supports: resetting.  # noqa: E501

        :return: The support_info_support_link of this CustomThemeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._support_info_support_link

    @support_info_support_link.setter
    def support_info_support_link(self, support_info_support_link):
        """Sets the support_info_support_link of this CustomThemeRequestModel.

        The URL that the support link leads to. This property supports: resetting.  # noqa: E501

        :param support_info_support_link: The support_info_support_link of this CustomThemeRequestModel.  # noqa: E501
        :type: str
        """

        self._support_info_support_link = support_info_support_link

    @property
    def support_info_support_link_text(self):
        """Gets the support_info_support_link_text of this CustomThemeRequestModel.  # noqa: E501

        Display text for support information link. This property supports: resetting.  # noqa: E501

        :return: The support_info_support_link_text of this CustomThemeRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._support_info_support_link_text

    @support_info_support_link_text.setter
    def support_info_support_link_text(self, support_info_support_link_text):
        """Sets the support_info_support_link_text of this CustomThemeRequestModel.

        Display text for support information link. This property supports: resetting.  # noqa: E501

        :param support_info_support_link_text: The support_info_support_link_text of this CustomThemeRequestModel.  # noqa: E501
        :type: str
        """

        self._support_info_support_link_text = support_info_support_link_text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CustomThemeRequestModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomThemeRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
