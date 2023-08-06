from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, use_wfm_for_sync: enums.AutoManualMode) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:PATTern:SYNC:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.pattern.sync.auto.set(use_wfm_for_sync = enums.AutoManualMode.AUTO) \n
		This command selects manual or automatic synchronization with a pattern waveform to speed up measurements. \n
			:param use_wfm_for_sync: AUTO | MANual
		"""
		param = Conversions.enum_scalar_to_str(use_wfm_for_sync, enums.AutoManualMode)
		self._core.io.write(f'SENSe:DDEMod:SEARch:PATTern:SYNC:AUTO {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoManualMode:
		"""SCPI: [SENSe]:DDEMod:SEARch:PATTern:SYNC:AUTO \n
		Snippet: value: enums.AutoManualMode = driver.applications.k70Vsa.sense.ddemod.search.pattern.sync.auto.get() \n
		This command selects manual or automatic synchronization with a pattern waveform to speed up measurements. \n
			:return: use_wfm_for_sync: AUTO | MANual"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:PATTern:SYNC:AUTO?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
