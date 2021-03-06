import requests

from models import Launch


class Connect(object):
    """
    Connect to api
    """

    def __init__(self, url, headers=None, params=None):
        """
        Connection constructor
        """

        if headers:
            self.__headers = headers
        else:
            self.__headers = {'Accept': 'application/json'}

        try:
            if params:
                self.__response = requests.get(url, self.__headers, params=params)
            else:
                self.__response = requests.get(url, self.__headers)

            self.__result = self.__response.json()
        except requests.exceptions.RequestException:
            print("Ocorreu um erro na comunicação com a API SpaceX")


    @property
    def result(self):
        """
        Get a JSON result of request.

        :return: JSON result
        """

        if type(self.__result) == dict:
            return Launch(
                flight_number=self.__result.get('flight_number'),
                mission_name=self.__result.get('mission_name'),
                rocket=self.__result.get('rocket').get('rocket_name'),
                rocket_type=self.__result.get('rocket').get('rocket_type'),
                launch_success=self.__result.get('launch_success'),
                launch_date=self.__result.get('launch_date_utc'),
                launch_year=self.__result.get('launch_year')
            )

        launchs = []
        for result in self.__result:
            launchs.append(
                Launch(
                    flight_number=result.get('flight_number'),
                    mission_name=result.get('mission_name'),
                    rocket=result.get('rocket').get('rocket_name'),
                    rocket_type=result.get('rocket').get('rocket_type'),
                    launch_success=result.get('launch_success'),
                    launch_date=result.get('launch_date_utc'),
                    launch_year=result.get('launch_year')
                )
            )

        return launchs

    @property
    def response(self):
        """
        Get the request response

        :return: response
        """

        return self.__response
