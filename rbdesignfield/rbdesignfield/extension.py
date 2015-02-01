# -*- coding: utf-8 -*-
import json 
import urllib
import urlparse
import requests
import logging
import sys

from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import ReviewRequestFieldsHook
from reviewboard.reviews.fields import BaseReviewRequestField

# enforce default sys encoding to be utf8 
reload(sys)  
sys.setdefaultencoding('utf8')

class DesignField(BaseReviewRequestField):
    """The design field on a review request."""
    field_id = 'pipapai_design_field'
    label = _('Design')

    one_line_per_change_entry = False

    def load_value(self, review_request_details):
        return review_request_details.get_bug_list()

    def should_render(self, bugs):
        return bugs is not None and len(bugs) > 0

    def save_value(self, value):
        ''' don't change the design value as the design might be posted later ''' 
        return False

    def render_value(self, bugs):
        bug_id = bugs[0]
        design_id = self._get_design_url_from_bug_id(bug_id)

        if design_id is not None:
            design_url = "http://design.ppp.com/design/sheji/%s" % design_id
            return '<a href="%s">设计 %s</a>' % (escape(design_url), escape(design_id))
        else:
            return ''

    def _get_design_url_from_bug_id(self, bug_id):
        ''' hard-coded the designboard url '''
        ''' FIXME: add this into admin page ''' 
        design_search_url = "http://design.ppp.com/design/search?keyword=%s&format=json" % bug_id
    
        request = requests.get(design_search_url)

        # designboard generates a 200 created response for this
        if request.status_code not in (requests.codes.created, requests.codes.ok):
            logging.error("Communication problem with designboard. ")
            logging.error("Please report the following:")
            logging.error("Request URL: %s" % designboard_search_url)
            logging.error("Status code: %s" % request.status_code)
            return None

        try:
            response = json.loads(request.content)
        except ValueError:
            logging.error("Malformed response received from designboard.")
            return None

        if response["id"] is None: 
            logging.error("An error occurred while accessing designboard.")
            logging.error(response)
            return None

        return response["id"]

class DesignFieldExtension(Extension):
    metadata = {
        'Name': _('Design'),
        'Summary': _('Add a design url to design board to show UI/UE design')
    }

    def initialize(self):
        ReviewRequestFieldsHook(self, 'info', [DesignField])
