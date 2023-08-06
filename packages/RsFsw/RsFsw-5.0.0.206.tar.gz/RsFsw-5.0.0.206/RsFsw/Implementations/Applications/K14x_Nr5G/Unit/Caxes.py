from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Caxes:
	"""Caxes commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caxes", core, parent)

	def set(self, axes: enums.AxesUnits) -> None:
		"""SCPI: UNIT:CAXes \n
		Snippet: driver.applications.k14Xnr5G.unit.caxes.set(axes = enums.AxesUnits.CARRier) \n
		This command selects the scale of the x-axis for result displays that show subcarrier results. \n
			:param axes: CARR Shows the number of the subcarriers on the x-axis. HZ Shows the frequency of the subcarriers on the x-axis.
		"""
		param = Conversions.enum_scalar_to_str(axes, enums.AxesUnits)
		self._core.io.write(f'UNIT:CAXes {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AxesUnits:
		"""SCPI: UNIT:CAXes \n
		Snippet: value: enums.AxesUnits = driver.applications.k14Xnr5G.unit.caxes.get() \n
		This command selects the scale of the x-axis for result displays that show subcarrier results. \n
			:return: axes: No help available"""
		response = self._core.io.query_str(f'UNIT:CAXes?')
		return Conversions.str_to_scalar_enum(response, enums.AxesUnits)
