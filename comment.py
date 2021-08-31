from instapy import smart_run
import random

comments = ['Nice shot! @{}',
            'I love your profile! @{}',
            'Your feed is an inspiration :thumbsup:',
            'Just incredible :open_mouth:',
            'What camera did you use @{}?',
            'Love your posts @{}',
            'Looks awesome @{}',
            'Getting inspired by you @{}',
            ':raised_hands: Yes!',
            'I can feel your passion @{} :muscle:']

def comment(session, account):
    with smart_run(session, account):
        """ Activity flow """
        #settings
        session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers= 5000, min_followers=50, min_following=50)
        session.like_by_tags(["natgeo"], amount=10)

        #activities
        session.set_do_comment(enabled=True, percentage=random.randint(25, 40))
        session.set_comments(comments)
        session.join_pods(topic='sports', engagement_mode='no_comments')
