{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1tj714dQDp1F3fIjD-UFI-C67c-fiInZe",
      "authorship_tag": "ABX9TyNW/O/qCqxP8sXeASUBkUXJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/coderami/Ordering_Destinations_Points/blob/main/point_ordering.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install getkey"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZbFxqzbuKM0U",
        "outputId": "f45dab62-82c1-445c-c4a4-0360cadf1646"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting getkey\n",
            "  Downloading getkey-0.6.5.tar.gz (13 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Building wheels for collected packages: getkey\n",
            "  Building wheel for getkey (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for getkey: filename=getkey-0.6.5-py3-none-any.whl size=11423 sha256=fc1e22d89b2f74008a5abf516bd7514bbf67cb47d331837ce4bc27a6c867f171\n",
            "  Stored in directory: /root/.cache/pip/wheels/3e/fb/aa/e77a72aace53412de4bd56d7388f39ec36ca3c9b8f17d44611\n",
            "Successfully built getkey\n",
            "Installing collected packages: getkey\n",
            "Successfully installed getkey-0.6.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from geopy.geocoders import Nominatim\n",
        "from geopy import distance"
      ],
      "metadata": {
        "id": "QBsBq5qYD8q4"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def dictSorter(dict):\n",
        "  import numpy as np\n",
        "  from collections import OrderedDict\n",
        "\n",
        "  keys = list(dict.keys())\n",
        "  values = list(dict.values())\n",
        "\n",
        "  sorted_value_index = np.argsort(values)\n",
        "  # print(sorted_value_index)\n",
        "  sorted_dict = {keys[i]: values[i] for i in sorted_value_index}\n",
        "  return sorted_dict"
      ],
      "metadata": {
        "id": "HEpYt8loCuIX"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def twoDictsSubtractor(dict1, dict2):\n",
        "  cun = 1\n",
        "  global dic_def\n",
        "  dic_def = {}\n",
        "\n",
        "  base = list(dict1.values())[0]\n",
        "\n",
        "  for item in dict2:\n",
        "    # print(item)\n",
        "    # print(dict2[item])\n",
        "    member = \"mem_{}\".format(cun)\n",
        "\n",
        "    dic_def[member] = abs(dict2[item] - base)\n",
        "    # print(dic_def)\n",
        "    cun += 1\n",
        "\n",
        "  print(dic_def)"
      ],
      "metadata": {
        "id": "F3sySg5KCwLc"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "current Location Address: 5155 Sheppard Ave East\n"
      ],
      "metadata": {
        "id": "fQtiaonDJBt_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "point 1: 1 Bloor St E"
      ],
      "metadata": {
        "id": "SMZnYKPKJnxt"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "point 2: 300 Bloor St E"
      ],
      "metadata": {
        "id": "Sd5Tt7B5Jri9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "point 3: 1696 Bayview St"
      ],
      "metadata": {
        "id": "86oRuhgJJvOd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "point 4: 50 Hargrave Lane"
      ],
      "metadata": {
        "id": "HPGmzMPKJxZo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "currentLocation = input(\"Enter your current location: \")\n",
        "geolocator = Nominatim(user_agent=\"point_ordering.py\")\n",
        "departureLocation = geolocator.geocode(currentLocation)\n",
        "print(\"\\n\")\n",
        "print( departureLocation)\n",
        "print(departureLocation.latitude, departureLocation.longitude)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gB1jTJD03rCW",
        "outputId": "248e1593-699c-4925-d6ad-c42c754e4d2c"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your current location: 5155 Sheppard Ave East\n",
            "\n",
            "\n",
            "Sheppard Avenue East, Concord Park Place, Don Valley North, North York, Toronto, Golden Horseshoe, Ontario, M2K 2W1, Canada\n",
            "43.7712275 -79.367035\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "destinationDir = {}\n",
        "counter = 1\n",
        "# while destinationDir[dirValue] != None:\n",
        "while True:\n",
        "  key = input(\"Enter destination location: \")\n",
        "  if key == \" \":\n",
        "    break\n",
        "\n",
        "  dirValue = \"point_{}\".format(counter)\n",
        "  destinationDir[dirValue] = key\n",
        "  counter += 1\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yQo0O3k34SDX",
        "outputId": "bab57c24-24a9-4638-b63b-f73e84baf5cf"
      },
      "execution_count": 6,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter destination location: 1 Bloor St E\n",
            "Enter destination location: 300 Bloor St E\n",
            "Enter destination location: 1696 Bayview St\n",
            "Enter destination location: 50 Hargrave Lane\n",
            "Enter destination location:  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "destinationDir"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lBifHvYP5f4Y",
        "outputId": "dc4e7d74-252b-4f67-ed78-b6fb4e6fe07d"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'point_1': '1 Bloor St E',\n",
              " 'point_2': '300 Bloor St E',\n",
              " 'point_3': '1696 Bayview St',\n",
              " 'point_4': '50 Hargrave Lane'}"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pointList = {}\n",
        "counter2 = 1\n",
        "\n",
        "for key in destinationDir:\n",
        "  value_1 = {}\n",
        "  # print(key, destinationDir[key])\n",
        "  geolocator = Nominatim(user_agent=\"point_ordering.py\")\n",
        "  location = geolocator.geocode(destinationDir[key])\n",
        "  print(location.latitude, location.longitude)\n",
        "  # print(location.latitude)\n",
        "  value_1[destinationDir[key]] = location.latitude, location.longitude\n",
        "  # print(value_1)\n",
        "  pointList[key] = value_1\n",
        "  counter2 += 1\n",
        "\n",
        "# print(pointList)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nujVbvYVIGc2",
        "outputId": "ddf59dc7-e23b-4c35-9dfc-c6b8edcbbf0a"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:urllib3.connectionpool:Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ReadTimeoutError(\"HTTPSConnectionPool(host='nominatim.openstreetmap.org', port=443): Read timed out. (read timeout=1)\")': /search?q=1+Bloor+St+E&format=json&limit=1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "43.66982485 -79.38610666444188\n",
            "43.672169350000004 -79.37988930525304\n",
            "46.52995007744788 -87.40613512861168\n",
            "43.72235307692308 -79.37938197435898\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# print(location.latitude, location.longitude)\n",
        "# point_0 = {}\n",
        "# point_0[currentLocation] = location.latitude, location.longitude\n",
        "# print(point_0)\n",
        "# pointList[\"point_0\"] = point_0\n",
        "print(pointList)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ojKI_60add_n",
        "outputId": "d78495e3-8d7a-47b2-c2ad-0f12b1a94cd0"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'point_1': {'1 Bloor St E': (43.66982485, -79.38610666444188)}, 'point_2': {'300 Bloor St E': (43.672169350000004, -79.37988930525304)}, 'point_3': {'1696 Bayview St': (46.52995007744788, -87.40613512861168)}, 'point_4': {'50 Hargrave Lane': (43.72235307692308, -79.37938197435898)}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "curLoc = (departureLocation.latitude, departureLocation.longitude)\n",
        "\n",
        "distLists = {}\n",
        "distListsValues = {}\n",
        "\n",
        "\n",
        "print(currentLocation)\n",
        "print(departureLocation, \"\\n\")\n",
        "# print(len(pointList))\n",
        "\n",
        "for key in pointList:\n",
        "  # print(key, pointList[key])\n",
        "  print(\"key = \", key)\n",
        "  for secKey in pointList[key]:\n",
        "    print(\"sec key:\", secKey)\n",
        "    print(\"lat and long:\", pointList[key][secKey])\n",
        "    print(\"distance to departure:\", distance.distance(curLoc, pointList[key][secKey]), \"\\n\")\n",
        "\n",
        "    distListsValues[secKey] = distance.distance(curLoc, pointList[key][secKey])\n",
        "\n",
        "    distLists[key] = distListsValues\n",
        "\n",
        "print(distLists)\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2YwOKLxperLK",
        "outputId": "6ce7a83f-cba2-418e-c957-131853a90d47"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5155 Sheppard Ave East\n",
            "Sheppard Avenue East, Concord Park Place, Don Valley North, North York, Toronto, Golden Horseshoe, Ontario, M2K 2W1, Canada \n",
            "\n",
            "key =  point_1\n",
            "sec key: 1 Bloor St E\n",
            "lat and long: (43.66982485, -79.38610666444188)\n",
            "distance to departure: 11.370856085149727 km \n",
            "\n",
            "key =  point_2\n",
            "sec key: 300 Bloor St E\n",
            "lat and long: (43.672169350000004, -79.37988930525304)\n",
            "distance to departure: 11.054668291966255 km \n",
            "\n",
            "key =  point_3\n",
            "sec key: 1696 Bayview St\n",
            "lat and long: (46.52995007744788, -87.40613512861168)\n",
            "distance to departure: 702.1583361289481 km \n",
            "\n",
            "key =  point_4\n",
            "sec key: 50 Hargrave Lane\n",
            "lat and long: (43.72235307692308, -79.37938197435898)\n",
            "distance to departure: 5.520620925618051 km \n",
            "\n",
            "{'point_1': {'1 Bloor St E': Distance(11.370856085149727), '300 Bloor St E': Distance(11.054668291966255), '1696 Bayview St': Distance(702.1583361289481), '50 Hargrave Lane': Distance(5.520620925618051)}, 'point_2': {'1 Bloor St E': Distance(11.370856085149727), '300 Bloor St E': Distance(11.054668291966255), '1696 Bayview St': Distance(702.1583361289481), '50 Hargrave Lane': Distance(5.520620925618051)}, 'point_3': {'1 Bloor St E': Distance(11.370856085149727), '300 Bloor St E': Distance(11.054668291966255), '1696 Bayview St': Distance(702.1583361289481), '50 Hargrave Lane': Distance(5.520620925618051)}, 'point_4': {'1 Bloor St E': Distance(11.370856085149727), '300 Bloor St E': Distance(11.054668291966255), '1696 Bayview St': Distance(702.1583361289481), '50 Hargrave Lane': Distance(5.520620925618051)}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(distance.distance(curLoc, pointList['point_1'][\"1696 bayview\"]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 148
        },
        "id": "tsP6QHZ738O2",
        "outputId": "11e9bbec-fd20-4861-bfbc-4cb16a38a5d6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'distance' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-44-8e9f161c9cfd>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdistance\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdistance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcurLoc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpointList\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'point_1'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"1696 bayview\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'distance' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "j4gxWGpi7_A9"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}