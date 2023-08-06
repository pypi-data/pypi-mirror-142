from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Method:
	"""Method commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("method", core, parent)

	def set(self, method: enums.GprdMeasMethod) -> None:
		"""SCPI: [SENSe]:ADEMod:MCPHase:METHod \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.mcPhase.method.set(method = enums.GprdMeasMethod.FLATtop) \n
		This command selects the method used for group delay measurements. This command is maintained for compatibility reasons
		only. As the R&S FSW MCGD application only supports orthogonal measurements, this command returns an error if the FLATtop
		parameter is used. \n
			:param method: ORTHogonal | FLATtop
		"""
		param = Conversions.enum_scalar_to_str(method, enums.GprdMeasMethod)
		self._core.io.write(f'SENSe:ADEMod:MCPHase:METHod {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GprdMeasMethod:
		"""SCPI: [SENSe]:ADEMod:MCPHase:METHod \n
		Snippet: value: enums.GprdMeasMethod = driver.applications.k17Mcgd.sense.ademod.mcPhase.method.get() \n
		This command selects the method used for group delay measurements. This command is maintained for compatibility reasons
		only. As the R&S FSW MCGD application only supports orthogonal measurements, this command returns an error if the FLATtop
		parameter is used. \n
			:return: method: ORTHogonal | FLATtop"""
		response = self._core.io.query_str(f'SENSe:ADEMod:MCPHase:METHod?')
		return Conversions.str_to_scalar_enum(response, enums.GprdMeasMethod)
