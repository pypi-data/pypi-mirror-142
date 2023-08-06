import requests
import os


class StorckClient:
    def __init__(
        self,
        api_host: str = "http://localhost:8000",
        user_token: str = None,
        workspace_token: str = None,
    ):
        """
        The main class for creating connection to storck database.

        :param api_host: The adress of the storck instance
        :param user_token: the token of the user, if not defined, the environment variable STORCK_USER_TOKEN will be used
        :param user_token: the token of the workspace, if not defined, the environment variable STORCK_WORKSPACE_TOKEN will be used
        """
        self.api_host = os.getenv("STORCK_API_HOST", default=api_host)
        self.user_token = user_token or os.getenv("STORCK_USER_TOKEN")
        self.workspace_token = workspace_token or os.getenv("STORCK_WORKSPACE_TOKEN")

    def auth_verify(self) -> dict:
        """

        Check whether user exists in storck.
        """
        self._is_authorized()
        return self._post(
            "/api/auth", headers={"Authorization": "Token {}".format(self.user_token)}
        )

    def set_workspace_token(self, workspace_token: str):
        """
        Will override the current workspace_token, and also environment variable
        """
        self.workspace_token = workspace_token.token
        os.putenv("STORCK_WORKSPACE_TOKEN", self.workspace_token)

    def create_workspace(self, name:str) -> dict:
        """
        Will create a workspace with given name.
        """
        self._is_authorized()
        content = self._post(
            "/api/workspace",
            data={"name": name},
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["data"]

    def get_workspaces(self) -> dict:
        """
        Gets the list of current workspaces


       :return: dict of workspaces
        """
        self._is_authorized()
        content = self._get(
            "/api/workspaces",
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["data"]["workspaces"]

    def get_files(self, name_contains:str=None, meta_search:str=None) -> dict:
        """
        Searches for files. If name_contains will be provided, looks for a filename containig gie string.
        If meta_search is provided, will use it as the JSON encoded string query.

        :param name_contains: A string with a pattern
        :param meta_search: A stringified JSON containing relevant query https://docs.djangoproject.com/en/4.0/topics/db/queries/#querying-jsonfield.
        This json will be unpacked to python dict, which will be unpacked as arguments of filter function in django.
        :return: list of files matching the query
        """
        self._is_authorized()
        self._is_workspace_set()
        query = {"token": self.workspace_token}
        if name_contains is not None:
            query["filename_contains"] = name_contains
        if meta_search is not None:
            query["meta_search"] = meta_search
        content = self._get(
            "/api/files",
            query=query,
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["files"]

    def get_info(self, file_id:int=None, path:str=None) -> dict:
        """
        Gets detailed information about the file.

        :param file_id: id of the file.
        :param path: database path of the file
        """
        self._is_authorized()
        self._is_workspace_set()
        content = self._get(
            "/api/file",
            query={
                "info": True,
                "path": path,
                "id": file_id,
                "token": self.workspace_token,
            },
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["file"]

    def upload_file(self, filename:str, path:str=None) -> dict:
        """
        Uploads the file to storck.

        :param filename: Path to the file on the client side.
        :param path: Optional database path to be used in storck. If not provided filename will be used instead.
        """

        self._is_authorized()
        self._is_workspace_set()
        return self._post(
            "/api/file",
            query={"token": self.workspace_token},
            data={"path": path or filename},
            files={"file": open(filename, "rb")},
            headers={"Authorization": "Token {}".format(self.user_token)},
        )

    def download_file(self, file_id: int) -> bytes:
        """
        Downloads the content of the file.

        :param file_id: Id of the file to downloaded.
        """
        self._is_authorized()
        self._is_workspace_set()
        return self._get_raw(
            "/api/file",
            query={"id": file_id, "token": self.workspace_token},
            headers={"Authorization": "Token {}".format(self.user_token)},
        )

    def add_user_to_workspace(self, user_id: int):
        """
        Adds users to workspace.

        :param user_id: the id of the user to be added to the workspace.
        """
        self._is_authorized()
        self._is_workspace_set()
        content = self._post(
            "/api/workspace/user",
            data={"user_id": user_id, "token": self.workspace_token},
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["data"]

    def _is_authorized(self):
        if self.user_token is None:
            raise Exception("You need to provide user token")

    def _is_workspace_set(self):
        if self.workspace_token is None:
            raise Exception("You need to provide workspace token")

    def _post(self, path, query=None, data=None, files=None, headers=None):
        content = requests.post(
            "{}{}".format(self.api_host, path),
            data=data,
            files=files,
            params=query,
            headers=headers,
        )
        content.raise_for_status()
        return content.json()

    def _get(self, path, query=None, headers=None):
        content = requests.get(
            "{}{}".format(self.api_host, path), params=query, headers=headers
        )
        content.raise_for_status()
        return content.json()

    def _get_raw(self, path, query=None, headers=None):
        content = requests.get(
            "{}{}".format(self.api_host, path),
            params=query,
            headers=headers,
            stream=True,
        )
        content.raise_for_status()
        return content.raw.read()



import os
import hashlib
import argparse
from os import listdir
from os.path import isfile, join
from requests import HTTPError



class AutoUploadScript:
    def __init__(self, api_host, user_token, workspace_token, upload_dir='./drop'):
        self.upload_dir = os.getenv('STORCK_AUTO_UPLOAD_DIR', upload_dir)
        self.storck_client = StorckClient(api_host, user_token, workspace_token)

    def load_files_list(self):
        files = [f for f in listdir(self.upload_dir) if isfile(join(self.upload_dir, f))]
        return files

    def filter_files(self, files_list):
        new_files = []
        for file in files_list:
            try:
                storck_file = self.storck_client.get_info(path=file)
                local_file_hash = self._hash_file(file)
                if local_file_hash != storck_file['hash']:
                    new_files.append(file)
            except HTTPError as e:
                if e.response.status_code == 404:
                    new_files.append(file)
                else:
                    raise e
        return new_files

    def upload(self, files):
        print(files)
        for file_path in files:
            self.storck_client.upload_file(self.upload_dir + "/" + file_path, path=file_path)

    def run(self):
        files = self.load_files_list()
        files = self.filter_files(files)
        self.upload(files)

    def _hash_file(self, file_path):
        with open(self.upload_dir + "/" + file_path, 'rb') as file:
            data = file.read()
        hasher = hashlib.md5()
        hasher.update(data)
        return hasher.hexdigest()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automatically upload files from a given directory')
    parser.add_argument('--host', '-a', dest='api_host', action='store',
                        help='STORCK api host')
    parser.add_argument('--user-token', '-u', dest='user_token', action='store',
                        help='STORCK user token')
    parser.add_argument('--workspace-token', '-w', dest='workspace_token', action='store',
                        help='STORCK workspace token')
    parser.add_argument('--dir', '-d', dest='auto_upload_dir', action='store',
                        help='auto upload directory')
    args = parser.parse_args()
    AutoUploadScript(args.api_host, args.user_token, args.workspace_token, args.auto_upload_dir).run()
