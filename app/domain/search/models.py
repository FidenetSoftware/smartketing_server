from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ...database import Base

class Search(Base):
    __tablename__ = 'search'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String, unique=True, index=True)
    creation_date = Column(DateTime(timezone=True), unique=True, index=True)
    update_date = Column(DateTime(timezone=True), unique=True, index=True)

    tweet_searches = relationship("TW_Extraction", back_populates="search")
    youtube_searches = relationship("YT_Extraction", back_populates="youtube")
    news_searches = relationship("News_Extraction", back_populates="news")
    twitch_searches = relationship("Twitch_Extraction", back_populates="twitch")
    