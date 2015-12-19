from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import SignalHook
from reviewboard.reviews.models import BaseComment, ReviewRequest
from reviewboard.reviews.signals import (review_request_publishing)
from reviewboard.reviews.errors import PublishError

class DraftCheckExtension(Extension):
   """Extends Review Board to check draft review"""
   metadata = {
      'Name': 'Draft request review check',
      'Summary': (
         'Check draft review request to improve review quality'
      ),
   }

   def initialize(self):
      hooks = [
         (review_request_publishing, self.on_review_request_publishing)
      ]

      for signal, handler in hooks:
         ''' set sandbox_errors = False to raise the exception to sender ''' 
         SignalHook(self, signal, handler, None, False)

   def on_review_request_publishing(self, user, review_request_draft, **kwargs): 
      """Handler for the review_request_publishing."""
      
      """ check blow validation"""
      """ 'summary': review_request.summary,
          'description': review_request.description,
          'testing_done': review_request.testing_done,
          'bugs_closed': review_request.bugs_closed,
          'branch': review_request.branch,
      """
      if review_request_draft.bugs_closed is None: 
         raise PublishError('bug number must be provided')

      if review_request_draft.branch is None: 
         raise PublishError('git branch must be provided')

      if len(review_request_draft.summary) < 10:
         raise PublishError('summary text is too short')

      if len(review_request_draft.description) < 20:
         raise PublishError('description text is too short')

      if len(review_request_draft.testing_done) < 50:
         raise PublishError('testing done is too short')
