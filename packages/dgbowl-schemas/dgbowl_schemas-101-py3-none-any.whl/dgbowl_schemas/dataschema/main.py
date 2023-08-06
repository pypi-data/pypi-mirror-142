from pydantic import BaseModel, validator, root_validator, Extra, PrivateAttr
from typing import Optional
import os
import logging

logger = logging.getLogger(__name__)


class Metadata(BaseModel):
    provenance: str
    version: str
    timezone: str = "localtime"
    provenance_metadata: Optional[dict]

    @root_validator(pre=True)
    def check_version(cls, values):
        version = values.get("version")
        if version is None:
            for k in {"dataschema_version", "schema_version"}:
                if k in values:
                    version = values.pop(k)
        values["version"] = version
        return values


class Input(BaseModel, extra=Extra.forbid):
    files: list[str]
    prefix: Optional[str]
    suffix: Optional[str]
    contains: Optional[str]
    exclude: Optional[str]
    encoding: Optional[str] = "UTF-8"

    @root_validator(pre=True)
    def check_exclusive(cls, values):
        keys = {"files", "folders"}.intersection(set(values))
        if len(keys) > 1:
            raise ValueError(
                f"Specifying multiple arguments ({keys}) to Input is not allowed."
            )
        elif len(keys) == 0:
            raise ValueError(f"Either 'files' or 'folders' must be supplied to Input.")
        if values.get("files") is not None:
            pass
        else:
            folders = values.pop("folders")
            files = []
            for folder in folders:
                files += [os.path.join(folder, file) for file in os.listdir(folder)]
            values["files"] = files
        return values

    def paths(self) -> list[str]:
        ret = []
        for path in self.files:
            tail = os.path.basename(path)
            inc = True
            if self.prefix is not None and not tail.startswith(self.prefix):
                inc = False
            if self.suffix is not None and not tail.endswith(self.suffix):
                inc = False
            if self.contains is not None and self.contains not in tail:
                inc = False
            if self.exclude is not None and self.exclude in tail:
                inc = False
            if inc:
                ret.append(path)
        return ret


class ED_File(BaseModel):
    path: str
    type: str
    match: Optional[str]


class ED_Filename(BaseModel):
    format: str
    len: int


class ED_Using(BaseModel):
    isostring: Optional[str]
    utsoffset: Optional[float]
    file: Optional[ED_File]
    filename: Optional[ED_Filename]

    @root_validator(pre=True)
    def check_exclusive(cls, values):
        keys = {"isostring", "utsoffset", "file", "filename"}.intersection(set(values))
        if len(keys) > 1:
            raise ValueError(
                f"Specifying multiple arguments ({keys}) to ExternalDate "
                "is not allowed."
            )
        return values


class ExternalDate(BaseModel):
    using: ED_Using
    mode: str = "add"
    _default: bool = PrivateAttr()

    class Config:
        extra = Extra.forbid

    def __init__(self, **data):
        self._default = False
        super().__init__(**data)

    @root_validator(pre=True)
    def check_using(cls, values):
        using = values.pop("using", None)
        if using is None and "from" in values:
            logger.warning(
                "Specifying 'using' parameter of ExternalDate via the 'from' key is "
                "deprecated and may stop working in future versions of Dataschema."
            )
            using = values.pop("from")
        if using is None:
            using = {"filename": {"format": "%Y-%m-%d-%H-%M-%S", "len": 19}}
            cls._default = True
        values["using"] = using
        return values

    @validator("mode")
    def mode_is_known(cls, v):
        if v not in {"add", "replace"}:
            raise ValueError(
                f"The provided ExternalDate 'mode' type '{v}' was not understood."
            )
        return v


class Timestamp(BaseModel):
    index: int = None
    format: str = None


class Parameters(BaseModel):
    filetype: Optional[str]

    @root_validator(pre=True)
    def check_tracetype(cls, values):
        if values.get("filetype") is None:
            filetype = values.pop("tracetype", None)
            if filetype is not None:
                logger.warning(
                    "Specifying 'filetype' in Parameters using the 'tracetype' key is "
                    "deprecated and may stop working in future versions of Dataschema."
                )
                values["filetype"] = filetype
        return values

    @validator("filetype", always=False)
    def filetype_is_known(cls, v):
        if v in {"drycal"}:
            logger.warning(
                "The entry '{v}' supplied as 'filetype' in Parameters is "
                "deprecated and may stop working in future versions of Dataschema."
            )
            return v
        if v not in {
            "ezchrom.asc",
            "fusion.json",
            "fusion.zip",
            "agilent.ch",
            "agilent.dx",
            "agilent.csv",
            "labview.csv",
            "quadstar.sac",
            "phi.spe",
            "drycal.csv",
            "drycal.rtf",
            "drycal.txt",
            "eclab.mpt",
            "eclab.mpr",
        }:
            raise ValueError(
                "The entry '{v}' supplied as 'filetype' in Parameters is "
                "not supported."
            )
        return v


class Step(BaseModel, extra=Extra.forbid):
    parser: str
    input: Input
    tag: str = None
    parameters: Optional[dict]
    externaldate: Optional[ExternalDate]
    export: Optional[str]

    @root_validator(pre=True)
    def check_import(cls, values):
        input = values.get("input")
        if input is None and "import" in values:
            logger.warning(
                "Specifying 'input' files of a Step using the 'import' key is "
                "deprecated and may stop working in future versions of 'dataschema'."
            )
            input = values.pop("import")
        if input is None:
            raise ValueError("The 'input' section has to be specified for each Step.")
        values["input"] = input
        return values

    @validator("externaldate", always=True, pre=True)
    def default_externaldate(cls, v):
        return v or {}

    @validator("parameters", always=True, pre=True)
    def default_parameters(cls, v):
        return v or {}

    @validator("parser")
    def parser_is_known(cls, v):
        if v not in {
            "chromtrace",
            "masstrace",
            "qftrace",
            "xpstrace",
            "basiccsv",
            "meascsv",
            "flowdata",
            "electrochem",
            "dummy",
        }:
            raise ValueError(
                f"The name '{v}' provided as a 'parser' in Step was not understood."
            )
        return v


class Dataschema(BaseModel, extra=Extra.forbid):
    """
    Schema of the Dataschema object.

    Must contain:
    
    - a 'metadata' entry containing a Metadata object
    - a 'steps' entry containing a list of Step objects

    """
    metadata: Metadata
    steps: list[Step]
