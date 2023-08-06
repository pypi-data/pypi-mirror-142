import requests
import os
import uuid
import codecs
import dill
import json
import functools

from dotenv import load_dotenv

load_dotenv()

daisi_base_url = "https://app.daisi.io"
daisi_base_route = "/pebble-api/pebbles"

headers = {}
if "ACCESS_TOKEN" in os.environ:
    headers.update({"Authorization": f"token {os.getenv('ACCESS_TOKEN')}"})


def load_dill_string(s):  # pragma: no cover
    return dill.loads(codecs.decode(s.encode(), "base64"))


def get_dill_string(obj):  # pragma: no cover
    return codecs.encode(dill.dumps(obj, protocol=5), "base64").decode()


def _is_jsonable(x):
    try:
        json.dumps(x)
        return True
    except (TypeError, OverflowError):
        return False


class Daisi:
    """
    A utility to assist in developing Daisis for the Daisi platform.

    A tool for creating, validating, publishing, and updating daisis.

    :param daisi_id: A daisi name or UUID
    :param base_url: The default URL to use for connecting to the daisi
    :param access_token: access token for authorizing to the platform
    """

    def __init__(
        self, daisi_id: str, *, base_url: str = daisi_base_url, access_token: str = ""
    ):
        """
        Daisi constructor method.

        :param daisi_id:  A Daisi name or UUID

        :raises ValueError: DaisiID Not Found (Non-200 response)
        """
        self.uuid = None
        self.name = None
        self.description = None
        self.base_url = base_url + daisi_base_route
        self.data_mapping = {}

        if access_token:
            headers["Authorization"] = f"token {access_token}"

        # Check if it's a valid uuid:
        try:
            check_uuid = uuid.UUID(daisi_id) is not None
        except Exception as e:
            check_uuid = False

        if check_uuid:
            r = requests.get(f"{self.base_url}/{daisi_id}", headers=headers)
            if r.status_code != 200:
                raise ValueError("The specified Daisi ID could not be found.")
            else:
                print(f"Found existing Daisi: {r.json()['name']}")

                self.name = r.json()["name"]
                self.uuid = daisi_id
        else:
            print(f"Calling {self.base_url}/search with query {daisi_id}")
            r = requests.get(
                f"{self.base_url}/search", params={"query": daisi_id}, headers=headers
            )
            result = r.json()

            if result:
                self.name = daisi_id
                daisi_id = result[0]["id"]
                print(f"Found existing Daisi: {daisi_id}")
                self.uuid = daisi_id
            else:
                # TODO: Handle git repo connection here
                raise ValueError("That daisi could not be found.")

        ss = self._schema()
        functionlist = [
            l["value"]
            for l in ss[0].get("props", {}).get("options", [])
            if ss[0].get("id") == "_endpoint"
        ]
        for f in functionlist:
            self.__setattr__(
                f, (lambda f: (lambda s, *a, **kwa: s._compute(f, *a, **kwa)).__get__(self))(f)
            )

    def _compute(self, _func="compute", *args, **kwargs):
        param_names = [p["id"] for p in self._schema(_func)]
        kwargs.update(zip(param_names, args))

        r = requests.post(
            f"{self.base_url}/{self.uuid}/compute/{_func}", json=kwargs, headers=headers
        )
        return self.unpickle_hidden(r.json()) if r.status_code == 200 else None

    def compute(self, file=None, func="compute", *args, **kwargs):
        param_names = [p["id"] for p in self._schema(func)]
        kwargs.update(zip(param_names, args))

        # Check whether any of the arguments are daisis
        # parsed_args = self.chain(args)
        parsed_args = self.pickle_hidden(kwargs)

        # Include the function as the endpoint, if provided
        parsed_args["_endpoint"] = func

        # Only include the file argument if it's not None
        if file:
            parsed_args["_file"] = file

        # Call the specified Daisi compute
        r = requests.post(
            f"{self.base_url}/{self.uuid}/compute", json=parsed_args, headers=headers
        )

        result = None
        if r.status_code == 200:
            result = self.unpickle_hidden(r.json())

        return result

    def _schema(self, func=None):
        """
        Query the Daisi schema from the Daisi platform.

        :return: Resulting schema if found, None if not found
        :rtype list
        """
        # Call the specified Daisi schema
        if not func:
            r = requests.get(f"{self.base_url}/{self.uuid}/schema", headers=headers)
        else:
            r = requests.get(
                f"{self.base_url}/{self.uuid}/schema/{func}", headers=headers
            )

        result = None
        if r.status_code == 200:
            result = r.json()

        return result

    def unpickle_hidden(self, output):
        final_output = []
        for out in [y["data"] for y in output["outputs"]]:
            if type(out) == str and out.startswith("lookup:"):
                # Get the binary data
                l_split = out.split("lookup:")

                r = requests.get(
                    f"{self.base_url}/pickle",
                    params={"lookup": l_split[1]},
                    headers=headers,
                )

                out = load_dill_string(r.content.decode())

                final_output.append(out)
            else:
                final_output.append(out)

        return final_output

    def store_pickle(self, data):
        my_args = {"data": data}

        # Call the specified Daisi compute
        r = requests.post(f"{self.base_url}/pickle", json=my_args, headers=headers)

        # Return the result
        return r.content.decode()

    def pickle_hidden(self, args):
        final_args = {}
        for k, v in args.items():
            if not _is_jsonable(v):
                x = self.store_pickle(get_dill_string(v))
                final_args[k] = "lookup:" + x
            else:
                final_args[k] = v

        return final_args

    @staticmethod
    def get_daisis(base_url=daisi_base_url):
        """
        Queries Daisi platform for a list of all current daisis.

        :return: List of daisis available on the Daisi platform.
        :rtype list
        """

        r = requests.get(
            f"{base_url}{daisi_base_route}", params={"pageSize": 10000}, headers=headers
        )
        result = r.json()

        return_list = []
        for daisi in result["pebbles"]:
            return_list.append(
                {
                    "id": daisi["id"],
                    "name": daisi["name"],
                    "description": daisi["description"],
                }
            )

        final_return = sorted(return_list, key=lambda x: x["name"])

        return final_return
