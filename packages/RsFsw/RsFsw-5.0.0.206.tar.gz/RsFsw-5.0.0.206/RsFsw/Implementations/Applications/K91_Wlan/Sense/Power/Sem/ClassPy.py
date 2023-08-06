from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ClassPy:
	"""ClassPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("classPy", core, parent)

	def set(self, index: float) -> None:
		"""SCPI: [SENSe]:POWer:SEM:CLASs \n
		Snippet: driver.applications.k91Wlan.sense.power.sem.classPy.set(index = 1.0) \n
		This command sets the Spectrum Emission Mask (SEM) power class index. The index represents the power classes to be
		applied. The index is directly related to the entries displayed in the power class drop-down box, within the SEM settings
		configuration page. \n
			:param index: No help available
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'SENSe:POWer:SEM:CLASs {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:SEM:CLASs \n
		Snippet: value: float = driver.applications.k91Wlan.sense.power.sem.classPy.get() \n
		This command sets the Spectrum Emission Mask (SEM) power class index. The index represents the power classes to be
		applied. The index is directly related to the entries displayed in the power class drop-down box, within the SEM settings
		configuration page. \n
			:return: index: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:CLASs?')
		return Conversions.str_to_float(response)
