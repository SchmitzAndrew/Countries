from instapy import smart_run

def follow(session, account):
    with smart_run(session, account):
        """ Activity flow """
        #settings
        session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers= 5000, min_followers=50, min_following=50)

        #activities
        session.follow_user_followers(['account'], amount=1000, randomize=False, interact=False)
