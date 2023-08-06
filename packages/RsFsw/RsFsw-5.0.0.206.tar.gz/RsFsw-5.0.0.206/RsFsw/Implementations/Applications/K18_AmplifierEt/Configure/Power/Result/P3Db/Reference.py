from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def set(self, ref_power: float) -> None:
		"""SCPI: CONFigure:POWer:RESult:P3DB:REFerence \n
		Snippet: driver.applications.k18AmplifierEt.configure.power.result.p3Db.reference.set(ref_power = 1.0) \n
		This command defines the input power corresponding to the gain reference required to calculate the compression points.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn off automatic calculation of the reference point (method RsFsw.Applications.K18_AmplifierEt.Configure.Power.Result.P3Db.State.set) . \n
			:param ref_power: numeric value Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(ref_power)
		self._core.io.write(f'CONFigure:POWer:RESult:P3DB:REFerence {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:POWer:RESult:P3DB:REFerence \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.power.result.p3Db.reference.get() \n
		This command defines the input power corresponding to the gain reference required to calculate the compression points.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn off automatic calculation of the reference point (method RsFsw.Applications.K18_AmplifierEt.Configure.Power.Result.P3Db.State.set) . \n
			:return: ref_power: numeric value Unit: dBm"""
		response = self._core.io.query_str(f'CONFigure:POWer:RESult:P3DB:REFerence?')
		return Conversions.str_to_float(response)
