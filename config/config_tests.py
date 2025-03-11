import os

from dotenv import load_dotenv

load_dotenv()

class ConfigTests:
    TESTING=True
    
    SECRET_KEY=os.getenv('SECRET_KEY')
    
    APP_PORT=os.getenv('APP_PORT')
    APP_HOST=os.getenv('APP_HOST')

    POSTGRES_USER=os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB=os.getenv('POSTGRES_DB')
    POSTGRES_PORT=os.getenv('POSTGRES_PORT')
    POSTGRES_HOST=os.getenv('POSTGRES_HOST')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@127.0.0.1:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"  
    