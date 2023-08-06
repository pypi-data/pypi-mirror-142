from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scaling:
	"""Scaling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scaling", core, parent)

	def set(self, scaling_type: enums.ScalingMode) -> None:
		"""SCPI: [SENSe]:CORRection:TRANsducer:SCALing \n
		Snippet: driver.sense.correction.transducer.scaling.set(scaling_type = enums.ScalingMode.LINear) \n
		This command selects the frequency scaling of the transducer factor. \n
			:param scaling_type: LINear | LOGarithmic
		"""
		param = Conversions.enum_scalar_to_str(scaling_type, enums.ScalingMode)
		self._core.io.write(f'SENSe:CORRection:TRANsducer:SCALing {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ScalingMode:
		"""SCPI: [SENSe]:CORRection:TRANsducer:SCALing \n
		Snippet: value: enums.ScalingMode = driver.sense.correction.transducer.scaling.get() \n
		This command selects the frequency scaling of the transducer factor. \n
			:return: scaling_type: LINear | LOGarithmic"""
		response = self._core.io.query_str(f'SENSe:CORRection:TRANsducer:SCALing?')
		return Conversions.str_to_scalar_enum(response, enums.ScalingMode)
