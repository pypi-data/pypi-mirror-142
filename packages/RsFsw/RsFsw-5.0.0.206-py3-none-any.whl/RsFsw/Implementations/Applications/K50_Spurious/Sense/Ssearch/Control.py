from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Control:
	"""Control commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("control", core, parent)

	def set(self, step: enums.MeasurementStep) -> None:
		"""SCPI: [SENSe]:SSEarch:CONTrol \n
		Snippet: driver.applications.k50Spurious.sense.ssearch.control.set(step = enums.MeasurementStep.NESTimate) \n
		Defines which steps of the measurement process are performed. All steps up to the selected step are performed. By default,
		all measurement steps are performed. For details on the measurement process steps see 'Measurement process'. \n
			:param step: SOVerview | NESTimate | SDETection | SPOTstep SOVerview Spectral overview only NESTimate Spectral overview and Noise Floor Estimation SDETection Spectral overview, Noise Floor Estimation, and Spurious Detection measurement SPOT Spot Search - all measurement steps are performed
		"""
		param = Conversions.enum_scalar_to_str(step, enums.MeasurementStep)
		self._core.io.write(f'SENSe:SSEarch:CONTrol {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MeasurementStep:
		"""SCPI: [SENSe]:SSEarch:CONTrol \n
		Snippet: value: enums.MeasurementStep = driver.applications.k50Spurious.sense.ssearch.control.get() \n
		Defines which steps of the measurement process are performed. All steps up to the selected step are performed. By default,
		all measurement steps are performed. For details on the measurement process steps see 'Measurement process'. \n
			:return: step: SOVerview | NESTimate | SDETection | SPOTstep SOVerview Spectral overview only NESTimate Spectral overview and Noise Floor Estimation SDETection Spectral overview, Noise Floor Estimation, and Spurious Detection measurement SPOT Spot Search - all measurement steps are performed"""
		response = self._core.io.query_str(f'SENSe:SSEarch:CONTrol?')
		return Conversions.str_to_scalar_enum(response, enums.MeasurementStep)
