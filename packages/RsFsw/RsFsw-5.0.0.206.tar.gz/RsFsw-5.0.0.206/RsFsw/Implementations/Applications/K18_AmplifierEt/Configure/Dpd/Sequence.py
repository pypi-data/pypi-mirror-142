from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequence:
	"""Sequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequence", core, parent)

	def set(self, state: enums.DpdOrder) -> None:
		"""SCPI: CONFigure:DPD:SEQuence \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.sequence.set(state = enums.DpdOrder.AMFirst) \n
		This command selects the order in which the AM/AM and AM/PM distortion are applied. Available when both have been turned
		on.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Turn on both AM/AM and AM/PM calculation (method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Amam.State.set / method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.AmPm.State.set) . \n
			:param state: AMFirst Calculates the AM/AM distortion first, then the AM/PM distortion. PMFirst Calculates the AM/PM distortion first, then the AM/AM distortion.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.DpdOrder)
		self._core.io.write(f'CONFigure:DPD:SEQuence {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DpdOrder:
		"""SCPI: CONFigure:DPD:SEQuence \n
		Snippet: value: enums.DpdOrder = driver.applications.k18AmplifierEt.configure.dpd.sequence.get() \n
		This command selects the order in which the AM/AM and AM/PM distortion are applied. Available when both have been turned
		on.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Turn on both AM/AM and AM/PM calculation (method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Amam.State.set / method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.AmPm.State.set) . \n
			:return: state: AMFirst Calculates the AM/AM distortion first, then the AM/PM distortion. PMFirst Calculates the AM/PM distortion first, then the AM/AM distortion."""
		response = self._core.io.query_str(f'CONFigure:DPD:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.DpdOrder)
