from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coefficient:
	"""Coefficient commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coefficient", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:STORe:MDPD:COEFficient \n
		Snippet: driver.applications.k18AmplifierEt.massMemory.store.mdpd.coefficient.set(filename = '1') \n
		Exports the memory DPD coefficients in a file in .csv format. \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'MMEMory:STORe:MDPD:COEFficient {param}')
