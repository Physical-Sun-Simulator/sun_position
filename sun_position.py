from math import sin, cos, radians, asin, acos, pi, degrees

def get_sun_elevation_angle(geographical_latitude: float, sun_declination: float, hour_angle: float) -> float:
    """
    Returns the sun elevation angle in rad (arm rotation).
    
    :param geographical_latitude: Geographical latitude of the assumed location in rad
    :param sun_declination: (Seasonal) sun declination of the earth in rad
    :param hour_angle: (Daily) hour angle of the earth in rad
    :return: sun elevation angle in rad
    """
    # TODO: Separate calculations
    return asin(cos(geographical_latitude) * cos(sun_declination) * hour_angle + sin(geographical_latitude) * sin(sun_declination))

def get_sun_azimuth_angle(sun_elevation_angle: float, geographical_latitude: float, sun_declination: float, true_solar_time: float) -> float:
    """
    Returns the sun azimuth angle in rad (table rotation) where
    - North sun azimuth angle = 0 rad
    - East sun azimuth angle = pi/2 rad
    - South sun azimuth angle = pi rad
    - West sun azimuth angle = 3pi/2 rad
    
    :param sun_elevation_angle: Sun elevation angle in rad
    :param geographical_latitude: (Seasonal) sun declination of the earth in rad
    :param sun_declination: (Seasonal) sun declination of the earth in rad
    :param true_solar_time: True Solar Time in (float) hours
    :return: sun azimuth angle in rad
    """
    # TODO: Separate calculations
    inner = (sin(sun_elevation_angle) * sin(geographical_latitude) - sin(sun_declination)) / (cos(sun_elevation_angle) * cos(geographical_latitude))
    if true_solar_time <= 12.00:
        return degrees(pi - acos(inner))
    else: # true_solar_time <= 12.00:
        return degrees(pi + acos(inner))

def get_sun_declination(day: float) -> float:
    """
    Returns an approximation of the sun declination in rad using Fourier series.
    
    :param day: day of the year
    :return: sun declination in rad
    """
    degrees_day = (2 * pi * day) / 365
    
    return 0.3948 - 23.2559 * cos(degrees_day + radians(9.1)) - 0.3915 * cos(2 * degrees_day + radians(5.4)) - 0.1764 * cos(3 * degrees_day + radians(26))

def get_hour_angle(true_solar_time: float) -> float:
    """
    Returns the hour angle in rad.
    
    :param true_solar_time: True Solar Time in (float) hours
    :return: hour angle in rad
    """
    common = radians(15) * abs(12 - true_solar_time)
    if true_solar_time < 12.00:
        return -common
    elif true_solar_time > 12.00:
        return common
    else:
        # Undefined behaviour
        raise Exception
    
def get_true_solar_time(local_clock_time: float, geographical_longitude: float, standard_time_meridian_longitude: float, equation_of_time: float) -> float:
    """
    Returns the true solar time in (float) hours.
    
    :param local_clock_time: Local clock Time in (float) hours
    :param geographical_longitude: geographical longitude in (float) hours
    :param standard_time_meridian_longitude: Longitude of the standard time meridian (pi/18 rad)
    """
    return local_clock_time + (geographical_longitude - standard_time_meridian_longitude) / (pi/18) + equation_of_time