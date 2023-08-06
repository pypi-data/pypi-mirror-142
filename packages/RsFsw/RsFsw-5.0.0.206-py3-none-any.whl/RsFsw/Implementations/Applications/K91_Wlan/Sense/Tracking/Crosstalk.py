from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crosstalk:
	"""Crosstalk commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crosstalk", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:TRACking:CROSstalk \n
		Snippet: driver.applications.k91Wlan.sense.tracking.crosstalk.set(state = False) \n
		Activates or deactivates the compensation for crosstalk between MIMO carriers. This command is only available for
		standard IEEE 802.11ac or n (MIMO) . For details see 'Crosstalk and spectrum flatness'. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:TRACking:CROSstalk {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:TRACking:CROSstalk \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.tracking.crosstalk.get() \n
		Activates or deactivates the compensation for crosstalk between MIMO carriers. This command is only available for
		standard IEEE 802.11ac or n (MIMO) . For details see 'Crosstalk and spectrum flatness'. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:TRACking:CROSstalk?')
		return Conversions.str_to_bool(response)
