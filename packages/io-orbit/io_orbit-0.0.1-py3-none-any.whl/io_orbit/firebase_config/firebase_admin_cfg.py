import firebase_admin
from firebase_admin import storage
from firebase_admin import credentials
import gcsfs
import os

class FirebaseBucketRights():
    def __init__(self) -> None:
        self.filesystem = gcsfs.GCSFileSystem(project=os.getenv('IO_PROJECT'), token=os.getenv('IO_KEY'))
        self.credentials = credentials.Certificate(os.getenv('IO_KEY'))
        self.initialize_app = firebase_admin.initialize_app(self.credentials)
        pass

    def initialize_firebase(self):
        fs = self.filesystem
        cred = self.credentials
        self.initialize_app
        return fs