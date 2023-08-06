from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, frequency: float, notch=repcap.Notch.Default) -> None:
		"""SCPI: [SENSe]:NPRatio:NOTCh<notch>:FREQuency:OFFSet \n
		Snippet: driver.sense.npratio.notch.frequency.offset.set(frequency = 1.0, notch = repcap.Notch.Default) \n
		Defines the center position of the notch in relation to the currently defined center frequency. \n
			:param frequency: Unit: HZ
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		self._core.io.write(f'SENSe:NPRatio:NOTCh{notch_cmd_val}:FREQuency:OFFSet {param}')

	def get(self, notch=repcap.Notch.Default) -> float:
		"""SCPI: [SENSe]:NPRatio:NOTCh<notch>:FREQuency:OFFSet \n
		Snippet: value: float = driver.sense.npratio.notch.frequency.offset.get(notch = repcap.Notch.Default) \n
		Defines the center position of the notch in relation to the currently defined center frequency. \n
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: frequency: Unit: HZ"""
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		response = self._core.io.query_str(f'SENSe:NPRatio:NOTCh{notch_cmd_val}:FREQuency:OFFSet?')
		return Conversions.str_to_float(response)
