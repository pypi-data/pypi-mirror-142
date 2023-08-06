from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EfLength:
	"""EfLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("efLength", core, parent)

	def set(self, length: float) -> None:
		"""SCPI: [SENSe]:DEMod:FILTer:EFLength \n
		Snippet: driver.applications.k91Wlan.sense.demod.filterPy.efLength.set(length = 1.0) \n
		This command specifies the equalizer filter length in chips. \n
			:param length: Range: 2 to 30
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'SENSe:DEMod:FILTer:EFLength {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:FILTer:EFLength \n
		Snippet: value: float = driver.applications.k91Wlan.sense.demod.filterPy.efLength.get() \n
		This command specifies the equalizer filter length in chips. \n
			:return: length: Range: 2 to 30"""
		response = self._core.io.query_str(f'SENSe:DEMod:FILTer:EFLength?')
		return Conversions.str_to_float(response)
