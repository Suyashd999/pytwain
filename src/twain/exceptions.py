class TwainError(Exception):
    """
    Base error for all errors returned by TWAIN driver
    """
    pass


class CapabilityFormatNotSupported(TwainError):
    """
    Specified capability is not supported by pytwain
    """
    pass


class DSTransferCancelled(TwainError):
    """
    Data transfer was cancelled by user
    """
    pass


class SMGetProcAddressFailed(TwainError):
    """
    Specified driver does not have DSM_Entry symbol defined
    """
    pass


class SMLoadFileFailed(TwainError):
    """
    Failed to load DLL
    """
    pass


class SMOpenFailed(TwainError):
    """
    DSM entry point returned error when called.
    """
    pass


class ImageFormatNotSupported(TwainError):
    """
    Image has unsupported format.
    E.g. compressed images are not supported currently.
    """
    pass


class BadCapability(TwainError):
    """
    Source does not support specified capability.
    Sources newer than 1.6 do not use report this error.
    """
    pass


class BadDestination(TwainError):
    """
    Operation was sent to invalid Source
    """
    pass


class BadProtocol(TwainError):
    """
    Operation is not recognized by Source
    """
    pass


class GeneralFailure(TwainError):
    """General failure.  Unload Source immediately."""
    pass


class CapBadOperation(TwainError):
    """Operation (i.e., Get or Set)  not supported on capability."""
    pass


class CapSeqError(TwainError):
    """Capability has dependencies on other capabilities and
    cannot be operated upon at this time.
    """
    pass


class CapUnsupported(TwainError):
    """
    Capability not supported by Source.
    Sources with version 1.6 and newer use this error instead of BadCapability error
    """
    pass


class CheckDeviceOnlineError(TwainError):
    """Check the device status using CAP_DEVICEONLINE, this
    condition code can be returned by any TWAIN operation
    in state 4 or higher, or from the state 3 DG_CONTROL /
    DAT_IDENTITY / MSG_OPENDS.  The state remains
    unchanged.  If in state 4 the Application can poll with
    CAP_DEVICELINE until the value returns TRUE.
    """
    pass


class DeniedError(TwainError):
    """
    Operation denied
    """
    pass


class FileExistsError(TwainError):
    """
    Specified file already exists.
    """
    pass


class FileWriteError(TwainError):
    """
    Operation failed writing to the file.
    """
    pass


class MaxConnectionsError(TwainError):
    """
    Device is connected to maximum number of applications it can support.
    """
    pass


class NoDataSourceError(TwainError):
    """
    No Source found
    """
    pass


class NotEmptyError(TwainError):
    """
    Directory not empty and cannot be deleted
    """
    pass


class OperationError(TwainError):
    """Internal Source error"""
    pass


class PaperDoubleFeedError(TwainError):
    """
    Feeder error.  This error is obsolete but may still be reported by older sources.
    """
    pass


class PaperJam(TwainError):
    """
    Paper got stuck in feeder
    """
    pass


class SequenceError(TwainError):
    """
    Operation was called at a wrong state
    """
    pass


class UnknownError(TwainError):
    """
    Unknown error code was returned.
    Probably need to upgrade pytds to newer version.
    """
    pass


class CancelAll(Exception):
    """Exception used by callbacks to cancel remaining image transfers"""
    pass


class CheckStatus(Exception):
    """This exception means that operation succeeded but user value was truncated
    to fit valid range
    """
    pass


# Following exception aliases are deprecated
# and will be removed in version 2.4.0
excCapabilityFormatNotSupported = CapabilityFormatNotSupported
excDSTransferCancelled = DSTransferCancelled
excSMGetProcAddressFailed = SMGetProcAddressFailed
excSMLoadFileFailed = SMLoadFileFailed
excSMOpenFailed = SMOpenFailed
excImageFormat = ImageFormatNotSupported
excTWCC_BADCAP = BadCapability
excTWCC_BADDEST = BadDestination
excTWCC_BADPROTOCOL = BadProtocol
excTWCC_BUMMER = GeneralFailure
excTWCC_CAPBADOPERATION = CapBadOperation
excTWCC_CAPSEQERROR = CapSeqError
excTWCC_CAPUNSUPPORTED = CapUnsupported
excTWCC_CHECKDEVICEONLINE = CheckDeviceOnlineError
excTWCC_DENIED = DeniedError
excTWCC_FILEEXISTS = FileExistsError
excTWCC_FILEWRITEERROR = FileWriteError
excTWCC_MAXCONNECTIONS = MaxConnectionsError
excTWCC_NODS = NoDataSourceError
excTWCC_NOTEMPTY = NotEmptyError
excTWCC_OPERATIONERROR = OperationError
excTWCC_PAPERDOUBLEFEED = PaperDoubleFeedError
excTWCC_PAPERJAM = PaperJam
excTWCC_SEQERROR = SequenceError
excTWCC_UNKNOWN = UnknownError
