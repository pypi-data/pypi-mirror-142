import logging
from io import StringIO
from time import gmtime
from typing import Generator

import allure
import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.runner import CallInfo

DEFAULT_LOG_FORMAT = "%(asctime)s.%(msecs)03dZ %(levelname)-8s %(name)s %(message)s"
DEFAULT_LOG_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"


def pytest_addoption(parser: Parser) -> None:
    group = parser.getgroup("allure-logging")

    group.addoption("--allure-log", action="store_true", help="Enable allure logger")
    group.addoption("--allure-log-fmt", default=DEFAULT_LOG_FORMAT, help="Allure logger format")
    group.addoption("--allure-log-datefmt", default=DEFAULT_LOG_DATE_FORMAT, help="Allure logger date format")
    group.addoption("--allure-log-level", default=logging.DEBUG, help="Allure logger level")
    group.addoption("--allure-log-failure", action="store_true", help="Attach the log only in case of failure")


def pytest_configure(config: Config) -> None:
    if config.option.allure_log:
        logger = AllureLoggerPlugin(config)
        name = config.pluginmanager.register(logger, "allure-pytest-logger")
        config.add_cleanup(lambda: config.pluginmanager.unregister(name=name))


class AllureLoggerPlugin:
    def __init__(self, config: Config) -> None:
        self.stream = StringIO()
        self.has_failure = False

        logging.basicConfig(
            format=config.option.allure_log_fmt,
            datefmt=config.option.allure_log_datefmt,
            stream=self.stream,
            level=config.option.allure_log_level,
        )
        logging.Formatter.converter = gmtime

    def cleanup(self) -> None:
        self.stream.truncate(0)
        self.stream.seek(0)
        self.has_failure = False

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(
        self,
        item: pytest.Item,
        call: CallInfo,  # pylint: disable=unused-argument
    ) -> Generator:
        outcome = yield

        report = outcome.get_result()

        self.has_failure |= report.outcome == "failed"

        if report.when == "teardown":
            self.stream.flush()

            if not item.config.option.allure_log_failure or self.has_failure:
                allure.attach(self.stream.getvalue(), name="log", attachment_type=allure.attachment_type.TEXT)

            self.cleanup()
