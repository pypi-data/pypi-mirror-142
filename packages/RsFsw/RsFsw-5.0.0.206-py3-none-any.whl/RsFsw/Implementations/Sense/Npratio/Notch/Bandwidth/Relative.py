from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	def set(self, percentage: float, notch=repcap.Notch.Default) -> None:
		"""SCPI: [SENSe]:NPRatio:NOTCh<notch>:BWIDth:RELative \n
		Snippet: driver.sense.npratio.notch.bandwidth.relative.set(percentage = 1.0, notch = repcap.Notch.Default) \n
		Defines the bandwidth of the individual notch as a percentage of the defined channel frequency. \n
			:param percentage: Range: 0 to 100
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.decimal_value_to_str(percentage)
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		self._core.io.write(f'SENSe:NPRatio:NOTCh{notch_cmd_val}:BWIDth:RELative {param}')

	def get(self, notch=repcap.Notch.Default) -> float:
		"""SCPI: [SENSe]:NPRatio:NOTCh<notch>:BWIDth:RELative \n
		Snippet: value: float = driver.sense.npratio.notch.bandwidth.relative.get(notch = repcap.Notch.Default) \n
		Defines the bandwidth of the individual notch as a percentage of the defined channel frequency. \n
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: percentage: Range: 0 to 100"""
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		response = self._core.io.query_str(f'SENSe:NPRatio:NOTCh{notch_cmd_val}:BWIDth:RELative?')
		return Conversions.str_to_float(response)
