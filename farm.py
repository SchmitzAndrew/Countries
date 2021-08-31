#farms follows
from instapy import smart_run
import random

def farm(session):
    with smart_run(session):
        session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=5000, min_followers=50,
                                        min_following=50)

        session.follow_user_followers([], amount=800,randomize=False, interact=False)

        session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"), style="FIFO",
                               unfollow_after=random.randint(10,12) * 60 * 60, sleep_delay=random.randint(500, 600))
