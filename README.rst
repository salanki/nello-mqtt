Nello.IO MQTT Binding
=======

Remote open your `Nello.IO <https://www.nello.io>`_ locations via MQTT. Simply publish a message like:

.. code:: JSON

  {
    "type": "open",
    "location_id": "a95a788a-e774-4561-8fc8-2225b3dccc21"
  }

A simpler message format is also supported:

.. code:: TEXT

  open a95a788a-e774-4561-8fc8-2225b3dccc21

Nello will publish all locations to the topic on connect, and also print to console.

.. code:: JSON

  {
    "location_id": "a95a788a-e774-4561-8fc8-2225b3dccc21",
    "type": "location",
    "address": "22 E 32nd st 10006 New York, , USA"
  }

Create a separate account for this integration or you will be constantly logged out from the nello app.

Thanks to Philipp Schmitt for `pynello <https://github.com/pschmitt/pynello>`_.

Run as Docker container
-----------

.. code:: bash

  docker run --name nello -d --restart=always -e NELLO_USERNAME=robot@account.com -e NELLO_PASSWORD=password -e MQTT_TOPIC=home/nello -e MQTT_BROKER=localhost -e MQTT_USER=myusernmae -e MQTT_PASSWORD=mysecret salanki/nello-mqtt:latest

Usage with OpenHAB
-----------

Simply use the `MQTT Binding <http://docs.openhab.org/addons/bindings/mqtt1/readme.html>`_.

.. code:: TEXT

  Switch EntryBuzzer <frontdoor> { mqtt=">[mybroker:home/nello:command:ON:OPEN a95a788a-e774-4561-8fc8-2225b3dccc21]", expire="5s,command=OFF" }

Example sitemap entry:

.. code:: TEXT

  Switch item=EntryBuzzer label="Entry Door" mappings=[ON="OPEN"] 
