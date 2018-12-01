


from trinity.extensibility import BaseIsolatedPlugin
from argparse import ArgumentParser, _SubParsersAction
import asyncio


class UselessPlugin(BaseIsolatedPlugin):

    @property
    def name(self) -> str:
        return "Useless plugin"

    def configure_parser(self,
                         arg_parser: ArgumentParser,
                         subparser: _SubParsersAction) -> None:
        arg_parser.add_argument(
            "--useless",
            action="store_true",
            help="Totally useless plugin",
        )

    def on_ready(self) -> None:
        if self.context.args.useless:
            self.logger.info("my useless plugin here")
            self.start()

    async def _periodically_report_stats(self):
        while True:
            self.logger.info("Fooooooooo")
            await asyncio.sleep(1)

    def do_start(self) -> None:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._periodically_report_stats())
        loop.close()