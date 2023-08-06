from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pscd:
	"""Pscd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pscd", core, parent)

	def set(self, format_py: enums.PdschFormat) -> None:
		"""SCPI: [SENSe][:LTE]:DL:FORMat:PSCD \n
		Snippet: driver.applications.k10Xlte.sense.lte.downlink.formatPy.pscd.set(format_py = enums.PdschFormat.OFF) \n
		This command selects the method of identifying the PDSCH resource allocation. \n
			:param format_py: OFF Applies the user configuration of the PDSCH subframe regardless of the signal characteristics. PDCCH Identifies the configuration according to the data in the PDCCH DCIs. PHYDET Manual PDSCH configuration: analysis only if the actual subframe configuration matches the configured one. Automatic PDSCH configuration: physical detection of the configuration.
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.PdschFormat)
		self._core.io.write(f'SENSe:LTE:DL:FORMat:PSCD {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PdschFormat:
		"""SCPI: [SENSe][:LTE]:DL:FORMat:PSCD \n
		Snippet: value: enums.PdschFormat = driver.applications.k10Xlte.sense.lte.downlink.formatPy.pscd.get() \n
		This command selects the method of identifying the PDSCH resource allocation. \n
			:return: format_py: OFF Applies the user configuration of the PDSCH subframe regardless of the signal characteristics. PDCCH Identifies the configuration according to the data in the PDCCH DCIs. PHYDET Manual PDSCH configuration: analysis only if the actual subframe configuration matches the configured one. Automatic PDSCH configuration: physical detection of the configuration."""
		response = self._core.io.query_str(f'SENSe:LTE:DL:FORMat:PSCD?')
		return Conversions.str_to_scalar_enum(response, enums.PdschFormat)
