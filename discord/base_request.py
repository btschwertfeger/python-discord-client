import requests
import json
from typing import Union, Optional, Any, List


class BaseRequestAPI:
    BASE_URL: str = "https://discord.com/api/v9"
    TIMEOUT: int = 10

    def __init__(
        self: "BaseRequestAPI",
        token: str,
        url: Optional[str] = None,
        api_version: Optional[str] = None,
    ) -> None:
        self._token: str = token
        if api_version != None:
            self.BASE_URL = f"https://discord.com/api/v{api_version}"
        if url is not None:
            self.BASE_URL = url
        self._session: requests.Session = self._get_session()

    def _request(
        self: "BaseRequestAPI",
        method: str,
        params: Optional[dict] = None,
        uri: str = "",
        headers: Optional[dict] = None,
        files: Optional[dict] = None,
    ) -> Any:
        if params is None:
            params = {}
        if headers is None:
            headers = {}

        data_json = ""
        payload: Optional[Union[dict, str]] = None
        if method in ("GET", "DELETE"):
            if params:
                strl = []
                for key in sorted(params):
                    strl.append("{}={}".format(key, params[key]))
                data_json += "&".join(strl)
                uri += f"?{data_json}"

        elif method in ("POST", "PUT", "PATCH") and params is not None:
            try:
                payload = json.dumps(params)
            except:
                payload = params

        url = f"{self.BASE_URL}{uri}"

        if method in ("GET", "DELETE"):
            return self.check_response(
                self._session.request(
                    method=method, url=url, headers=headers, timeout=self.TIMEOUT
                )
            )

        if method == "POST":
            return self.check_response(
                self._session.post(
                    url=url,
                    data=payload,
                    headers=headers,
                    files=files,
                    timeout=self.TIMEOUT,
                )
            )
        if method in ("PATCH", "PUT"):
            return self.check_response(
                self._session.request(
                    method=method,
                    url=url,
                    data=payload,
                    headers=headers,
                    timeout=self.TIMEOUT,
                )
            )

        raise ValueError("Could not find a matching request type!")

    def _get_session(self) -> requests.Session:
        session: requests.Session = requests.Session()
        session.headers.update(
            {
                "authorization": f"Bot {self._token}",
                "content-type": "application/json",
                "user-agent": "python-discord-client",
            }
        )

        return session

    def _send_file_attachment(
        self: "BaseRequestAPI",
        method: str,
        uri: str,
        file_names: List[str],
        payload: Optional[dict] = None,
        headers: Optional[dict] = None,
    ) -> Any:
        if payload is None:
            payload = {}
        if headers is None:
            headers = {}
        self._session.headers.update({"content-type": None})
        headers.update({"Content-Disposition": 'form-data; name="payload_json"'})
        payload = {"payload_json": json.dumps(payload)}
        prepared_files: dict = {}
        for i, filename in enumerate(file_names):
            file_type: str = filename.split(".")[-1]
            media_type: Optional[str] = None
            if file_type in ["jpg", "png", "jpeg", "gif"]:
                media_type = "image"
                if file_type == "svg":
                    file_type = "svg+xml"

            prepared_files[f"files[{i}]"] = (
                filename,
                open(filename, "rb"),
                f"{media_type}/{file_type}",
                {
                    "Content-Disposition": f'form-data; name="files[{i}]"; filename="{filename}"'
                },
            )

        for key, value in prepared_files.items():
            payload[key] = value

        response = self._request(
            method, params=payload, files=prepared_files, headers=headers, uri=uri
        )
        self._session.headers.update({"content-type": "application/json"})
        return response

    @staticmethod
    def check_response(response: requests.Response) -> Union[dict, list, Any]:
        if f"{response.status_code}"[0] == "2":
            try:
                return response.json()
            except ValueError:
                raise Exception(response.content)
        else:
            raise Exception(f"{response.status_code}: {response.text}")
