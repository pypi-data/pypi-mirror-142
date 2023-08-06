import json
import logging
import os
import sys
from datetime import datetime, timedelta
from enum import Enum, unique

from atomicwrites import atomic_write

logger = logging.getLogger(__name__)

ACCOUNTS = "accounts"
REPORTS = "reports"
FILENAME_HISTORY_FILTER_USERS = "history_filters_users.json"
FILENAME_INTERACTED_USERS = "interacted_users.json"
OLD_FILTER = "filter.json"
FILTER = "filters.yml"
USER_LAST_INTERACTION = "last_interaction"
USER_FOLLOWING_STATUS = "following_status"

FILENAME_WHITELIST = "whitelist.txt"
FILENAME_BLACKLIST = "blacklist.txt"
FILENAME_COMMENTS = "comments_list.txt"
FILENAME_MESSAGES = "pm_list.txt"


class Storage:
    interacted_users_path = None
    interacted_users = {}

    history_filter_users_path = None
    history_filter_users = {}

    filter_path = None
    filter = {}

    comment_path = None
    comment = []

    whitelist = []
    blacklist = []

    def __init__(self, my_username):
        if my_username is None:
            logger.error(
                "No username, thus the script won't get access to interacted users and sessions data."
            )
            return

        if not os.path.exists(f"{ACCOUNTS}/{my_username}"):
            os.makedirs(f"{ACCOUNTS}/{my_username}")

        self.interacted_users_path = (
            f"{ACCOUNTS}/{my_username}/{FILENAME_INTERACTED_USERS}"
        )
        if os.path.exists(self.interacted_users_path):
            with open(self.interacted_users_path, encoding="utf-8") as json_file:
                try:
                    self.interacted_users = json.load(json_file)
                except Exception as e:
                    logger.error(
                        f"Please check {json_file.name}, it contains this error: {e}"
                    )
                    sys.exit(0)

        self.history_filter_users_path = (
            f"{ACCOUNTS}/{my_username}/{FILENAME_HISTORY_FILTER_USERS}"
        )

        if os.path.exists(self.history_filter_users_path):
            with open(self.history_filter_users_path, encoding="utf-8") as json_file:
                try:
                    self.history_filter_users = json.load(json_file)
                except Exception as e:
                    logger.error(
                        f"Please check {json_file.name}, it contains this error: {e}"
                    )
                    sys.exit(0)

        self.filter_path = f"{ACCOUNTS}/{my_username}/{FILTER}"
        if not os.path.exists(self.filter_path):
            self.filter_path = f"{ACCOUNTS}/{my_username}/{OLD_FILTER}"

        whitelist_path = f"{ACCOUNTS}/{my_username}/{FILENAME_WHITELIST}"
        if os.path.exists(whitelist_path):
            with open(whitelist_path, encoding="utf-8") as file:
                self.whitelist = [line.rstrip() for line in file]

        blacklist_path = f"{ACCOUNTS}/{my_username}/{FILENAME_BLACKLIST}"
        if os.path.exists(blacklist_path):
            with open(blacklist_path, encoding="utf-8") as file:
                self.blacklist = [line.rstrip() for line in file]

        self.report_path = f"{ACCOUNTS}/{my_username}/{REPORTS}/"

    def can_be_reinteract(self, last_interaction, hours_that_have_to_pass):
        if hours_that_have_to_pass > timedelta(hours=0):
            delta = datetime.now() - last_interaction
            if delta < hours_that_have_to_pass:
                return False
            else:
                return True
        else:
            return False

    def check_user_was_interacted(self, username):
        """returns when an username has been interacted, False if not already interacted"""
        user = self.interacted_users.get(username)
        if user is None:
            return False, None

        last_interaction = datetime.strptime(
            user[USER_LAST_INTERACTION], "%Y-%m-%d %H:%M:%S.%f"
        )
        return True, last_interaction

    def get_following_status(self, username):
        user = self.interacted_users.get(username)
        if user is None:
            return FollowingStatus.NOT_IN_LIST
        else:
            return FollowingStatus[user[USER_FOLLOWING_STATUS].upper()]

    def add_filter_user(self, username, profile_data, skip_reason=None):
        user = profile_data.__dict__
        user["follow_button_text"] = (
            profile_data.follow_button_text.name
            if not profile_data.is_restricted
            else None
        )
        user["skip_reason"] = None if skip_reason is None else skip_reason.name
        self.history_filter_users[username] = user
        if self.history_filter_users_path is not None:
            with atomic_write(
                self.history_filter_users_path, overwrite=True, encoding="utf-8"
            ) as outfile:
                json.dump(self.history_filter_users, outfile, indent=4, sort_keys=False)

    def add_interacted_user(
        self,
        username,
        session_id,
        followed=False,
        unfollowed=False,
        scraped=False,
        liked=0,
        watched=0,
        commented=0,
        pm_sent=False,
        job_name=None,
        target=None,
    ):
        user = self.interacted_users.get(username, {})
        user[USER_LAST_INTERACTION] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        if followed:
            user[USER_FOLLOWING_STATUS] = FollowingStatus.FOLLOWED.name.lower()
        elif unfollowed:
            user[USER_FOLLOWING_STATUS] = FollowingStatus.UNFOLLOWED.name.lower()
        elif scraped:
            user[USER_FOLLOWING_STATUS] = FollowingStatus.SCRAPED.name.lower()
        else:
            user[USER_FOLLOWING_STATUS] = FollowingStatus.NONE.name.lower()

        # Save only the last session_id
        user["session_id"] = session_id

        # Save only the last job_name and target
        if not user.get("job_name"):
            user["job_name"] = job_name
        if not user.get("target"):
            user["target"] = target

        # Increase the value of liked, watched or commented if we have already a value
        user["liked"] = liked if "liked" not in user else (user["liked"] + liked)
        user["watched"] = (
            watched if "watched" not in user else (user["watched"] + watched)
        )
        user["commented"] = (
            commented if "commented" not in user else (user["commented"] + commented)
        )

        # Update the followed or unfollowed boolean only if we have a real update
        user["followed"] = (
            followed
            if "followed" not in user or user["followed"] != followed
            else user["followed"]
        )
        user["unfollowed"] = (
            unfollowed
            if "unfollowed" not in user or user["unfollowed"] != unfollowed
            else user["unfollowed"]
        )
        user["scraped"] = (
            scraped
            if "scraped" not in user or user["scraped"] != scraped
            else user["scraped"]
        )
        # Save the boolean if we sent a PM
        user["pm_sent"] = (
            pm_sent
            if "pm_sent" not in user or user["pm_sent"] != pm_sent
            else user["pm_sent"]
        )
        self.interacted_users[username] = user
        self._update_file()

    def is_user_in_whitelist(self, username):
        return username in self.whitelist

    def is_user_in_blacklist(self, username):
        return username in self.blacklist

    def _get_last_day_interactions_count(self):
        count = 0
        users_list = list(self.interacted_users.values())
        for user in users_list:
            last_interaction = datetime.strptime(
                user[USER_LAST_INTERACTION], "%Y-%m-%d %H:%M:%S.%f"
            )
            is_last_day = datetime.now() - last_interaction <= timedelta(days=1)
            if is_last_day:
                count += 1
        return count

    def _update_file(self):
        if self.interacted_users_path is not None:
            with atomic_write(
                self.interacted_users_path, overwrite=True, encoding="utf-8"
            ) as outfile:
                json.dump(self.interacted_users, outfile, indent=4, sort_keys=False)


@unique
class FollowingStatus(Enum):
    NONE = 0
    FOLLOWED = 1
    UNFOLLOWED = 2
    NOT_IN_LIST = 3
    SCRAPED = 4
