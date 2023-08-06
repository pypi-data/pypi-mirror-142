from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	def get(self, notch=repcap.Notch.Default) -> float:
		"""SCPI: CONFigure:GENerator:NPRatio:NOTCh<notch>:CLOCk \n
		Snippet: value: float = driver.configure.generator.npratio.notch.clock.get(notch = repcap.Notch.Default) \n
		Queries the generator clock frequency. \n
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: clock_frequency: 1..n irrelevant"""
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:NOTCh{notch_cmd_val}:CLOCk?')
		return Conversions.str_to_float(response)
