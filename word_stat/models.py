import datetime

from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Word(Base):
    __tablename__ = "word"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str]
    tf: Mapped[float]
    idf: Mapped[float]
    count: Mapped[int]
    file_id: Mapped[int] = mapped_column(ForeignKey('file.id'))


class File(Base):
    __tablename__ = "file"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    status: Mapped[str]
    collection_id: Mapped[int] = mapped_column(ForeignKey('collection.id'))


class FileCollection(Base):
    __tablename__ = "collection"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(), server_default=func.now())
