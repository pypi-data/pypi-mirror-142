from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, type_py: enums.PhaseTrackingMethod) -> None:
		"""SCPI: [SENSe][:LTE]:UL:TRACking:PHASe \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.tracking.phase.set(type_py = enums.PhaseTrackingMethod.OFF) \n
		This command selects the phase tracking method. \n
			:param type_py: OFF Deactivate phase tracking PIL Pilot only PILP Pilot and payload
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.PhaseTrackingMethod)
		self._core.io.write(f'SENSe:LTE:UL:TRACking:PHASe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PhaseTrackingMethod:
		"""SCPI: [SENSe][:LTE]:UL:TRACking:PHASe \n
		Snippet: value: enums.PhaseTrackingMethod = driver.applications.k10Xlte.sense.lte.uplink.tracking.phase.get() \n
		This command selects the phase tracking method. \n
			:return: type_py: OFF Deactivate phase tracking PIL Pilot only PILP Pilot and payload"""
		response = self._core.io.query_str(f'SENSe:LTE:UL:TRACking:PHASe?')
		return Conversions.str_to_scalar_enum(response, enums.PhaseTrackingMethod)
