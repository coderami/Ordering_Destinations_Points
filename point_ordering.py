{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1tj714dQDp1F3fIjD-UFI-C67c-fiInZe",
      "authorship_tag": "ABX9TyP+W+eketFZvYBF2TipmSgt",
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
      "execution_count": null,
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
        "!pip install folium"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7LRe5u5yzCkG",
        "outputId": "375454de-1cc6-4861-df46-d09bc06e6511"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: folium in /usr/local/lib/python3.10/dist-packages (0.14.0)\n",
            "Requirement already satisfied: branca>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from folium) (0.7.2)\n",
            "Requirement already satisfied: jinja2>=2.9 in /usr/local/lib/python3.10/dist-packages (from folium) (3.1.4)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from folium) (1.25.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from folium) (2.31.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2>=2.9->folium) (2.1.5)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->folium) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->folium) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->folium) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->folium) (2024.6.2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from geopy.geocoders import Nominatim\n",
        "from geopy import distance\n",
        "import folium"
      ],
      "metadata": {
        "id": "QBsBq5qYD8q4"
      },
      "execution_count": 49,
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
      "execution_count": null,
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
      "execution_count": null,
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
        "point 3: 1696 Bayview Ave"
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
      "execution_count": null,
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
        "outputId": "fb495474-ff6f-4654-8dec-1d42cfd83c96"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter destination location: 1 bloor st e\n",
            "Enter destination location: 300 bloor st e\n",
            "Enter destination location: 1696 bayview ave\n",
            "Enter destination location: 50 hargrave lane\n",
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
        "outputId": "42a2f89a-ced0-41b8-c926-784304d7f907"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'point_1': '1 bloor st e',\n",
              " 'point_2': '300 bloor st e',\n",
              " 'point_3': '1696 bayview ave',\n",
              " 'point_4': '50 hargrave lane'}"
            ]
          },
          "metadata": {},
          "execution_count": 40
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
        "outputId": "bea3f9f4-478d-4152-8eff-06af44754a03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "43.66982485 -79.38610666444188\n",
            "43.672169350000004 -79.37988930525304\n",
            "43.7088373 -79.3764984\n",
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
        "outputId": "4365d58c-3d58-45d1-9a9d-d91df07ca393"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'point_1': {'1 bloor st e': (43.66982485, -79.38610666444188)}, 'point_2': {'300 bloor st e': (43.672169350000004, -79.37988930525304)}, 'point_3': {'1696 bayview ave': (43.7088373, -79.3764984)}, 'point_4': {'50 hargrave lane': (43.72235307692308, -79.37938197435898)}}\n"
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
        "    # distListsValues[secKey] = distance.distance(curLoc, pointList[key][secKey])\n",
        "\n",
        "    distLists[key] = distance.distance(curLoc, pointList[key][secKey])\n",
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
        "outputId": "aa02397b-f2f1-4f0c-8c02-87a96de44c02"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5155 Sheppard Ave East\n",
            "Sheppard Avenue East, Concord Park Place, Don Valley North, North York, Toronto, Golden Horseshoe, Ontario, M2K 2W1, Canada \n",
            "\n",
            "key =  point_1\n",
            "sec key: 1 bloor st e\n",
            "lat and long: (43.66982485, -79.38610666444188)\n",
            "distance to departure: 11.370856085149727 km \n",
            "\n",
            "key =  point_2\n",
            "sec key: 300 bloor st e\n",
            "lat and long: (43.672169350000004, -79.37988930525304)\n",
            "distance to departure: 11.054668291966255 km \n",
            "\n",
            "key =  point_3\n",
            "sec key: 1696 bayview ave\n",
            "lat and long: (43.7088373, -79.3764984)\n",
            "distance to departure: 6.973790069424031 km \n",
            "\n",
            "key =  point_4\n",
            "sec key: 50 hargrave lane\n",
            "lat and long: (43.72235307692308, -79.37938197435898)\n",
            "distance to departure: 5.520620925618051 km \n",
            "\n",
            "{'point_1': Distance(11.370856085149727), 'point_2': Distance(11.054668291966255), 'point_3': Distance(6.973790069424031), 'point_4': Distance(5.520620925618051)}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sortedPoint = dictSorter(distLists)"
      ],
      "metadata": {
        "id": "j4gxWGpi7_A9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(sortedPoint)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7Neh8V2fas_y",
        "outputId": "7ef9a00a-e8d7-42cf-c26b-8e2a09508980"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'point_4': Distance(5.520620925618051), 'point_3': Distance(6.973790069424031), 'point_2': Distance(11.054668291966255), 'point_1': Distance(11.370856085149727)}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "finalOrderedList = {}\n",
        "\n",
        "for key in sortedPoint:\n",
        "  # for key2 in pointList[key]:\n",
        "  #   print(key2)\n",
        "  # finalOrderedList[key] =\n",
        "  print(key, pointList[key])\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yeSAMR6pdqDP",
        "outputId": "7f34002b-43b7-4f81-fd77-fb2bb75c816d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "point_4 {'50 hargrave lane': (43.72235307692308, -79.37938197435898)}\n",
            "point_3 {'1696 bayview ave': (43.7088373, -79.3764984)}\n",
            "point_2 {'300 bloor st e': (43.672169350000004, -79.37988930525304)}\n",
            "point_1 {'1 bloor st e': (43.66982485, -79.38610666444188)}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "m = folium.Map(location=[departureLocation.latitude, departureLocation.longitude], zoom_start=12)"
      ],
      "metadata": {
        "id": "TQmSC9uqjgb4"
      },
      "execution_count": 51,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "folium.Marker(location=[departureLocation.latitude, departureLocation.longitude]).add_to(m)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hn6h7Aluz1Tt",
        "outputId": "ea017710-3cf3-4568-b2a4-69c2da3be751"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<folium.map.Marker at 0x7c662edc70d0>"
            ]
          },
          "metadata": {},
          "execution_count": 52
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "m"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 854
        },
        "id": "jFGjW2LG0KL8",
        "outputId": "94e1580d-0b7d-4f21-8cad-d7dfedb2c008"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<folium.folium.Map at 0x7c662edc4fa0>"
            ],
            "text/html": [
              "<div style=\"width:100%;\"><div style=\"position:relative;width:100%;height:0;padding-bottom:60%;\"><span style=\"color:#565656\">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc=\"&lt;!DOCTYPE html&gt;\n",
              "&lt;html&gt;\n",
              "&lt;head&gt;\n",
              "    \n",
              "    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;\n",
              "    \n",
              "        &lt;script&gt;\n",
              "            L_NO_TOUCH = false;\n",
              "            L_DISABLE_3D = false;\n",
              "        &lt;/script&gt;\n",
              "    \n",
              "    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;\n",
              "    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;\n",
              "    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;\n",
              "    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;\n",
              "    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;\n",
              "    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;\n",
              "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;\n",
              "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;\n",
              "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;\n",
              "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;\n",
              "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;\n",
              "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;\n",
              "    \n",
              "            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,\n",
              "                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;\n",
              "            &lt;style&gt;\n",
              "                #map_4f69c2cd7f25aed48eff667bd02b9afb {\n",
              "                    position: relative;\n",
              "                    width: 100.0%;\n",
              "                    height: 100.0%;\n",
              "                    left: 0.0%;\n",
              "                    top: 0.0%;\n",
              "                }\n",
              "                .leaflet-container { font-size: 1rem; }\n",
              "            &lt;/style&gt;\n",
              "        \n",
              "&lt;/head&gt;\n",
              "&lt;body&gt;\n",
              "    \n",
              "    \n",
              "            &lt;div class=&quot;folium-map&quot; id=&quot;map_4f69c2cd7f25aed48eff667bd02b9afb&quot; &gt;&lt;/div&gt;\n",
              "        \n",
              "&lt;/body&gt;\n",
              "&lt;script&gt;\n",
              "    \n",
              "    \n",
              "            var map_4f69c2cd7f25aed48eff667bd02b9afb = L.map(\n",
              "                &quot;map_4f69c2cd7f25aed48eff667bd02b9afb&quot;,\n",
              "                {\n",
              "                    center: [43.7712275, -79.367035],\n",
              "                    crs: L.CRS.EPSG3857,\n",
              "                    zoom: 12,\n",
              "                    zoomControl: true,\n",
              "                    preferCanvas: false,\n",
              "                }\n",
              "            );\n",
              "\n",
              "            \n",
              "\n",
              "        \n",
              "    \n",
              "            var tile_layer_eb3e554b50222f8d8e14d92ddf30b77d = L.tileLayer(\n",
              "                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,\n",
              "                {&quot;attribution&quot;: &quot;Data by \\u0026copy; \\u003ca target=\\&quot;_blank\\&quot; href=\\&quot;http://openstreetmap.org\\&quot;\\u003eOpenStreetMap\\u003c/a\\u003e, under \\u003ca target=\\&quot;_blank\\&quot; href=\\&quot;http://www.openstreetmap.org/copyright\\&quot;\\u003eODbL\\u003c/a\\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}\n",
              "            ).addTo(map_4f69c2cd7f25aed48eff667bd02b9afb);\n",
              "        \n",
              "    \n",
              "            var marker_8e8f2f3ecbd76fcd79a3ba3b80f478e7 = L.marker(\n",
              "                [43.7712275, -79.367035],\n",
              "                {}\n",
              "            ).addTo(map_4f69c2cd7f25aed48eff667bd02b9afb);\n",
              "        \n",
              "&lt;/script&gt;\n",
              "&lt;/html&gt;\" style=\"position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;\" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "EQMJFbJF0LBu"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}