""" module:: uds.programmer
    :platform: Posix
    :synopsis: A class file for a uds programmer
    moduleauthor:: Patrick Menschel (menschel.p@posteo.de)
    license:: GPL v3
"""
import threading
import time
from abc import ABC, abstractmethod

from enum import IntEnum, auto

from uds.common import *

from uds.client import UdsClient

import logging


class ProgrammerStates(IntEnum):
    """
    The enum for ProgrammerStates
    """
    NotConnected = auto()
    Connected = auto()
    PreProgramming = auto()
    SwitchToProgrammingMode = auto()
    UnlockDeviceForProgramming = auto()
    BlockProgramming = auto()
    PostProgramming = auto()
    ProgrammingFinished = auto()
    ProgrammingError = auto()
    Idle = auto()


class ProgrammingException(Exception):
    """
    General Programming Error
    """
    pass

class UdsProgrammerABC(ABC):
    """
    Abstract Base Class for an UDS Programmer class
    """

    def __init__(self,
                 client: Optional[UdsClient] = None,
                 programming_filepath: Optional[str] = None,
                 ):
        """
        Constructor

        :param client: A UdsClient for the uds services layer. Optional
                       Theoretically this can be created after reading a programming file.
        :param programming_filepath: The path to a programming file.
                                    It will be loaded automatically.
        """
        self._logger = logging.getLogger(__name__)
        self._client = client
        self._sleep_interval = 1  # 1 second

        self._programming_file = None
        self._expected_identifications = None
        self._state = None
        self._progress = None
        self._worker = threading.Thread(target=self.handle_state_machine)
        self._worker.setDaemon(True)

        if programming_filepath is not None:
            try:
                self.load_programming_file(filepath=programming_filepath)
            except AssertionError:
                raise ValueError("Could not load {0}".format(programming_filepath))

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, val):
        self._progress = val

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        assert isinstance(val, ProgrammerStates)
        self._logger.debug("Switch State {0} -> {1}".format(self.state.name, val.name))
        self._state = val

    def start_programming(self):
        assert self._client is not None
        assert self._programming_file is not None

        self._worker.start()  # when programming file has been loaded and uds client is set

    def check_if_connected(self):
        """
        A function to check if the programmer which
        by itself is a client, is connected to a server.
        :return: True if connected, False otherwise.
        """
        if self._client is not None:
            assert isinstance(self._client, UdsClient)
            try:
                self._client.tester_present()
            except UdsTimeoutError:
                return False
            else:
                return True

    def handle_state_machine(self):
        """
        The actual worker daemon of this class.
        :return: None
        """
        try:
            while True:
                if self.state == ProgrammerStates.NotConnected:
                    if self.check_if_connected():
                        self.state = ProgrammerStates.Connected
                    else:
                        self._logger.debug("{0} - sleep {1}".format(self.state.name, self._sleep_interval))
                        time.sleep(self._sleep_interval)

                elif self.state == ProgrammerStates.Connected:
                    self.state = ProgrammerStates.PreProgramming

                elif self.state == ProgrammerStates.PreProgramming:
                    if self.pre_programming():
                        self.state = ProgrammerStates.SwitchToProgrammingMode
                    else:
                        self.state = ProgrammerStates.ProgrammingError

                elif self.state == ProgrammerStates.SwitchToProgrammingMode:
                    if self.switch_to_programming_mode():
                        self.state = ProgrammerStates.UnlockDeviceForProgramming
                    else:
                        self.state = ProgrammerStates.ProgrammingError

                elif self.state == ProgrammerStates.UnlockDeviceForProgramming:
                    if self.unlock_device():
                        self.state = ProgrammerStates.BlockProgramming

                elif self.state == ProgrammerStates.BlockProgramming:
                    if self.block_programming():
                        self.state = ProgrammerStates.PostProgramming
                    else:
                        self.state = ProgrammerStates.ProgrammingError

                elif self.state == ProgrammerStates.PostProgramming:
                    if self.post_programming():
                        self.state = ProgrammerStates.ProgrammingFinished
                    else:
                        self.state = ProgrammerStates.ProgrammingError

                elif self.state == ProgrammerStates.ProgrammingFinished:
                    self.state = ProgrammerStates.Idle

                elif self.state == ProgrammerStates.ProgrammingError:
                    self.state = ProgrammerStates.Idle

                else:
                    # idle state
                    self._logger.info("{0} - nothing to do, sleeping 5 seconds".format(self.state.name))
                    time.sleep(self._sleep_interval)
        except ProgrammingException:
            LOGGER.error("State machine shutting down due to an error in State Handling {0}".format(self.state.name))


    @abstractmethod
    def load_programming_file(self, filepath: str) -> None:
        """
        1st phase of programming. Loading a programming file.
        Although uds has been standardized, the programming sequences have not and basically every EOM has
        their own flavor. Since ODX based formats have emerged, namely PDX, a programming ODX format,
        a programming file provides
           - binary data: the actual binaries to be programmed
           - means of communication with the target device: typically CAN IDs for an ISOTP channel
           - device compatibility checks based on what identification the device provides,
             e.g. a part number is provided by read data by id
           - device unlock and signature methods, e.g. used crypto functions and keys
           - meta data for each binary data:
             - where the binary goes, e.g. address or index of a binary block and
               subsequently if the location has to be erased in case of flash memory
             - precalculated hashes and signatures for binary blocks
             - binary data may be encrypted or compressed and the programming
               application must know this to populate the corresponding uds services
        This abstracted programmer must obtain all necessary information from the programming file.
        A OrderedDict of blocks has to be provided, ordered because because it matters in which sequence
        blocks are programmed. An item must provide meta data on the block, the definition is
        block_id: {"block_name": str,  # something to display
                   "block_address": int,  # where to put this block
                   "erase_before_download": bool,  # erase flag for destinations that need to be erased, e.g. flash
                   "uds_data_format_identifier": int, # a parameter for request download, e.g. compressed, encrypted
                   "binary_data": bytes,  # the actual data of the block, can be compressed or encrypted
                  }
        There can be general information on communication parameters as well.
        For example, some devices can't handle address items or size items other then 4bytes. In that case the item
        "uds_address_and_length_format_identifier": int, # parameter of request download
        has to be filled. To be continued...
        """

    @abstractmethod
    def pre_programming(self) -> bool:
        """
        2nd phase of programming
        Pre_programming:
        It consists of a couple of steps that occur linear.
        - Identification Check (Application / Optional)
          In case the programming file provides information or identification patterns on the target device,
          this should be checked against the connected device.
        - Preconditions Check (Application)
          An ECU must perform some task, so it must be asked if it is safe to purge regular operation,
          reboot and stay in bootloader without starting application.
        - Preparations Step (Application)
          Any necessary preparation, e.g. disable the settings of DTCs and stop all unnecessary communication.
          This is not actually plausible because when a programming session is started, the scope of operation
          of the ecu typically is very small, so it would not do anything other than handle diagnostic requests.
          It may even happen that an ECU does tell it's communication partners that it is not available for a limited
          time, i.e. like you tell your neighbors that your on holiday for the weekend, so they don't miss you
          and hopefully water your plants.
        - Transition to Programming Session (Application -> Bootloader)
          The most obvious step last but not least, the start of the programming session, which typically involves
          a reboot to bootloader, and setting some flags before, so bootloader waits for programming instead
          of starting application.
          This phase should also contain a sanity check if the programming session has been reached.

        :return: True if met, False otherwise
        """

    # 3rd phase of programming - the programming in programming session
    # this requires a state machine which is not yet written, however tasks during programming can be
    # abstracted into separate functions.

    def switch_to_programming_mode(self) -> bool:
        """
        Switch to Programming Mode
        Typically, a device has a second stage bootloader that has flash programming routines.
        There have been different methods to switch to bootloader operation, the most obvious one is to
        call DiagnosticSessionControl with Value Programming Mode.
        A child class should overwrite this method in case it this step is different.

        :return: True if successful, False otherwise
        """
        try:
            self._client.diagnostic_session_control(session=DiagnosticSession.ProgrammingSession)
        except UdsProtocolException as e:
            self._logger.error(e)
            return False
        else:
            return True

    @abstractmethod
    def unlock_device(self) -> bool:
        """
        Unlock the device for programming.
        Access to uds services required for programming usually require privileged access that can be gained by
        unlocking the device via security access methods. This procedure should be done in this function.

        :return: True if successful, False otherwise
        """

    @abstractmethod
    def pre_block_download(self,
                           addr: int,
                           erase_block: bool,
                           ) -> bool:
        """
        Prepare a block download.
        This function intended for block specific tasks before the block is downloaded.
        In general there are multiple things to do when programming a block.
        At first there are hardware constraints. A non-volatile flash memory block needs to be erased
        before it can be programmed again. Therefore the uds client commands the uds server to erase
        that block, typically be routine control uds service.
        Another task may be the use of a journal for a block, e.g. a programming entry, who?, what?, when?,
        how often has the block been programmed, when does it starts to wear out?

        :return: True if successful, False otherwise
        """


    def block_programming(self, blocks: dict):
        """
        A universal function for the state block programming.
        :return: True if successful, False otherwise
        """
        try:
            for block in blocks:
                self.pre_block_download(addr=block.get("addr"),
                                        erase_block=block.get("erase_block"))
                self.download_block(addr=block.get("addr"),
                                    data=block.get("data"),
                                    compression_method=block.get("compression_method"),
                                    encryption_method=block.get("encryption_method"),
                                    transfer_request_parameters=block.get("transfer_request_parameters"))
                self.post_block_download(addr=block.get("addr"),
                                         checksum=block.get("checksum"),
                                         signature=block.get("signature"))
            return True
        except UdsProtocolException:
            return False


    def download_block(self,
                       addr: int,
                       data: bytes,
                       compression_method: CompressionMethod = CompressionMethod.NO_COMPRESSION,
                       encryption_method: EncryptionMethod = EncryptionMethod.NO_ENCRYPTION,
                       transfer_request_parameters: bytes = bytes()) -> True:
        """
        Download a block.
        This function is universal due to the defined set of uds services for this purpose.
        :param addr: The address of the download.
        :param data: The data to be transferred.
        :param compression_method: The method of compression.
        :param encryption_method: The method of encryption.
        :param transfer_request_parameters: A never used manufacturer specific value.
        :return: Nothing.
        """
        size = len(data)
        self._logger.debug("Download Block - Request Download addr {0} size {1}".format(addr, size))
        resp = self._client.request_download(addr=addr,
                                             size=size,
                                             compression_method=compression_method,
                                             encryption_method=encryption_method)
        block_size = resp.get("max_block_length")

        for chunk_idx, chunk_bytes in enumerate(
                [data[idx:idx + block_size] for idx in range(0, len(data), block_size)]):
            self._logger.debug(
                "Download Block - Transfer Data Block {0} Size {1}".format(chunk_idx + 1, len(chunk_bytes)))
            self._client.transfer_data(block_sequence_counter=chunk_idx + 1,
                                       data=chunk_bytes)
        self._logger.debug("Download Block - Request Transfer Exit")
        self._client.request_transfer_exit(transfer_request_parameters=transfer_request_parameters)
        self._logger.debug("Download Block - Complete")

        success = True
        return success

    @abstractmethod
    def post_block_download(self,
                            addr: int,
                            checksum: bytes,
                            signature: bytes,
                            ) -> bool:
        """
        Check a block after download.
        This function is intended for block specific tasks after a block was downloaded.
        Typical task is a check for data integrity, e.g. the uds client starts a checksum routine
        on the uds server and either provides the expected checksum for check or the uds server sends
        the checksum back, so the client can compare and decide what to do.
        There may also be crypto involved, e.g. a signature check.

        :return: True if successful, False otherwise
        """

    @abstractmethod
    def post_programming(self) -> bool:
        """
        Post programming.
        This function is intended for the big cleanup after the block programming has happened.
        The goal is to have the freshly programmed device resume it's tasks by starting application again.
        This is usually done by switching back to default session or calling ecu reset.
        After the device is running application again, it may also be needed to re-enable services that have
        been disabled in pre programming step.
        :return: True if successful, False otherwise
        """


