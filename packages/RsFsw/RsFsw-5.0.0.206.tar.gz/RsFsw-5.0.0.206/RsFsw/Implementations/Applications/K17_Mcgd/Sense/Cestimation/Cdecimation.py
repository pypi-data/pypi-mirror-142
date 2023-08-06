from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cdecimation:
	"""Cdecimation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdecimation", core, parent)

	def set(self, value: int) -> None:
		"""SCPI: [SENSe]:CESTimation:CDECimation \n
		Snippet: driver.applications.k17Mcgd.sense.cestimation.cdecimation.set(value = 1) \n
		Improves the measurement speed by decimating the number of carriers used for the frequency estimation synchronization as
		a speed vs accuracy tradeoff in carrier estimation mode 'All Carriers'. For example, a value of '1000' configures the
		synchronization to only use each 1000th carrier for frequency estimation and significantly speeds up the measurement for
		scenarios with large number of carriers (100k carriers scenarios) while still providing good measurement accuracy.
		A value of '1' provides the best possible measurement accuracy. The value is clipped internally to 2 carriers if set
		larger then the available number of carriers configured in the multi-carrier signal description. \n
			:param value: numeric value
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:CESTimation:CDECimation {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:CESTimation:CDECimation \n
		Snippet: value: int = driver.applications.k17Mcgd.sense.cestimation.cdecimation.get() \n
		Improves the measurement speed by decimating the number of carriers used for the frequency estimation synchronization as
		a speed vs accuracy tradeoff in carrier estimation mode 'All Carriers'. For example, a value of '1000' configures the
		synchronization to only use each 1000th carrier for frequency estimation and significantly speeds up the measurement for
		scenarios with large number of carriers (100k carriers scenarios) while still providing good measurement accuracy.
		A value of '1' provides the best possible measurement accuracy. The value is clipped internally to 2 carriers if set
		larger then the available number of carriers configured in the multi-carrier signal description. \n
			:return: value: numeric value"""
		response = self._core.io.query_str(f'SENSe:CESTimation:CDECimation?')
		return Conversions.str_to_int(response)
