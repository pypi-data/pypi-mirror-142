from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scale:
	"""Scale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scale", core, parent)

	def set(self, state: enums.ScalingMode) -> None:
		"""SCPI: CONFigure:MODeling:SCALe \n
		Snippet: driver.applications.k18AmplifierEt.configure.modeling.scale.set(state = enums.ScalingMode.LINear) \n
		This command selects the method by which the input power range is split into smaller ranges for the calculation of the
		amplifier model. \n
			:param state: LINear Input power range is split on a linear basis. LOGarithmic Input power range is split on a logarithmic basis.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.ScalingMode)
		self._core.io.write(f'CONFigure:MODeling:SCALe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ScalingMode:
		"""SCPI: CONFigure:MODeling:SCALe \n
		Snippet: value: enums.ScalingMode = driver.applications.k18AmplifierEt.configure.modeling.scale.get() \n
		This command selects the method by which the input power range is split into smaller ranges for the calculation of the
		amplifier model. \n
			:return: state: LINear Input power range is split on a linear basis. LOGarithmic Input power range is split on a logarithmic basis."""
		response = self._core.io.query_str(f'CONFigure:MODeling:SCALe?')
		return Conversions.str_to_scalar_enum(response, enums.ScalingMode)
