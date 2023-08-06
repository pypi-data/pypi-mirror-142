from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def set(self, frequency: float, notch=repcap.Notch.Default) -> None:
		"""SCPI: [SENSe]:NPRatio:NOTCh<notch>:BWIDth[:ABSolute] \n
		Snippet: driver.sense.npratio.notch.bandwidth.absolute.set(frequency = 1.0, notch = repcap.Notch.Default) \n
		Defines the bandwidth of the individual notch as an absolute value. \n
			:param frequency: Unit: HZ
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		self._core.io.write(f'SENSe:NPRatio:NOTCh{notch_cmd_val}:BWIDth:ABSolute {param}')

	def get(self, notch=repcap.Notch.Default) -> float:
		"""SCPI: [SENSe]:NPRatio:NOTCh<notch>:BWIDth[:ABSolute] \n
		Snippet: value: float = driver.sense.npratio.notch.bandwidth.absolute.get(notch = repcap.Notch.Default) \n
		Defines the bandwidth of the individual notch as an absolute value. \n
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: frequency: Unit: HZ"""
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		response = self._core.io.query_str(f'SENSe:NPRatio:NOTCh{notch_cmd_val}:BWIDth:ABSolute?')
		return Conversions.str_to_float(response)
