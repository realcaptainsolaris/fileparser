from pathlib import Path
from pydantic import BaseModel, Field, field_validator


class FileInfo(BaseModel):
    name: str
    suffix: str = Field(default="")
    type: str = Field(default="unknown")

    @field_validator("type", mode="before")
    def normalize_type(cls, v: str) -> str:
        return v.lower() if v else "unknown"


def parse(filename: str) -> FileInfo:
    """Parse file information using pathlib and return a validated Pydantic model."""
    path = Path(filename)
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"{filename!r} not found or not a file")

    data = {
        "name": path.stem,
        "suffix": path.suffix,
        "type": path.suffix.lstrip(".") or "unknown",
    }

    return FileInfo(**data)
