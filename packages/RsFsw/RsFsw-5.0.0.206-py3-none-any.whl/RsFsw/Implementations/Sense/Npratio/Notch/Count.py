from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, amount: float, notch=repcap.Notch.Default) -> None:
		"""SCPI: [SENSe]:NPRatio:NOTCh<notch>:COUNt \n
		Snippet: driver.sense.npratio.notch.count.set(amount = 1.0, notch = repcap.Notch.Default) \n
		Defines the number of notches for which results are determined. Note that even if bandwidths for further notches are
		defined, only the number specified here are actually calculated and displayed. \n
			:param amount: integer Range: 1 to 25
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.decimal_value_to_str(amount)
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		self._core.io.write(f'SENSe:NPRatio:NOTCh{notch_cmd_val}:COUNt {param}')

	def get(self, notch=repcap.Notch.Default) -> float:
		"""SCPI: [SENSe]:NPRatio:NOTCh<notch>:COUNt \n
		Snippet: value: float = driver.sense.npratio.notch.count.get(notch = repcap.Notch.Default) \n
		Defines the number of notches for which results are determined. Note that even if bandwidths for further notches are
		defined, only the number specified here are actually calculated and displayed. \n
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: amount: integer Range: 1 to 25"""
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		response = self._core.io.query_str(f'SENSe:NPRatio:NOTCh{notch_cmd_val}:COUNt?')
		return Conversions.str_to_float(response)
