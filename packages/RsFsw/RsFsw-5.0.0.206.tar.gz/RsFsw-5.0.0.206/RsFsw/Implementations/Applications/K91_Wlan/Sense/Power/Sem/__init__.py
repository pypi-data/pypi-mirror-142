from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sem:
	"""Sem commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sem", core, parent)

	@property
	def classPy(self):
		"""classPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_classPy'):
			from .ClassPy import ClassPy
			self._classPy = ClassPy(self._core, self._cmd_group)
		return self._classPy

	def set(self, standard: enums.StandardK91) -> None:
		"""SCPI: [SENSe]:POWer:SEM \n
		Snippet: driver.applications.k91Wlan.sense.power.sem.set(standard = enums.StandardK91.ETSI) \n
		This command sets the Spectrum Emission Mask (SEM) measurement type. \n
			:param standard: (enum or string) IEEE | ETSI | User User Settings and limits are configured via a user-defined XML file. Load the file using method RsFsw.Applications.K91_Wlan.MassMemory.Load.Sem.State.set. IEEE Settings and limits are as specified in the IEEE Std 802.11n™-2009 Figure 20-17—Transmit spectral mask for 20 MHz transmission. For other IEEE standards see the parameter values in the table below. After a query, IEEE is returned for all IEEE standards. ETSI Settings and limits are as specified in the ETSI standard.
		"""
		param = Conversions.enum_ext_scalar_to_str(standard, enums.StandardK91)
		self._core.io.write(f'SENSe:POWer:SEM {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.StandardK91:
		"""SCPI: [SENSe]:POWer:SEM \n
		Snippet: value: enums.StandardK91 = driver.applications.k91Wlan.sense.power.sem.get() \n
		This command sets the Spectrum Emission Mask (SEM) measurement type. \n
			:return: standard: (enum or string) IEEE | ETSI | User User Settings and limits are configured via a user-defined XML file. Load the file using method RsFsw.Applications.K91_Wlan.MassMemory.Load.Sem.State.set. IEEE Settings and limits are as specified in the IEEE Std 802.11n™-2009 Figure 20-17—Transmit spectral mask for 20 MHz transmission. For other IEEE standards see the parameter values in the table below. After a query, IEEE is returned for all IEEE standards. ETSI Settings and limits are as specified in the ETSI standard."""
		response = self._core.io.query_str(f'SENSe:POWer:SEM?')
		return Conversions.str_to_scalar_enum_ext(response, enums.StandardK91)

	def clone(self) -> 'Sem':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sem(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
