#!/bin/bash
iw dev wlan0mon del
iw phy phy0 interface add wlan0 type managed
