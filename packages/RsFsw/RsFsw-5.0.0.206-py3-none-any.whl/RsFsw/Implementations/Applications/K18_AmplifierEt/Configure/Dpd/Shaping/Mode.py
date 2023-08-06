from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, method: enums.ShapingMethod) -> None:
		"""SCPI: CONFigure:DPD:SHAPing:MODE \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.shaping.mode.set(method = enums.ShapingMethod.POLYnomial) \n
		This command selects the method use to shape the DPD function. \n
			:param method: POLYnomial DPD function based on the characteristics of the polynomial system model. TABLe DPD function based on the correction values kept in a table calculated by the R&S SMW.
		"""
		param = Conversions.enum_scalar_to_str(method, enums.ShapingMethod)
		self._core.io.write(f'CONFigure:DPD:SHAPing:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ShapingMethod:
		"""SCPI: CONFigure:DPD:SHAPing:MODE \n
		Snippet: value: enums.ShapingMethod = driver.applications.k18AmplifierEt.configure.dpd.shaping.mode.get() \n
		This command selects the method use to shape the DPD function. \n
			:return: method: POLYnomial DPD function based on the characteristics of the polynomial system model. TABLe DPD function based on the correction values kept in a table calculated by the R&S SMW."""
		response = self._core.io.query_str(f'CONFigure:DPD:SHAPing:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ShapingMethod)
