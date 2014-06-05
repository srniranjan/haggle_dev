#!/usr/bin/python2.5
#
# Copyright 2009 Roman Nurik
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines common geo math functions used throughout the library."""

__author__ = 'api.roman.public@gmail.com (Roman Nurik)'

import math
import logging

import geotypes
import geocell

RADIUS = 6378135


def distance(p1, p2):
  """Calculates the great circle distance between two points (law of cosines).

  Args:
    p1: A geotypes.Point or db.GeoPt indicating the first point.
    p2: A geotypes.Point or db.GeoPt indicating the second point.

  Returns:
    The 2D great-circle distance between the two given points, in meters.
  """
  p1lat, p1lon = math.radians(p1.lat), math.radians(p1.lon)
  p2lat, p2lon = math.radians(p2.lat), math.radians(p2.lon)
  return RADIUS * math.acos(min(math.sin(p1lat) * math.sin(p2lat) +
      math.cos(p1lat) * math.cos(p2lat) * math.cos(p2lon - p1lon),1))

def mid_point(p1, p2):
  p1lat, p1lon = math.radians(p1.lat), math.radians(p1.lon)
  p2lat, p2lon = math.radians(p2.lat), math.radians(p2.lon)
  delta_lon = p2lon - p1lon
  bx = math.cos(p2lat) * math.cos(delta_lon);
  by = math.cos(p2lat) * math.sin(delta_lon);
    
  p3lat = math.atan2(math.sin(p1lat) + math.sin(p2lat), math.sqrt( (math.cos(p1lat) + bx) * (math.cos(p1lat) + bx) + by*by) );
  p3lon = p1lon + math.atan2(by, math.cos(p1lat) + bx);
  return geotypes.Point(math.degrees(p3lat), math.degrees(p3lon))

def find_center_and_radius_of(square):  
  bbox = geocell.compute_box(square)
  south_west_bound = bbox.south_west
  north_east_bound = bbox.north_east
  midpoint = mid_point(south_west_bound, north_east_bound)
  radius = distance(midpoint, north_east_bound)
  return midpoint, radius
