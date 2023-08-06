import logging
import sys
import traceback
from datetime import datetime
from http.client import HTTPException
from socket import timeout

from colorama import Fore, Style
from uiautomator2.exceptions import UiObjectNotFoundError

from AllInOneInstagramBot.core.device_facade import DeviceFacade
from AllInOneInstagramBot.core.report import print_full_report
from AllInOneInstagramBot.core.utils import (
    close_instagram,
    open_instagram,
    random_sleep,
    save_crash,
    stop_bot,
)
from AllInOneInstagramBot.core.views import TabBarView

logger = logging.getLogger(__name__)


def run_safely(device, device_id, sessions, session_state, screen_record, configs):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            session_state = sessions[-1]
            try:
                func(*args, **kwargs)
            except KeyboardInterrupt:
                try:
                    # Catch Ctrl-C and ask if user wants to pause execution
                    logger.info(
                        "CTRL-C detected . . .",
                        extra={"color": f"{Style.BRIGHT}{Fore.YELLOW}"},
                    )
                    logger.info(
                        f"-------- PAUSED: {datetime.now().strftime('%H:%M:%S')} --------",
                        extra={"color": f"{Style.BRIGHT}{Fore.YELLOW}"},
                    )
                    logger.info(
                        "NOTE: This is a rudimentary pause. It will restart the action, while retaining session data.",
                        extra={"color": Style.BRIGHT},
                    )
                    logger.info(
                        "Press RETURN to resume or CTRL-C again to Quit: ",
                        extra={"color": Style.BRIGHT},
                    )

                    input("")

                    logger.info(
                        f"-------- RESUMING: {datetime.now().strftime('%H:%M:%S')} --------",
                        extra={"color": f"{Style.BRIGHT}{Fore.YELLOW}"},
                    )
                    TabBarView(device).navigateToProfile()
                except KeyboardInterrupt:
                    stop_bot(device, sessions, session_state)

            except (
                DeviceFacade.JsonRpcError,
                DeviceFacade.AppHasCrashed,
                IndexError,
                HTTPException,
                timeout,
                UiObjectNotFoundError,
            ):
                logger.error(traceback.format_exc())
                logger.info(
                    f"List of running apps: {', '.join(device.deviceV2.app_list_running())}."
                )
                save_crash(device)
                session_state.totalCrashes += 1
                if session_state.check_limit(
                    limit_type=session_state.Limit.CRASHES, output=True
                ):
                    logger.error(
                        "Reached crashes limit. Bot has crashed too much! Please check what's going on."
                    )
                    stop_bot(device, sessions, session_state)
                logger.info("Something unexpected happened. Let's try again.")
                close_instagram(device)
                random_sleep()
                if not open_instagram(device):
                    print_full_report(sessions, configs.args.scrape_to_file)
                    sessions.persist(directory=session_state.my_username)
                    sys.exit(2)
                TabBarView(device).navigateToProfile()
            except Exception as e:
                logger.error(traceback.format_exc())
                for exception_line in traceback.format_exception_only(type(e), e):
                    logger.critical(
                        f"'{exception_line}' -> This kind of exception will stop the bot (no restart)."
                    )
                logger.info(
                    f"List of running apps: {', '.join(device.deviceV2.app_list_running())}"
                )
                save_crash(device)
                close_instagram(device)
                print_full_report(sessions, configs.args.scrape_to_file)
                sessions.persist(directory=session_state.my_username)
                raise e

        return wrapper

    return actual_decorator