class ExampleUdsProgrammer(UdsProgrammerABC):
    def load_programming_file(self, filepath: str) -> bool:
        """
        Load the programming file. Save filepath to private variable
        for an easy example.
        :param filepath: The filepath.
        :return: True if successful.
        """
        self._programming_file = filepath
        return True

    def pre_programming(self) -> bool:
        """
        Check if the logical preconditions for programming are fulfilled.
        You won't flash an engine ecu while the engine is running, would you?
        Well it can be done in some rare cases.
        :return: True if successful.
        """
        check_programming_did = 0xBEEF
        data = self._client.read_data_by_id(did=check_programming_did).get("data")
        status = bool.from_bytes(data, "big")
        return status

    def unlock_device(self) -> bool:
        """
        Execute seed and key routine to unlock the device.
        :return: True if successful.
        """
        security_level = 1
        seed = self._client.security_access(security_level=security_level).get("seed")
        key = struct.pack(">I", struct.unpack(">I", seed)[0] + 1)
        self._client.security_access(security_level=security_level + 1, key=key)
        success = True
        return success

    def pre_block_download(self,
                           addr: int,
                           erase_block: bool,
                           ) -> bool:
        """
        Write the workshop name into the device for
        an easy example.
        :param addr: The address of the block.
        :param erase_block: The erase flag.
        :return: True if successful.
        """
        workshop_did = 0xCAFE
        self._client.write_data_by_id(did=workshop_did, data="1234".encode())
        success = True
        return success

    def post_block_download(self,
                            addr: int,
                            checksum: bytes,
                            signature: bytes,
                            ) -> bool:
        """
        Execute a check routine in device.
        :param addr: The address of the block.
        :param checksum: The block checksum.
        :param signature: The block signature.
        :return: True if successful.
        """
        self._client.routine_control(routine_control_type=RoutineControlType.StartRoutine,
                                     routine_id=0x1234,
                                     data=bytes.fromhex("11 22 33 44 55 66 77 88"))
        success = True
        return success

    def post_programming(self) -> bool:
        """
        Write the programming date for an easy example.
        :return: True if successful.
        """
        programming_date_did = 0x4242
        self._client.write_data_by_id(did=programming_date_did, data=bytes.fromhex("11 22 33 44"))
        success = True
        return success
