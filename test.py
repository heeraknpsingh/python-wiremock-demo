import time

import pytest
import requests

from wiremock.testing.testcontainer import wiremock_container
from wiremock.constants import Config
from wiremock.client import *

final_url = "/3/movie/76600?api_key=e7a78b19e4fe41a54a52d422f873d734"


@pytest.fixture
def wiremock_server():
    with wiremock_container(secure=False) as wm:
        Config.base_url = wm.get_url("__admin")
        Mappings.create_mapping(
            Mapping(
                request=MappingRequest(method=HttpMethods.GET, url=final_url),
                response=MappingResponse(status=200,
                                         body="{\"adult\":false,\"backdrop_path\":\"/8rpDcsfLJypbO6vREc0547VKqEv.jpg"
                                              "\",\"belongs_to_collection\":{\"id\":87096,\"name\":\"Avatar "
                                              "Collection\",\"poster_path\":\"/uO2yU3QiGHvVp0L5e5IatTVRkYk.jpg\","
                                              "\"backdrop_path\":\"/gxnvX9kF7RRUQYvB52dMLPgeJkt.jpg\"},"
                                              "\"budget\":460000000,\"genres\":[{\"id\":878,\"name\":\"Science "
                                              "Fiction\"},{\"id\":12,\"name\":\"Adventure\"},{\"id\":28,"
                                              "\"name\":\"Action\"}],"
                                              "\"homepage\":\"https://www.avatar.com/movies/avatar-the-way-of-water"
                                              "\",\"id\":76600,\"imdb_id\":\"tt1630029\","
                                              "\"original_language\":\"en\",\"original_title\":\"Avatar: The Way of "
                                              "Water\",\"overview\":\"Set more than a decade after the events of the "
                                              "first film, learn the story of the Sully family (Jake, Neytiri, "
                                              "and their kids), the trouble that follows them, the lengths they go to "
                                              "keep each other safe, the battles they fight to stay alive, "
                                              "and the tragedies they endure.\",\"popularity\":244.682,"
                                              "\"poster_path\":\"/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg\","
                                              "\"production_companies\":[{\"id\":127928,"
                                              "\"logo_path\":\"/h0rjX5vjW5r8yEnUBStFarjcLT4.png\",\"name\":\"20th "
                                              "Century Studios\",\"origin_country\":\"US\"},{\"id\":574,"
                                              "\"logo_path\":\"/nLNW1TeFUYU0M5U0qmYUzOIwlB6.png\","
                                              "\"name\":\"Lightstorm Entertainment\",\"origin_country\":\"US\"}],"
                                              "\"production_countries\":[{\"iso_3166_1\":\"US\",\"name\":\"United "
                                              "States of America\"}],\"release_date\":\"2022-12-14\","
                                              "\"revenue\":2320250281,\"runtime\":192,\"spoken_languages\":[{"
                                              "\"english_name\":\"English\",\"iso_639_1\":\"en\","
                                              "\"name\":\"English\"}],\"status\":\"Released\",\"tagline\":\"Return to "
                                              "Pandora.\",\"title\":\"Avatar: The Way of Water\",\"video\":false,"
                                              "\"vote_average\":7.632,\"vote_count\":10931}"),
                persistent=False,
            )
        )
        yield wm


def test_verify_movie_id(wiremock_server):
    time.sleep(1)
    response = requests.get(wiremock_server.get_url(final_url))
    assert response.status_code == 200
    assert response.json()['id'] == 76600


def test_verify_movie_original_title(wiremock_server):
    time.sleep(1)
    response = requests.get(wiremock_server.get_url(final_url))
    assert response.status_code == 200
    assert response.json()['original_title'] == f"Avatar: The Way of Water"


def test_verify_movie_title(wiremock_server):
    time.sleep(1)
    response = requests.get(wiremock_server.get_url(final_url))
    assert response.status_code == 200
    assert response.json()['title'] == f"Avatar: The Way of Water"


def test_verify_vote_average(wiremock_server):
    time.sleep(1)
    response = requests.get(wiremock_server.get_url(final_url))
    assert response.status_code == 200
    assert response.json()['status'] == f"Released"
